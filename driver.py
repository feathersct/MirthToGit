from fileinput import filename
import string
from xml.etree import ElementTree
import requests
import colorama
import time
from datetime import datetime
from colorama import Fore
from services.mirthService import MirthService
import json
import base64
import pathlib
from github import Github
from github import InputGitTreeElement

config = json.load(open('config.json'))

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest'
}

def checkForChanges():
    file_list = []
    changeEvents = []

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

        # Loop through events
        for e in events.events:
            try:
                # Process Updated Channel Changes
                if e.name == 'Update channel' or e.name == 'Create channel':
                    if e.attributes[0][0] == 'channel':
                        a = e.attributes[0][1]
                        channelId = a.split(',')[0].split('=')[1]

                        if channelId != None:
                            channels = service.getChannels({
                                "channelId" : channelId
                            })

                            file_list.append(saveFile("Channels\\" + channels.channels[0].name, channels.channels[0].xmlString()))
                            
                            user = service.getUser(e.userId)
                            changeEvents.append(f"{user.username} {e.name}: {channels.channels[0].name}")

                            print(Fore.RED + 'ChannelId: ' + channels.channels[0].name + Fore.WHITE)
            except Exception as ex:
                n = 0 # do nothing

            try:
                # Process updated code template changes
                if e.attributes[1][0] == 'updatedCodeTemplates':
                    if e.attributes[1][1] != None:
                        a = e.attributes[1][1]
                        codeTemplateId = a.split(',')[0].split('=')[1]

                        if codeTemplateId != None:
                            codeTemplates = service.getCodeTemplates({
                                "codeTemplateId" : codeTemplateId
                            })
                            file_list.append(saveFile("CodeTemplates\\" + codeTemplates.codeTemplates[0].name, codeTemplates.codeTemplates[0].xmlString()))
                            user = service.getUser(e.userId)
                            changeEvents.append(f"{user.username} {e.name}: {codeTemplates.codeTemplates[0].name}")


                            print(Fore.RED + 'CodeTemplate: ' + codeTemplates.codeTemplates[0].name + Fore.WHITE)
            except Exception as ex:
                print(ex)
                n = 0 # do nothing
        


        # ----------------------
        #  Push Changes to Git
        # ----------------------
        if len(file_list) > 0:
            githubProp = config.get('github')

            g = Github(githubProp.get('username'), githubProp.get('password'))
            repo = g.get_user().get_repo(githubProp.get('repo')) 

            commit_message = '; '.join(changeEvents)
            master_ref = repo.get_git_ref('heads/main')
            master_sha = master_ref.object.sha
            base_tree = repo.get_git_tree(master_sha)

            element_list = list()
            for i, entry in enumerate(file_list):
                with open(entry) as input_file:
                    data = input_file.read()
                if entry.endswith('.png'): # images must be encoded
                    data = base64.b64encode(data)

                fileName = entry.replace(f"{str(pathlib.Path().resolve())}\\files\\", '').replace('\\','/')
                element = InputGitTreeElement(fileName, '100644', 'blob', data)
                element_list.append(element)

            tree = repo.create_git_tree(element_list, base_tree)
            parent = repo.get_git_commit(master_sha)
            commit = repo.create_git_commit(commit_message, tree, [parent])
            master_ref.edit(commit.sha)   

            file_list.clear()
            changeEvents.clear()

        time.sleep(20)

def saveFile(name, xmlStr):
    path = pathlib.Path().resolve()
    filename = f"{str(path)}\\files\\{name}.xml"
    f = open(filename, "w")
    f.write(xmlStr)
    f.close()

    return filename


checkForChanges()
