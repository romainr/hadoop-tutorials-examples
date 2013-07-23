#
# Generates columns and cell data for an analytics tables of 1000+ columns
# cf. url
#

# create 'analytics', 'hour', 'day', 'total'


import itertools
import random

random.seed(1)

ROWS = 100
HOURS = range(0, 25)
DAYS = range(0, 366)
COUNTRIES = ['US', 'France', 'Italy']
FAMILLIES = ['hour', 'day', 'total']


# Utilities

def columns_hours():
  FAMILLY = 'hour'
  cols = []
  for hour in HOURS:
    cols.append('%s:%02d-%s' % (FAMILLY, hour, 'total'))
    for country in COUNTRIES:
      cols.append('%s:%02d-%s' % (FAMILLY, hour, country))
  return cols

def columns_days():
  FAMILLY = 'day'
  cols = []
  for day in DAYS:
    cols.append('%s:%03d-%s' % (FAMILLY, day, 'total'))
    for country in COUNTRIES:
      cols.append('%s:%03d-%s' % (FAMILLY, day, country))
  return cols

def columns_total():
  FAMILLY = 'total'
  return ['%s:%s' % (FAMILLY, col)  for col in ['total'] + COUNTRIES]

def get_domain(n):
  return ['domain.%s' % n]

def total():
  return [count_by_country(10000)]

def days():
  return [count_by_country(1000) for day in DAYS]

def hours():
  return [count_by_country(100) for hour in HOURS]

def count_by_country(n):
  counts = [random.randrange(1, n) for country in COUNTRIES]
  return [sum(counts)] + counts

def print_columns():
  all_cols = columns_hours() + columns_days() + columns_total()
  print "-Dimporttsv.columns=HBASE_ROW_KEY," + ','.join(['%s' % col for col in all_cols])

def generate_data(data_file):
  f = open(data_file, 'w')

  for i in xrange(ROWS):
    a = hours() + days() + total()
    f.write('\t'.join(get_domain(i) + map(str, itertools.chain.from_iterable(a))) + '\n')

  print 'done'


# Main

#
# Print columns and generate data into a file
#
print_columns()
generate_data('/tmp/hbase-analytics.tsv')
