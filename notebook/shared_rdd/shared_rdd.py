
#
# Start a ShareableRdd('states') on a remote Livy pypsark session.
# pip install requests
# 

import requests
import json


class SharedRdd2():
  
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
    return r.json()['data']
 

states = SharedRdd2('http://localhost:8998/sessions/0', 'states')


print states.get('ak')
print states.get('ca')

