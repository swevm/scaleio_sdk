from scaleio import *

logging.basicConfig(format='%(asctime)s: %(levelname)s %(module)s:%(funcName)s | %(message)s', level=logging.WARNING)
sio = ScaleIO("https://192.168.100.51/api","admin","Password1!",verify_ssl=False) # HTTPS must be used as there seem to be an issue with 302 responses in Requests when using POST
    
sio.create_volume_by_pd_name('testvol101', 8192, sio.get_pd_by_name('default'))
#sio.map_volume_to_sdc(sio.get_volume_by_name('testvol101'), sio.get_sdc_by_id('ce4d7e2a00000001'), True)
#sio.map_volume_to_sdc(sio.get_volume_by_name('testvol101'), sio.get_sdc_by_id('ce4d7e2900000000'), True)

pprint(sio.volumes)
