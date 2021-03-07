Map cfg = [:]

    cfg.nodeBin       = "~/.nodenv/shims:/usr/local/bin"

    cfg.hpFortifyApp  = "MER"

    cfg.hpFortifyBin  = "/opt/HPE_Security/Fortify_SCA_and_Apps/bin"

    cfg.hpFortifyUrl  = "https://fortify.someplace.com:8443/ssc/"

    cfg.hpFortifyAuth = "fSomeAuthThing"

//        cfg.javaLibsNexus = "http://devil/nexus/content/repositories/snapshots"

//        cfg.depTrackUrl   = "http://ci-dash:3002/deptrack"

 

String test = "This is the test String"

init(cfg)

process(test)

 

def process(String ProcessTestString) {

    //                        def errors

    //       init()

    //                        addFiles(patterns)

    //       scanToFPR()

    //       upload()

    //                        cleanup()

    //                        return errors

    PrintVariables(ProcessTestString)

}

 

def PrintVariables(String TestString) {

   String hpFortifyApp  = "MER"

    String hpFortifyBin  = "/opt/HPE_Security/Fortify_SCA_and_Apps/bin"

    String hpFortifyUrl  = "https://fortify.someplace.com:8443/ssc/"

    String hpFortifyAuth = "fSomeAuthThing"

    String version = "MER_1.1"

    String build = version

    String perTypeArgs = "-Xmx480M"

    println "Printing test string from PrintVariables: " + TestString

    println build

    println hpFortifyUrl

}

 

def init(Map fortify_parameters) {

    println "Fortify parameter: " + fortify_parameters.hpFortifyBin

    println "Doing the Init method"

}