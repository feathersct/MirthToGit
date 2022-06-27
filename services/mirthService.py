import requests
from models.channels.channels import Channels
from models.codeTemplates.codeTemplates import CodeTemplates
from models.events.events import Events
from models.users.users import Users


class MirthService:
    apiUrl = "";
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest'
    }

    def __init__(self, configuration):
        #configuration is a json object
        self.instance = configuration.get('instanceName')
        self.credentials = configuration.get('credentials')
        self.jsessionId = ''

        # intialize and login
        self.initialize(True)

    # Intialize any variables after constructor
    def initialize(self, login=False):
        self.apiUrl = f"https://{self.instance}:8443/api"

        if(login):
            self.login()

    # User Calls
    def login(self):
        x = requests.post(f"{self.apiUrl}/users/_login?username={self.credentials.get('username')}&password={self.credentials.get('password')}", verify=False, headers=self.headers)

        self.jsessionId = x.cookies.get('JSESSIONID')

    def getUsers(self):
        users = requests.get(f"{self.apiUrl}/users", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return Users(users.content)

    # Event Calls
    def getEvents(self, params = {}):

        parameters = []
        for key,value in params.items():
            parameters.append(f"{key}={value}")

        encParam = '?' + '&'.join(parameters)

        events = requests.get(f"{self.apiUrl}/events" + encParam, headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return Events(events.content)

    # Channel Calls
    def getChannels(self, params = {}):
        
        parameters = []
        for key,value in params.items():
            parameters.append(f"{key}={value}")

        encParam = '?' + '&'.join(parameters)

        events = requests.get(f"{self.apiUrl}/channels" + encParam, headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return Channels(events.content)

    # Code Template Calls
    def getCodeTemplates(self, params = {}):
        
        parameters = []
        for key,value in params.items():
            parameters.append(f"{key}={value}")

        encParam = '?' + '&'.join(parameters)

        events = requests.get(f"{self.apiUrl}/codeTemplates" + encParam, headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return CodeTemplates(events.content)





