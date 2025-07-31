from django.shortcuts import render
from django.views import View
import requests
from .models import Weather

# Create your views here.

class WeatherView(View):
    template_name = 'weatherapp/weather.html'

    def get(self, request):
        api_key = '19ac529bcbf8f18138a0db580024b20b'
        city = request.GET.get('city')
        weather_record = None

        if city:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                icon = data['weather'][0]['icon']

                weather_record = Weather(city=city, temperature=temperature, humidity=humidity, icon=icon)
                weather_record.save()

        previous_records = Weather.objects.all().order_by('-created_at')
        context = {
            'weather': weather_record,
            'previous_records': previous_records
        }
        return render(request, self.template_name, context)