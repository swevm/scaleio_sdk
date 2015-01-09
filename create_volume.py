from lib import scaleio

connection = scaleio.sdk(debug = True)
connection.login('192.168.100.42', 'admin', 'Password1!')

pdDict = connection.listProtectionDomains()

# Create a Volume
volName = "testvol019" # Volume name - CHANGE TO NAME YOU WANT
volSize = "8388608" # Size of volume in kb - CHANGE TO SIZE YOU NEED
volPd = "default" # Protection domain to create volume in - ADJUST TO ProtectionDomain you want Volume to be created in
for key, value in pdDict.iteritems():
    if key == volPd:
        connection.createVolumeByName(volName, volSize, value)

# Get latest dictionary of Volumes
vols = connection.listVolumes()
        
# By default a created SDC do not get a default name assigned to it, unfortunately.

# Map existing volume to SDC
mapToVol = "testvol019" # Cleartext name of Volume to map to SDC
mapToSdc = "733fffab00000002" # Hardcoded SDC Id. Since I dont have any name assigned to SDCs I have use a hardcoded SDC Id. Add you own SDC ID.
for key, value in vols.iteritems():
    if mapToVol == key:
        mapToVolId = value
        mapVol = connection.mapVolumeToSdcById(mapToVolId, mapToSdc, "True")

connection.logout()