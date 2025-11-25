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
        },
        {
            'id': 'afrique-colonisation',
            'titre': "L'Europe, la Méditerranée et l'Afrique au XXe siècle",
            'description': 'Colonisation, décolonisation et héritages post-coloniaux',
            'url': '/cours/afrique-colonisation'
        },
        {
            'id': 'onu-integration',
            'titre': "L'ONU pendant la Guerre Froide et l'intégration régionale",
            'description': 'Organisations internationales, régionalisme et accords commerciaux',
            'url': '/cours/onu-integration'
        },
        {
            'id': 'organisations-internationales',
            'titre': "Histoire des organisations internationales",
            'description': 'De la SDN à l\'ONU : institutionnalisation des relations internationales',
            'url': '/cours/organisations-internationales'
        },
        {
            'id': 'quest-ce-que-europe',
            'titre': "Qu'est-ce que l'Europe ?",
            'description': 'Définitions, mythes et représentations de l\'idée européenne',
            'url': '/cours/quest-ce-que-europe'
        },
        {
            'id': 'definitions-ri',
            'titre': "Les relations internationales - Définitions",
            'description': 'Introduction historiographique et acteurs des relations internationales',
            'url': '/cours/definitions-ri'
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

@app.route('/cours/afrique-colonisation')
def cours_afrique_colonisation():
    return render_template('cours_afrique.html')

@app.route('/cours/onu-integration')
def cours_onu_integration():
    return render_template('cours_onu.html')

@app.route('/cours/organisations-internationales')
def cours_organisations_internationales():
    return render_template('cours_organisations.html')

@app.route('/cours/quest-ce-que-europe')
def cours_europe():
    return render_template('cours_europe.html')

@app.route('/cours/definitions-ri')
def cours_definitions_ri():
    return render_template('cours_definitions_ri.html')

if __name__ == '__main__':
    app.run(debug=True)