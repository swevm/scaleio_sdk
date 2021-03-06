# PythonScale

#### A module for interacting with the EMC ScaleIO 1.3+ REST API.

Authors: Magnus Nilsson & Matt Cowger

Requirements:

* Python 2.6+
* [Requests](http://docs.python-requests.org/en/latest/)
* [Requests-Toolbelt](https://github.com/sigmavirus24/requests-toolbelt)
* ScaleIO 1.3 or 1.31 installtion with REST API Gateway configured (note, the [Vagrantfile](https://github.com/virtualswede/vagrant-scaleio) from @virtualswede works fine for development)

Examples of use:

```
from scaleio import ScaleIO
sio = ScaleIO("http://192.168.50.12/api","admin","Scaleio123",verify_ssl=False)

#print all the known SDCs:
pprint(sio.sdc)

#print all the known SDSs:
pprint(sio.sds)

#print all the known Volumes:
pprint(sio.volumes)

#print all the known Protection Domains:
pprint(sio.protection_domains)

#Create a new Volume
sio.create_volume_by_pd_name('testvol001', 8192, sio.get_pd_by_name('default'))

#Map Volume to SDC (get_sdc_by_ip('ipaddr') can be used also to map against an SDC)
sio.map_volume_to_sdc(sio.get_volume_by_name('testvol'), sio.get_sdc_by_id('ce4d7e2a00000001'), False)

#Unmap Volume from SDC
sio.unmap_volume_from_sdc(sio.get_volume_by_name('testvol'), sio.get_sdc_by_id('ce4d7e2a00000001'))

#Delete Volume
sio.delete_volume(sio.get_volume_by_name('testvol'), 'ONLY_ME')


