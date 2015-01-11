from lib import scaleio

connection = sdk.sdk(debug = False)
connection.login('192.168.100.42', 'admin', 'Password1!')

#Get Dictionary of Volumes
vols = connection.listVolumes()

removeVolName = "testvol019" # Cleartext name of Volume to map to SDC
for key, value in vols.iteritems():
    if removeVolName == key:
        removeVolResponse = connection.removeVolumeById(value, "ONLY_ME")

connection.logout()