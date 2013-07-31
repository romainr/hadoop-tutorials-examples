##
## Insert various data into HBase
##

## cd $HUE_HOME (e.g. cd /usr/share/hue(/opt/cloudera/parcels/CDH-XXXXX/share/hue if using parcels))
## build/env/bin/hue shell
##

from hbase.api import HbaseApi

HbaseApi().putRow('Cluster', 'events', 'hue-20130801', {'doc:txt': 'Hue is awesome!'})
HbaseApi().putRow('Cluster', 'events', 'hue-20130801', {'doc:json': '{"user": "hue", "coolness": "extra"}'})
HbaseApi().putRow('Cluster', 'events', 'hue-20130802', {'doc:version': '<xml>I like HBase</xml>'})
HbaseApi().putRow('Cluster', 'events', 'hue-20130802', {'doc:version': '<xml>I LOVE HBase</xml>'})


## From https://github.com/romainr/hadoop-tutorials-examples
## cd /tmp
## git clone https://github.com/romainr/hadoop-tutorials-examples.git

root='/tmp/hadoop-tutorials-examples'

HbaseApi().putRow('Cluster', 'events', 'hue-20130801', {'doc:img': open(root + '/hbase-tables/data/hue-logo.png', "rb").read()})
HbaseApi().putRow('Cluster', 'events', 'hue-20130801', {'doc:html': open(root + '/hbase-tables/data/gethue.com.html', "rb").read()})
HbaseApi().putRow('Cluster', 'events', 'hue-20130801', {'doc:pdf': open(root + '/hbase-tables/data/gethue.pdf', "rb").read()})

