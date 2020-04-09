from darksky.api import DarkSky
from darksky.types import languages, units, weather


API_KEY = 'e2fea81b36c2588f1315c4ad2b721989'
darksky = DarkSky(API_KEY)

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode("Qutub Minar")


latitude = location.latitude
longitude = location.longitude

forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    values_units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
)

temp = forecast.currently.temperature
summ = forecast.currently.summary

import requests, json
response = requests.get("https://api.nasa.gov/planetary/apod?api_key=YV5qKOZHskncZ7HiZgw90jdXODbXijaXkdvLHol7")
url = response.json()['url']
head = response.json()['title']
exp = response.json()['explanation']

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    title="Home"
    return render_template("index.html",title=title)

@app.route("/about")
def about():
    title = "About"
    return render_template("about.html",title=title)

@app.route("/contact")
def contact():
    title = "Contact"
    return render_template("contact.html",title=title)

@app.route("/weather")
def weather():
    title = "Weather"
    return render_template("weather.html",title=title,temp=temp,summ=summ)

@app.route("/pod")
def pod():
    title = "Picture of the Day"
    return render_template("pod.html",title=title,url=url,head=head,exp=exp)


if __name__ == '__main__':
    app.run()