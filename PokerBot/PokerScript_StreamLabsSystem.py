import json
import os
import codecs
import random

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

class Deck:
    _READY = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", 
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", 
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", 
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH"]

    ready = _READY[:]
    table = []
    inUse = []
    burned = []

    def __init__(self):
        return

    def __str__(self):
        return ' '.join(self.ready)

    def resetDeck(self):
        self.ready = self._READY[:]
        self.burned = []
        self.inUse = []

    def flipCard(self):
        self.table.append(self._pullRandCard())

    def dealCard(self):
        c = self._pullRandCard()
        self.inUse.append(c)
        return c

    def burn(self):
        self.burned.append(self._pullRandCard())

    def _pullRandCard(self):
        i = random.randint(0, len(self.ready) - 1)
        r = self.ready.pop(i)
        return r

class Table:
    deck = Deck()
    players = []
    isHand = False

    def __init__(self):
        return
    
    def __str__(self):
        return "Players seated: " + self.players + ", Is active hand: " + self.isHand

    def openTable(self):
        self.deck.resetDeck()
        self.players = []
        print("The table is now accepting buyins.")
        return
    
    def dealHand(self):
        self.deck.resetDeck()
        for i in range(2):
            for p in self.players:
                p.append(self.deck.dealCard())
        
        return

    def addPlayer(self, player):
        self.players.append(player)
        return

    def removePlayer(self):
        return

    def getPlayer(self):
        return

def Init():
    global configs, environment, commands, table
    work_dir = os.path.dirname(__file__)
    try:
        with codecs.open(os.path.join(work_dir, "./src/config.json"), encoding='utf-8-sig') as configs_json:
            configs = json.load(configs_json, encoding='utf-8-sig')
        with codecs.open(os.path.join(work_dir, "./src/environment.json"), encoding='utf-8-sig') as environment_json:
            environment = json.load(environment_json, encoding='utf-8-sig')
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
    if data.IsChatMessage() and (commands.data.GetParam(0).lower()) and Parent.HasPermission(data.User, configs["permission"], "") and not Parent.IsOnUserCooldown(ScriptName, data.GetParam(0).lower(), data.User):
        username = data.UserName
        points = Parent.GetPoints(data.User)
        currency = Parent.GetCurrencyName()
        
        responseMessage = configs["responseMessage"]
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


def main():
    global configs, environment, commands
    work_dir = os.path.dirname(__file__)
    try:
        with codecs.open(os.path.join(work_dir, "./src/config.json"), encoding='utf-8-sig') as configs_json:
            configs = json.load(configs_json, encoding='utf-8-sig')
        with codecs.open(os.path.join(work_dir, "./src/environment.json"), encoding='utf-8-sig') as environment_json:
            environment = json.load(environment_json, encoding='utf-8-sig')
        with codecs.open(os.path.join(work_dir, "./src/commands.json"), encoding='utf-8-sig') as commands_json:
            commands = json.load(commands_json, encoding='utf-8-sig')
    except Exception as e:
        print("Error on config reads: " + repr(e))
    

    print("Command 1: " + commands[0]['cmd'])
    table = Table()
    table.openTable()
    table.addPlayer([])
    table.addPlayer([])
    table.addPlayer([])
    table.dealHand()
    for p in table.players:
        print("Player Hand: " + str(p))



if __name__ == "__main__":
    main()
