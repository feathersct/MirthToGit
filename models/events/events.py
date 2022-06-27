import xml.etree.ElementTree as ET
from models.events.event import Event

class Events:
    def __init__(self, listXML):
        events = ET.fromstring(listXML)
        self.events = []

        for e in events.findall('./event'):
            self.events.append(Event(e))