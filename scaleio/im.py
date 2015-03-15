import json
import requests
import time
from requests.auth import HTTPBasicAuth
from requests_toolbelt import SSLAdapter
from requests_toolbelt import MultipartEncoder
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl
import logging
import time
from os import listdir
from os.path import isfile, join
import logging

from pprint import pprint

class TLS1Adapter(HTTPAdapter):
    """
    A custom HTTP adapter we mount to the session to force the use of TLSv1, which is the only thing supported by
    the gateway.  Python 2.x tries to establish SSLv2/3 first which failed.
    """
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLSv1)

class Im_Generic_Object(object):
    @classmethod
    def get_class_name(cls):
        """
        A helper method that returns the name of the class.  Used by __str__ below
        """
        return cls.__name__

    def __str__(self):
        """
        A convinience method to pretty print the contents of the class instance
        """
        # to show include all variables in sorted order
        return "<{}> @ {}:\n".format(self.get_class_name(), id(self)) + "\n".join(
            ["  %s: %s" % (key.rjust(22), self.__dict__[key]) for key in sorted(set(self.__dict__))])

    def __repr__(self):
        return self.__str__()
    
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
class Im_Command_Status(Im_Generic_Object):
    """
    Request:
    
    Parameters:
    
    Response:
    {"192.168.100.42":[{"node":{"ostype":"unknown","nodeName":null,"nodeIPs":["192.168.100.42"],"domain":null,"userName":null,"password":null,"liaPassword":"Password1!"},"validateClean":false,"validateExactVersion":false,"commandState":"completed","startTime":"2015-01-25T14:19:45.722Z","message":"Command completed successfully","result":{"diskDevices":[{"diskName":"sda2"},{"diskName":"sda1"},{"diskName":"dm-0"},{"diskName":"sr0"},{"diskName":"fd0"},{"diskName":"sdb"},{"diskName":"sda"},{"diskName":"dm-1"}],"installedComponents":[{"ecsComponentType":"sds","version":{"version":"1.31-256.2"}},{"ecsComponentType":"mdm","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sdc","version":{"version":"1.31-256.2"}},{"ecsComponentType":"callhome","version":{"version":"1.31-256.2"}},{"ecsComponentType":"lia","version":{"version":"1.31-256.2"}}],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-25T14:19:46.012Z"},"allowedState":"query","archived":false,"commandName":".ValidateNodeCommand"}],"MDM Commands":[{"mdmIPs":[],"mdmPassword":"","configuration":{"installationId":"4777d14d7609d6e4","mdmIPs":["192.168.100.42","192.168.100.41"],"mdmPassword":"Password1!","liaPassword":"Password1!","licenseKey":null,"primaryMdm":{"node":{"ostype":"unknown","nodeName":null,"nodeIPs":["192.168.100.41"],"domain":null,"userName":null,"password":null,"liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"scinia"},{"diskName":"sr0"},{"diskName":"sda2"},{"diskName":"fd0"},{"diskName":"sda"},{"diskName":"dm-0"},{"diskName":"sda1"},{"diskName":"sdb"},{"diskName":"dm-1"}],"installedComponents":[{"ecsComponentType":"callhome","version":{"version":"1.31-256.2"}},{"ecsComponentType":"lia","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sdc","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sds","version":{"version":"1.31-256.2"}},{"ecsComponentType":"mdm","version":{"version":"1.31-256.2"}}],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-25T14:19:45.973Z"},"managementIPs":["192.168.100.42","192.168.100.41"],"mdmIPs":["192.168.100.41"]},"secondaryMdm":{"node":{"ostype":"unknown","nodeName":null,"nodeIPs":["192.168.100.42"],"domain":null,"userName":null,"password":null,"liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"sda2"},{"diskName":"sda1"},{"diskName":"dm-0"},{"diskName":"sr0"},{"diskName":"fd0"},{"diskName":"sdb"},{"diskName":"sda"},{"diskName":"dm-1"}],"installedComponents":[{"ecsComponentType":"sds","version":{"version":"1.31-256.2"}},{"ecsComponentType":"mdm","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sdc","version":{"version":"1.31-256.2"}},{"ecsComponentType":"callhome","version":{"version":"1.31-256.2"}},{"ecsComponentType":"lia","version":{"version":"1.31-256.2"}}],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-25T14:19:46.012Z"},"managementIPs":["192.168.100.42","192.168.100.41"],"mdmIPs":["192.168.100.42"]},"tb":{"node":{"ostype":"unknown","nodeName":null,"nodeIPs":["192.168.100.43"],"domain":null,"userName":null,"password":null,"liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"sr0"},{"diskName":"sda"},{"diskName":"sda2"},{"diskName":"sda1"},{"diskName":"dm-1"},{"diskName":"dm-0"},{"diskName":"sdb"},{"diskName":"fd0"},{"diskName":"scinia"}],"installedComponents":[{"ecsComponentType":"tb","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sds","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sdc","version":{"version":"1.31-256.2"}},{"ecsComponentType":"lia","version":{"version":"1.31-256.2"}}],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-25T14:19:45.898Z"},"tbIPs":["192.168.100.43"]},"sdsList":[{"node":{"ostype":"unknown","nodeName":null,"nodeIPs":["192.168.100.41"],"domain":null,"userName":null,"password":null,"liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"scinia"},{"diskName":"sr0"},{"diskName":"sda2"},{"diskName":"fd0"},{"diskName":"sda"},{"diskName":"dm-0"},{"diskName":"sda1"},{"diskName":"sdb"},{"diskName":"dm-1"}],"installedComponents":[{"ecsComponentType":"callhome","version":{"version":"1.31-256.2"}},{"ecsComponentType":"lia","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sdc","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sds","version":{"version":"1.31-256.2"}},{"ecsComponentType":"mdm","version":{"version":"1.31-256.2"}}],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-25T14:19:45.973Z"},"sdsName":"SDS_[192.168.100.41]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.41"],"sdsOnlyIPs":[],"sdcOnlyIPs":[],"devices":[],"optimized":false,"port":7072},{"node":{"ostype":"unknown","nodeName":null,"nodeIPs":["192.168.100.43"],"domain":null,"userName":null,"password":null,"liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"sr0"},{"diskName":"sda"},{"diskName":"sda2"},{"diskName":"sda1"},{"diskName":"dm-1"},{"diskName":"dm-0"},{"diskName":"sdb"},{"diskName":"fd0"},{"diskName":"scinia"}],"installedComponents":[{"ecsComponentType":"tb","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sds","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sdc","version":{"version":"1.31-256.2"}},{"ecsComponentType":"lia","version":{"version":"1.31-256.2"}}],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-25T14:19:45.898Z"},"sdsName":"SDS_[192.168.100.43]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.43"],"sdsOnlyIPs":[],"sdcOnlyIPs":[],"devices":[],"optimized":false,"port":7072},{"node":{"ostype":"unknown","nodeName":null,"nodeIPs":["192.168.100.42"],"domain":null,"userName":null,"password":null,"liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"sda2"},{"diskName":"sda1"},{"diskName":"dm-0"},{"diskName":"sr0"},{"diskName":"fd0"},{"diskName":"sdb"},{"diskName":"sda"},{"diskName":"dm-1"}],"installedComponents":[{"ecsComponentType":"sds","version":{"version":"1.31-256.2"}},{"ecsComponentType":"mdm","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sdc","version":{"version":"1.31-256.2"}},{"ecsComponentType":"callhome","version":{"version":"1.31-256.2"}},{"ecsComponentType":"lia","version":{"version":"1.31-256.2"}}],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-25T14:19:46.012Z"},"sdsName":"SDS_[192.168.100.42]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.42"],"sdsOnlyIPs":[],"sdcOnlyIPs":[],"devices":[],"optimized":false,"port":7072}],"sdcList":[{"node":{"ostype":"unknown","nodeName":null,"nodeIPs":["192.168.100.42"],"domain":null,"userName":null,"password":null,"liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"sda2"},{"diskName":"sda1"},{"diskName":"dm-0"},{"diskName":"sr0"},{"diskName":"fd0"},{"diskName":"sdb"},{"diskName":"sda"},{"diskName":"dm-1"}],"installedComponents":[{"ecsComponentType":"sds","version":{"version":"1.31-256.2"}},{"ecsComponentType":"mdm","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sdc","version":{"version":"1.31-256.2"}},{"ecsComponentType":"callhome","version":{"version":"1.31-256.2"}},{"ecsComponentType":"lia","version":{"version":"1.31-256.2"}}],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-25T14:19:46.012Z"},"splitterRpaIp":null},{"node":{"ostype":"unknown","nodeName":null,"nodeIPs":["192.168.100.43"],"domain":null,"userName":null,"password":null,"liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"sr0"},{"diskName":"sda"},{"diskName":"sda2"},{"diskName":"sda1"},{"diskName":"dm-1"},{"diskName":"dm-0"},{"diskName":"sdb"},{"diskName":"fd0"},{"diskName":"scinia"}],"installedComponents":[{"ecsComponentType":"tb","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sds","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sdc","version":{"version":"1.31-256.2"}},{"ecsComponentType":"lia","version":{"version":"1.31-256.2"}}],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-25T14:19:45.898Z"},"splitterRpaIp":null},{"node":{"ostype":"unknown","nodeName":null,"nodeIPs":["192.168.100.41"],"domain":null,"userName":null,"password":null,"liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"scinia"},{"diskName":"sr0"},{"diskName":"sda2"},{"diskName":"fd0"},{"diskName":"sda"},{"diskName":"dm-0"},{"diskName":"sda1"},{"diskName":"sdb"},{"diskName":"dm-1"}],"installedComponents":[{"ecsComponentType":"callhome","version":{"version":"1.31-256.2"}},{"ecsComponentType":"lia","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sdc","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sds","version":{"version":"1.31-256.2"}},{"ecsComponentType":"mdm","version":{"version":"1.31-256.2"}}],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-25T14:19:45.973Z"},"splitterRpaIp":null}],"callHomeConfiguration":null,"remoteSyslogConfiguration":null},"noUpload":false,"noInstall":false,"noLia":false,"allowReboot":false,"liaOnly":false,"commandState":"completed","startTime":"2015-01-25T14:19:46.134Z","message":"Command completed successfully","result":null,"allowedState":"query","archived":false,"commandName":".ValidateAndOrchestrateNewCommandsForUpgradeCommand"},{"mdmIPs":["192.168.100.42","192.168.100.41"],"mdmPassword":"Password1!","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"install","archived":false,"commandName":".WaitForNormalClusterModeCommand"},{"mdmIPs":["192.168.100.42","192.168.100.41"],"mdmPassword":"Password1!","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"install","archived":false,"commandName":".WaitForNoDegradedCommand"},{"mdmIPs":["192.168.100.42","192.168.100.41"],"mdmPassword":"Password1!","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"install","archived":false,"commandName":".SwitchMdmOwnershipCommand"},{"mdmIPs":["192.168.100.42","192.168.100.41"],"mdmPassword":"Password1!","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"install","archived":false,"commandName":".WaitForNoDegradedCommand"},{"mdmIPs":["192.168.100.42","192.168.100.41"],"mdmPassword":"Password1!","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"install","archived":false,"commandName":".WaitForNoDegradedCommand"},{"mdmIPs":["192.168.100.42","192.168.100.41"],"mdmPassword":"Password1!","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"install","archived":false,"commandName":".SwitchMdmOwnershipCommand"},{"mdmIPs":["192.168.100.42","192.168.100.41"],"mdmPassword":"Password1!","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"install","archived":false,"commandName":".WaitForNoDegradedCommand"},{"mdmIPs":["192.168.100.42","192.168.100.41"],"mdmPassword":"Password1!","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"install","archived":false,"commandName":".WaitForNormalClusterModeCommand"},{"mdmIPs":["192.168.100.42","192.168.100.41"],"mdmPassword":"Password1!","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"install","archived":false,"commandName":".WaitForNoDegradedCommand"},{"mdmIPs":["192.168.100.42","192.168.100.41"],"mdmPassword":"Password1!","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"install","archived":false,"commandName":".WaitForNoDegradedCommand"},{"mdmIPs":["192.168.100.42","192.168.100.41"],"mdmPassword":"Password1!","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"install","archived":false,"commandName":".WaitForNoDegradedCommand"},{"mdmIPs":["192.168.100.42","192.168.100.41"],"mdmPassword":"Password1!","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"install","archived":false,"commandName":".WaitForNoDegradedCommand"}],"192.168.100.43":[{"node":{"ostype":"unknown","nodeName":null,"nodeIPs":["192.168.100.43"],"domain":null,"userName":null,"password":null,"liaPassword":"Password1!"},"validateClean":false,"validateExactVersion":false,"commandState":"completed","startTime":"2015-01-25T14:19:45.722Z","message":"Command completed successfully","result":{"diskDevices":[{"diskName":"sr0"},{"diskName":"sda"},{"diskName":"sda2"},{"diskName":"sda1"},{"diskName":"dm-1"},{"diskName":"dm-0"},{"diskName":"sdb"},{"diskName":"fd0"},{"diskName":"scinia"}],"installedComponents":[{"ecsComponentType":"tb","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sds","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sdc","version":{"version":"1.31-256.2"}},{"ecsComponentType":"lia","version":{"version":"1.31-256.2"}}],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-25T14:19:45.898Z"},"allowedState":"query","archived":false,"commandName":".ValidateNodeCommand"}],"192.168.100.41":[{"node":{"ostype":"unknown","nodeName":null,"nodeIPs":["192.168.100.41"],"domain":null,"userName":null,"password":null,"liaPassword":"Password1!"},"validateClean":false,"validateExactVersion":false,"commandState":"completed","startTime":"2015-01-25T14:19:45.723Z","message":"Command completed successfully","result":{"diskDevices":[{"diskName":"scinia"},{"diskName":"sr0"},{"diskName":"sda2"},{"diskName":"fd0"},{"diskName":"sda"},{"diskName":"dm-0"},{"diskName":"sda1"},{"diskName":"sdb"},{"diskName":"dm-1"}],"installedComponents":[{"ecsComponentType":"callhome","version":{"version":"1.31-256.2"}},{"ecsComponentType":"lia","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sdc","version":{"version":"1.31-256.2"}},{"ecsComponentType":"sds","version":{"version":"1.31-256.2"}},{"ecsComponentType":"mdm","version":{"version":"1.31-256.2"}}],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-25T14:19:45.973Z"},"allowedState":"query","archived":false,"commandName":".ValidateNodeCommand"}]}
    """
    
    def __init__(self,
        id=None,
        links=None,
        name=None
    ):
        self.id=id
        self.links = []
        if links:
            for link in links:
                self.links.append(Link(link['href'], link['rel']))
        self.name=name

    @staticmethod
    def from_dict(dict):
        """
        A convinience method that directly creates a new instance from a passed dictionary (that probably came from a
        JSON response from the server.
        """
        return Im_Command_Status(**dict)

