from django.shortcuts import render,HttpResponse,reverse,HttpResponseRedirect
from django import forms
from .forms import *
import datetime
from .models import EggInfo
from  django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView
from .IncubatorMonitor.sensor import *
import random
from .IncubatorMonitor.interface import systemInterface
import json

This_Interface = systemInterface()
eggList = This_Interface.getEggList()
eggTimerSetJson = ""
settingsJson = ""
def home(request):
	eggTimerSetJson = json.load(open('buffer.txt'))
	settings = json.load(open('settings.txt'))
	return render(request,'home.html',{'eggTimerSetJson':eggTimerSetJson})

def programmingPage(request):
	eggList = This_Interface.getEggList()
	Addform = AddEggForm(request.POST or None)
	Delform = DeleteEggForm(request.POST or None)
	Clearform = ClearAllEggsFromDBForm(request.POST or None)
	TimeForm = TimerForm(request.POST or None)
	TimeTurnForm = TimerForm(request.POST or None)
	InfoEgg = EggInfo.objects.all()
	if request.method == 'POST':
		if request.method == 'POST' and "add-submit" in request.POST:
			if Addform.is_valid():
				Addform = AddEggForm(request.POST or None)
				t1 = request.POST.get('breed')
				t2 = request.POST.get('eggType')
				t3 = request.POST.get('eggSize')
				Eg = EggInfo.objects.create(breed=t1, typeOfEgg=t2, sizeOfEgg=t3)
				Eg.save()
				InfoEgg = EggInfo.objects.all()
				This_Interface.addEggToBatch(t1, t2, t3)
				eggList = This_Interface.getEggList()
			else:
				print(Addform.errors)
		if request.method == 'POST' and "delete-submit" in request.POST:
				#Delform = DeleteEggForm(request.POST or None)
				if Delform.is_valid():
					choice = request.POST.get('eggToDelete')
					Eg = EggInfo.objects.filter(id=choice).delete()
					InfoEgg = EggInfo.objects.all()
				else:
					print(Delform.errors)
		if request.method == 'POST' and "clear-submit" in request.POST:
			#Clearform = ClearAllEggsFromDBForm(request.POST or None)
				if Clearform.is_valid():
					choice = request.POST.get('field')

					if choice == "True":
						print("Choice made!")
						Eg = EggInfo.objects.all().delete()
						InfoEgg = EggInfo.objects.all()
				else:
					print(Clearform.errors)
		if request.method == 'POST' and "time-submit" in request.POST:
			#Clearform = ClearAllEggsFromDBForm(request.POST or None)
				if TimeForm.is_valid():
					days = request.POST.get('DaysInTimer')
					hours= request.POST.get('HoursInTimer')
					minutes = request.POST.get('MinutesInTimer')
					seconds = request.POST.get('SecondsInTimer')
					setFlag = "true"
					with open('buffer.txt', 'w') as outfile:
						timerToSet = {'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds, 'Flag': setFlag}
						json.dump(timerToSet,outfile)
					print(days," ",hours," ",minutes," ",seconds)
				else:
					print(Clearform.errors)

		if request.method == 'POST' and "turn-time-submit" in request.POST:
			#Clearform = ClearAllEggsFromDBForm(request.POST or None)
				if TimeTurnForm.is_valid():
					days = request.POST.get('DaysInTimer')
					hours= request.POST.get('HoursInTimer')
					minutes = request.POST.get('MinutesInTimer')
					seconds = request.POST.get('SecondsInTimer')
					setFlag = "true"
					with open('buffer.txt', 'w') as outfile:
						timerToSet = {'TurnDays': days, 'TurnHours': hours, 'TurnMinutes': minutes, 'TurnSeconds': seconds, 'Flag': setFlag}
						json.dump(timerToSet,outfile)
					print(days," ",hours," ",minutes," ",seconds)
				else:
					print(Clearform.errors)
	else:
		Addform = AddEggForm()
		Delform = DeleteEggForm()
		Clearform = ClearAllEggsFromDBForm()
		InfoEgg = EggInfo.objects.all()
		TimeForm = TimerForm()
		TimeTurnForm = TimerForm()

	return render(request, 'IncubatorProgramming.html', {'Addform': Addform,'Delform': Delform,'ClearForm': Clearform,'InfoEgg':InfoEgg,'TimerForm':TimeForm,'TimeTurnForm':TimeTurnForm})

def settingsPage(request):

	tempForm = TemperatureForm()
	timeForm = TimeUnitForm()
	if request.method == 'POST':
		if request.method == 'POST' and "temperature-change-submit" in request.POST:
			tempForm = TemperatureForm(request.POST or None)
			if tempForm.is_valid():
				choice = request.POST.get('temperatureChoice')
				if choice == "Celsius":
					with open('settings.txt', 'r') as outfile:
						#settingsToSet = {'TemperatureUnit':choice}
						data = json.load(outfile)
						data['TemperatureUnit'] = choice
						with open("settings.txt", "w") as jsonFile:
							json.dump(data, jsonFile)
					This_Interface.setTemperatureUnits("Celsius")
				elif choice == "Farenheit":
					with open('settings.txt', 'r') as outfile:
						#settingsToSet = {'TemperatureUnit':choice}
						data = json.load(outfile)
						data['TemperatureUnit'] = choice
						with open("settings.txt", "w") as jsonFile:
							json.dump(data, jsonFile)
					This_Interface.setTemperatureUnits("Farenheit")
				elif choice == "Kelvin":
					with open('settings.txt', 'r') as outfile:
						#settingsToSet = {'TemperatureUnit':choice}
						data = json.load(outfile)
						data['TemperatureUnit'] = choice
						with open("settings.txt", "w") as jsonFile:
							json.dump(data, jsonFile)
					This_Interface.setTemperatureUnits("Kelvin")
				else:
					with open('settings.txt', 'r') as outfile:
						#settingsToSet = {'TemperatureUnit':choice}
						data = json.load(outfile)
						data['TemperatureUnit'] = choice
						with open("settings.txt", "w") as jsonFile:
							json.dump(data, jsonFile)
					This_Interface.setTemperatureUnits("Celsius")
			else:
				print(tempForm.errors)
		if request.method == 'POST' and "time-change-submit" in request.POST:
			tempForm = TemperatureForm(request.POST or None)
			timeForm = TimeUnitForm(request.POST or None)
			if tempForm.is_valid():
				choice = request.POST.get('TimeChoice')
				print(choice)
				if choice == "12":
					with open('settings.txt', 'r') as outfile:
						# settingsToSet = {'TemperatureUnit':choice}
						data = json.load(outfile)
						data['TimeFormat'] = choice
						with open("settings.txt", "w") as jsonFile:
							json.dump(data, jsonFile)
				else:
					with open('settings.txt', 'r') as outfile:
						# settingsToSet = {'TemperatureUnit':choice}
						data = json.load(outfile)
						data['TimeFormat'] = choice
						with open("settings.txt", "w") as jsonFile:
							json.dump(data, jsonFile)
			else:
				print(tempForm.errors)
	else:
			tempForm = TemperatureForm()
			timeForm = TimeUnitForm()
	return render(request,'IncubatorSettingsPage.html',{'TempForm':tempForm,'TimeForm':timeForm})

def helpPage(request):
	return render(request,'helpGuide.html')

def temperatureView(request):
		temperature = random.randint(-20,120)
		settings = json.load(open('settings.txt'))
		return render(request,'temperature.html',{'Temperature':temperature,'SystemConfiguration':settings})

def humidityView(request):
		humidity = random.randint(1,100)
		return render(request,'humidity.html',{'Humidity':humidity})
