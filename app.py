from flask import Flask, request, render_template
from animal_script.main import AnimalScript

app = Flask(__name__)
animal_script = AnimalScript()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    code = request.form['code']
    output = animal_script.evaluate_multiline(code)
    return output

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False, host='0.0.0.0')
