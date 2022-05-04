from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)


    def __init__(self, email, password, is_active):
        self.email = email
        self.password = password
        self.is_active = is_active

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


#characters
class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(250),nullable=False)
    gender = db.Column(db.String(10),nullable=True)
    eye_color = db.Column(db.String(10), nullable=True)
    hair_color = db.Column(db.String(10), nullable=True)
    skin_color = db.Column(db.String(10), nullable=True)
    birth_year = db.Column(db.String(20), nullable=True)
    height = db.Column(db.Integer, nullable=True)
    mass = db.Column(db.Integer, nullable=True)

    def __init__(self, id, name, url, gender=None,
        eye_color=None, hair_color=None,skin_color=None, birth_year=None,
        height=None, mass=None):
        self.id = id
        self.name = name
        self.url = url
        self.gender = gender
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.birth_year = birth_year
        self.height = height
        self.mass = mass

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "gender": self.gender,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "birth_year": self.birth_year,
            "height": self.height,
            "mass": self.mass
        }


#Planets
class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer, nullable=True)
    orbital_period = db.Column(db.Integer, nullable=True)
    rotation_period = db.Column(db.Integer, nullable=True)
    climate = db.Column(db.String(20),nullable=True)
    terrain = db.Column(db.String(20),nullable=True)
    population = db.Column(db.Integer, nullable=True)
    surface_water = db.Column(db.Integer, nullable=True)
    gravity = db.Column(db.Integer, nullable=True)

    def __init__(self, id, name, url, diameter=None,
        orbital_period=None, rotation_period=None,climate=None, terrain=None,
        population=None, surface_water=None, gravity=None):
        self.id = id
        self.name = name
        self.url = url
        self.diameter = diameter
        self.orbital_period = orbital_period
        self.rotation_period = rotation_period
        self.climate = climate
        self.terrain = terrain
        self.population = population
        self.surface_water = surface_water
        self.gravity = gravity

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "diameter": self.diameter,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population,
            "surface_water": self.surface_water,
            "gravity": self.gravity
        }


#Personaje favorito
class FavoritesCharacters(db.Model):
    __tablename__ = 'favorites_characters'
    id_user = db.Column(db.Integer,db.ForeignKey('user.id'), primary_key = True)
    id_character = db.Column(db.Integer, nullable=False)

    def __init__(self, id_user, id_character):
        self.id_user = id_user
        self.id_character = id_character

    def __repr__(self):
        return '<FavoritesCharacter %r>' % self.id_character

    def serialize(self):
        return {
            "id_character": self.id_character,
        }


#Planeta favorito
class FavoritesPlanets(db.Model):
    __tablename__ = 'favorites_planet'
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    id_planet = db.Column(db.Integer, nullable=False)

    def __init__(self, id_user, id_planet):
        self.id_user = id_user
        self.id_planet = id_planet

    def __repr__(self):
        return '<FavoritesPlanet %r>' % self.id_planet

    def serialize(self):
        return {
            "id_planet": self.id_planet,
        }
