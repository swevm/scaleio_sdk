import json
import requests
import ssl
from requests.auth import HTTPBasicAuth
from requests_toolbelt import SSLAdapter

class sdk:
    
    def __init__(self, **kwargs):
        self._props = kwargs # This will create a Dictionary where all variables get stored.
        #_DEFAULT_HEADERS = {'Content-type': 'Application/json', 'Accept':'Application/json','Version': '1.0'}
        self._BASE_URL = 'https://'
        self._baseHeader = {'Accept':'application/json','Version':'1.0'}
        self._basePostHeader = {'Content-type':'application/json','Version':'1.0'}
        self.apiconnector = requests.Session()
        self.set_props('authToken', '') # Empty out authToken == state not logged in
    
    def set_props(self, k, v):
        self._props[k] = v
    
    def get_props(self, k):
        return self._props.get(k, None)    
    
    def login(self, mdm_host, username, password):
        self.apiconnector.mount(self._BASE_URL + mdm_host , SSLAdapter(ssl.PROTOCOL_TLSv1))
        response = self.apiconnector.get(self._BASE_URL + mdm_host + '/api/login', verify=False, auth=HTTPBasicAuth(username,password), headers=self._baseHeader)
        
        requests.packages.urllib3.disable_warnings() # From now on, supress all SSL warnings on unverified certificates
        
        self.set_props('username', username)
        self.set_props('password', password)
        self.set_props('mdm_host', mdm_host)
        self.set_props('authToken', response.text.strip('"'))
        self._BASE_URL += mdm_host
        if self.get_props('debug'):
            print 'base_url = ' + self._BASE_URL
            print 'Auth token: ' + self.get_props('authToken')
        return {'authToken', self.get_props('authToken')}
    
    def logout(self):
        if self.get_props('debug'):
            print 'logout()'
        response = self.apiconnector.get(self._BASE_URL + '/api/logout', verify=False, auth=HTTPBasicAuth('', self.get_props('authToken')), headers=self._baseHeader)
        # There no response to this call so it impossible to know if one is successfully logged out or not.                
        self.set_props('authToken', '') # Empty string tell use we are not logged in
        return {'authToken', self.get_props('authToken')}     
    
    def listSdc(self):
        if self.get_props('debug'):
            print 'listSdc()'
        response = self.apiconnector.get(self._BASE_URL + '/api/types/Sdc/instances', verify=False, auth=HTTPBasicAuth('', self.get_props('authToken')), headers=self._baseHeader)
        self.responseDict = {}
        jsonResponse = json.loads(response.text)   
        for js in jsonResponse:
            if not js["name"]:
                js["name"] = 'SDC_' + js["sdcIp"] + '_SHOULD_HAVE_A_DEFAULT_NAME'
                self.responseDict[js["name"]] = js["id"]
                if self.get_props('debug'):
                    print 'SDC Name: ' + js["name"] + ' with ID ' + js["id"] + ' and IP, ' + js["sdcIp"]
        return self.responseDict

    def listSdcByIp(self):
        if self.get_props('debug'):
            print 'listSdcByIp()'
        response = self.apiconnector.get(self._BASE_URL + '/api/types/Sdc/instances', verify=False, auth=HTTPBasicAuth('', self.get_props('authToken')), headers=self._baseHeader)
        self.responseDict = {}
        jsonResponse = json.loads(response.text)   
        for js in jsonResponse:
            if not js["name"]:
                js["name"] = 'SDC_' + js["sdcIp"] + '_SHOULD_HAVE_A_DEFAULT_NAME'
                self.responseDict[js["sdcIp"]] = js["id"]
                if self.get_props('debug'):
                    print 'SDC ID: ' + js["id"] + ' with IP ' + js["sdcIp"]
        return self.responseDict

    def listSds(self):
        #header = {'Accept':'application/json','Version':'1.0'}
        response = self.apiconnector.get(self._BASE_URL + '/api/types/Sds/instances', verify=False, auth=HTTPBasicAuth('', self.get_props('authToken')), headers=self._baseHeader)
        if self.get_props('debug'):
            print 'listSds():'
            print response.text  
        self.responseDict = {}
        jsonResponse = json.loads(response.text)
        for js in jsonResponse:
            self.responseDict[js["name"]] = js["id"]
            if self.get_props('debug'):
                print 'SDS name: [' + js["name"] + ']: ' + js["id"]
        return self.responseDict
    
    def listVolumes(self):
        response = self.apiconnector.get(self._BASE_URL + '/api/types/Volume/instances', verify=False, auth=HTTPBasicAuth('', self.get_props('authToken')), headers=self._baseHeader)
        if self.get_props('debug'):
           print 'listVolumes():'
        self.responseDict = {}
        jsonResponse = json.loads(response.text)
        for js in jsonResponse:
            self.responseDict[js["name"]] = js["id"]
            if self.get_props('debug'):
                print 'Volume [' + js["name"] + '] with ID= ' + js["id"] + 'SizeInKb= ' + str(js["sizeInKb"]) + ''
        return self.responseDict
    
    def listProtectionDomains(self):
        response = self.apiconnector.get(self._BASE_URL + '/api/types/ProtectionDomain/instances', verify=False, auth=HTTPBasicAuth('', self.get_props('authToken')), headers=self._baseHeader)
        if self.get_props('debug'): 
            print 'listProtectionDomains():'
        self.responseDict = {}
        jsonResponse = json.loads(response.text)
        if self.get_props('debug'):
            for js in jsonResponse:
                self.responseDict[js["name"]] = js["id"]
                if self.get_props('debug'):
                    print 'ProtectionDomain [' + js["name"] + '] with ID= ' + js["id"] + ''
        return self.responseDict
    
    def createVolumeByName(self, volName, volSizeInKb, protectionDomainId):
        jsondict = {'protectionDomainId': protectionDomainId, 'volumeSizeInKb': volSizeInKb,  'name': volName}
        response = self.apiconnector.post(self._BASE_URL + '/api/types/Volume/instances', verify=False, auth=HTTPBasicAuth('', self.get_props('authToken')), headers=self._basePostHeader, data=json.dumps(jsondict))
        if self.get_props('debug'):
            print 'JSON POST: ' + json.dumps(jsondict)
            print 'createVolume():'
            print response.text

    def removeVolumeById(self, volId, removeMode):
        """
        /api/instances/Volume::{id}/action/removeVolume
        Method: POST
        Required: removeMode - "ONLY_ME" or "INCLUDING_DESCENDANTS" or "DESCENDANTS_ONLY" or "WHOLE_VTREE"
        """
        jsondict = {'removeMode': removeMode}
        response = self.apiconnector.post(self._BASE_URL + '/api/instances/Volume::' + volId + '/action/removeVolume', verify=False, auth=HTTPBasicAuth('', self.get_props('authToken')), headers=self._basePostHeader, data=json.dumps(jsondict))
        if self.get_props('debug'):
            print 'JSON POST: ' + json.dumps(jsondict)
            print 'removeVolume():'
            print response.text            

    def createVolumeByPdName(self, volName, volSizeInKb, protectionDomainName):
        # Find which pdId match protectionDomainName
        #for key, value in pdDict.iteritems():
        #    if key == volPd:
        #        print "%s: %s" % (key, value) 
        #header = {'Content-type':'application/json'}
        jsondict = {'protectionDomainId': protectionDomainId, 'volumeSizeInKb': volSizeInKb,  'name': volName}
        response = self.apiconnector.post(self._BASE_URL + '/api/types/Volume/instances', verify=False, auth=HTTPBasicAuth('', self.get_props('authToken')), headers=self._basePostHeader, data=json.dumps(jsondict))
        if self.get_props('debug'):
            print 'JSON POST: ' + json.dumps(jsondict)
            print 'createVolume():'
            print response.text
            
    def mapVolumeToSdcById(self, volId, sdcId, allowMultipleMappings):
        #print "SDC ID: " + sdcId
        #print "VOL ID: " + volId
        #print "AllowMultiple: " + allowMultipleMappings
        """
        Map a volume to one or all SDC nodes
        /api/instances/Volume::{id}/action/add MappedSdc
        Type: POST
        Required: sdcId - SDC ID
        Optional: allowMultipleMappings - "TRUE" or "FALSE"
            If allSdcs appears, map volume to all clients
            Map - exposes a volume to all SDC nodes. The exposure will also include SDC nodes that will be added after the execution of this request
        """
        jsondict = {'sdcId': sdcId, 'allowMultipleMappings': allowMultipleMappings}
        response = self.apiconnector.post(self._BASE_URL + '/api/instances/Volume::' + volId + '/action/addMappedSdc', verify=False, auth=HTTPBasicAuth('', self.get_props('authToken')), headers=self._basePostHeader, data=json.dumps(jsondict))
        if self.get_props('debug'):
            print 'JSON POST: ' + json.dumps(jsondict)
            print 'mapVolumeToSdc():'
            print response.text

    def mapVolumeToSdcByIp(self, volId, sdcIp, allowMultipleMappings):
        print "SDC IP: " + sdcIp
        print "VOL ID: " + volId
        print "AllowMultiple: " + allowMultipleMappings
        """
        Map a volume to one or all SDC nodes by using its IP address
        /api/instances/Volume::{id}/action/add MappedSdc
        Type: POST
        Required: sdcIp - Ip address to SDC
        Optional: allowMultipleMappings - "TRUE" or "FALSE"
            If allSdcs appears, map volume to all clients
            Map - exposes a volume to all SDC nodes. The exposure will also include SDC nodes that will be added after the execution of this request
        """
        sdcIpDict = self.listSdcByIp()
        for ipKey, valueId in sdcIpDict.iteritems():
            if ipKey == sdcIp:
                sdcId = valueId
        jsondict = {'sdcId': sdcId, 'allowMultipleMappings': allowMultipleMappings}
        response = self.apiconnector.post(self._BASE_URL + '/api/instances/Volume::' + volId + '/action/addMappedSdc', verify=False, auth=HTTPBasicAuth('', self.get_props('authToken')), headers=self._basePostHeader, data=json.dumps(jsondict))
        if self.get_props('debug'):
            print 'JSON POST: ' + json.dumps(jsondict)
            print 'mapVolumeToSdc():'
            print response.text
            
    def unmmapVolumeFromSdc(self, volId, sdcId):
        """
        Unmap a volume from one or all SDC nodes
        /api/instances/Volu me::{id}/action/removeMappedSdc
        Method: POST
        Required: sdcId - SDC ID or allSdcs Optional: ignoreScsiInitiators - "TRUE" or "FALSE"
        If allSdcs appears, unmap volume from all SDCs.
        """
        #header = {'Content-type':'application/json'}
        jsondict = {'sdcId': sdcId}
        response = self.apiconnector.post(self._BASE_URL + '/api/instances/Volume::' + volId + '/action/removeMappedSdc', verify=False, auth=HTTPBasicAuth('', self.get_props('authToken')), headers=self._basePostHeader, data=json.dumps(jsondict))
        if self.get_props('debug'):
            print 'JSON POST: ' + json.dumps(jsondict)
            print 'unmapVolumeFromSdc():'
            print response.text