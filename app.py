import os
from flask import Flask
from models import setup_db
from flask_cors import CORS
from models import db, Person
import sys

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        if excited == 'true': greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return jsonify({ 'greeting': "Be cool, man, be coooool! You're almost a FSND grad!"})

    @app.route('/hello')
    def say_hello():
        danny = Person(name='Danny', catchphrase='Howdy')
        try:
            db.session.add(danny)
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info())
        finally:
            db.session.close()

        dannyGet = Person.query.first()


        return dannyGet.catchphrase + '!' + ' ' + dannyGet.name 

    return app

app = create_app()

if __name__ == '__main__':
    app.run()