from flask import Flask, render_template, request
from temp import temp
from calorie import Calorie

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('calories_form.html')

@app.route('/calculate_calories', methods=['POST'])
def calculate_calories():
    weight = int(request.form['weight'])
    height = float(request.form['height'])
    age = int(request.form['age'])
    country = request.form['country'].lower()
    city = request.form['city'].lower()

    temperature = temp(country, city).get()
    calorie = Calorie(weight, height, age, temp=temperature)
    calculated_calories = calorie.calculate()

    return render_template('calories_result.html', calories=calculated_calories, temperature=temperature)

if __name__ == "__main__":
    app.run(debug=True)
