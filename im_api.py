# ScaleIO Installation Manager API

IMPORTANT: This API is not public!!! I reverse engineered ut to proove how Python can be used to manage a ScaleIO cluster using
the IM API instead of the builtin web interface.


Install process:
Install using this web interface:
    Upload the installation packages to the Installation Manager.
    Upload a CSV topology file, review it, and initiate the installation.
    Monitor and approve the installation progress.


## Install Cluster process
Login to IM
Upload install pkgs
Upload CSV containing new cluster configuration
Initiate Install
    Set credentials for MDM
    Set credentials for IM
    Configure Advanced settings and call home as well
Complete Install
    Monitor status
    Acknowledge on when completed status
Start upload phase
    Monitor status
Start install phase
    Monitor status
Start configuration phase
    Monitor status

    
    

## Expand Cluster process

## Upgrade exising Cluster



## IM API methods



### getSErverVersion
```
function getServerVersion(successHandler)^M
{^M
    $.ajax({^M
        url: "/version",^M
        type: "GET",^M
        cache: false,^M
```

### sendGlobalCommand
```
/ valid commands: abort --> abortPending | archive --> archiveAll | retry --> retryFailed^M
function sendGlobalCommand(command, successHandler, extraParam)^M
{^M
    $.ajax({^M
        url: "/types/Command/instances/actions/" + command,^M
        type: "POST",^M
        data: JSON.stringify(extraParam),^M
        contentType: "application/json",^M
        cache: false,^M
        processData:false,^M

```


### uploadCSVConfigurationFilen
```
^M
        this.removeChild(this.children[1]); // remove the select element - it confuses IE browsers^M
        var formURL = this.getAttribute("action");^M
        var formData = new FormData(this);^M
^M
        $.ajax({^M
            url: formURL,^M
            type: "POST",^M
            data: formData,^M
            mimeType:"multipart/form-data",^M
            contentType: false,^M
            cache: false,^M
            processData:false,^M
            success: function(data, textStatus, jqXHR)^M
```



### getInstallerUrl
```
function getInstallerURL()^M
{^M
    var skipUpload = $("#skipUploadId").prop('checked');^M
    var skipInstall = $("#skipInstallId").prop('checked');^M
    var skipConfig = $("#skipConfigId").prop('checked');^M
    ^M
    var installerUrl = "/types/Installation/instances/" +^M
        "?noUpload=" + skipUpload +^M
        "&noInstall=" + skipInstall +^M
        "&noConfigure=" + skipConfig;^M
^M
    // debug only^M
    var sdsInstances = $("#sdsInstances").val();^M
    if (sdsInstances != 0)^M
    {^M
        installerUrl += "&sdsInstances=" + $("#sdsInstances").val();^M
    }^M
^M
    if (isExtendOperation())^M
    {^M
        installerUrl += "&extend=true";^M
    }^M
^M
    return installerUrl;^M
}^M
```



