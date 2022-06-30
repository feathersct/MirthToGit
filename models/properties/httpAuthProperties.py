from typing import Type
from models.mirthElement import MirthElement


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
