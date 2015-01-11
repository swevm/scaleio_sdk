from lib import sdk

connection = sdk.sdk(debug = True)
connection.login('192.168.100.42', 'admin', 'Password1!')

pdDict = connection.listProtectionDomains()

# Create a Volume
volName = "testvol001" # Volume name - CHANGE TO NAME YOU WANT
volSize = "8388608" # Size of volume in kb - CHANGE TO SIZE YOU NEED
volPd = "default" # Protection domain to create volume in - ADJUST TO ProtectionDomain you want Volume to be created in
for key, value in pdDict.iteritems():
    if key == volPd:
        connection.createVolumeByName(volName, volSize, value)

# Get dictionary of Volumes and print them
vols = connection.listVolumes()
for key, value in vols.iteritems():
    print "Key:" + key + " Value: " + value

connection.logout()