class ScaleIO_Node_Object(Im_Generic_Object):
    """
    Do not use. Will be the common denominator for ScaleIO configuration nodes.
    All config object should inherit this base
    """
    
    def __init__(self,
        domain=None,
        liaPassword=None,
        nodeIPs=None,
        nodeName=None,
        ostype=None,
        password=None,
        userName=None
    ):
        self.domain=domain
        self.liaPassword=liaPassword
        self.nodeIPs=[]
        if nodeIPs:
            for nodeIp in nodeIPs:
                self.nodeIPs.append(nodeIp)
        self.nodeName=nodeName
        self.ostype=ostype
        self.password=password
        self.userName=userName
    
    @staticmethod
    def from_dict(dict):
        """
        A convinience method that directly creates a new instance from a passed dictionary (that probably came from a
        JSON response from the server.
        """
        return ScaleIO_Node_Object(**dict)

class Primary_Mdm_Object(Im_Generic_Object):
    """
    Python object representation of a primary MDM.
    """
    
    def __init__(self,
        managementIPs=None,
        mdmIPs=None,
        node=None,
        nodeInfo=None
    ):
        # Data retrieved is a JSON representation of a primary MDM with 'node' as its root
        self.managementIPs=[]
        if managementIPs:
            for mgmtIP in managementIPs:
                self.managementIPs.append(mgmtIP)
        self.node=ScaleIO_Node_Object.from_dict(node)
        self.nodeInfo=nodeInfo
        
    @staticmethod
    def from_dict(dict):
        """
        A convinience method that directly creates a new instance from a passed dictionary (that probably came from a
        JSON response from the server.
        """
        return Primary_Mdm_Object(**dict)

