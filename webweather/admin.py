from django.contrib import admin
from .models import datas

admin.site.register(datas)

HumidityHumiditydat=data(city='Pune',weather='test',tempreture='11.2',Humidity=22.0)
		dat.save()
		return render(request,'home.html',contex)