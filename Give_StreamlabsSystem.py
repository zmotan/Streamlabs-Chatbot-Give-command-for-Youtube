import clr
import sys
import json
import os
import ctypes
import codecs


ScriptName = "Give points"
Website = "http://zmotan.com"
Description = "Script for transfering points between Youtube users."
Creator = "Zmotan"
Version = "4.20.69"


configFile = "config.json"
settings = {}


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
		viewerLegitList = []
		viewerLowerList = []
		viewerListID = []
		giveToName = ""
		
		if paramCount >= 3:
			lastIndex = paramCount - 1
			lastParam = data.GetParam(lastIndex)
			receiverNameTemp = data.Message
			receiverNameTemp = receiverNameTemp.replace(settings["command"]+" ", "")
			receiverNameTemp = receiverNameTemp.replace(" "+lastParam, "")
			firstLetterRNT = receiverNameTemp[:1]
			if firstLetterRNT == "@":
				receiverName = receiverNameTemp[1:]
			else: 
				receiverName = receiverNameTemp

			try:
				costs = int(lastParam)
			except:
				if lastParam == 'all': 
					costs = giverPoints
				elif lastParam == 'ALL': 
					costs = giverPoints
				elif lastParam == 'All': 
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
			currentViewers = Parent.GetViewerList()
			for viewer in currentViewers:
				viewerListID.append(viewer)
		
				viewerLegitName = Parent.GetDisplayName(viewer)
				viewerLegitList.append(viewerLegitName)
				
				viewerLowerName = Parent.GetDisplayName(viewer).lower()
				viewerLowerList.append(viewerLowerName)

			if receiverName.lower() in viewerLowerList:
				viewerIndex = viewerLowerList.index(receiverName.lower())
				giveToName = viewerLegitList[viewerIndex]
				giveToID = viewerListID[viewerIndex]
				
				Parent.RemovePoints(giverID, giverName, costs)			
				Parent.AddPoints(giveToID, giveToName, costs)
				
				outputMessage = settings["responseSuccess"]
			else:
				giveToName = receiverName
				outputMessage = settings["responseNoTargetFound"]


		outputMessage = outputMessage.replace("$cost", str(costs))
		outputMessage = outputMessage.replace("$user", giverName)
		outputMessage = outputMessage.replace("$points", str(giverPoints))
		outputMessage = outputMessage.replace("$currency", Parent.GetCurrencyName())
		outputMessage = outputMessage.replace("$command", settings["command"])
		outputMessage = outputMessage.replace("$target", giveToName)
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