class Mdm_Object(Im_Generic_Object):
    """
    Python object representation of a MDM (primary or secondary look eactly the same configuration wise).
    """
    
    def __init__(self,
        managementIPs=None,
        mdmIPs=None,
        node=None,
        nodeInfo=None
    ):
        self.managementIPs=[]
        if managementIPs:
            for mgmtIP in managementIPs:
                self.managementIPs.append(mgmtIP)
        self.node=ScaleIO_Node_Object.from_dict(node)
        self.nodeInfo=nodeInfo
        
    @staticmethod
    def from_dict(dict):
        """
        A convinience method that directly creates a new instance from a passed dictionary (that probably came from a
        JSON response from the server.
        """
        #print "*** Class Mdm_Object, from_dict(**dict) method:"
        #pprint (dict)
        return Mdm_Object(**dict)

class Tb_Object(Im_Generic_Object):
    """
    Python object representation of a TB.
    """
    
    def __init__(self,
        node=None,
        nodeInfo=None,
        tbIPs=None
    ):
        self.node=ScaleIO_Node_Object.from_dict(node)
        self.nodeInfo=nodeInfo
        self.tbIPs=[]
        if tbIPs:
            for tbIp in tbIPs:
                self.tbIPs.append(tbIp)
        
    @staticmethod
    def from_dict(dict):
        """
        A convinience method that directly creates a new instance from a passed dictionary (that probably came from a
        JSON response from the server.
        """
        #print "*** Class Tb_Object, from_dict(**dict) method:"
        #pprint (dict)
        return Tb_Object(**dict)

class Sdc_Object(Im_Generic_Object):
    """
    Python object representation of a MDM (primary or secondary look eactly the same configuration wise).
    """
    
    def __init__(self,
        node=None,
        nodeInfo=None,
        splitterRpaIp=None
    ):
        self.node=ScaleIO_Node_Object.from_dict(node)
        self.nodeInfo=nodeInfo
        self.splitterRpaIp=splitterRpaIp
        
    @staticmethod
    def from_dict(dict):
        """
        A convinience method that directly creates a new instance from a passed dictionary (that probably came from a
        JSON response from the server.
        """
        return Sdc_Object(**dict)

class Sds_Device_Object(Im_Generic_Object):
    """
    Python object representation of a MDM (primary or secondary look eactly the same configuration wise).
    """
    
    def __init__(self,
        devicePath=None,
        storagePool=None,
        deviceName=None
    ):
        self.devicePath=devicePath
        self.storagePool=storagePool
        self.deviceName=deviceName
        
    @staticmethod
    def from_dict(dict):
        """
        A convinience method that directly creates a new instance from a passed dictionary (that probably came from a
        JSON response from the server.
        """
        return Sds_Device_Object(**dict)

class Sds_Object(Im_Generic_Object):
    """
    Python object representation of a MDM (primary or secondary look eactly the same configuration wise).
    """
    
    def __init__(self,
        node=None,
        nodeInfo=None,
        sdsName=None,
        protectionDomain=None,
        faultSet=None,
        allIPs=None,
        sdsOnlyIPs=None,
        sdcOnlyIPs=None,
        devices=None,
        optimized=None,
        port=None
    ):
        self.node=ScaleIO_Node_Object.from_dict(node)
        self.nodeInfo=nodeInfo
        self.sdsName=sdsName
        self.protectionDomain=protectionDomain
        self.faultSet=faultSet
        self.allIPs=[]
        for allIp in allIPs:
            self.allIPs.append(allIp)
        self.sdsOnlyIPs=[]
        if sdsOnlyIPs:
            for sdsOnlyIp in sdsOnlyIPs:
                self.sdsOnlyIPs.append(sdsOnlyIp)
        self.sdcOnlyIPs=[]
        if sdcOnlyIPs:
            for sdcOnlyIp in sdcOnlyIPs:
                self.sdcOnlyIPs.append(sdcOnlyIp)
        self.devices=[]
        if devices:
            for device in devices:
                self.devices.append(Sds_Device_Object(device))
        self.optimized=optimized
        self.port=port
        
    @staticmethod
    def from_dict(dict):
        """
        A convinience method that directly creates a new instance from a passed dictionary (that probably came from a
        JSON response from the server.
        """
        return Sds_Object(**dict)

class Call_Home_Configuration_Object(Im_Generic_Object):
    """
    Python object representation of a MDM (primary or secondary look eactly the same configuration wise).
    """
    
    def __init__(self,
        emailFrom=None,
        mdmUsername=None,
        mdmPassword=None,
        customerName=None,
        host=None,
        port=None,
        tls=None,
        smtpUsername=None,
        smtpPassword=None,
        alertEmailTo=None,
        severity=None
    ):
        self.emailFrom=emailFrom
        self.mdmUsername=mdmUsername
        self.mdmPassword=mdmPassword
        self.customerName=customerName
        self.host=host
        self.port=port
        self.tls=tls
        self.smtpUsername=smtpUsername
        self.smtpPassword=smtpPassword
        self.alertEmailTo=alertEmailTo
        self.severity=severity
        
    @staticmethod
    def from_dict(dict):
        """
        A convinience method that directly creates a new instance from a passed dictionary (that probably came from a
        JSON response from the server.
        """
        return Call_Home_Configuration_Object(**dict)

class Remote_Syslog_Configuration_Object(Im_Generic_Object):
    """
    Python object representation of a MDM (primary or secondary look eactly the same configuration wise).
    """
    
    def __init__(self,
        ip=None,
        port=None,
        facility=None
    ):
        self.ip=ip
        self.port=port
        self.facility=facility
        
    @staticmethod
    def from_dict(dict):
        """
        A convinience method that directly creates a new instance from a passed dictionary (that probably came from a
        JSON response from the server.
        """
        return Remote_Syslog_Configuration_Object(**dict)

class ScaleIO_System_Object(Im_Generic_Object):
    """
    Root configuration object
    """
    
    def __init__(self,
        installationId=None,
        mdmIPs=None,
        mdmPassword=None,
        liaPassword=None,
        licenseKey=None,
        primaryMdm=None,
        secondaryMdm=None,
        tb=None,
        sdsList=None,
        sdcList=None,
        callHomeConfiguration=None,
        remoteSyslogConfiguration=None
        
    ):
        self.installationId=installationId
        self.mdmIPs = []
        for mdmIP in mdmIPs:
            self.mdmIPs.append(mdmIP)
        self.mdmPassword=mdmPassword
        self.liaPassword=liaPassword
        self.licenseKey=licenseKey
        self.primaryMdm=Mdm_Object.from_dict(primaryMdm)
        self.secondaryMdm=Mdm_Object.from_dict(secondaryMdm)
        self.tb=Tb_Object.from_dict(tb)
        self.sdsList=[]
        for sds in sdsList:
            self.sdsList.append(Sds_Object.from_dict(sds))
        self.sdcList=[]
        for sdc in sdcList:
            self.sdcList.append(Sdc_Object.from_dict(sdc))
        if callHomeConfiguration != None:
            self.callHomeConfiguration=Call_Home_Configuration_Object.from_dict(callHomeConfiguration)
        else:
            self.callHomeConfiguration = None
        if remoteSyslogConfiguration != None:
            self.remoteSyslogConfiguration=Remote_Syslog_Configuration_Object.from_dict(remoteSyslogConfiguration)
        else:
            self.remoteSyslogConfiguration = None
            
    def setLiaPassword(self, value):
        self.liaPassword = value
        
    def setMdmPassword(self, value):
        self.mdmPassword = value
    
    
    @staticmethod
    def from_dict(dict):
        """
        A convinience method that directly creates a new instance from a passed dictionary (that probably came from a
        JSON response from the server.
        """
        #print "*** Class ScaleIO_System_Object - .from_dict(**dict)"
        #pprint (dict)
        return ScaleIO_System_Object(**dict)
    

