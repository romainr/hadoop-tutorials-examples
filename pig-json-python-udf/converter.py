from com.xhaus.jyson import JysonCodec as json

@outputSchema("business:chararray")
def tsvify(line):
  business_json = json.loads(line)
  business = map(unicode, business_json.values())
  return '\t'.join(business).replace('\n', ' ').encode('utf-8')

