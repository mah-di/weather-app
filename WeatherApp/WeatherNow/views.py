from django.shortcuts import redirect, render
import requests
from .forms import CityForm
from .models import City

# Create your views here.





def index(req):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=567c16e0cb01072346b5398d6556483e&units=metric'
    message = ''
    message_alert = 'is-danger'

    if req.method == 'POST':
        form = CityForm(req.POST)

        if form.is_valid():
            city_name = form.cleaned_data.get('name').capitalize()

            if City.objects.filter(name=city_name).count() == 0:
                r = requests.get(url.format(city_name)).json()

                if r['cod'] == 200:
                    City.objects.create(name=city_name)
                    message = 'City Added To Dashboard!'
                    message_alert = 'is-success'

                else:
                    message = 'City Not Found!'

            else:
                message = 'City Already Added To Dashboard!'
    
    form = CityForm()

    cities = City.objects.all()
    weather_data = []

    for city in cities:
        response = requests.get(url.format(city.name)).json()
        city_weather = {
            'city' : city.name,
            'temp' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon']
        }
        weather_data.append(city_weather)

    return render(req, 'WeatherNow/weather.html', context={'weather_data': weather_data, 'form': form, 'message': message, 'message_alert': message_alert})





def city_details(req, city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=567c16e0cb01072346b5398d6556483e&units=metric'

    response = requests.get(url).json()
    print('url: ', url)
    print('city: ', city_name)
    print(response)
    city_weather = {
        'city' : city_name,
        'temp' : response['main']['temp'],
        'temp_feel' : response['main']['feels_like'],
        'min_temp': response['main']['temp_min'],
        'max_temp': response['main']['temp_max'],
        'humidity' : response['main']['humidity'],
        'pressure' : response['main']['pressure'],
        'weather' : response['weather'][0]['main'],
        'weather_description' : response['weather'][0]['description'],
        'wind' : {
            'speed' : response['wind']['speed'],
            'direction' : response['wind']['deg'],
            'gust' : response['wind']['gust'] if 'gust' in response['wind'] else 'N/A',
        },
        'visibility' : response['visibility'],
        'country' : response['sys']['country'],
        'icon' : response['weather'][0]['icon']
    }
    
    return render(req, 'WeatherNow/detail_weather.html', context={'city_weather': city_weather})





def delete_city(req, city):
    City.objects.get(name=city).delete()

    return redirect('home')