class Im(Im_Generic_Object):
    """
    The IM class provides a pythonic way to interact with and manage a ScaleIO cluster using Installation Manager API/
    """
    def __init__(self, api_url, username, password, verify_ssl=False, LiaPassword=None):
        """
        Initializes the class

        :param api_url: Base URL for the API.  Often the MDM host.
        :type api_url: str
        :param username: Username to login with
        :type username: str
        :param password: Password
        :type password: str
        :return: A ScaleIO object
        :rtype: ScaleIO
        """

        self._username = username
        self._password = password
        self._im_api_url = api_url
        self._im_session = requests.Session()
        #self._im_session.headers.update({'Accept': 'application/json', 'Version': '1.0'}) # Accept only json
        self._im_session.mount('https://', TLS1Adapter())
        self._im_verify_ssl = verify_ssl
        self._im_logged_in = False
        requests.packages.urllib3.disable_warnings() # Disable unverified connection warning.
        self._cluster_config_cached = None
        self._cache_contains_uncommitted = None
        
        self.SIO_Configuration_Object = None # Holds a DICT representation of the ScaleIO System Configuration

    def _get_cached_config_json(self):
        return self._cluster_config_cached
    
    def _login(self):
        """
        LOGIN CAN ONLY BE DONE BY POSTING TO A HTTP FORM.
        A COOKIE IS THEN USED FOR INTERACTING WITH THE API
        """

        self._im_session.headers.update({'Content-Type':'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'})
        #self._im_session.mount('https://', TLS1Adapter())
        #self._im_verify_ssl = False
        self.j_username = self._username
        self.j_password = self._password
        requests.packages.urllib3.disable_warnings() # Disable unverified connection warning.
        payload = {'j_username': self.j_username, 'j_password': self.j_password, 'submit':'Login'}
        
        # login to ScaleIO IM
        r = self._im_session.post(
            "{}/{}".format(self._im_api_url,"j_spring_security_check"),
            verify=self._im_verify_ssl,
            #headers = {'Content-Type':'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'},
            data=payload)
        print "Login method()"
        #print r.text
        self._im_logged_in = True
        logging.basicConfig(level=logging.DEBUG)
        
        """
        ADD CODE:
        Check if this is IM have existing configuration. If so populate ScaleIO_configurtion_object
        """
        
    def _check_login(self):
        if not self._im_logged_in:
            self._im_login()
        else:
            pass
        return None
    
    # FIX _do_get method, easier to have one place to do error handling than in all other methods that call _do_get()
    def _do_get(self, uri, **kwargs):
        """
        Convinient method for GET requests
        Returns http request status value from a POST request
        """
        #TODO:
        # Add error handling. Check for HTTP status here would be much more conveinent than in each calling method
        scaleioapi_get_headers = {'Content-type':'application/json','Version':'1.0'}
        
        if kwargs:
            for key, value in kwargs.iteritems():
                if key == 'headers':
                    scaleio_get_headersvalue = value

        try:
            #response = self._im_session.get("{}/{}".format(self._api_url, uri), headers = scaleioapi_get_headers, payload = scaleio_payload).json()
            response = self._im_session.get("{}/{}".format(self._api_url, uri), **kwargs).json()
            #response = self._session.get(url, headers=scaleioapi_post_headers, **kwargs)
            if response.status_code == requests.codes.ok:
                return response
            else:
                raise RuntimeError("_do_get() - HTTP response error" + response.status_code)
        except:
            raise RuntimeError("_do_get() - Communication error with ScaleIO gateway")
        return response

    def _do_put(self, uri, **kwargs):
        """
        Convinient method for POST requests
        Returns http request status value from a POST request
        """
        #TODO:
        # Add error handling. Check for HTTP status here would be much more conveinent than in each calling method
        scaleioapi_put_headers = {'content-type':'application/json'}
        print "_do_put()"
        if kwargs:
            for key, value in kwargs.iteritems():
                #if key == 'headers':
                #    scaleio_post_headers = value
                #    print "Adding custom PUT headers"
                if key == 'json':
                    payload = value
        try:
            #self._session.headers.update({'Content-Type':'application/json'})
            response = self._session.put(url, headers=scaleioapi_put_headers, verify_ssl=self._im_verify_ssl, data=json.dumps(payload))
            print "PUT call:"
            print response.text
            if response.status_code == requests.codes.ok:
                return response
            else:
                raise RuntimeError("_do_put() - HTTP response error" + response.status_code)
        except:
            print "PUT call response:"
            print response.text
            raise RuntimeError("_do_put() - Communication error with ScaleIO gateway")
        return response
    
    def _do_post(self, url, **kwargs):
        """
        Convinient method for POST requests
        Returns http request status value from a POST request
        """
        #TODO:
        # Add error handling. Check for HTTP status here would be much more conveinent than in each calling method
        scaleioapi_post_headers = {'Content-type':'application/json','Version':'1.0'}
        print "_dopost()"
        if kwargs:
            for key, value in kwargs.iteritems():
                if key == 'headers':
                    scaleio_post_headers = value
                    print "Adding custom POST headers"
                if key == 'files':
                    upl_files = value
                    print "Adding files to upload"
        try:
            response = self._session.post(url, headers=scaleioapi_post_headers, verify_ssl=self._im_verify_ssl, files=upl_files)
            print "POST call:"
            print response.text
            if response.status_code == requests.codes.ok:
                return response
            else:
                raise RuntimeError("_do_post() - HTTP response error" + response.status_code)
        except:
            print "POST call response:"
            print response.text
            raise RuntimeError("_do_post() - Communication error with ScaleIO gateway")
        return response
 
    def get_installation_instances(self):
        print "/types/Installation/instances/"
        resp = self._im_session.get("{}/{}".format(self._im_api_url, 'types/Installation/instances'))
        print resp.text

    def get_state(self, count=None):
        print "/types/State/instances/"
        payload = {'_':'1425822717883'}
        referer = 'https://192.168.100.12/install.jsp'
        resp = self._im_session.get("{}/{}".format(self._im_api_url, 'types/State/instances/'), params = payload)
        print "URL: " + resp.url
        print resp.text
    
    def set_state(self, state):
        # state can be: query, upload, install, configure
        if state == 'query':
            resp = self._im_session.put("{}/{}".format(self._im_api_url,"types/State/instances/"),data =json.dumps({"state":"query"}), headers={'Content-Type':'application/json'})
            print "PUT Request URL: " + resp.url
            print "QUERY Response:"
            print resp.text
            return True
        if state == 'upload':
            resp = self._im_session.put("{}/{}".format(self._im_api_url,"types/State/instances/"),data =json.dumps({"state":"upload"}), headers={'Content-Type':'application/json'})
            print "PUT Request URL: " + resp.url
            print "UPLOAD Response:"
            print resp.text
            return True
        if state == 'install':
            resp = self._im_session.put("{}/{}".format(self._im_api_url,"types/State/instances/"),data =json.dumps({"state":"install"}), headers={'Content-Type':'application/json'})
            return True
            print "PUT Request URL: " + resp.url
            print "INSTALL Response:"
            print resp.text
        if state == 'configure':
            resp = self._im_session.put("{}/{}".format(self._im_api_url,"types/State/instances/"),data =json.dumps({"state":"configure"}), headers={'Content-Type':'application/json'})
            return True
            print "PUT Request URL: " + resp.url
            print "CONFIGURE Response:"
            print resp.text
        return False
    
    def set_abort_pending(self, newstate):
        """
        Method to set Abort state if something goes wrong during provisioning
        Method also used to finish provisioning process when all is completed
        Method: POST
        """
        # NOT TO BE USED
        default_minimal_cluster_config = '{"installationId":null,"mdmIPs":["192.168.102.12","192.168.102.13"],"mdmPassword":"Scaleio123","liaPassword":"Scaleio123","licenseKey":null,"primaryMdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.12"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"managementIPs":null,"mdmIPs":["192.168.102.12"]},"secondaryMdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.13"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"managementIPs":null,"mdmIPs":["192.168.102.13"]},"tb":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.11"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"tbIPs":["192.168.102.11"]},"sdsList":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.11"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.102.11]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.102.11"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/home/vagrant/scaleio1","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.12"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.102.12]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.102.12"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/home/vagrant/scaleio1","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.13"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.102.13]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.102.13"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/home/vagrant/scaleio1","storagePool":null,"deviceName":null}],"optimized":false,"port":7072}],"sdcList":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.11"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.12"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.13"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null}],"callHomeConfiguration":null,"remoteSyslogConfiguration":null}'
        r1 = self._im_session.post(
            "{}/{}".format(self._im_api_url,"types/Command/instances/actions/abortPending"),
            headers={'Content-type':'application/json','Version':'1.0'}, 
            verify=self._im_verify_ssl,
            data = newstate,
            stream=True
        )
        if not r1.ok:
            # Something went wrong
            print "Error set_abort_pending()"
        
        print "Response after set_abort_pending()"
        # RESPONSE NEED TO BE WRAPPED IN tey/catch. Can?t assume JSON is returned.
        print r1.text
        #pprint (json.loads(r1.text))
        return r1.text

    def set_archive_all(self):
        """
        Last method to be called when provisioning is complete
        Method: POST
        """
        r1 = self._im_session.post(
            "{}/{}".format(self._im_api_url,"types/Command/instances/actions/archiveAll"),
            headers={'Content-type':'application/json','Version':'1.0'}, 
            verify=self._im_verify_ssl,
            data = '',
            stream=True
        )
        if not r1.ok:
            # Something went wrong
            print "Error set_archive_all()"
        
        print "Response after set_archive_all()"
        # RESPONSE NEED TO BE WRAPPED IN tey/catch. Can?t assume JSON is returned.
        print r1.text
        #pprint (json.loads(r1.text))
        return r1.text

    def get_version(self):
        print "/version/"
        payload = {'_':'1425822717883'}
        referer = 'https://192.168.100.12/status.jsp'
        resp = self._im_session.get("{}/{}".format(self._im_api_url, 'version/'), params = payload)
        print "URL: " + resp.url
        print resp.text    
        
    def get_installation_packages_latest(self):
        """
        In 1.31-256 getting latest or all packages seem not to work. Always same result not matter what value 'onlLatest' have. Same situation in IM WEBUI too.
        """
        parameter = {'onlyLatest':'False'}
        resp = self._im_session.get("{}/{}".format(self._im_api_url, 'types/InstallationPackageWithLatest/instances'), params=parameter)
        #resp = self._im_session.get('https://192.168.100.52/types/InstallationPackageWithLatest/instances', params=parameter)
        jresp = json.loads(resp.text)

        pprint(jresp)

    def get_installation_packages(self):
        """
        In 1.31-256 getting latest or all packages seem not to work. Always same result not matter what value 'onlLatest' have. Same situation in IM WEBUI too.
        """
        parameter = {'onlyLatest':'False'}
        resp = self._im_session.get("{}/{}".format(self._im_api_url, 'types/InstallationPackageWithLatest/instances'), params=parameter)
        #resp = self._im_session.get('https://192.168.100.52/types/InstallationPackageWithLatest/instances', params=parameter)
        jresp = json.loads(resp.text)
        pprint(jresp.text)

    def get_command(self, count=None):
        print "/types/Command/instances"
        payload = {'_':'1425822717883'}
        resp = self._im_session.get("{}/{}".format(self._im_api_url, 'types/Command/instances/'), params = payload)
        #resp = self._im_session.get('https://192.168.100.42/types/Command/instances').json()
        print "URL: " + resp.url
        pprint (resp.text)
        
    def get_nodeinfo_instances(self):
        print "/types/NodeInfo/instances/actions/downloadGetInfo"
        resp = self._im_session.get("{}/{}".format(self._im_api_url, 'types/NodeInfo/instances/actions/downloadGetInfo'))
        #resp = self._im_session.get('https://192.168.100.42/types/NodeInfo/instances/actions/downloadGetInfo')
        pprint (resp.text)

    def get_configuration_instances(self, count=None):
        print "/types/Configuration/instances"
        payload = {'_':''}
        resp = self._im_session.get("{}/{}".format(self._im_api_url, 'types/Configuration/instances/'))
        #resp = self._im_session.get('https://192.168.100.42/types/Configuration/instances')
        pprint (resp.text)

    def get_cluster_topology(self, mdmIP, mdmPassword, liaPassword=None):
        # Topology is returned as a file. Save it into a string. Parse as JSON.
        # When adding nodes to existing ScaleIO cluster using IM all node change are driven by changing topology CSV file.
        
        
        #print "Get Topology - Import into ScaleIO_Configuration_Object"
        
        #print "IM SESSION OBJECT:"
        #pprint (self._im_session)
        
        pay1 = {'mdmIps':[mdmIP],'mdmPassword':mdmPassword} #,'liaPassword':liaPassword}
        #pay1 = {'mdmIp':'192.168.100.42','mdmPassword':'Password1!','liaPassword':'Password1!'}
        r1 = self._im_session.post(
            "{}/{}".format(self._im_api_url,"types/Configuration/instances/actions/refreshAndGet"),
            headers={'Content-type':'application/json','Version':'1.0'},
            verify=self._im_verify_ssl,
            json=pay1,
            stream=True
        )
        if not r1.ok:
            # Something went wrong
            print "Error retrieving get_cluster_topology()"
        
        print "*** get_cluster_topology() ***"
        pprint (json.loads(r1.text))
        return r1.text
    
    def retrieve_scaleio_cluster_configuration(self, mdmIP, mdmPassword, liaPassword=None):
        sysconf_json = self.get_cluster_topology(mdmIP, mdmPassword, liaPassword)
        a = ScaleIO_System_Object.from_dict(json.loads(sysconf_json))
        a.setMdmPassword(mdmPassword)
        a.setLiaPassword(liaPassword)
        self._cluster_config_cached = a
        self._cache_contains_uncommitted = False

    def populate_scaleio_cluster_configuration_cache(self, mdmIP, mdmPassword, liaPassword=None):
        sysconf_json = self.get_cluster_topology(mdmIP, mdmPassword, liaPassword)
        confObj = ScaleIO_System_Object.from_dict(json.loads(sysconf_json))
        confObj.setMdmPassword(mdmPassword)
        confObj.setLiaPassword(liaPassword)
        self._cluster_config_cached = confObj
        self._cache_contains_uncommitted = False

    def write_cluster_config_to_disk(self):
        with open("cache.json", "w") as file:
            file.write(self._cluster_config_cached.to_JSON())
            file.close()
    
    def read_cluster_config_from_disk(self, filename = None):
        
        if filename:
            with open(filename, "r") as file:
                #result = file.read()
                confObj = ScaleIO_System_Object.from_dict(json.loads(file.read()))
                file.close()
        else:
            with open("cache.json", "r") as file:
                #result = file.read()
                confObj = ScaleIO_System_Object.from_dict(json.loads(file.read()))
                file.close()
        self._cluster_config_cached = confObj
        self._cache_contains_uncommitted = False

    #def push_cached_cluster_configuration(self, jsonstring, mdmPassword, liaPassword, noUpload = False, noInstall= False, noConfigure = False):
    def push_cached_cluster_configuration(self, mdmPassword, liaPassword, noUpload = False, noInstall= False, noConfigure = False):
        """
        Method push cached ScaleIO cluster configuration to IM (reconfigurations that have been made to cached configuration are committed using IM)
        Method: POST
        https://192.168.100.51/types/Installation/instances/?noUpload=false&noInstall=false&noConfigure=false
        Attach JSON cluster configuration as request payload (data). Add MDM and LIA passwords)
        """
        config_params = {'noUpload': noUpload, 'noInstall': noInstall, 'noConfigure':noConfigure}
        print "Push cached ScaleIO cluster configuration to IM"
        self._cluster_config_cached.setMdmPassword(mdmPassword)
        self._cluster_config_cached.setLiaPassword(liaPassword)
        pprint (self._cluster_config_cached.to_JSON())

        # NOT TO BE USED - Fix JSON dump to IM accepted format. COMPARE WHAT THIS CLASS DUMP TO WHAT THE INSTALLER CREATE IN BELOW JSON STRING
        #default_minimal_cluster_config = '{"installationId":null,"mdmIPs":["192.168.102.12","192.168.102.13"],"mdmPassword":"Scaleio123","liaPassword":"Scaleio123","licenseKey":null,"primaryMdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.12"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"managementIPs":null,"mdmIPs":["192.168.102.12"]},"secondaryMdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.13"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"managementIPs":null,"mdmIPs":["192.168.102.13"]},"tb":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.11"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"tbIPs":["192.168.102.11"]},"sdsList":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.11"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.102.11]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.102.11"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/home/vagrant/scaleio1","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.12"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.102.12]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.102.12"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/home/vagrant/scaleio1","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.13"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.102.13]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.102.13"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/home/vagrant/scaleio1","storagePool":null,"deviceName":null}],"optimized":false,"port":7072}],"sdcList":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.11"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.12"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.13"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null}],"callHomeConfiguration":null,"remoteSyslogConfiguration":null}'
        default_minimal_cluster_config = '{"installationId":null,"mdmIPs":["192.168.102.12","192.168.102.13"],"mdmPassword":"Scaleio123","liaPassword":"Scaleio123","licenseKey":null,"primaryMdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.12"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"managementIPs":null,"mdmIPs":["192.168.102.12"]},"secondaryMdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.13"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"managementIPs":null,"mdmIPs":["192.168.102.13"]},"tb":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.11"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"tbIPs":["192.168.102.11"]},"sdsList":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.11"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.102.11]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.102.11"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdc","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.12"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.102.12]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.102.12"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdc","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.13"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.102.13]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.102.13"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdc","storagePool":null,"deviceName":null}],"optimized":false,"port":7072}],"sdcList":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.11"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.12"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.102.13"],"domain":null,"userName":"root","password":"vagrant","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null}],"callHomeConfiguration":null,"remoteSyslogConfiguration":null}'
        #default_minimal_cluster_config = '{"installationId":null,"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","liaPassword":"Password1!","licenseKey":null,"primaryMdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"managementIPs":null,"mdmIPs":["192.168.100.51"]},"secondaryMdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"managementIPs":null,"mdmIPs":["192.168.100.52"]},"tb":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"tbIPs":["192.168.100.53"]},"sdsList":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.100.51]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.51"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.100.52]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.52"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.100.53]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.53"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072}],"sdcList":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null}],"callHomeConfiguration":null,"remoteSyslogConfiguration":null}'
        
        r1 = self._im_session.post(
            "{}/{}".format(self._im_api_url,"types/Installation/instances/"),
            headers={'Content-type':'application/json','Version':'1.0'},
            params = config_params, 
            verify=self._im_verify_ssl,
            #json=json.loads(self._cluster_config_cached.to_JSON()),
            json = json.loads(default_minimal_cluster_config),
            stream=True
        )
        if not r1.ok:
            # Something went wrong
            print "Error push_cached_cluster_configuration()"
        
        print "Response after push_cached_cluster_configuration()"
        
        # RESPONSE NEED TO BE WRAPPED IN tey/catch. Can?t assume JSON is returned.
        print r1.text
        #pprint (json.loads(r1.text))
        return r1.text
    
    def add_sds_to_cluster(self, sdsobject):
        self._cluster_config_cached.sdsList.append(sdsobject)
        self._cache_contains_uncommitted = True
                
    def create_minimal_scaleio_cluster(self, setMdmPassword, setLiaPassword):
        """
        Using IM this method create a 3-node ScaleIO cluster with 2xMDM, 1xTB, 3x SDS (using /dev/sdb), 3x SDC
        """
        self.read_cluster_config_from_disk("minimal-cluster.json")
        #self._cluster_config_cached.setMdmPassword(setMdmPassword)
        #self._cluster_config_cached.setLiaPassword(setLiaPassword)
        self.push_cached_cluster_configuration(setMdmPassword, setLiaPassword)
    
    # Add API client methods here that interact with IM API
    @property
    def system(self): # Change to something that is usable. A Class for Generate CSV for example.
        pass
    
    def uploadPackages(self, directory):        
        """
        Not working. Am not able ot figure out how to upload. IT return status 200OK with this code but do not store the files.
        In tomcat.log (IM) there?s a complaint about character encoding whn uploading file. Not sure how to rectiy it in requests post call though
        """
        files_to_upload_dict = {}
        files_to_upload_list = [ f for f in listdir(directory) if isfile(join(directory,f)) ]

        print "Files to upload:"
        for index in range(len(files_to_upload_list)):
            print "  " + files_to_upload_list[index]
            self.uploadFileToIM (directory, files_to_upload_list[index], files_to_upload_list[index])
            #file_tuple = {'files':{str(files_to_upload_list[index]), open(directory + files_to_upload_list[index], 'rb'), 'application/x-rpm'}}      
            #file_tuple = {str(files_to_upload_list[index]), {open(directory + files_to_upload_list[index], 'rb'), 'application/x-rpm'}}
            #file_tuple = {'files': (str(files_to_upload_list[index]), open(directory + files_to_upload_list[index], 'rb'), 'application/x-rpm')}
            #file_tuple = (str(files_to_upload_list[index]), open(directory + files_to_upload_list[index], 'rb'))
            #file_tuple = {str(files_to_upload_list[index]), open(directory + files_to_upload_list[index], 'rb'), 'application/x-rpm'}
            #files_data_to_upload_list.append(file_tuple)
        print "No more files"
        #print "Files to upload Dictionary:"

        
    def uploadFileToIM (self, directory, filename, title):
        """
        Parameters as they look in the form for uploading packages to IM
        """
        parameters = {'data-filename-placement':'inside',
                      'title':str(filename),
                      'filename':str(filename),
                      'type':'file',
                      'name':'files',
                      'id':'fileToUpload',
                      'multiple':''
                      }
        file_dict = {'files':(str(filename), open(directory + filename, 'rb'), 'application/x-rpm')}
        m = MultipartEncoder(fields=file_dict)
        
        #c_type  = m.content_type + '; charset=UTF-8'
        #upload_headers={'Referer':'https://192.168.100.42/packages.jsp'}
        #self._im_session.headers.update("")
        #self._im_session.mount('https:
        
        
        temp_username = self._username
        temp_password = self._password
        temp_im_api_url = self._im_api_url
        temp_im_session = requests.Session()
        #self._im_session.headers.update({'Accept': 'application/json', 'Version': '1.0'}) # Accept only json
        temp_im_session.mount('https://', TLS1Adapter())
        temp_im_verify_ssl = self._im_verify_ssl


        resp = temp_im_session.post(
        #resp = self._do_post(
            "{}/{}".format(temp_im_api_url,"types/InstallationPackage/instances/uploadPackage"),
            auth=HTTPBasicAuth('admin', 'Password1!'),
            #headers = m.content_type,
            files = file_dict,
            verify = False,
            data = parameters
            )
                
    def deleteFileFromIM(self, filename):
        pass
        """
        Request URL:https://192.168.100.42/instances/InstallationPackage::EMC-ScaleIO-tb-1.31-260.3.el6.x86_64.rpm/
        Request Method:DELETE
        """
    
    def uploadCsvConfiguration(self, conf_filename):
        """
        NOT NEEDED. JSON can be POSTed to IM instead of sending a CSV that is locally parsed and converted to JSON.
        
        Remote Address:192.168.100.51:443
        Request URL:https://192.168.100.51/types/Configuration/instances/actions/parseFromCSV
        Request Method:POST
        Status Code:200 OK
        Request Headersview source
        Accept:*/*
        Accept-Encoding:gzip, deflate
        Accept-Language:en-US,en;q=0.8,sv;q=0.6
        Connection:keep-alive
        Content-Length:433
        Content-Type:multipart/form-data; boundary=----WebKitFormBoundaryY1f2eTo1mOvh744k
        Cookie:JSESSIONID=A0823886072B2CEBA327A9185AC2BFE0
        Host:192.168.100.51
        Origin:https://192.168.100.51
        Referer:https://192.168.100.51/install.jsp
        User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36
        X-Requested-With:XMLHttpRequest
        Request Payload
        ------WebKitFormBoundaryY1f2eTo1mOvh744k
        Content-Disposition: form-data; name="file"; filename="ScaleIO_Minimal_Config_51.csv"
        Content-Type: text/csv

        """
        parameters = {'selectInstallOrExtend':'install', #'install' or 'extend'
                      'name':'file',
                      'id':'fileToUpload',
                      'filename':'config.csv'
                      }
        file_dict = {'file':('config.csv', open(conf_filename, 'rb'), 'text/csv')}
        """
        files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
        """
        
        temp_username = self._username
        temp_password = self._password
        temp_im_api_url = self._im_api_url
        temp_im_session = requests.Session()
        #self._im_session.headers.update({'Accept': 'application/json', 'Version': '1.0'}) # Accept only json
        temp_im_session.mount('https://', TLS1Adapter())
        temp_im_verify_ssl = self._im_verify_ssl


        resp = temp_im_session.post(
        #resp = self._do_post(
            "{}/{}".format(temp_im_api_url,"types/Configuration/instances/actions/parseFromCSV"),
            auth=HTTPBasicAuth('admin', 'Password1!'),
            #headers = m.content_type,
            files = file_dict,
            verify = False,
            data = parameters
            )
        pprint (resp)
     
    def getInstallerUrl(self):
        pass

