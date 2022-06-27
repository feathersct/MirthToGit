# MirthToGit

MirthToGit is a python script to monitor and push changes to Mirth Connect Instances

## Getting Started
Clone the GitHub project and add a config file (config.json) to the root directory.

Config file must match the following: 
```sh
{
    "instanceName": "{instance IP or DNS Name}",
    "credentials": {
        "username": "{username}", 
        "password": "{password}"
    },
    "github": {
        "username" : "{github password}",
        "password" : "{github password}",
        "repo" : "{github repo to hold channels and code templates}"
    }
}
```