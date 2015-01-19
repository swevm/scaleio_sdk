from scaleio import *

logging.basicConfig(format='%(asctime)s: %(levelname)s %(module)s:%(funcName)s | %(message)s', level=logging.WARNING)
sio = ScaleIO("https://192.168.100.42/api","admin","Password1!",verify_ssl=False) # HTTPS must be used as there seem to be an issue with 302 responses in Requests when using POST
    
#sio.delete_volume(sio.get_volume_by_name('testvol009'), 'ONLY_ME')
  
sio.delete_volume(sio.get_volume_by_name('testvol201'), 'ONLY_ME', autoUnmap=True)

pprint(sio.volumes)