##======================================================
#       ScaleIO IM Installation process State Machine
##======================================================

##===============================================
## TRANSITIONS

class Transition(object):
	# Code executed when transitioning from one state to another
	def __init__(self, toState):
		self.toState = toState
		
	def Execute(self):
		print ("Transitioning...")
		print ""


##===============================================
## STATES

class State(object):
	# The base template state which all others will inherit from
	def __init__(self, FSM, im_inst):
		self.FSM = FSM
		self.timer = 0
		self.startTime = 0
		im_instance = im_inst
		# Possible states: IDLE, PENDING, FAILED, COMPLETED
		#print self.FSM.getCurrentStateStatus()
		
	def Enter(self):
		self.FSM.setCurrentStateStatus('PENDING')
		pass
	
	def Execute (self):
		pass
	
	def status (self):
		pass
	
	def Next(self):
		pass
	
	def Exit(self):
		pass

class Query(State):
	# Worker class - Takes care of managing IM QUERY phase and do status control of each phase
	def __init__(self, FSM, im_inst):
		super(Query, self).__init__(FSM, im_inst)
		self.calling_object = im_inst
		
	def Enter(self):
		print ("Entering QUERY phase")
		super(Query, self).Enter()

	def Execute (self):
		print ("Start ScaleIO IM Query phase")
		self.FSM.imapi.set_state('query')
		time.sleep(15)

		self.Next()
		if self.FSM.autoTransition:
			self.FSM.Execute()

	def Next(self):
		print ("Advance to next step")
		self.FSM.ToTransition("toUPLOAD") # Move to next step
		
	def Exit(self):
		print ("Exiting QUERY phase.")

