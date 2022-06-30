from typing import Type
from models.mirthElement import MirthElement
from models.properties.httpAuthProperties import *
from models.properties.receiverProperties import *
from models.properties.schemeProperties import *


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



