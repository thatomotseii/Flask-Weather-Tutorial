from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

# Defining routes for application
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/weather', methods=['GET'])
def get_weather():
    # Get Form Data with the request.args.get(name of form input)
    city = request.args.get('city')
    if not city or not bool(city.strip()):
        city = "Bloemfontein"
    
    # Call the method to get weather with the city inserted in the form
    weather_data = get_current_weather(city)
    
    if weather_data.get('cod') != 200:
        return render_template("not-found.html")
    
    # Returning Data from JSON File to our weather.html Template
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f'{weather_data["main"]["temp"]:.1f}',
        feels_like=f'{weather_data["main"]["feels_like"]:.1f}'
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
