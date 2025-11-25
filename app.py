from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cours_list = [
        {
            'id': 'economie-20e',
            'titre': 'Relations économiques internationales au XXe siècle',
            'description': 'Mondialisation, crises et question environnementale',
            'url': '/cours/economie-20e'
        }
    ]
    return render_template('index.html', cours=cours_list)

@app.route('/cours/economie-20e')
def cours_economie():
    return render_template('cours_economie.html')

if __name__ == '__main__':
    app.run(debug=True)