import requests
from flask import Flask, render_template, request
import urllib

app = Flask(__name__)

# Defined these variables outside of the home function so I can use them globally within the function
name = ''
description = ''
temp = ''
wind = '' 
icon = ''

# Routes for web pages
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        global name
        global description
        global temp
        global wind
        global icon

        city = request.form.get('city')
        
        try:
            #API call below, then formatting the response into json
            weather_key = '7113e7c022e4e898beaddbba87f4b835'
            url = 'https://api.openweathermap.org/data/2.5/weather'
            params = {'APPID': weather_key, 'q': city,'icon': icon, 'units': 'imperial'}
            response = requests.get(url, params=params)
            weather = response.json()

            # Weather information stored into variables and formatted into a string
            name = weather['name']
            description = weather['weather'][0]['description']
            temp = weather['main']['temp']
            wind = weather['wind']['speed']
            icon = weather['weather'][0]['icon']
        except:
            return 'ERROR, SOMETHING WENT WRONG, PLEASE ENTER A VALID CITY?'
        
    return render_template('layout.html', name=name, description=description, temp=temp, wind=wind, icon=icon)



if __name__ == '__main__':
    app.run(debug=True)