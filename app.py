from flask import Flask, render_template 
import requests 
from dotenv import load_dotenv, dotenv_values

config = dotenv_values ('.env')
load_dotenv('.env')

app = Flask (__name__)

def get_weather_data(city):
    API_KEY = config['API_KEY']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=es&appid={API_KEY}'

    r = requests.get(url).json()
    print (r)
    return r
    
@app.route('/prueba')
def prueba():
    clima=get_weather_data('London')
    temperatura=str(clima['main']['temp'])
    descripcion= str(clima['weather'][0]['description'])
    icono=str(clima['weather'][0]['icon'])
    r_json={
        'ciudad': 'London',
        'temperatura':temperatura,
        'descripcion': descripcion,
        'icono': icono
        }
    return render_template('weather.html', clima = r_json)
 
@app.route('/clima')
def clima():
    return'Clima'

if __name__ == '__main__':
    app.run(debug = True)

