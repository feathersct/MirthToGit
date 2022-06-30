from typing import Type
from models.channels.connector import ConnectorProperties
from models.properties.httpAuthProperties import *
from models.properties.receiverProperties import *
from models.properties.schemeProperties import *


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
        else:
            return ConnectorProperties
    
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