### getInstallerUrl (POST - This seem to start the install process with a JSON config payload)
```


                    serverConfigJSON.remoteSyslogConfiguration =^M
                    {^M
                        ip : $("#syslogHost").val(),^M
                        port: $("#syslogPort").val(),^M
                        facility: $("#facilitySelect").val()^M
                    };^M
                    
                    
                    
                serverConfigJSON.callHomeConfiguration = {^M
^M
                    emailFrom: $("#callHomeEmailFrom").val(),^M
                     mdmUsername: $("#callHomeMdmUsername").val(),^M
                     mdmPassword: $("#callHomeMdmPassword").val(),^M
                     customerName: $("#callHomeCustomer").val(),^M
                     host: $("#smtpHost").val(),^M
                     port: parseInt($("#smtpPort").val()),^M
                     tls: $("#useTls").prop('checked'),^M
                     smtpUsername: $("#smtpUser").val(),^M
                     smtpPassword: $("#smtpPassword").val(),^M
                     alertEmailTo: $("#callHomeEmailTo").val(),^M
                     severity: $("#severitySelect").val()^M
                }^M
            }^M
            setServerState({ state : ServerState.QUERY },^M
                function() { showAppendedMessage("Querying the nodes once again to validate configuration...");} );^M
            $.ajax({^M
                url: getInstallerURL(),^M
                type: "POST",^M
                data: JSON.stringify(serverConfigJSON),             ^M
                contentType: "application/json",^M
                cache: false,^M
                processData:false,^M
                success: function(data, textStatus, jqXHR)^M
                {^M






function setServerState(newStateJson, successHandler)^M
{^M
      $.ajax({^M
            url: "/types/State/instances/",^M
            type: "PUT",^M
            data: JSON.stringify(newStateJson),^M
            contentType: "application/json",^M
            cache: false,^M




### General IM API stuff
var ServerGlobalCommand = { "ABORT_PENDING" : "abortPending", "ARCHIVE" : "archiveAll", "RETRY" : "retryFailed" };^M
var ajaxResponseContent = { "EMPTY_IS_ERROR": "empty", "NON_EMPTY_IS_ERROR": "non_empty"};^M
^M
var PENDING = "PENDING";^M
var RUNNING = "RUNNING";^M
var COMPLETE = "COMPLETE";^M
^M
var isPhaseComplete =^M
{^M
    "install": PENDING,^M
    "upload":PENDING,^M
    "configure":PENDING,^M
    "query":PENDING,^M
    "clean": PENDING^M
};^M
^M
var stateOrderMap =^M
{^M
    idle: ["upload", "install", "configure", "query", "clean"],^M
    uninstall: [ "query", "clean"],^M
    install: [ "query", "upload", "install", "configure"],^M
    upgrade: [ "query", "upload", "install"],^M
    getInfo: ["query"],^M
    configureCallHome: ["configure"],^M
    queryNodes: ["query"],^M
    getConfiguration: ["query"],^M
    unknown: ["query"]^M
};^M
^M
var operationsThatRequireNotification = [ "uninstall", "install", "upgrade", "getInfo" ];^M
^M








function refreshAndGet(mdmCredentialsJSON)^M
{^M
    hidePreviousMessages();^M
    curRunningAjax =  $.ajax(^M
    {^M
        url: "/types/Configuration/instances/actions/refreshAndGet",^M
        type: "POST",^M
        data: JSON.stringify(mdmCredentialsJSON),^M
        contentType: "application/json; charset=utf-8",^M
        cache: false,^M
        processData:false,^M
        
        
        
        

#######  CODE STUFF #######


    """
    Request:
    https://192.168.100.42/version?_=1422195679298
    
    Parameters:
        version: <installId>
    
    Response:
    {"major":"1","minor":"31","revision":"2","build":"256","serverTime":"2015-01-25T14:20:50.021Z","buildTime":"2014-12-01 16:43"}
    
    """
    
    """
    Request:
    https://192.168.100.42/types/State/instances/?_=1422195679301
    Parameters:
    ? What is the parameter in the request above. It is similar but a bit different for every request that I got from Goolge Chrome Dev Tools.
    Looks like om sequence ID, but I am unable to fins trace of a sequence ID in any response so atm I don+t know how this one is generated.
    
    Response:
    {"state":"query","operation":"upgrade"}
    
    
    Call to this API method happen in status.jsp:
            function getAndDisplayProgress()
        {
            $.ajax({
                url: '/types/Command/instances/',
                type: "GET",
                cache: false,
                processData:false,
                success: function(data, textStatus, jqXHR)
                {
                    debug("success: " + data + " , " + textStatus + " , " + jqXHR.responseText );
                    if (!IsAjaxResponseErroneous(jqXHR,"retrieving installation progress",ajaxResponseContent.EMPTY_IS_ERROR))
                    {
                        updateGridAndSummary(data);
                    }
                },
                error: function (data, textStatus, jqXHR)
                {
                    debug("ERR " + data + " , " + textStatus + " , " + jqXHR.error);
                    showError("Error retreving installation progress: " + jqXHR + "," + textStatus );
                }
            });
        }
    
    And in common.js:
    function getOutstandingCommandsInServer(callback)^M
{^M
    $.ajax({^M
        url: '/types/Command/instances/',^M
        type: "GET",^M
        cache: false,^M
        processData:false,^M
        success: function(data, textStatus, jqXHR)^M
        {^M
            debug("success: " + data + " , " + textStatus + " , " + jqXHR.responseText );^M
            if (!IsAjaxResponseErroneous(jqXHR,"retrieving server status: ",ajaxResponseContent.EMPTY_IS_ERROR))^M
            {^M
                // somehow "hacky" solution:^M
                // count "pending" versus "completed"^M
                var pendingCount = 0;^M
                var pendingList = JSON.stringify(data).match(/"pending"/g);^M
                if (pendingList)^M
                {^M
                    pendingCount = pendingList.length;^M
                }^M
                var completedCount = 0^M
                var completedList = JSON.stringify(data).match(/"completed"/g);^M
                if (completedList)^M
                {^M
                    completedCount = completedList.length;^M
                }^M
                if (callback) { callback(pendingCount,completedCount); }^M
            }^M
        },^M
        error: function (data, textStatus, jqXHR)^M
        {^M
            debug("ERR " + data + " , " + textStatus + " , " + jqXHR.error);^M
            showError("Error retrieving server status: " + jqXHR + "," + textStatus );^M
            if (callback) { callback(-1,-1); }^M
        }^M
    });^M
}^M

Same command but POST:
// valid commands: abort --> abortPending | archive --> archiveAll | retry --> retryFailed^M
function sendGlobalCommand(command, successHandler, extraParam)^M
{^M
    $.ajax({^M
        url: "/types/Command/instances/actions/" + command,^M
        type: "POST",^M
        data: JSON.stringify(extraParam),^M
        contentType: "application/json",^M
        cache: false,^M
        processData:false,^M
        success: function(data, textStatus, jqXHR)^M
        {^M
            debug("success: " + data + " , " + textStatus + " , " + jqXHR.responseText );^M
            if ( !IsAjaxResponseErroneous(jqXHR, "setting state", ajaxResponseContent.NON_EMPTY_IS_ERROR ) )^M
            {^M
                if (successHandler) { successHandler(command); }^M
            }^M
        },^M
        error: function (data, textStatus, jqXHR)^M
        {^M
            ajaxErrorCallback(data, textStatus, jqXHR, "sending command: '" + command.camelCaseToFlat() + "'");^M
        }^M
    });^M
}^M





    """
    
def im_login(self):
        # login.jsp
        # Input:
        # j_username
        # j_password
        # Action: /jspring_security_check
        
        # User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
        # Referer https://192.168.100.42/login.jsp
        
        self._im_session = requests.Session()
        self._im_session.headers.update({'Content-Type':'application/x-www-form-urlencoded','Referer': 'https://192.168.100.42/login.jsp', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'})
        self._im_session.mount('https://', TLS1Adapter())
        self._im_verify_ssl = False
        self.j_username = "admin"
        self.j_password = "Password1!"
        requests.packages.urllib3.disable_warnings() # Disable unverified connection warning.
        payload = {'j_username': 'admin', 'j_password': 'Password1!', 'submit':'Login'}
        
        # login to ScaleIO IM
        r = self._im_session.post(
            "{}/{}".format("https://192.168.100.42","j_spring_security_check"),
            verify=self._im_verify_ssl,
            data=payload
        )
        
        
        r1 = self._im_session.post(
            "{}/{}".format("https://192.168.100.42","types/Upgrade/generateCSV"),
            verify=self._im_verify_ssl,
            data=''
        )
        pprint (r1)
        
        
        print "/types/Installation/instances/"
        #resp = self._im_session.get('https://192.168.100.42/types/Installation/instances')
        #resp = self._im_session.get('https://192.168.100.42/api/instances')

        resp = self._im_session.get('https://192.168.100.42/types/InstallationPackageWithLatest/instances')
        jresp = json.loads(resp.text)
        pprint(jresp)
        #r = requests.post("https://192.168.100.42/j_spring_security_check", data=payload)
        #print(r.text)
        print "/types/Command/instances"
        resp = self._im_session.get('https://192.168.100.42/types/Command/instances')
        print resp.text
        #r = requests.post("https://192.168.100.42/j_spring_security_check", data=payload)
        #print(r.text)
        print "/types/NodeInfo/instances/actions/downloadGetInfo"
        resp = self._im_session.get('https://192.168.100.42/types/NodeInfo/instances/actions/downloadGetInfo')
        pprint (json.loads(resp.text))
        #r = requests.post("https://192.168.100.42/j_spring_security_check", data=payload)
        #print(r.text)

        print "/types/Configuration/instances"
        resp = self._im_session.get('https://192.168.100.42/types/Configuration/instances')
        pprint (json.loads(resp.text))

        print "Get Topology"
        pay1 = {'mdmIps':['192.168.100.42'],'mdmPassword':'Password1!'}
        #pay1 = {'mdmIP':'192.168.100.42','mdmPassword':'Password1!','liaPassword':'Password1!'}
        r1 = self._im_session.post(
            "{}/{}".format("https://192.168.100.42","types/Configuration/instances/actions/refreshAndGet"),
            verify=self._im_verify_ssl,
            json=pay1
        )
        pprint (r1)
        
    def im_maintain_credentials(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.post("http://httpbin.org/post", json=payload)
        print(r.text)
    
    def im_get_installation_packages(self):
        resp = self._im_session.get('https://192.168.100.42/types/Command/instances')
        print resp.text
        
    """
        url:'/types/InstallationPackageWithLatest/instances',
        datatype: "json",
        colNames:['Type','OS', 'Linux flavor', 'Version', 'Latest', 'Size', 'File name'],
        colModel:[
            {name:'type',width:100,                 sortable:true, sorttype:"text",     formatter:typeFormatter     },
            {name:'operatingSystem', width:100,     sortable:true, sorttype:"text",     formatter:osFormatter       },
            {name:'linuxFlavour', width:100,        sortable:true, sorttype:"text",     formatter:flavorFormatter   },
            {name:'version',width:100,              sortable:true, sorttype:"text"                                  },
            {name:'latest',  width:100,             sortable:true, sorttype:"text",     formatter:latestFormatter,
                search:false },
            {name:'size',    width:100,             sortable:true, sorttype:"integer",  formatter:sizeFormatter,
                search:false },
            {name:'filename', width:300,            sortable:true, sorttype:"text"                                  }
        ]
    
    """

    """
    ALL MAPPED IM REST METHODS:
Mapped "{[/types/Upgrade/generateCSV],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.CSVController.downloadCsvTopology(javax.servlet.http.HttpServletResponse,java.lang.String) throws java.io.IOException
Mapped "{[/types/Configuration/instances/actions/parseFromCSV],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public com.emc.s3g.scaleio.domain.installation.configuration.Configuration com.emc.s3g.scaleio.web.controller.installation.CSVController.parseCSV(com.emc.s3g.scaleio.web.entity.installation.CSVFile,boolean)
Mapped "{[/types/Command/instances/actions/archiveAll],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.InstallationCommandController.archiveAllCommands()
Mapped "{[/types/Command/instances/actions/abortPending],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.InstallationCommandController.abortPendingCommands(com.emc.s3g.scaleio.web.entity.installation.StateObject)
Mapped "{[/types/Command/instances],methods=[GET],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public java.util.Map<java.lang.String, java.util.List<com.emc.s3g.scaleio.domain.installation.commands.BaseCommand>> com.emc.s3g.scaleio.web.controller.installation.InstallationCommandController.listCommands()
Mapped "{[/types/Command/instances/actions/abortArchive],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.InstallationCommandController.abortAndArchive(com.emc.s3g.scaleio.web.entity.installation.StateObject)
Mapped "{[/types/Command/instances/actions/retryFailed],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.InstallationCommandController.retryFailedCommands()
Mapped "{[/types/Configuration/instances],methods=[GET],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public com.emc.s3g.scaleio.domain.installation.configuration.Configuration com.emc.s3g.scaleio.web.controller.installation.InstallationController.getConfiguration()
Mapped "{[/types/ConfigureCallHome/instances],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.InstallationController.configureCallHome(com.emc.s3g.scaleio.domain.installation.configuration.Configuration,javax.servlet.http.HttpServletResponse)
Mapped "{[/types/ChangeConfiguration/instances],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.InstallationController.changeConfiguration(com.emc.s3g.scaleio.domain.installation.configuration.Configuration,java.lang.String,java.lang.String,javax.servlet.http.HttpServletResponse)
Mapped "{[/types/Configuration/instances/actions/refresh],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.InstallationController.refreshConfiguration(com.emc.s3g.scaleio.web.entity.installation.MdmCredentials,javax.servlet.http.HttpServletResponse)
Mapped "{[/types/Configuration/instances/actions/refreshAndGet],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public com.emc.s3g.scaleio.domain.installation.configuration.Configuration com.emc.s3g.scaleio.web.controller.installation.InstallationController.refreshGetConfiguration(com.emc.s3g.scaleio.web.entity.installation.MdmCredentials,boolean)
Mapped "{[/types/Logs/instances/getLog],methods=[GET],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.InstallationController.getLog(java.lang.String,javax.servlet.http.HttpServletResponse)
Mapped "{[/types/Installation/instances],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.InstallationController.install(com.emc.s3g.scaleio.domain.installation.configuration.Configuration,boolean,boolean,boolean,java.lang.Integer,boolean,javax.servlet.http.HttpServletResponse) throws com.emc.s3g.scaleio.domain.installation.InstallationRuntimeException
Mapped "{[/types/Upgrade/instances],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.InstallationController.upgrade(com.emc.s3g.scaleio.domain.installation.configuration.Configuration,boolean,boolean,boolean,java.lang.Integer,boolean,boolean,javax.servlet.http.HttpServletResponse)
Mapped "{[/types/Uninstall/instances],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.InstallationController.clear(com.emc.s3g.scaleio.domain.installation.configuration.Configuration,boolean,boolean,javax.servlet.http.HttpServletResponse)
Mapped "{[/types/InstallationPackage/instances/uploadPackage],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public com.emc.s3g.scaleio.web.entity.ErrorResult com.emc.s3g.scaleio.web.controller.installation.InstallationPackageController.uploadPackage(com.emc.s3g.scaleio.web.entity.UploadedFiles)
Mapped "{[/instances/InstallationPackage::{fileName}],methods=[DELETE],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public java.lang.Boolean com.emc.s3g.scaleio.web.controller.installation.InstallationPackageController.deletePackage(java.lang.String)
Mapped "{[/types/InstallationPackageWithLatest/instances],methods=[GET],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public java.util.Set<com.emc.s3g.scaleio.web.entity.installation.InstallationPackageView> com.emc.s3g.scaleio.web.controller.installation.InstallationPackageController.listInstallationPackagesWithLatest(boolean)
Mapped "{[/types/InstallationPackage/instances],methods=[GET],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public java.util.Set<com.emc.s3g.scaleio.domain.installation.InstallationPackage> com.emc.s3g.scaleio.web.controller.installation.InstallationPackageController.listInstallationPackages()
Mapped "{[/types/NodeInfo/instances],methods=[GET],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public java.util.Map<com.emc.s3g.scaleio.domain.installation.SystemNode, com.emc.s3g.scaleio.domain.installation.NodeInfo> com.emc.s3g.scaleio.web.controller.installation.NodeInfoController.listNodes()
Mapped "{[/types/NodeInfo/instances/actions/refresh],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.NodeInfoController.refreshNodeInfo(com.emc.s3g.scaleio.domain.installation.configuration.Configuration,javax.servlet.http.HttpServletResponse)
Mapped "{[/types/NodeInfo/instances/actions/downloadGetInfo],methods=[GET],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.NodeInfoController.getInfo(javax.servlet.http.HttpServletResponse)
Mapped "{[/types/NodeInfo/instances/actions/getInfo],methods=[POST],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.NodeInfoController.getInfo(com.emc.s3g.scaleio.domain.installation.configuration.Configuration,boolean,boolean,boolean,boolean,javax.servlet.http.HttpServletResponse)
Mapped "{[/types/State/instances/],methods=[GET],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public com.emc.s3g.scaleio.web.entity.installation.StateObject com.emc.s3g.scaleio.web.controller.installation.StateController.getState()
Mapped "{[/types/State/instances/],methods=[PUT],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.installation.StateController.setState(com.emc.s3g.scaleio.web.entity.installation.StateObject)
Mapped "{[/errors/5{num}.html],methods=[],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.HttpErrorController.handleFileDownloadError(javax.servlet.http.HttpServletResponse,int)
Mapped "{[/errors/4{num}.html],methods=[],params=[],headers=[],consumes=[],produces=[],custom=[]}" onto public void com.emc.s3g.scaleio.web.controller.HttpErrorController.handle4XXErrors(javax.servlet.http.HttpServletResponse,int)
    
    """
    
    def im_manage_packages(self):
        pass
    """
        <form id="packagesForms" class="form-inline"
        action="/types/InstallationPackage/instances/uploadPackage"
        method="post"
        enctype="multipart/form-data">
            <div class="row">
            <div class="col-xs-12 col-sm-9 col-md-7">
            <input id="fileToUpload" type="file" name="files" class="btn btn-default right-padding-sm"
                   data-filename-placement="inside" title="Browse ..." multiple>
            <span title="Click to upload the selected package">
                <button type=button id="uploadButton" class="btn btn-dark"
                        disabled="disabled"><i class="icon-upload-alt right-padding-sm"></i>Upload</button> &nbsp;
            </span>
            <span title="Select package(s) to remove from the Installation Manager">
                <button type=button id="deletePackage" class="btn btn-dark"
                        disabled="disabled"><i class="icon-remove right-padding-sm"></i>Delete</button>
            </span>
            <span title="Click to abort the delete packages operation"> &nbsp;
                <button type=button id="cancelDeletePackage" class="btn btn-default hidden">
                    <i class="icon-stop right-padding-sm"></i>Abort delete operation</button>
            </span>
            </div>
        </div>
    </form>
    
    """
    
    
    def im_get_installer_url(self):
        pass
    """
    function getInstallerURL()
{
    var skipUpload = $("#skipUploadId").prop('checked');
    var skipInstall = $("#skipInstallId").prop('checked');
    var skipConfig = $("#skipConfigId").prop('checked');
    
    var installerUrl = "/types/Installation/instances/" +
        "?noUpload=" + skipUpload +
        "&noInstall=" + skipInstall +
        "&noConfigure=" + skipConfig;
        
    """




Writeup of installation process and what API methods the web interface call to do certain things.

Login:
    
Upload packages:
Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/InstallationPackage/instances/uploadPackage
Request Method:POST
Status Code:200 OK
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Content-Length:19304870
Content-Type:multipart/form-data; boundary=----WebKitFormBoundaryPPpmloO4KkM07Jc5
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Origin:https://192.168.100.51
Referer:https://192.168.100.51/packages.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Request Payload
------WebKitFormBoundaryPPpmloO4KkM07Jc5
Content-Disposition: form-data; name="files"; filename="EMC-ScaleIO-callhome-1.31-256.2.el7.x86_64.rpm"
Content-Type: application/x-rpm


------WebKitFormBoundaryPPpmloO4KkM07Jc5
Content-Disposition: form-data; name="files"; filename="EMC-ScaleIO-lia-1.31-256.2.el7.x86_64.rpm"
Content-Type: application/x-rpm


------WebKitFormBoundaryPPpmloO4KkM07Jc5
Content-Disposition: form-data; name="files"; filename="EMC-ScaleIO-mdm-1.31-256.2.el7.x86_64.rpm"
Content-Type: application/x-rpm


------WebKitFormBoundaryPPpmloO4KkM07Jc5
Content-Disposition: form-data; name="files"; filename="EMC-ScaleIO-sdc-1.31-256.2.el7.x86_64.rpm"
Content-Type: application/x-rpm


------WebKitFormBoundaryPPpmloO4KkM07Jc5
Content-Disposition: form-data; name="files"; filename="EMC-ScaleIO-sds-1.31-256.2.el7.x86_64.rpm"
Content-Type: application/x-rpm


------WebKitFormBoundaryPPpmloO4KkM07Jc5
Content-Disposition: form-data; name="files"; filename="EMC-ScaleIO-tb-1.31-256.2.el7.x86_64.rpm"
Content-Type: application/x-rpm


------WebKitFormBoundaryPPpmloO4KkM07Jc5--
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Date:Wed, 28 Jan 2015 21:40:34 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding


Get list of uploaded packages:
Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/InstallationPackageWithLatest/instances?onlyLatest=false&_search=false&nd=1422481237767&rows=10&page=1&sidx=&sord=desc
Request Method:GET
Status Code:200 OK
Request Headersview source
Accept:application/json, text/javascript, */*; q=0.01
Accept-Encoding:gzip, deflate, sdch
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Referer:https://192.168.100.51/packages.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Query String Parametersview sourceview URL encoded
onlyLatest:false
_search:false
nd:1422481237767
rows:10
page:1
sidx:
sord:desc
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Content-Type:application/json;charset=UTF-8
Date:Wed, 28 Jan 2015 21:40:34 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding


Response:
[{"version":"1.31-256.2","operatingSystem":"linux","linuxFlavour":"rhel7","label":"256.2.el7.x86_64","filename":"EMC-ScaleIO-mdm-1.31-256.2.el7.x86_64.rpm","type":"mdm","size":8051868,"latest":true},{"version":"1.31-256.2","operatingSystem":"linux","linuxFlavour":"rhel7","label":"256.2.el7.x86_64","filename":"EMC-ScaleIO-callhome-1.31-256.2.el7.x86_64.rpm","type":"callhome","size":22356,"latest":true},{"version":"1.31-256.2","operatingSystem":"linux","linuxFlavour":"rhel7","label":"256.2.el7.x86_64","filename":"EMC-ScaleIO-lia-1.31-256.2.el7.x86_64.rpm","type":"lia","size":2009860,"latest":true},{"version":"1.31-256.2","operatingSystem":"linux","linuxFlavour":"rhel7","label":"256.2.el7.x86_64","filename":"EMC-ScaleIO-tb-1.31-256.2.el7.x86_64.rpm","type":"tb","size":2403044,"latest":true},{"version":"1.31-256.2","operatingSystem":"linux","linuxFlavour":"rhel7","label":"256.2.el7.x86_64","filename":"EMC-ScaleIO-sds-1.31-256.2.el7.x86_64.rpm","type":"sds","size":2937008,"latest":true},{"version":"1.31-256.2","operatingSystem":"linux","linuxFlavour":"rhel7","label":"256.2.el7.x86_64","filename":"EMC-ScaleIO-sdc-1.31-256.2.el7.x86_64.rpm","type":"sdc","size":3879612,"latest":true}]


Install stage/config/upload CSV:
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
Content-Type:multipart/form-data; boundary=----WebKitFormBoundarynBIVxPg57VV5ef5L
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Origin:https://192.168.100.51
Referer:https://192.168.100.51/install.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Request Payload
------WebKitFormBoundarynBIVxPg57VV5ef5L
Content-Disposition: form-data; name="file"; filename="ScaleIO_Minimal_Config_51.csv"
Content-Type: text/csv


------WebKitFormBoundarynBIVxPg57VV5ef5L--
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Content-Type:application/json;charset=UTF-8
Date:Wed, 28 Jan 2015 21:43:27 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding


Response:
{"installationId":null,"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":null,"liaPassword":null,"licenseKey":null,"primaryMdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"managementIPs":null,"mdmIPs":["192.168.100.51"]},"secondaryMdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"managementIPs":null,"mdmIPs":["192.168.100.52"]},"tb":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"tbIPs":["192.168.100.53"]},"sdsList":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.100.52]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.52"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.100.53]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.53"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"sdsName":"SDS_[192.168.100.51]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.51"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072}],"sdcList":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":null},"nodeInfo":null,"splitterRpaIp":null}],"callHomeConfiguration":null,"remoteSyslogConfiguration":null}

Request by JavaSCript file to get some kind of status was done automatically:
Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/State/instances/?_=1422481356131
Request Method:GET
Status Code:200 OK
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate, sdch
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Referer:https://192.168.100.51/install.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Query String Parametersview sourceview URL encoded
_:1422481356131
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Content-Type:application/json;charset=UTF-8
Date:Wed, 28 Jan 2015 21:42:32 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding

Response:
{"state":"upload","operation":"idle"}

Set passwords, callhome config:
Password for MDM see
Password for LIA set

Unchecked (no config) for Advanced, Syslog and Call Home

Click on start installation button:

Three different backend API calls was done
Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/State/instances/
Request Method:PUT
Status Code:200 OK
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate, sdch
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Content-Length:17
Content-Type:application/json
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Origin:https://192.168.100.51
Referer:https://192.168.100.51/install.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Request Payloadview source
{state: "query"}
state: "query"
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Date:Wed, 28 Jan 2015 21:48:36 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding


Backnd request no 2 (looks like we dont need the CSV upload stage but a direct JSON call to API):
Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/Installation/instances/?noUpload=false&noInstall=false&noConfigure=false
Request Method:POST
Status Code:202 Accepted
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Content-Length:2646
Content-Type:application/json
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Origin:https://192.168.100.51
Referer:https://192.168.100.51/install.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Query String Parametersview sourceview URL encoded
noUpload:false
noInstall:false
noConfigure:false
Request Payloadview source
{installationId: null, mdmIPs: ["192.168.100.51", "192.168.100.52"], mdmPassword: "Password1!",?}
callHomeConfiguration: null
installationId: null
liaPassword: "Password1!"
licenseKey: null
mdmIPs: ["192.168.100.51", "192.168.100.52"]
mdmPassword: "Password1!"
primaryMdm: {,?}
remoteSyslogConfiguration: null
sdcList: [{,?}, {,?}, {,?}]
sdsList: [{,?}, {,?}, {,?}]
secondaryMdm: {,?}
tb: {,?}
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Date:Wed, 28 Jan 2015 21:48:36 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding


3rd API call:
Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/State/instances/
Request Method:PUT
Status Code:200 OK
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate, sdch
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Content-Length:17
Content-Type:application/json
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Origin:https://192.168.100.51
Referer:https://192.168.100.51/install.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Request Payloadview source
{state: "query"}
state: "query"
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Date:Wed, 28 Jan 2015 21:48:36 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding



Now navigating to Monitor Stage:
Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/State/instances/?_=1422481928148
Request Method:GET
Status Code:200 OK
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate, sdch
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Referer:https://192.168.100.51/status.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Query String Parametersview sourceview URL encoded
_:1422481928148
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Content-Type:application/json;charset=UTF-8
Date:Wed, 28 Jan 2015 21:52:08 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding

Response:
{"state":"query","operation":"install"}


Start upload phase:
Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/State/instances/
Request Method:PUT
Status Code:200 OK
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate, sdch
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Content-Length:18
Content-Type:application/json
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Origin:https://192.168.100.51
Referer:https://192.168.100.51/status.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Request Payloadview source
{state: "upload"}
state: "upload"
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Date:Wed, 28 Jan 2015 21:53:59 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding

Status check:
Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/State/instances/?_=1422481928239
Request Method:GET
Status Code:200 OK
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate, sdch
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Referer:https://192.168.100.51/status.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Query String Parametersview sourceview URL encoded
_:1422481928239
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Content-Type:application/json;charset=UTF-8
Date:Wed, 28 Jan 2015 21:54:23 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding

Response:
{"state":"upload","operation":"install"}

Initiate Install state:
Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/State/instances/
Request Method:PUT
Status Code:200 OK
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate, sdch
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Content-Length:19
Content-Type:application/json
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Origin:https://192.168.100.51
Referer:https://192.168.100.51/status.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Request Payloadview source
{state: "install"}
state: "install"
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Date:Wed, 28 Jan 2015 21:55:13 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding

Check install state:
    Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/State/instances/?_=1422481928273
Request Method:GET
Status Code:200 OK
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate, sdch
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Referer:https://192.168.100.51/status.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Query String Parametersview sourceview URL encoded
_:1422481928273
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Content-Type:application/json;charset=UTF-8
Date:Wed, 28 Jan 2015 21:55:13 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding

Response:
{"state":"install","operation":"install"}



Check command state status:
Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/Command/instances/?_=1422481928277
Request Method:GET
Status Code:200 OK
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate, sdch
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Referer:https://192.168.100.51/status.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Query String Parametersview sourceview URL encoded
_:1422481928277
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Content-Type:application/json;charset=UTF-8
Date:Wed, 28 Jan 2015 21:55:17 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding

Response:
{"192.168.100.51":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"validateClean":true,"validateExactVersion":false,"commandState":"completed","startTime":"2015-01-28T21:48:37.114Z","message":"Command completed successfully","result":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"allowedState":"query","archived":false,"commandName":".ValidateNodeCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"mdm","commandState":"completed","startTime":"2015-01-28T21:53:59.611Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"callhome","commandState":"completed","startTime":"2015-01-28T21:54:01.511Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"sds","commandState":"completed","startTime":"2015-01-28T21:54:02.211Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"sdc","commandState":"completed","startTime":"2015-01-28T21:54:03.111Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"lia","commandState":"completed","startTime":"2015-01-28T21:54:04.012Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"mdm","installationId":null,"allowReboot":false,"arguments":{},"commandState":"running","startTime":"2015-01-28T21:55:13.911Z","message":null,"result":null,"logFilename":"install_mdm_192.168.100.51_2015-01-28-22-55-13.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"callhome","installationId":null,"allowReboot":false,"arguments":{},"commandState":"pending","startTime":null,"message":null,"result":null,"logFilename":null,"allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"sds","installationId":null,"allowReboot":false,"arguments":{},"commandState":"pending","startTime":null,"message":null,"result":null,"logFilename":null,"allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"sdc","installationId":null,"allowReboot":false,"arguments":{"MDM_IP":"192.168.100.51,192.168.100.52"},"commandState":"pending","startTime":null,"message":null,"result":null,"logFilename":null,"allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"lia","installationId":null,"allowReboot":false,"arguments":{"TOKEN":"Password1!"},"commandState":"pending","startTime":null,"message":null,"result":null,"logFilename":null,"allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"addPrimaryMdmCommand":{"commandName":".AddPrimaryMdmCommand","mdmIPs":["192.168.100.51"],"mdmPassword":"Password1!","mdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"managementIPs":null,"mdmIPs":["192.168.100.51"]},"commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".AddPrimaryMdmCommand"},"commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".SetInstallationIdCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","sds":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"sdsName":"SDS_[192.168.100.51]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.51"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},"commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".AddSdsCommand"}],"MDM Commands":[{"configuration":{"installationId":null,"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","liaPassword":"Password1!","licenseKey":null,"primaryMdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"managementIPs":null,"mdmIPs":["192.168.100.51"]},"secondaryMdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sda1"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda"},{"diskName":"/dev/fd0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.343Z"},"managementIPs":null,"mdmIPs":["192.168.100.52"]},"tb":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/sda2"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda"},{"diskName":"/dev/sdb"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sda1"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.924Z"},"tbIPs":["192.168.100.53"]},"sdsList":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/sda2"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda"},{"diskName":"/dev/sdb"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sda1"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.924Z"},"sdsName":"SDS_[192.168.100.53]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.53"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"sdsName":"SDS_[192.168.100.51]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.51"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sda1"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda"},{"diskName":"/dev/fd0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.343Z"},"sdsName":"SDS_[192.168.100.52]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.52"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072}],"sdcList":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/sda2"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda"},{"diskName":"/dev/sdb"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sda1"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.924Z"},"splitterRpaIp":null},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"splitterRpaIp":null},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sda1"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda"},{"diskName":"/dev/fd0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.343Z"},"splitterRpaIp":null}],"callHomeConfiguration":null,"remoteSyslogConfiguration":null},"mdmIPs":[],"mdmPassword":"","noUpload":false,"noInstall":false,"noConfigure":false,"sdsInstances":null,"extend":false,"commandState":"completed","startTime":"2015-01-28T21:48:39.034Z","message":"Command completed successfully","result":null,"allowedState":"query","archived":false,"commandName":".ValidateAndOrchestrateNewCommandsForInstallCommand"},{"mdmIPs":["192.168.100.51"],"mdmPassword":"Password1!","mdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"managementIPs":null,"mdmIPs":["192.168.100.51"]},"commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".AddPrimaryMdmCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","mdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sda1"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda"},{"diskName":"/dev/fd0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.343Z"},"managementIPs":null,"mdmIPs":["192.168.100.52"]},"commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".AddSecondaryMdmCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","tb":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/sda2"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda"},{"diskName":"/dev/sdb"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sda1"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.924Z"},"tbIPs":["192.168.100.53"]},"commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".AddTbCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".SwitchToClusterModeCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","protectionDomainName":"default","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".AddProtectionDomainCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".SetSpareCapacitiesCommand"}],"192.168.100.52":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"validateClean":true,"validateExactVersion":false,"commandState":"completed","startTime":"2015-01-28T21:48:37.115Z","message":"Command completed successfully","result":{"diskDevices":[{"diskName":"/dev/sda1"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda"},{"diskName":"/dev/fd0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.343Z"},"allowedState":"query","archived":false,"commandName":".ValidateNodeCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"mdm","commandState":"completed","startTime":"2015-01-28T21:53:59.618Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"callhome","commandState":"completed","startTime":"2015-01-28T21:54:01.730Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"sds","commandState":"completed","startTime":"2015-01-28T21:54:02.418Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"sdc","commandState":"completed","startTime":"2015-01-28T21:54:03.311Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"lia","commandState":"completed","startTime":"2015-01-28T21:54:04.211Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"mdm","installationId":null,"allowReboot":false,"arguments":{},"commandState":"running","startTime":"2015-01-28T21:55:13.914Z","message":null,"result":null,"logFilename":"install_mdm_192.168.100.52_2015-01-28-22-55-13.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"callhome","installationId":null,"allowReboot":false,"arguments":{},"commandState":"pending","startTime":null,"message":null,"result":null,"logFilename":null,"allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"sds","installationId":null,"allowReboot":false,"arguments":{},"commandState":"pending","startTime":null,"message":null,"result":null,"logFilename":null,"allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"sdc","installationId":null,"allowReboot":false,"arguments":{"MDM_IP":"192.168.100.51,192.168.100.52"},"commandState":"pending","startTime":null,"message":null,"result":null,"logFilename":null,"allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"lia","installationId":null,"allowReboot":false,"arguments":{"TOKEN":"Password1!"},"commandState":"pending","startTime":null,"message":null,"result":null,"logFilename":null,"allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"addPrimaryMdmCommand":{"commandName":".AddPrimaryMdmCommand","mdmIPs":["192.168.100.51"],"mdmPassword":"Password1!","mdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"managementIPs":null,"mdmIPs":["192.168.100.51"]},"commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".AddPrimaryMdmCommand"},"commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".SetInstallationIdCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","sds":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sda1"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda"},{"diskName":"/dev/fd0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.343Z"},"sdsName":"SDS_[192.168.100.52]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.52"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},"commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".AddSdsCommand"}],"192.168.100.53":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"validateClean":true,"validateExactVersion":false,"commandState":"completed","startTime":"2015-01-28T21:48:37.119Z","message":"Command completed successfully","result":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/sda2"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda"},{"diskName":"/dev/sdb"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sda1"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.924Z"},"allowedState":"query","archived":false,"commandName":".ValidateNodeCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"tb","commandState":"completed","startTime":"2015-01-28T21:53:59.618Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"sds","commandState":"completed","startTime":"2015-01-28T21:54:01.221Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"sdc","commandState":"completed","startTime":"2015-01-28T21:54:02.114Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"lia","commandState":"completed","startTime":"2015-01-28T21:54:03.116Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"tb","installationId":null,"allowReboot":false,"arguments":{},"commandState":"running","startTime":"2015-01-28T21:55:13.919Z","message":null,"result":null,"logFilename":"install_tb_192.168.100.53_2015-01-28-22-55-13.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"sds","installationId":null,"allowReboot":false,"arguments":{},"commandState":"pending","startTime":null,"message":null,"result":null,"logFilename":null,"allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"sdc","installationId":null,"allowReboot":false,"arguments":{"MDM_IP":"192.168.100.51,192.168.100.52"},"commandState":"pending","startTime":null,"message":null,"result":null,"logFilename":null,"allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"lia","installationId":null,"allowReboot":false,"arguments":{"TOKEN":"Password1!"},"commandState":"pending","startTime":null,"message":null,"result":null,"logFilename":null,"allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"addPrimaryMdmCommand":{"commandName":".AddPrimaryMdmCommand","mdmIPs":["192.168.100.51"],"mdmPassword":"Password1!","mdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"managementIPs":null,"mdmIPs":["192.168.100.51"]},"commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".AddPrimaryMdmCommand"},"commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".SetInstallationIdCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","sds":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/sda2"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda"},{"diskName":"/dev/sdb"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sda1"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.924Z"},"sdsName":"SDS_[192.168.100.53]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.53"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},"commandState":"pending","startTime":null,"message":null,"result":null,"allowedState":"configure","archived":false,"commandName":".AddSdsCommand"}]}


Initiate Confgiure State:
    Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/State/instances/
Request Method:PUT
Status Code:200 OK
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate, sdch
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Content-Length:21
Content-Type:application/json
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Origin:https://192.168.100.51
Referer:https://192.168.100.51/status.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Request Payloadview source
{state: "configure"}
state: "configure"
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Date:Wed, 28 Jan 2015 21:59:19 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding


Check state:
    Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/State/instances/?_=1422481928438
Request Method:GET
Status Code:200 OK
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate, sdch
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Referer:https://192.168.100.51/status.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Query String Parametersview sourceview URL encoded
_:1422481928438
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Content-Type:application/json;charset=UTF-8
Date:Wed, 28 Jan 2015 21:59:19 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding

Response:
{"state":"configure","operation":"install"}

GEt configure state status:
Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/Command/instances/?_=1422481928452
Request Method:GET
Status Code:200 OK
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate, sdch
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Referer:https://192.168.100.51/status.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Query String Parametersview sourceview URL encoded
_:1422481928452
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Content-Type:application/json;charset=UTF-8
Date:Wed, 28 Jan 2015 21:59:38 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding

Response:
{"192.168.100.51":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"validateClean":true,"validateExactVersion":false,"commandState":"completed","startTime":"2015-01-28T21:48:37.114Z","message":"Command completed successfully","result":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"allowedState":"query","archived":false,"commandName":".ValidateNodeCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"mdm","commandState":"completed","startTime":"2015-01-28T21:53:59.611Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"callhome","commandState":"completed","startTime":"2015-01-28T21:54:01.511Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"sds","commandState":"completed","startTime":"2015-01-28T21:54:02.211Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"sdc","commandState":"completed","startTime":"2015-01-28T21:54:03.111Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"lia","commandState":"completed","startTime":"2015-01-28T21:54:04.012Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"mdm","installationId":null,"allowReboot":false,"arguments":{},"commandState":"completed","startTime":"2015-01-28T21:55:13.911Z","message":"Command completed successfully","result":null,"logFilename":"install_mdm_192.168.100.51_2015-01-28-22-55-13.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"callhome","installationId":null,"allowReboot":false,"arguments":{},"commandState":"completed","startTime":"2015-01-28T21:55:20.911Z","message":"Command completed successfully","result":null,"logFilename":"install_callhome_192.168.100.51_2015-01-28-22-55-20.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"sds","installationId":null,"allowReboot":false,"arguments":{},"commandState":"completed","startTime":"2015-01-28T21:55:23.011Z","message":"Command completed successfully","result":null,"logFilename":"install_sds_192.168.100.51_2015-01-28-22-55-23.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"sdc","installationId":null,"allowReboot":false,"arguments":{"MDM_IP":"192.168.100.51,192.168.100.52"},"commandState":"completed","startTime":"2015-01-28T21:55:27.412Z","message":"Command completed successfully","result":null,"logFilename":"install_sdc_192.168.100.51_2015-01-28-22-55-27.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"lia","installationId":null,"allowReboot":false,"arguments":{"TOKEN":"Password1!"},"commandState":"completed","startTime":"2015-01-28T21:55:43.311Z","message":"Command completed successfully","result":null,"logFilename":"install_lia_192.168.100.51_2015-01-28-22-55-43.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"addPrimaryMdmCommand":{"commandName":".AddPrimaryMdmCommand","mdmIPs":["192.168.100.51"],"mdmPassword":"Password1!","mdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"managementIPs":null,"mdmIPs":["192.168.100.51"]},"commandState":"completed","startTime":"2015-01-28T21:59:19.834Z","message":"Command completed successfully","result":null,"allowedState":"configure","archived":false,"commandName":".AddPrimaryMdmCommand"},"commandState":"completed","startTime":"2015-01-28T21:59:32.611Z","message":"Command completed successfully","result":null,"allowedState":"configure","archived":false,"commandName":".SetInstallationIdCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","sds":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"sdsName":"SDS_[192.168.100.51]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.51"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},"commandState":"aborted","startTime":null,"message":"Stopped due to previously failed command","result":null,"allowedState":"configure","archived":false,"commandName":".AddSdsCommand"}],"MDM Commands":[{"configuration":{"installationId":null,"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","liaPassword":"Password1!","licenseKey":null,"primaryMdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"managementIPs":null,"mdmIPs":["192.168.100.51"]},"secondaryMdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sda1"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda"},{"diskName":"/dev/fd0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.343Z"},"managementIPs":null,"mdmIPs":["192.168.100.52"]},"tb":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/sda2"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda"},{"diskName":"/dev/sdb"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sda1"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.924Z"},"tbIPs":["192.168.100.53"]},"sdsList":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/sda2"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda"},{"diskName":"/dev/sdb"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sda1"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.924Z"},"sdsName":"SDS_[192.168.100.53]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.53"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"sdsName":"SDS_[192.168.100.51]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.51"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sda1"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda"},{"diskName":"/dev/fd0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.343Z"},"sdsName":"SDS_[192.168.100.52]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.52"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072}],"sdcList":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/sda2"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda"},{"diskName":"/dev/sdb"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sda1"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.924Z"},"splitterRpaIp":null},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"splitterRpaIp":null},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sda1"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda"},{"diskName":"/dev/fd0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.343Z"},"splitterRpaIp":null}],"callHomeConfiguration":null,"remoteSyslogConfiguration":null},"mdmIPs":[],"mdmPassword":"","noUpload":false,"noInstall":false,"noConfigure":false,"sdsInstances":null,"extend":false,"commandState":"completed","startTime":"2015-01-28T21:48:39.034Z","message":"Command completed successfully","result":null,"allowedState":"query","archived":false,"commandName":".ValidateAndOrchestrateNewCommandsForInstallCommand"},{"mdmIPs":["192.168.100.51"],"mdmPassword":"Password1!","mdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"managementIPs":null,"mdmIPs":["192.168.100.51"]},"commandState":"completed","startTime":"2015-01-28T21:59:19.834Z","message":"Command completed successfully","result":null,"allowedState":"configure","archived":false,"commandName":".AddPrimaryMdmCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","mdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sda1"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda"},{"diskName":"/dev/fd0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.343Z"},"managementIPs":null,"mdmIPs":["192.168.100.52"]},"commandState":"completed","startTime":"2015-01-28T21:59:32.542Z","message":"Command completed successfully","result":null,"allowedState":"configure","archived":false,"commandName":".AddSecondaryMdmCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","tb":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/sda2"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda"},{"diskName":"/dev/sdb"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sda1"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.924Z"},"tbIPs":["192.168.100.53"]},"commandState":"completed","startTime":"2015-01-28T21:59:32.638Z","message":"Command completed successfully","result":null,"allowedState":"configure","archived":false,"commandName":".AddTbCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","commandState":"failed","startTime":"2015-01-28T21:59:32.839Z","message":"Command failed: Could not connect to 192.168.100.51,192.168.100.52","result":null,"allowedState":"configure","archived":false,"commandName":".SwitchToClusterModeCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","protectionDomainName":"default","commandState":"aborted","startTime":null,"message":"Stopped due to previously failed command","result":null,"allowedState":"configure","archived":false,"commandName":".AddProtectionDomainCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","commandState":"aborted","startTime":null,"message":"Stopped due to previously failed command","result":null,"allowedState":"configure","archived":false,"commandName":".SetSpareCapacitiesCommand"}],"192.168.100.52":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"validateClean":true,"validateExactVersion":false,"commandState":"completed","startTime":"2015-01-28T21:48:37.115Z","message":"Command completed successfully","result":{"diskDevices":[{"diskName":"/dev/sda1"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda"},{"diskName":"/dev/fd0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.343Z"},"allowedState":"query","archived":false,"commandName":".ValidateNodeCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"mdm","commandState":"completed","startTime":"2015-01-28T21:53:59.618Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"callhome","commandState":"completed","startTime":"2015-01-28T21:54:01.730Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"sds","commandState":"completed","startTime":"2015-01-28T21:54:02.418Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"sdc","commandState":"completed","startTime":"2015-01-28T21:54:03.311Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"lia","commandState":"completed","startTime":"2015-01-28T21:54:04.211Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"mdm","installationId":null,"allowReboot":false,"arguments":{},"commandState":"completed","startTime":"2015-01-28T21:55:13.914Z","message":"Command completed successfully","result":null,"logFilename":"install_mdm_192.168.100.52_2015-01-28-22-55-13.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"callhome","installationId":null,"allowReboot":false,"arguments":{},"commandState":"completed","startTime":"2015-01-28T21:55:20.223Z","message":"Command completed successfully","result":null,"logFilename":"install_callhome_192.168.100.52_2015-01-28-22-55-20.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"sds","installationId":null,"allowReboot":false,"arguments":{},"commandState":"completed","startTime":"2015-01-28T21:55:22.111Z","message":"Command completed successfully","result":null,"logFilename":"install_sds_192.168.100.52_2015-01-28-22-55-22.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"sdc","installationId":null,"allowReboot":false,"arguments":{"MDM_IP":"192.168.100.51,192.168.100.52"},"commandState":"completed","startTime":"2015-01-28T21:55:26.412Z","message":"Command completed successfully","result":null,"logFilename":"install_sdc_192.168.100.52_2015-01-28-22-55-26.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"lia","installationId":null,"allowReboot":false,"arguments":{"TOKEN":"Password1!"},"commandState":"completed","startTime":"2015-01-28T21:55:41.313Z","message":"Command completed successfully","result":null,"logFilename":"install_lia_192.168.100.52_2015-01-28-22-55-41.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"addPrimaryMdmCommand":{"commandName":".AddPrimaryMdmCommand","mdmIPs":["192.168.100.51"],"mdmPassword":"Password1!","mdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"managementIPs":null,"mdmIPs":["192.168.100.51"]},"commandState":"completed","startTime":"2015-01-28T21:59:19.834Z","message":"Command completed successfully","result":null,"allowedState":"configure","archived":false,"commandName":".AddPrimaryMdmCommand"},"commandState":"completed","startTime":"2015-01-28T21:59:32.612Z","message":"Command completed successfully","result":null,"allowedState":"configure","archived":false,"commandName":".SetInstallationIdCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","sds":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.52"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sda1"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda"},{"diskName":"/dev/fd0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.343Z"},"sdsName":"SDS_[192.168.100.52]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.52"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},"commandState":"aborted","startTime":null,"message":"Stopped due to previously failed command","result":null,"allowedState":"configure","archived":false,"commandName":".AddSdsCommand"}],"192.168.100.53":[{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"validateClean":true,"validateExactVersion":false,"commandState":"completed","startTime":"2015-01-28T21:48:37.119Z","message":"Command completed successfully","result":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/sda2"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda"},{"diskName":"/dev/sdb"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sda1"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.924Z"},"allowedState":"query","archived":false,"commandName":".ValidateNodeCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"tb","commandState":"completed","startTime":"2015-01-28T21:53:59.618Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"sds","commandState":"completed","startTime":"2015-01-28T21:54:01.221Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"sdc","commandState":"completed","startTime":"2015-01-28T21:54:02.114Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"componentType":"lia","commandState":"completed","startTime":"2015-01-28T21:54:03.116Z","message":"Command completed successfully","result":null,"allowedState":"upload","archived":false,"commandName":".UploadCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"tb","installationId":null,"allowReboot":false,"arguments":{},"commandState":"completed","startTime":"2015-01-28T21:55:13.919Z","message":"Command completed successfully","result":null,"logFilename":"install_tb_192.168.100.53_2015-01-28-22-55-13.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"sds","installationId":null,"allowReboot":false,"arguments":{},"commandState":"completed","startTime":"2015-01-28T21:55:23.816Z","message":"Command completed successfully","result":null,"logFilename":"install_sds_192.168.100.53_2015-01-28-22-55-23.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"sdc","installationId":null,"allowReboot":false,"arguments":{"MDM_IP":"192.168.100.51,192.168.100.52"},"commandState":"completed","startTime":"2015-01-28T21:55:33.116Z","message":"Command completed successfully","result":null,"logFilename":"install_sdc_192.168.100.53_2015-01-28-22-55-33.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"ecsComponentType":"lia","installationId":null,"allowReboot":false,"arguments":{"TOKEN":"Password1!"},"commandState":"completed","startTime":"2015-01-28T21:55:49.413Z","message":"Command completed successfully","result":null,"logFilename":"install_lia_192.168.100.53_2015-01-28-22-55-49.log","allowedState":"install","archived":false,"commandName":".InstallCommand"},{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"addPrimaryMdmCommand":{"commandName":".AddPrimaryMdmCommand","mdmIPs":["192.168.100.51"],"mdmPassword":"Password1!","mdm":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.51"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sdb"},{"diskName":"/dev/sda1"},{"diskName":"/dev/sda"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda2"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.173Z"},"managementIPs":null,"mdmIPs":["192.168.100.51"]},"commandState":"completed","startTime":"2015-01-28T21:59:19.834Z","message":"Command completed successfully","result":null,"allowedState":"configure","archived":false,"commandName":".AddPrimaryMdmCommand"},"commandState":"completed","startTime":"2015-01-28T21:59:32.617Z","message":"Command completed successfully","result":null,"allowedState":"configure","archived":false,"commandName":".SetInstallationIdCommand"},{"mdmIPs":["192.168.100.51","192.168.100.52"],"mdmPassword":"Password1!","sds":{"node":{"ostype":"linux","nodeName":null,"nodeIPs":["192.168.100.53"],"domain":null,"userName":"root","password":"password","liaPassword":"Password1!"},"nodeInfo":{"diskDevices":[{"diskName":"/dev/sr0"},{"diskName":"/dev/sda2"},{"diskName":"/dev/dm-0"},{"diskName":"/dev/dm-1"},{"diskName":"/dev/sda"},{"diskName":"/dev/sdb"},{"diskName":"/dev/fd0"},{"diskName":"/dev/sda1"}],"installedComponents":[],"osType":"linux","linuxFlavour":"rhel7","timestamp":"2015-01-28T21:48:38.924Z"},"sdsName":"SDS_[192.168.100.53]","protectionDomain":"default","faultSet":null,"allIPs":["192.168.100.53"],"sdsOnlyIPs":null,"sdcOnlyIPs":null,"devices":[{"devicePath":"/dev/sdb","storagePool":null,"deviceName":null}],"optimized":false,"port":7072},"commandState":"aborted","startTime":null,"message":"Stopped due to previously failed command","result":null,"allowedState":"configure","archived":false,"commandName":".AddSdsCommand"}]}
'CommandState' can be: Pending, Successuflly Completed, and more. Execute this call and see what states it avan hav.




If something failed one can RETRY:
Remote Address:192.168.100.51:443
Request URL:https://192.168.100.51/types/Command/instances/actions/retryFailed
Request Method:POST
Status Code:200 OK
Request Headersview source
Accept:*/*
Accept-Encoding:gzip, deflate
Accept-Language:en-US,en;q=0.8,sv;q=0.6
Connection:keep-alive
Content-Length:4
Content-Type:application/json
Cookie:JSESSIONID=5BBDAD2D5FC5F8B946DADAF3C5DD3C65
Host:192.168.100.51
Origin:https://192.168.100.51
Referer:https://192.168.100.51/status.jsp
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
X-Requested-With:XMLHttpRequest
Request Payloadview source
null
No Properties
Response Headersview source
Cache-Control:no-cache
Cache-Control:no-store
Content-Encoding:gzip
Date:Wed, 28 Jan 2015 22:02:13 GMT
Expires:Thu, 01 Jan 1970 00:00:00 GMT
Pragma:no-cache
Server:Apache-Coyote/1.1
Transfer-Encoding:chunked
Vary:Accept-Encoding

Response:
    
