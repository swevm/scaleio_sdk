from lib import scaleio

connection = scaleio.sdk(debug = False)
connection.login('192.168.100.42', 'admin', 'Password1!')

sdcDict = connection.listSdc()
print "SIO SDCs"
print "--------"
for key, value in sdcDict.iteritems():
    print "Name: %s with ID %s" % (key, value)

connection.logout()