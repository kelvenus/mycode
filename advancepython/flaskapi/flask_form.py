from flask import Flask, redirect, url_for, render_template
import requests
app = Flask(__name__)  

@app.route('/planets')
def planets():
    data = []
    for i in range(1, 11):
        planetapi = requests.get(f'https://swapi.co/api/planets/{i}/?format=json')
        getplanet = planetapi.json()
        data.append({'name': getplanet['name'], 'climate': getplanet['climate'], 'gravity': getplanet['gravity']})

    #print(data[f'name': 'climate'])
    print(data) 
    return render_template('planets.html', planetname = data)
	
if __name__ == '__main__':
   #app.run(port=5006, host='0.0.0.0') add host ip to allow a particular host
   app.run(port=5006)
