import json
import os
import codecs
import random


from collections import namedtuple

# Required to properly identify imports in Streamlabs
import sys
sys.path.append('.\Services\Scripts\PokerBot')
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import clr
clr.AddReference("IronPython.Modules.dll")
clr.AddReference("System.Windows.Forms")

from src.command import Command
from src.deck import Deck
from src.table import Table
from src.player import Player

# Describes issue with whispers:
#   https://github.com/tmijs/tmi.js/issues/333
# Whispering requires bot to be approved for rate limit increase:
#

# Variable Required by Streamlabs
ScriptName = "Poker Script"
Website = "https://github.com/demarcot"
Description = "Script for interactive chat-based Texas Hold 'em."
Creator = ""
Version = ""

scriptState = None

# Initialize the Script State
def Init():
    global scriptState, ScriptName, Website, Description, Creator, Version

    scriptState = ScriptState()

    work_dir = os.path.dirname(__file__)
    try:
        with codecs.open(os.path.join(work_dir, "./src/config/config.json"), encoding='utf-8-sig') as configs_json:
            scriptState.configs = json.load(configs_json, encoding='utf-8-sig')
        with codecs.open(os.path.join(work_dir, "./src/config/environment.json"), encoding='utf-8-sig') as environment_json:
            scriptState.environment = json.load(environment_json, encoding='utf-8-sig')
        with codecs.open(os.path.join(work_dir, "./src/config/commands.json"), encoding='utf-8-sig') as commands_json:
            scriptState.commands = json.load(commands_json, encoding='utf-8-sig', object_hook=Command.ConvertDictToObj)
        log("Configs, env vars, and commands loaded.")
    except Exception as e:
        log("Default settings used: " + repr(e))
        scriptState.configs = {
            "responseMessage" : "[WARNING] Default settings in use. Config file not processed.",
            "cooldown" : 0,
            "permission" : "Everyone"
        }
        scriptState.environment = {
            "creator": "Unknown",
            "version": "0.0.0"
        }

    scriptState.Creator = scriptState.environment["creator"]
    Creator = scriptState.Creator
    scriptState.Version = scriptState.environment["version"]
    Version = scriptState.Version
    scriptState.table = Table() # Table initialized, but closed
    return

def Execute(data):
    scriptState.HandleCommand(data.GetParam(0).lower(), Parent, data)
    return

def Tick():
    return

def ReloadSettings(jsonData):
    return

def Unload():
    return

def send_message(message):
    Parent.SendStreamMessage(message)
    return

def send_whisper(user, message):
    Parent.SendStreamWhisper(user, message)
    return

def log(message):
    Parent.Log(scriptState.ScriptName, message)
    return

class ScriptState:
    def __init__(self):
        self.ScriptName = "Poker Script"
        self.Website = "https://github.com/demarcot"
        self.Description = "Script for interactive chat-based Texas Hold 'em."
        self.Creator = ""
        self.Version = ""

        self.environment = {}
        self.configs = {}
        self.commands = {}
        self.table = None

        return

    def HandleCommand(self, cmdName, parent, data):
        curCommand = self.FetchCommand(cmdName)
        if (
            curCommand is not None and 
            data.IsChatMessage() and 
            parent.HasPermission(data.User, curCommand.permission, "") and 
            not parent.IsOnUserCooldown(self.ScriptName, data.GetParam(0).lower(), data.User)
        ):
            params = []
            for i in range(1, data.GetParamCount()): # Skip 1st param (the command)
                params.append(data.GetParam(i))
        
            self.DispatchCommand(curCommand, parent, data, params)
        return

    def FetchCommand(self, cmdName):
        for c in self.commands:
            if c.cmd == cmdName:
                return c
        return None

    def DispatchCommand(self, cmd, parent, data, params):
        log("Dispatching command: " + str(cmd) + ", " + str(data))
        responseMessage = cmd.val1
        responseMessage = responseMessage.replace("$user", data.UserName)
        send_message(responseMessage)
        #TODO(Tom): Use this if bot is ever cleared for whispers
        #send_whisper(data.UserName, responseMessage)
        
        #Parent.AddUserCooldown(ScriptName, commandName, data.User, settings["cooldown"])
        #Parent.RemovePoints(data.User, username, cost)
        #username = data.UserName
        #points = Parent.GetPoints(data.User)
        #currency = Parent.GetCurrencyName()
        #responseMessage = curCommand.val1
        #responseMessage = responseMessage.replace("$user", data.UserName)
        #send_message(responseMessage)
        return


'''
def main():
    global configs, environment, commands
    work_dir = os.path.dirname(__file__)
    try:
        with codecs.open(os.path.join(work_dir, "./src/config/config.json"), encoding='utf-8-sig') as configs_json:
            configs = json.load(configs_json, encoding='utf-8-sig')
        with codecs.open(os.path.join(work_dir, "./src/config/environment.json"), encoding='utf-8-sig') as environment_json:
            environment = json.load(environment_json, encoding='utf-8-sig')
        with codecs.open(os.path.join(work_dir, "./src/config/commands.json"), encoding='utf-8-sig') as commands_json:
            commands = json.load(commands_json, encoding='utf-8-sig', object_hook=Command.ConvertDictToObj)
    except Exception as e:
        print("Error on config reads: " + repr(e))
    

    print("Command: " + str(commands[0]))
    print("Command: " + str(commands[1]))
    table = Table()
    table.openTable()
    table.addPlayer(Player("tom", configs['stackSize'], []))
    table.addPlayer(Player("bob", configs['stackSize'], []))
    table.addPlayer(Player("jon", configs['stackSize'], []))
    table.dealHand()
    for p in table.players:
        print("Player Hand: " + str(p))



if __name__ == "__main__":
    main()
'''