class Upload(State):
	# Worker class - Takes care of managing IM QUERY phase and do status control of each phase
	def __init__(self, FSM, im_inst):
		super(Upload, self).__init__(FSM, im_inst)
		
	def Enter(self):
		print ("Entering UPLOAD phase")
		super(Upload, self).Enter()

	def Execute (self):
		print ("Upload of binaries to nodes")
		# Call set_state
		self.FSM.imapi.set_state('upload') # Set IM to UPLOAD state
		time.sleep(60)
		
		self.Next()
		if self.FSM.autoTransition:
			self.FSM.Execute()
	
	def Next(self):
		print ("Advance to next step")
		self.FSM.ToTransition("toINSTALL") # Move to next step
		
	def Exit(self):
		print ("Exiting UPLOAD phase.")


class Install(State):
	# Worker class - Takes care of managing IM QUERY phase and do status control of each phase
	def __init__(self, FSM, im_inst):
		super(Install, self).__init__(FSM, im_inst)
		
	def Enter(self):
		print ("Entering install phase")
		super(Install, self).Enter()

	def Execute (self):
		print ("Installing ScaleIO binaries")
		# Call set_state
		self.FSM.imapi.set_state('install') # Set IM to QUERY state
		time.sleep(60)
		
		self.Next()
		if self.FSM.autoTransition:
			self.FSM.Execute()
			
	def Next(self):
		print ("Advance to next step")
		self.FSM.ToTransition("toCONFIGURE") # Move to next step
		
	def Exit(self):
		print ("Exiting INSTALL phase.")


