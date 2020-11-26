import json
import os
import codecs
import random

# Describes issue with whispers
#https://github.com/tmijs/tmi.js/issues/333

ScriptName = "Poker Script"
Website = "https://github.com/demarcot"
Description = "Script for interactive chat-based Texas Hold 'em."
Creator = ""
Version = ""

settings = {}
commandName = ""

class Deck:
    _READY = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", 
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", 
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", 
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH"]

    ready = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", 
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", 
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", 
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH"]
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
        self.table.append(self.pullRandCard())

    def dealCard(self):
        c = self.pullRandCard()
        self.inUse.append(c)
        return c

    def burn(self):
        self.burned.append(self.pullRandCard())

    def pullRandCard(self):
        i = random.randint(0, len(self.ready) - 1)
        r = self.ready.pop(i)
        return r

    

def Init():
    global settings, commandName
    work_dir = os.path.dirname(__file__)
    deck = Deck()
    try:
        with codecs.open(os.path.join(work_dir, "config.json"), encoding='utf-8-sig') as json_file:
            settings = json.load(json_file, encoding='utf-8-sig')
            Creator = settings["creator"]
            Version = settings["version"]
    except:
        settings = {
            "commandName" : "!test",
            "responseMessage" : "Command was used by $user",
            "cooldown" : 15,
            "permission" : "Everyone"
            }
    commandName = settings["commandName"]
    log("Deck ready: " + str(deck))
    #log("Deck ready... ")
    return

def Execute(data):
    if data.IsChatMessage() and (data.GetParam(0).lower() == commandName) and Parent.HasPermission(data.User, settings["permission"], "") and not Parent.IsOnUserCooldown(ScriptName, commandName, data.User):
        username = data.UserName
        points = Parent.GetPoints(data.User)
        currency = Parent.GetCurrencyName()
        
        responseMessage = settings["responseMessage"]
        responseMessage = responseMessage.replace("$user", data.UserName)
        send_message(responseMessage)

        #TODO(Tom): Use this if bot is ever cleared for whispers
        send_whisper(data.UserName, responseMessage)
        
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

"""
def main():
    d = Deck()
    d.burn()
    d.dealCard()
    d.dealCard()
    print("Ready: " + ' '.join(d.ready))
    print("In Use: " + ' '.join(d.inUse))
    print("Burned: " + ' '.join(d.burned))
    print("\n\n")

    d.resetDeck()
    print("Ready: " + ' '.join(d.ready))
    print("In Use: " + ' '.join(d.inUse))
    print("Burned: " + ' '.join(d.burned))
    d.burn()
    d.dealCard()
    d.dealCard()
    print("Ready: " + ' '.join(d.ready))
    print("In Use: " + ' '.join(d.inUse))
    print("Burned: " + ' '.join(d.burned))
    print("\n\n")

    d.resetDeck()
    print("Ready: " + ' '.join(d.ready))
    print("In Use: " + ' '.join(d.inUse))
    print("Burned: " + ' '.join(d.burned))


if __name__ == "__main__":
    main()
"""