import requests
from services.mirthService import MirthService

from models.users.users import Users

mirthConfig = {
    "instanceName": "18.208.106.238",
    "credentials": {
        "username": "admin", 
        "password": "admin"
    }
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest'
}

service = MirthService(mirthConfig)

userList = service.getUsers()
events = service.getEvents(
        {
            "name": "Create channel",
            "outcome": "SUCCESS",
            "limit": 20
        }
    )

print("jfjf")


