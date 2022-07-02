from typing import Type
from models.mirthElement import MirthElement

class Connector(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
        
        self.metaDataId = self.getSafeText('metaDataId')
        self.name = self.getSafeText('name')
        self.transportName = self.getSafeText('transportName')
        self.mode = self.getSafeText('mode')
        self.enabled = self.getSafeText('enabled')
        self.waitForPrevious = self.getSafeText('waitForPrevious')

        prop = Mapping.recieverProperties(self.root.find('properties').attrib['class'])
        
        self.properties = prop(self.root.find('properties'))

class ConnectorProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
        
        self.protocol = self.getSafeText('protocol')
        self.name = self.getSafeText('name')
        self.pluginProperties = [ConnectorPluginProperties]

        for e in self.root.findall('./pluginProperties'):
            self.pluginProperties.append(ConnectorPluginProperties(e))

class ConnectorPluginProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
    
        self.name = self.getSafeText('name')
     

class SourceConnectorProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.responseVariable = self.getSafeText("responseVariable")
        self.respondAfterProcessing = self.getSafeText("respondAfterProcessing")
        self.processBatch = self.getSafeText("processBatch")
        self.firstResponse = self.getSafeText("firstResponse")
        self.processingThreads = self.getSafeText("processingThreads")
        self.queueBufferSize = self.getSafeText("queueBufferSize")
        self.resourceIds = []

        for e in self.root.findall('./resourceIds/entry'):
            strings = e.findall('./string')
            self.resourceIds.append((strings[0].text, strings[1].text))

class ListenerConnectorProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.host = self.getSafeText('host')
        self.port = self.getSafeText('port')

class PollConnectorProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.pollingType = self.getSafeText('pollingType')
        self.pollOnStart = self.getSafeText('pollOnStart')
        self.pollingFrequency = self.getSafeText('pollingFrequency')
        self.pollingHour = self.getSafeText('pollingHour')
        self.pollingMinute = self.getSafeText('pollingMinute')
        self.cronJobs = []  #TODO: implement
        self.pollConnectorPropertiesAdvanced = PollConnectorPropertiesAdvanced(self.root.find('pollConnectorPropertiesAdvanced'))

class PollConnectorPropertiesAdvanced(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.weekly = self.getSafeText('weekly')
        self.inactiveDays = []
        self.dayOfMonth = self.getSafeText('dayOfMonth')
        self.allDay = self.getSafeText('allDay')
        self.startingHour = self.getSafeText('startingHour')
        self.startingMinute = self.getSafeText('startingMinute')
        self.endingHour = self.getSafeText('endingHour')
        self.endingMinute = self.getSafeText('endingMinute')

        # in active days
        for e in self.root.findall('./inactiveDays/boolean'):
            self.inactiveDays.append(e.text)


#region ReceiverProperties
class VmReceiverProperties(ConnectorProperties):
    def __init__(self, uXml):
        ConnectorPluginProperties.__init__(self, uXml)

        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))

class DICOMReceiverProperties(ConnectorProperties):
    def __init__(self, uXml):
        ConnectorPluginProperties.__init__(self, uXml)

        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
        self.listenerConnectorProperties = ListenerConnectorProperties(self.root.find('listenerConnectorProperties'))
        self.soCloseDelay =  self.getSafeText("soCloseDelay")
        self.releaseTo =  self.getSafeText("releaseTo")
        self.requestTo = self.getSafeText("requestTo")
        self.idleTo =  self.getSafeText("idleTo") 
        self.reaper =  self.getSafeText("reaper")
        self.rspDelay =  self.getSafeText("rspDelay")
        self.pdv1 =  self.getSafeText("pdv1")
        self.sndpdulen =  self.getSafeText("sndpdulen")
        self.rcvpdulen =  self.getSafeText("rcvpdulen") 
        self.asyncc =  self.getSafeText("async")
        self.bigEndian = self.getSafeText("bigEndian")
        self.bufSize =  self.getSafeText("bufSize")
        self.defts =  self.getSafeText("defts")
        self.dest =  self.getSafeText("dest") 
        self.nativeData = self.getSafeText("nativeData")
        self.sorcvbuf =  self.getSafeText("sorcvbuf")
        self.sosndbuf =  self.getSafeText("sosndbuf")
        self.tcpDelay =  self.getSafeText("tcpDelay")
        self.keyPW =  self.getSafeText("keyPW")
        self.keyStore =  self.getSafeText("keyStore")
        self.keyStorePW =  self.getSafeText("keyStorePW")
        self.noClientAuth =  self.getSafeText("noClientAuth")
        self.nossl2 =  self.getSafeText("nossl2")
        self.tls =  self.getSafeText("tls")
        self.trustStore =  self.getSafeText("trustStore")
        self.trustStorePW =  self.getSafeText("trustStorePW")
        self.applicationEntity =  self.getSafeText("applicationEntity")
        self.localHost =  self.getSafeText("localHost")
        self.localPort =  self.getSafeText("localPort") 
        self.localApplicationEntity =  self.getSafeText("localApplicationEntity")