class Configure(State):
	# Worker class - Takes care of managing IM QUERY phase and do status control of each phase
	def __init__(self, FSM, im_inst):
		super(Configure, self).__init__(FSM, im_inst)
		
	def Enter(self):
		print ("Entering configure phae")
		super(Configure, self).Enter()

	def Execute (self):
		print ("Configure ScaleIO cluster")
		# Call set_state
		self.FSM.imapi.set_state('configure') # Set IM to QUERY state
		time.sleep(60)
		
		self.Next()
		if self.FSM.autoTransition:
			self.FSM.Execute()
		
	def Next(self):
		print ("Advance to next step")
		self.FSM.ToTransition("toARCHIVE") # Move to next step
		
	def Exit(self):
		print ("Exiting CONFIGURE phase.")

class Archive(State):
	# Worker class - Takes care of managing IM QUERY phase and do status control of each phase
	def __init__(self, FSM, im_inst):
		super(Archive, self).__init__(FSM, im_inst)
		
	def Enter(self):
		print ("Entering archive phase")
		super(Archive, self).Enter()

	def Execute (self):
		print ("Completing ScaleIO cluster install")
		#print ("Execute self.set_archive_all()")
		self.FSM.imapi.set_archive_all()
		time.sleep(10)
		
		self.Next()
		if self.FSM.autoTransition:
			self.FSM.Execute()
		
	def Next(self):
		print ("Advance to next step")
		self.FSM.ToTransition("toCOMPLETE") # Move to next step
		
	def Exit(self):
		print ("Exiting ARCHIVE phase.")

class Complete(State):
	# Worker class - Takes care of managing IM QUERY phase and do status control of each phase
	def __init__(self, FSM, im_inst):
		super(Complete, self).__init__(FSM, im_inst)
		
	def Enter(self):
		print ("Entering COMPLETE phase")
		super(Complete, self).Enter()

	def Execute (self):
		print ("Installation complete!")
		self.FSM.setCurrentStateStatus('COMPLETED')
		print self.FSM.getCurrentStateStatus()
		self.FSM.imapi.get_state()
		
	def Next(self):
		self.FSM.setCurrentStateStatus('COMPLETED')

	def Exit(self):
		print ("Exiting COMPLETE phase.")

##===============================================
## FINITE STATE MACHINE

