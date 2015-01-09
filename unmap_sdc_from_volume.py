from lib import scaleio

connection = scaleio.sdk(debug = True)
connection.login('192.168.100.42', 'admin', 'Password1!')

#Get Dictionary of Volumes
vols = connection.listVolumes()

# By default a created SDC do not get a default name assigned to it, unfortunately.
# Map existing volume to SDC
removeVol = "testvol002" # Cleartext name of Volume to map to SDC
mappedSdcId = "733fffab00000002" # Hardcoded SDC Id. Since I dont have any name assigned to SDCs I have use a hardcoded SDC Id.
for key, value in vols.iteritems():
    if removeVol == key:
        removeVolResponse = connection.unmmapVolumeFromSdc(value, mappedSdcId)

connection.logout()