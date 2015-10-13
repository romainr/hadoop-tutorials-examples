
# Start a named RDD on a remote Livy PypSpark session that simulates a shared in memory key/value store.
# To start in a Livy PySpark session.

class ShareableRdd():
  
  def __init__(self):
    self.data = sc.parallelize([])

  def get(self, key):
    return self.data.filter(lambda row: row[0] == key).take(1)
  
  def set(self, key, value):
    new_key = sc.parallelize([[key, value]])
    self.data = self.data.union(new_key)
    

a = ShareableRdd()

a.set('ak', 'Alaska')
a.set('ca', 'California')


a.get('ak')

