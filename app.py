from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/pokemon', methods=['GET','POST'])
def pokemon():
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon').lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            if not data:
                error_string = f'There is no pokemon named {pokemon_name}'
                return render_template("pokemon.html.j2", error = error_string)
            else:
                pokemon_dict = {
                    'pokemon_name': data['name'],
                    'ability_name': data['abilities'][0]['ability']['name'],
                    'base_experience': data['base_experience'],
                    'sprite_ULR': data['sprites']['front_shiny']
                }
                return render_template('pokemon.html.j2',pokemon=pokemon_dict)
        else:
            error_string = "Something went wrong"
            render_template("pokemon.html.j2", error=error_string)
    return render_template('pokemon.html.j2')