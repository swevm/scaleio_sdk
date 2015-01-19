from scaleio import *

logging.basicConfig(format='%(asctime)s: %(levelname)s %(module)s:%(funcName)s | %(message)s', level=logging.WARNING)
sio = ScaleIO("https://192.168.100.42/api","admin","Password1!",verify_ssl=False) # HTTPS must be used as there seem to be an issue with 302 responses in Requests when using POST
    
sio.map_volume_to_sdc(sio.get_volume_by_name('testvol101'), sio.get_sdc_by_id('ce4d7e2a00000001'), True)
sio.map_volume_to_sdc(sio.get_volume_by_name('testvol101'), sio.get_sdc_by_ip('192.168.100.43'), True)

