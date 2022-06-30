from typing import Type
from models.mirthElement import MirthElement


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

