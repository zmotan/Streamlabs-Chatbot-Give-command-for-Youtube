import clr
import sys
import json
import os
import ctypes
import codecs
from System.Collections.Generic import List


ScriptName = "Give points"
Website = "http://zmotan.com"
Description = "Script for transfering points between Youtube users."
Creator = "Zmotan"
Version = "4.20"

configFile = "config.json"
settings = {}
receiverName = ""


def ScriptToggled(state):
	return

def Init():
	global settings

	path = os.path.dirname(__file__)
	try:
		with codecs.open(os.path.join(path, configFile), encoding='utf-8-sig', mode='r') as file:
			settings = json.load(file, encoding='utf-8-sig')
	except:
		settings = {
			"liveOnly": False,
			"command": "!give",
			"permission": "Everyone",
			"responseNotEnoughPoints": "$user, you don't have $cost $currency, you have $points $currency.",
			"responseNotIntiger": "$user, value is not positive intiger or argument is missing. Must be at least 1. Template: !give [username] [value]",
			"responseSuccess": "$user gave $target $cost $currency.",
			"responseNoTargetFound": "$user, user with name $target was not found.",
			"responseGiverIsTaker": "$user, what's the point of giving yourself nothing?"
		}


def Execute(data):
	if data.IsChatMessage() and data.GetParam(0).lower() == settings["command"] and Parent.HasPermission(data.User, settings["permission"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
		outputMessage = ""
		giverID = data.User
		giverName = data.UserName
		giverPoints = Parent.GetPoints(giverID)
		paramCount = data.GetParamCount()
		receiverName = ""

		if paramCount >= 3:
			lastIndex = paramCount - 1
			lastParam = data.GetParam(lastIndex)
			tempmessage = data.Message
			messageArray = tempmessage.split()
			messageArray.pop(lastIndex)
			messageArray.pop(0)
			receiverNameTemp = ' '.join(messageArray)
			firstLetterRNT = receiverNameTemp[:1]
			if firstLetterRNT == "@":
				receiverName = receiverNameTemp[1:]
			else: 
				receiverName = receiverNameTemp

			Parent.Log(ScriptName, receiverNameTemp + " -> " + receiverName)
			try:
				costs = int(lastParam)
			except:
				if data.GetParam(lastIndex) == 'all': 
					costs = giverPoints
				elif data.GetParam(lastIndex) == 'ALL': 
					costs = giverPoints
				elif data.GetParam(lastIndex) == 'All': 
					costs = giverPoints
				else :
					costs = -1
		else:
			costs = -1


		if (costs > Parent.GetPoints(giverID)):
			outputMessage = settings["responseNotEnoughPoints"]
		elif (costs <= 0):
			outputMessage = settings["responseNotIntiger"]
		elif giverName == receiverName:
			outputMessage = settings["responseGiverIsTaker"]
		else:
			for viewer in Parent.GetViewerList():
				viewerName = Parent.GetDisplayName(viewer)
				if receiverName.lower() == viewerName.lower():
					Parent.RemovePoints(giverID, giverName, costs)
					Parent.AddPoints(viewer, viewerName, costs)
					outputMessage = settings["responseSuccess"]
					break
				else:
					outputMessage = settings["responseNoTargetFound"]


		outputMessage = outputMessage.replace("$cost", str(costs))
		outputMessage = outputMessage.replace("$user", giverName)
		outputMessage = outputMessage.replace("$points", str(giverPoints))
		outputMessage = outputMessage.replace("$currency", Parent.GetCurrencyName())
		outputMessage = outputMessage.replace("$command", settings["command"])
		outputMessage = outputMessage.replace("$target", receiverName)
		Parent.SendStreamMessage(outputMessage)

	return

def ReloadSettings(jsonData):
	Init()

	return

def OpenReadMe():
	location = os.path.join(os.path.dirname(__file__), "README.txt")
	os.startfile(location)
	return

def Tick():
	return
