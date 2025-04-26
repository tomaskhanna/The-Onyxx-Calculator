from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('mobcalc.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operator = request.form['operator']

    try:
        num1 = float(num1)
        num2 = float(num2)

        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtract':
            result = num1 - num2
        elif operator == 'multiply':
            result = num1 * num2
        elif operator == 'divide':
            result = num1 / num2
        elif operator == 'sin':
            result = math.sin(math.radians(num1))
        elif operator == 'cos':
            result = math.cos(math.radians(num1))
        elif operator == 'tan':
            result = math.tan(math.radians(num1))
        elif operator == 'power':
            result = math.pow(num1, num2)
        elif operator == 'sqrt':
            result = math.sqrt(num1)

        else:
            result = "Invalid operation"
    except Exception as e:
        result = f"Error: {e}"

    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)