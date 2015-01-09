from lib import scaleio

connection = scaleio.sdk(debug = False)
connection.login('192.168.100.42', 'admin', 'Password1!')

print "Volumes in SIO cluster"
print "----------------------"
vols = connection.listVolumes()
for key, value in vols.iteritems():
    print "Name: %s with ID %s" % (key, value)
    
connection.logout()