class DatabaseReceiverProperties(ConnectorProperties):
    def __init__(self, uXml):
        ConnectorPluginProperties.__init__(self, uXml)

        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
        self.pollConnectorProperties = PollConnectorProperties(self.root.find('pollConnectorProperties'))
        self.driver = self.getSafeText("driver")
        self.url = self.getSafeText("url")
        self.username = self.getSafeText("username")
        self.password = self.getSafeText("password")
        self.select = self.getSafeText("select")
        self.update = self.getSafeText("update")
        self.useScript = self.getSafeText("useScript")
        self.aggregateResults = self.getSafeText("aggregateResults")
        self.cacheResults = self.getSafeText("cacheResults")
        self.keepConnectionOpen = self.getSafeText("keepConnectionOpen")
        self.updateMode = self.getSafeText("updateMode")
        self.retryCount = self.getSafeText("retryCount")
        self.retryInterval = self.getSafeText("retryInterval")
        self.fetchSize = self.getSafeText("fetchSize")
        self.encoding = self.getSafeText("encoding")
        
class FileReceiverProperties(ConnectorProperties):
    def __init__(self, uXml):
        ConnectorPluginProperties.__init__(self, uXml)

        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
        self.pollConnectorProperties = PollConnectorProperties(self.root.find('pollConnectorProperties'))
        self.scheme = self.getSafeText("scheme")
        prop = schemeProperties(self.root.find('schemeProperties').attrib['class'])
        
        self.properties = prop(self.root.find('schemeProperties'))
        self.host = self.getSafeText("host")
        self.fileFilter = self.getSafeText("fileFilter")
        self.regex = self.getSafeText("regex")
        self.directoryRecursion = self.getSafeText("directoryRecursion")
        self.ignoreDot = self.getSafeText("ignoreDot")
        self.anonymous = self.getSafeText("anonymous")
        self.username = self.getSafeText("username")
        self.password = self.getSafeText("password")
        self.timeout = self.getSafeText("timeout")
        self.secure = self.getSafeText("secure")
        self.passive = self.getSafeText("passive")
        self.validateConnection = self.getSafeText("validateConnection")
        self.afterProcessingAction = self.getSafeText("afterProcessingAction")
        self.moveToDirectory = self.getSafeText("moveToDirectory")
        self.moveToFileName = self.getSafeText("moveToFileName")
        self.errprReadingAction = self.getSafeText("errprReadingAction")
        self.errorResponseAction = self.getSafeText("errorResponseAction")
        self.errorMoveToDirectory = self.getSafeText("errorMoveToDirectory")
        self.errorMoveToFileName = self.getSafeText("errorMoveToFileName")
        self.checkFileAge = self.getSafeText("checkFileAge")
        self.fileAge = self.getSafeText("fileAge")
        self.fileSizeMinimum = self.getSafeText("fileSizeMinimum")
        self.fileSizeMaximum = self.getSafeText("fileSizeMaximum")
        self.ignoreFileSizeMaximum = self.getSafeText("ignoreFileSizeMaximum")
        self.sortBy = self.getSafeText("sortBy")
        self.binary = self.getSafeText("binary")
        self.charsetEncoding = self.getSafeText("charsetEncoding")
        
class HttpReceiverProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.pluginProperties = []

        if len(self.root.find('./pluginProperties').findall('./*')) > 0:
            for e in self.root.find('./pluginProperties').findall('./*'):
                prop = httpAuthProperties(e.tag)
        
                self.pluginProperties.append(prop(e))

        self.listenerConnectorProperties = ListenerConnectorProperties(self.root.find('listenerConnectorProperties'))
        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
        self.xmlBody = self.getSafeText('xmlBody')
        self.parseMultipart = self.getSafeText('parseMultipart')
        self.includeMetadata = self.getSafeText('includeMetadata')
        self.binaryMimeTypes = self.getSafeText('binaryMimeTypes')
        self.binaryMimeTypesRegex = self.getSafeText('binaryMimeTypesRegex')
        self.responseContentType = self.getSafeText('responseContentType')
        self.responseDataTypeBinary = self.getSafeText('responseDataTypeBinary')
        self.responseStatusCode = self.getSafeText('responseStatusCode')
        self.responseHeaders = '' #TODO: Implement
        self.responseHeadersVariable = self.getSafeText('responseHeadersVariable')
        self.useResponseHeadersVariable = self.getSafeText('useResponseHeadersVariable')
        self.charset = self.getSafeText('charset')
        self.contextPath = self.getSafeText('contextPath')
        self.staticResources = '' #TODO: Implement
#endregion

#region HttpAuthProperties
class BasicHttpAuthProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.authType = self.getSafeText('authType')
        self.realm = self.getSafeText('realm')
        self.credentials = []
        for e in self.root.findall('./credentials/entry'):
            strings = e.findall('./string')
            self.credentials.append((strings[0].text, strings[1].text))

        self.isUseCredentialsVariable = self.getSafeText('isUseCredentialsVariable')
        self.credentialsVariable = self.getSafeText('credentialsVariable')

class DigestHttpAuthProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.authType = self.getSafeText('authType')
        self.realm = self.getSafeText('realm')
        self.credentials = []
        for e in self.root.findall('./credentials/entry'):
            strings = e.findall('./string')
            self.credentials.append((strings[0].text, strings[1].text))

        self.isUseCredentialsVariable = self.getSafeText('isUseCredentialsVariable')
        self.credentialsVariable = self.getSafeText('credentialsVariable')
        self.qopModes = self.root.find('qopModes')
        self.opaque = self.getSafeText('opaque')
        self.algorithm = self.root.find('algorithms')

class JavaScriptHttpAuthProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.authType = self.getSafeText('authType')
        self.script = self.getSafeText('script')

class CustomHttpAuthProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.authType = self.getSafeText('authType')
        self.authenticatorClass = self.getSafeText('authenticatorClass')

        self.properties = []
        for e in self.root.findall('./properties/entry'):
            strings = e.findall('./string')
            self.properties.append((strings[0].text, strings[1].text))

class OAuth2HttpAuthProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.authType = self.getSafeText('authType')
        self.tokenLocation = self.getSafeText('tokenLocation')
        self.locationKey = self.getSafeText('locationKey')
        self.verificationURL = self.getSafeText('verificationURL')
#endregion

#region SchemeProperties
class SchemeProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

class SftpSchemeProperties(SchemeProperties):
    def __init__(self, uXml):
        SchemeProperties.__init__(self, uXml)

        self.passwordAuth = self.getSafeText('passwordAuth')
        self.keyAuth = self.getSafeText('keyAuth')
        self.keyFile = self.getSafeText('keyFile')
        self.passPhrase = self.getSafeText('passPhrase')
        self.hostKeyChecking = self.getSafeText('hostKeyChecking')
        self.knownHostsFile = self.getSafeText('knownHostsFile')
        self.configurationSettings = []

        for e in self.root.findall('./configurationSettings/entry'):
            strings = e.findall('./string')
            self.configurationSettings.append((strings[0].text, strings[1].text))
        
class FTPSchemeProperties(SchemeProperties):
    def __init__(self, uXml):
        SchemeProperties.__init__(self, uXml)

        self.initalCommands = []

        for e in self.root.findall('./initialCommands/string'):
            self.initalCommands.append(e.text)
        
class S3SchemeProperties(SchemeProperties):
    def __init__(self, uXml):
        SchemeProperties.__init__(self, uXml)

        self.useDefaultCredentialProviderChain = self.getSafeText('useDefaultCredentialProviderChain')
        self.useTemporaryCredentials = self.getSafeText('useTemporaryCredentials')
        self.duration = self.getSafeText('useTemporaryCredentials')
        self.region = self.getSafeText('useTemporaryCredentials')
        self.customerHeaders = []   # TODO: implement

class SmbSchemeProperties(SchemeProperties):
    def __init__(self, uXml):
        SchemeProperties.__init__(self, uXml)

        self.smbMinVersion = self.getSafeText('smbMinVersion')
        self.smbMaxVersion = self.getSafeText('smbMaxVersion')
#endregion

#region Mapping
class Mapping():   
    def recieverProperties(c: str) -> Type:
        if c == "com.mirth.connect.connectors.vm.VmReceiverProperties":
            return VmReceiverProperties
        elif c == "com.mirth.connect.connectors.dimse.DICOMReceiverProperties":
            return DICOMReceiverProperties
        elif c == "com.mirth.connect.connectors.jdbc.DatabaseReceiverProperties":
            return DatabaseReceiverProperties
        elif c == "com.mirth.connect.connectors.file.FileReceiverProperties":
            return FileReceiverProperties
        elif c == "com.mirth.connect.connectors.http.HttpReceiverProperties":
            return HttpReceiverProperties
    
    def schemeProperties(c: str) -> Type:
        if c == "com.mirth.connect.connectors.file.SftpSchemeProperties":
            return SftpSchemeProperties
        elif c == "com.mirth.connect.connectors.file.FTPSchemeProperties":
            return FTPSchemeProperties
        elif c == "com.mirth.connect.connectors.file.S3SchemeProperties":
            return S3SchemeProperties    
        elif c == "com.mirth.connect.connectors.file.SmbSchemeProperties":
            return SmbSchemeProperties
    
    def httpAuthProperties(c: str) -> Type:
        if c == "com.mirth.connect.plugins.httpauth.basic.BasicHttpAuthProperties":
            return BasicHttpAuthProperties
        elif c == "com.mirth.connect.plugins.httpauth.digest.DigestHttpAuthProperties":
            return DigestHttpAuthProperties
        elif c == "com.mirth.connect.plugins.httpauth.javascript.JavaScriptHttpAuthProperties":
            return JavaScriptHttpAuthProperties
        elif c == "com.mirth.connect.plugins.httpauth.custom.CustomHttpAuthProperties":
            return CustomHttpAuthProperties
        elif c == "com.mirth.connect.plugins.httpauth.oauth2.OAuth2HttpAuthProperties":
            return OAuth2HttpAuthProperties

#endregion