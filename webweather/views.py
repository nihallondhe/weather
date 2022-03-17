from django.shortcuts import render
import requests
from .models import datas

def home(request):
	try:
		
	
			if request.method == 'POST':
					searchWord = request.POST.get('search','')
					city=searchWord
					url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=fdndfjnldf232323BALDLSDNLA
					data = requests.get(url).json()
					hum ={'city' : data['name'],'weather':data['weather'][0]['icon'],'temp':data['main']['temp'],'Humidity':data['main']['humidity']}
					lat = data['coord']['lat']
					lon=data['coord']['lon']
					#print(request.data)
					print(request.GET)
					lon=data['coord']['lon']
					weather=data['weather'][0]['icon']
					lat=data['coord']['lat']
					Humidity=data['main']['humidity']
					temp=data['main']['temp']
					Humidity=data['main']['humidity']
					dat=datas(city=city,weather=weather,tempreture=temp,Humidity=lon,lon=lon,lat=lat)
					dat.save()
					raw=datas.objects.all()
					#( searchWord)
					return render(request,'home.html',{'lon':lon,'lat':lat})
			else:
				city='Delhi'
				url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=946758bb24b6ec04e31730074bb296d0'
				data = requests.get(url).json()
				hum ={'city' : data['name'],'weather':data['weather'][0]['icon'],'temp':data['main']['temp'],'Humidity':data['main']['humidity']}
				lat = data['coord']['lat']
					#hums=list[hum]
				lon=data['coord']['lon']
				#print(request.data)
				print(request.GET)
				contex = {'lon':data['coord']['lon'],
				'lat':data['coord']['lat'],
				'hum':{'city' : data['name'],'weather':data['weather'][0]['icon'],'temp':data['main']['temp'],'Humidity':data['main']['humidity']}


				}
				Humidity=data['main']['humidity']
				temp=data['main']['temp']
				Humidity=data['main']['humidity']
				dat=datas(city='Pune',weather='test',tempreture='11.2',Humidity=22.0)
				dat.save()
				raw=datas.objects.all()
				return render(request,'home.html',raw)
	except:
		raw=datas.objects.all()
		print(raw)
		return render(request,'home.html')
