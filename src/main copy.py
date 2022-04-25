"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from models import Character, Planet, FavoritesCharacters, FavoritesPlanets 

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


#Aquí comienzan los endpoints de la tarea

#get people (LISTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO)
@app.route('/people', methods=['GET'])
def people():

    try:
        characters = Character.query.all()
        characters = list(map(lambda x: x.serialize(), characters))
        return jsonify(characters), 200

    except:
        response_body = {
            "msg": "Hubo un error en traer los personajes"
        }
        return jsonify(response_body), 500


#get people específica (LISTOOOOOOOOOOOOOOOOOOOOOOOO)
@app.route('/character/<int:character_id>', methods=['GET'])
def single_character():

    try:
        id_character = int(request.args.get('id_character'))
        one_character = Character.query.filter_by(id=id_character)
        one_character = list(map(lambda x: x.serialize(), one_character))
        return jsonify(one_character), 200

    except:
        response_body = {
            "msg": "Hubo un error en traer un personaje en específico"
        }
        return jsonify(response_body), 500


#get planets (LISTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO)
@app.route('/planets', methods=['GET'])
def planets():

    try:
        planetas = Planet.query.all()
        planets = list(map(lambda x: x.serialize(), planets))
        return jsonify(planets), 200

    except:
        response_body = {
            "msg": "Hubo un error en traer los planetas"
        }
        return jsonify(response_body), 500


#get planets específico (LISTOOOOOOOOOOOOOOOOOOOO)
@app.route('/planets/<int:planet_id>', methods=['GET'])
def single_planet():

    try:
        id_planet = int(request.args.get('id_planet'))
        one_planet = Planet.query.filter_by(id=id_planet)
        one_planet = list(map(lambda x: x.serialize(), one_planet))
        return jsonify(one_planet), 200

    except:
        response_body = {
            "msg": "Hubo un error trayendo un planeta en específico"
        }
        return jsonify(response_body), 500


#endpoints adicionales

#obtener usuarios (LISTOOOOOOOOOOOOOOOOOOOOOOO)
@app.route('/users', methods=['GET'])
def getusers():

    try:
        usuarios = User.query.all()
        usuarios = list(map(lambda x: x.serialize(), usuarios))
        return jsonify(usuarios), 200

    except:
        response_body = {
            "msg": "Hubo un error"
        }
        return jsonify(response_body), 500


#user favorites (LISTOOOOOOOOOOOOOOOOOOOOOOOO)
@app.route('/users/favorites', methods =['GET'])
def user_favs():

    try:
        id_user = int(request.args.get('id_user'))
        fav_character = FavoritesCharacters.query.filter_by(id_user=id_user)
        fav_character = list(map(lambda x: x.serialize(), fav_character))
        
        fav_planet = FavoritesPlanets.query.filter_by(id_user=id_user)
        fav_planet = list(map(lambda x: x.serialize(), fav_planet))

        favs = {
            'character': fav_character,
            'planets': fav_planet,
        }
        return jsonify(favs), 200

    except:
        response_body = {
            "msg": "Hubo un error en recuperar los favoritos"
        }
        return jsonify(response_body), 500


#agrega un personaje favorito
@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_people_fav():

    response_body = {
        "msg":"Hello, this is your POST /addpeoplefav response"
    }

    return jsonify(response_body), 200


#agrega un planeta favorito
@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_planet_fav():

    response_body = {
        "msg":"Hello, this is your POST /addplanetfav response"
    }

    return jsonify(response_body), 200


#borrar personaje favorito
@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_fav_people():

    response_body = {
        "msg": "Hello, this is your DELETE /deletefavpeople response"
    }

    return jsonify(response_body), 200


#borrar planeta favorito
@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_fav_planet():

    response_body = {
        "msg": "Hello, this is your DELETE /deletefavplanet response"
    }

    return jsonify(response_body), 200


#Aquí terminan los endpoints de la tarea


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
