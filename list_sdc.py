from lib import sdk

connection = sdk.sdk(debug = True)
connection.login('192.168.100.42', 'admin', 'Password1!')

sdcIpDict = connection.listSdcByIp()

sdcDict = connection.listSdc()
print "SIO SDCs"
print "--------"
for key, value in sdcDict.iteritems():
    print "Name: %s with ID %s" % (key, value)

connection.logout()