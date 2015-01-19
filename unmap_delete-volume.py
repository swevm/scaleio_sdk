from scaleio import *

logging.basicConfig(format='%(asctime)s: %(levelname)s %(module)s:%(funcName)s | %(message)s', level=logging.WARNING)
sio = ScaleIO("https://localhost:4443/api","admin","Password1!",verify_ssl=False) # HTTPS must be used as there seem to be an issue with 302 responses in Requests when using POST
#sio = ScaleIO("https://192.168.100.42/api","admin","Password1!",verify_ssl=False) # HTTPS must be used as there seem to be an issue with 302 responses in Requests when using POST
pprint(sio.sdc)
#pprint(sio.sds)
pprint(sio.volumes)
#pprint(sio.protection_domains)
    
#sio.create_volume_by_pd_name('testvol201', 8192, sio.get_pd_by_name('default'), mapAll=True)
    
#sio.create_volume_by_pd_name('testvol101', 8192, sio.get_pd_by_name('default'))
#sio.map_volume_to_sdc(sio.get_volume_by_name('testvol101'), sio.get_sdc_by_id('ce4d7e2a00000001'), True)
#sio.map_volume_to_sdc(sio.get_volume_by_name('testvol101'), sio.get_sdc_by_id('ce4d7e2900000000'), True)
    
#sio.unmap_volume_from_sdc(sio.get_volume_by_name('testvol009'), sio.get_sdc_by_id('ce4d7e2a00000001'))
#sio.delete_volume(sio.get_volume_by_name('testvol009'), 'ONLY_ME')
  
#sio.delete_volume(sio.get_volume_by_name('testvol201'), 'ONLY_ME', autoUnmap=True)earth:scaleio
