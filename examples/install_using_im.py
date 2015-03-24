import im
import logging
from pprint import pprint

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