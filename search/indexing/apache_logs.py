#!/usr/bin/env python
"""
Parses Apache Log files into a CSV data file ready to be indexed by Solr.

Input format:
demo.gethue.com:80 49.206.186.56 - - [04/May/2014:07:38:53 +0000] "GET /oozie/?format=json&type=running HTTP/1.1" 200 324 "http://demo.gethue.com/oozie/" "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.132 Safari/537.36"

Requires these libraries:
pip install pyyaml ua-parser
https://github.com/tobie/ua-parser

pip install pygeoip
https://github.com/appliedsec/pygeoip

Download http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.xz
from http://dev.maxmind.com/geoip/legacy/geolite/

Script is quick & dirty and given as an example.
"""

import csv
import re
import uuid

import pygeoip

from datetime import datetime
from ua_parser import user_agent_parser


INPUT_LOGS = 'other_vhosts_access.log'
OUTPUT_CSV = 'index_data.csv'
MAX_ROWS = 1000

LINE_RE = re.compile('(?P<host>.+?) (?P<client_ip>[(\d\.)]+) - - \[(?P<time>.*?)\] "(?P<request>.+?)" (?P<code>\d+) (?P<bytes>\d+) "(?P<referer>.*?)" "(?P<user_agent>.*?)"')


def parse_line(line):
  data = LINE_RE.match(line).groupdict()

  del data['host']

  data['record'] = line
  data['id'] = uuid.uuid4()

  start = data['time'].replace(' +0000', '')
  start_ts = datetime.strptime(start, '%d/%b/%Y:%H:%M:%S')
  start = start_ts.strftime('%Y-%m-%dT%H:%M:%SZ')  # e.g. 2014-02-26T13:24:09Z
  data['time'] = start

  try:
    data['method'], data['url'], data['protocol'] = data['request'].split() # e.g. GET /metastore/table/default/sample_07 HTTP/1.1
    extension = data['url'].rsplit('.')
    data['extension'] = extension[-1] if len(extension) > 1 else None
  except Exception, e:
    print e
    data['method'], data['url'], data['protocol'] = None, None, None
    data['extension'] = None

  user_agent_string = data['user_agent'] # e.g. 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
  ua = user_agent_parser.Parse(user_agent_string)
  data['device_family'] = ua['device']['family']
  data['os_family'] = ua['os']['family']
  data['os_major'] = ua['os']['major']
  data['user_agent_family'] = ua['user_agent']['family']
  data['user_agent_major'] = ua['user_agent']['major']

  try:
    data['app'] = data['url'].split('/')[1]
  except:
    data['app'] = 'desktop'

  try:
    data['subapp'] = data['url'].split('/')[2]
    if '?' in data['subapp'] or '&' in data['subapp'] or '=' in data['subapp']:
      data['subapp'] = ''
  except:
    data['subapp'] = ''

  g = geoloc(data['client_ip'])
  if g is None:
    g = {}
  # From http://pygeoip.readthedocs.org/en/v0.3.1/getting-started.html
  data['city'] = g.get('city')
  data['country_code3'] = g.get('country_code3')
  data['latitude'] = g.get('latitude')
  data['longitude'] = g.get('longitude')
  data['country_code'] = g.get('country_code')
  data['country_name'] = g.get('country_name')
  data['region_code'] = g.get('region_code')

  return data


gi = pygeoip.GeoIP('GeoLiteCity.dat') # http://dev.maxmind.com/geoip/legacy/geolite/

def geoloc(ip):
  return gi.record_by_addr(ip)


if __name__ == "__main__":
  csvfile = open(OUTPUT_CSV, 'wb')
  headers = None

  for line in open(INPUT_LOGS).readlines()[:MAX_ROWS]:
    a = parse_line(line)

    if headers is None:
      headers = a.keys()
      print headers
      dw = csv.DictWriter(csvfile, delimiter=',', fieldnames=headers)
      dw.writeheader()
      spamwriter = csv.writer(csvfile, delimiter=',')

    if a['client_ip'] != '127.0.0.1':
      spamwriter.writerow([a[key] for key in headers])

  print 'done!'
