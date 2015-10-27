
#
# Access a named RDD on a remote Livy PypSpark session that simulates a shared in memory key/value store.
# To type in a regular Python shell.
# Depends on: pip install requests
# 

import requests
import json


class SharedRdd():
  """
  Perform REST calls to a remote PySpark shell containing a Shared named RDD.
  """  
  def __init__(self, session_url, name):
    self.session_url = session_url
    self.name = name
    
  def get(self, key):
    return self._curl('%(rdd)s.get("%(key)s")' % {'rdd': self.name, 'key': key})
  
  def set(self, key, value):
    return self._curl('%(rdd)s.set("%(key)s", "%(value)s")' % {'rdd': self.name, 'key': key, 'value': value})
  
  def _curl(self, code):
    statements_url = self.session_url + '/statements'
    data = {'code': code}
    r = requests.post(statements_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    resp = r.json()
    statement_id = str(resp['id'])
    while resp['state'] == 'running':
      r = requests.get(statements_url + '/' + statement_id)
      resp = r.json()  

    if 'output' in resp: # Case Livy returns automatically
      return resp['output']['data']
    else:
      return resp['data']


states = SharedRdd('http://localhost:8998/sessions/0', 'states')


print states.get('ak')
print states.get('ca')

