from models.channels.connector import ListenerConnectorProperties, Mapping, SourceConnectorProperties
from models.mirthElement import MirthElement


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
        prop = Mapping.schemeProperties(self.root.find('schemeProperties').attrib['class'])
        
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
                prop = Mapping.httpAuthProperties(e.tag)
        
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
   