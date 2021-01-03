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

ScriptName = "Poker Script"
Website = "https://github.com/demarcot"
Description = "Script for interactive chat-based Texas Hold 'em."
Creator = ""
Version = ""

environment = {}
configs = {}
commands = {}

def Init():
    global configs, environment, commands, table

    log("Initiating...")
    work_dir = os.path.dirname(__file__)
    try:
        with codecs.open(os.path.join(work_dir, "./src/config/config.json"), encoding='utf-8-sig') as configs_json:
            configs = json.load(configs_json, encoding='utf-8-sig')
        with codecs.open(os.path.join(work_dir, "./src/config/environment.json"), encoding='utf-8-sig') as environment_json:
            environment = json.load(environment_json, encoding='utf-8-sig')
        with codecs.open(os.path.join(work_dir, "./src/config/commands.json"), encoding='utf-8-sig') as commands_json:
            commands = json.load(commands_json, encoding='utf-8-sig', object_hook=Command.ConvertDictToObj)
    except Exception as e:
        log("Default settings used: " + repr(e))
        configs = {
            "responseMessage" : "[WARNING] Default settings in use. Config file not processed.",
            "cooldown" : 0,
            "permission" : "Everyone"
        }
        environment = {
            "creator": "Unknown",
            "version": "0.0.0"
        }

    Creator = environment["creator"]
    Version = environment["version"]
    table = Table()
    log("Creator: " + Creator)
    return

def Execute(data):
    curCommand = FetchCommand(data.GetParam(0).lower())
    if data.IsChatMessage() and Parent.HasPermission(data.User, curCommand.permission, "") and not Parent.IsOnUserCooldown(ScriptName, data.GetParam(0).lower(), data.User):
        log("In Message handler." + str(curCommand))
        username = data.UserName
        points = Parent.GetPoints(data.User)
        currency = Parent.GetCurrencyName()
        
        responseMessage = curCommand.val1
        responseMessage = responseMessage.replace("$user", data.UserName)
        send_message(responseMessage)

        #TODO(Tom): Use this if bot is ever cleared for whispers
        #send_whisper(data.UserName, responseMessage)
        
        #Parent.AddUserCooldown(ScriptName, commandName, data.User, settings["cooldown"])
        #Parent.RemovePoints(data.User, username, cost)
    return

def DoStuff():
    log("stuff has happened!")
    return

def FetchCommand(cmdName):
    for c in commands:
        if c.cmd == cmdName:
            return c
    return None

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
    Parent.Log(ScriptName, message)
    return

def convertDictToObject(jsonObj):
    return namedtuple('X', jsonObj.keys())(*jsonObj.values())

def convertDictToCommand(jsonObj):
    return Command(jsonObj['cmd'], jsonObj['permission'], jsonObj['val1'], jsonObj['val2'])

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