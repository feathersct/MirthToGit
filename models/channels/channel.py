class Channel:
    def __init__(self, uXml):
        self.id = uXml.find('id').text
        self.nextMetaDataId = uXml.find('nextMetaDataId').text
        self.description = uXml.find('description').text
        self.name = uXml.find('name').text
        self.revision = uXml.find('revision').text

        #TODO: convert to class
        self.sourceConnector = uXml.find('sourceConnector')
        self.preprocessingScript = uXml.find('preprocessingScript')
        self.postprocessingScript = uXml.find('postprocessingScript')
        self.deployScript = uXml.find('deployScript')
        self.undeployScript = uXml.find('undeployScript')
        self.properties = uXml.find('properties')

        self.destinationConnectors = []
        for c in uXml.findall('./destinationConnectors/connector'):
            self.destinationConnectors.append(c)