class FSM(object):
	# Holds the states and transitions available, 
	# executes current states main functions and transitions
	def __init__(self, imapi):
		self.states = {}
		self.transitions = {}
		self.curState = None
		self.prevState = None ## USE TO PREVENT LOOPING 2 STATES FOREVER
		self.trans = None
		self.autoTransition = False
		self.completed = False
		self.curStateStatus = 'IDLE'
		self.imapi = imapi

	def AddTransition(self, transName, transition):
		self.transitions[transName] = transition
		
	def enableAutoTransition(self):
		self.autoTransition = True
	
	def disableAutoTransition(self):
		self.autoTransition = False

	def AddState(self, stateName, state):
		self.states[stateName] = state

	def SetState(self, stateName):
		self.prevState = self.curState
		self.curState = self.states[stateName]
	
	def getState(self):
		return curState
	
	def setCurrentStateStatus(self, status):
		print "*** Setting currentStateStatus to " + status + " ***" 
		self.curStateStatus = status
		if status == 'COMPLETED':
			self.trans = None
		#	self.curState = None
		print "setCurrentStateStatus() = " + self.curStateStatus
	
	def getCurrentStateStatus(self):
		return self.curStateStatus
		# Return IDLE, FAILED, PENDING, COMPLETE
		
	def ToTransition(self, toTrans):
		self.trans = self.transitions[toTrans]

	def Next(self):
		if self.curStateStatus == 'IDLE' or self.curStateStatus == 'PENDING':
			self.curState.Next()
			if self.autoTransition:
				self.Execute()
		else:
			self.trans = None
			print " Status is COMPLETE - Next() will not do anything"
			
	def Execute(self):
		print "FSM Execute() - curStateStatus = " + self.curStateStatus
		if self.curStateStatus == 'IDLE' or self.curStateStatus == 'PENDING':
			self.setCurrentStateStatus('PENDING')
			if (self.trans):
				self.curState.Exit()
				self.trans.Execute()
				self.SetState(self.trans.toState)
				self.curState.Enter()
				self.trans = None
			self.curState.Execute()
		else:
			print "Status is COMPLETE"
			self.trans = None
##===============================================
## IMPLEMENTATION

Char = type("Char", (object,), {})

class InstallerFSM:
	# Base character which will be holding the Finite State Machine,
	# which in turn will hold the states and transitions.
	def __init__(self, imapi, automatic=False):
		self.FSM = FSM(imapi)
		if automatic:
			self.FSM.enableAutoTransition()
			
		## STATES
		self.FSM.AddState("QUERY", Query(self.FSM, imapi))
		self.FSM.AddState("UPLOAD", Upload(self.FSM, imapi))
		self.FSM.AddState("INSTALL", Install(self.FSM, imapi))
		self.FSM.AddState("CONFIGURE", Configure(self.FSM, imapi))
		self.FSM.AddState("ARCHIVE", Archive(self.FSM, imapi))
		self.FSM.AddState("COMPLETE", Complete(self.FSM, imapi))

		## TRANSITIONS
		self.FSM.AddTransition("toQUERY", Transition("QUERY"))
		self.FSM.AddTransition("toUPLOAD", Transition("UPLOAD"))
		self.FSM.AddTransition("toINSTALL", Transition("INSTALL"))
		self.FSM.AddTransition("toCONFIGURE", Transition("CONFIGURE"))
		self.FSM.AddTransition("toARCHIVE", Transition("ARCHIVE"))
		self.FSM.AddTransition("toCOMPLETE", Transition("COMPLETE"))
		
		self.FSM.SetState("QUERY") # When executing FSM first time always start at QUERY phase
	
	def Next(self):
		self.FSM.Next()
	
	def getCurrentStateStatus(self):
		return self.FSM.getCurrentStateStatus()
		
	def Execute(self):
		self.FSM.Execute()


##===============================================
## IM Integration Implmentation  

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s: %(levelname)s %(module)s:%(funcName)s | %(message)s', level=logging.WARNING)
    
    # If one want to attach to a ScaleIO lab environment remotely and have only SSH as access mechanism:
    # Attach to SSH server with local port forward: ssh -L 4443:192.168.100.42:443 <host>
    # Change Class initialization below to Im("https://localhost:4443, "", "") if running over SSH tunnel - As above running remotely against lab
    #imconn = Im("https://192.168.100.51","admin","Password1!",verify_ssl=False) # "Password1!") # HTTPS must be used as there seem to be an issue with 302 responses in Requests when using POST

    imconn = Im("https://192.168.102.12","admin","Scaleio123",verify_ssl=False) # "Password1!") # HTTPS must be used as there seem to be an issue with 302 responses in Requests when using POST

    imconn._login() # WORKS!

    #imconn.get_installation_packages_latest() # Always return all uploaded packages. Seem versioning does not work. At least not in ScaleIO 1.31.256 (IM)
    
    #imconn.uploadCsvConfiguration('/Users/swevm/Downloads/RHEL6_260/51_config.csv') # WORKS??? - Dont think it worksm 20150205
    
    ### UPLOAD RPM PACKAGES TO BE DEPLOYED BY IM ###
    #imconn.uploadPackages('/Users/swevm/Downloads/RHEL6_1277/') # WORKS!
    #imconn.get_installation_packages_latest() # WORKS with issues. Only return all packages not latest. Seem to be a bug in IM
    im_installer = InstallerFSM(imconn, True)
    
    print "***  State  ***"
    print imconn.get_state()
    print "*** Command State ***"
    print imconn.get_command()
    print "*** Version ***"
    print imconn.get_version()
    print ""
    print ""
    
    #Get ScaleiIO cluster configuration from IM - Populate class cache
    #imconn.populate_scaleio_cluster_configuration_cache("192.168.102.12", "Scaleio123", "Scaleio123") # Populate confiugration cache
    #imconn.cache_config_to_disk() # Create persistent copy of cluster configuration in JSON format

    ####################
    # INSTALLER STAGES #
    ####################
    
    #1
    #imconn.read_cluster_config_from_disk() # Read cluster confiuguration from disk and populate configuration cache.
    
    ### Only create_minimal_scaleio_cluster() works atm
    #imconn.push_cached_cluster_configuration(imconn.get_cached_cluster_configuration_json(), 'Password1!', 'Password1!') # NEED TESTING - Send configuration to IM to start installation
    
    ### RERUN IM INSTALL PROCESS - EXTRACT JSON CONFIG TO FIND OUT WHERE DEVICE(S) TO BE USED BY SDS NODES ARE CONFIGURED TO ALLOW CREATING A BASIC MINIMUM 3 NODE CLUSTER WITH VAGRANT
    print "Create minimal cluster - with static JSON"
    imconn.create_minimal_scaleio_cluster("Password1!", "Password1!")


    #print "*** Set QUERY state ***"
    #2
    #imconn.set_state('query')
    #2
    #imconn.set_state('upload')    
    #3
    #imconn.set_state('install')
    #4
    #imconn.set_state('configure')
    #5
    #imconn.set_state('query') # - SEEM NOT TO BE NEEDED TO CALL IN ORDER TO MARK INSTALL PROCESS AS COMPLETE
    #6
    #imconn.set_abort_pending('null') # - SEEM NOT TO BE NEEDED TO CALL IN ORDER TO MARK INSTALL PROCESS AS COMPLETE Not sure why this is part of the Finish process during installation - Is this also used to abort failed stages????
    #7
    #imconn.set_archive_all() # THIS MARK INSTALL PROCESS FINSHED AND COMPLETED
    
    print "Start Install process!!!"
    im_installer.Execute() # Start install process
    
    print "***  State  ***"
    print imconn.get_state()
    print "*** Command State ***"
    print imconn.get_command()
    
    #print "***  State  ***"
    #print imconn.get_state()
        
    print ""
    print ""
    #print "***** get_cached_cluster_configuration_json() *****"
    #print imconn._cluster_config_cached.to_JSON() # Works. to_JSON implemented as a method for all classes that inherit from ScaleIO base class   
    
   