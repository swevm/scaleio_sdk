from lib import sdk

connection = sdk.sdk(debug = True)
connection.login('192.168.100.42', 'admin', 'Password1!')

pdDict = connection.listProtectionDomains()



# Map existing volume to SDC
mapToVol = "testvol008" # Cleartext name of Volume to map to SDC
vols = connection.listVolumes()


#mapToSdc = "ce4d7e2900000000" # Hardcoded SDC Id. Since I dont have any name assigned to SDCs I have use a hardcoded SDC Id. Add you own SDC ID.
for key, value in vols.iteritems():
    if mapToVol == key:
        connection.mapVolumeToSdcByIp(value, "192.168.100.43", "True")

connection.logout()