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
        },
        {
            'id': 'diplomatie-culturelle',
            'titre': 'Relations internationales et diplomatie culturelle',
            'description': 'Échanges culturels, soft power et hégémonies culturelles au XXe siècle',
            'url': '/cours/diplomatie-culturelle'
        },
        {
            'id': 'migrations',
            'titre': 'Histoire des migrations internationales contemporaines',
            'description': 'Phénomènes migratoires, causes et évolutions du XIXe au XXIe siècle',
            'url': '/cours/migrations'
        }
    ]
    return render_template('index.html', cours=cours_list)

@app.route('/cours/economie-20e')
def cours_economie():
    return render_template('cours_economie.html')

@app.route('/cours/diplomatie-culturelle')
def cours_diplomatie_culturelle():
    return render_template('cours_diplomatie_culturelle.html')

@app.route('/cours/migrations')
def cours_migrations():
    return render_template('cours_migrations.html')

if __name__ == '__main__':
    app.run(debug=True)