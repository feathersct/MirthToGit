import requests
import colorama
import time
from datetime import datetime
from colorama import Fore
from services.mirthService import MirthService
import json
import base64
from github import Github
from github import InputGitTreeElement

config = json.load(open('config.json'))

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest'
}

service = MirthService(config)
end_date = None

while True:
    # Set Dates to query for events
    if end_date is None:
        start_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000−0400")
    else:
        start_date = end_date

    end_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000−0400")

    # Get Channels
    events = service.getEvents(
            {
                "outcome": "SUCCESS",
                "limit": 20,
                "startDate": start_date,
                "endDate": end_date
            }
        )

    for e in events.events:
        try:
            if events.events[0].attributes[0][0] == 'channel':
                a = events.events[0].attributes[0][1]
                channelId = a.split(',')[0].split('=')[1]

                if channelId != None:
                    channels = service.getChannels({
                        "channelId" : channelId
                    })

                    print(Fore.RED + 'ChannelId: ' + channels.channels[0].name + Fore.WHITE)
        except:
            n = 0 # do nothing

        try:
            if e.attributes[1][0] == 'updatedCodeTemplates':
                if e.attributes[1][1] != None:
                    a = e.attributes[1][1]
                    codeTemplateId = a.split(',')[0].split('=')[1]

                    if codeTemplateId != None:
                        codeTemplates = service.getCodeTemplates({
                            "codeTemplateId" : codeTemplateId
                        })

                        print(Fore.RED + 'CodeTemplate: ' + codeTemplates.codeTemplates[0].name + Fore.WHITE)
        except:
            n = 0 # do nothing
    time.sleep(5)



