'''Your app.py is responsible for:
Creating a Flask application
Configuring CORS (Cross-Origin Resource Sharing)
Setting up the database (SQLAlchemy)
Registering Blueprints (routes)
Creating tables in the database
Running the app when executed directly'''

'''Flask: The core framework for creating a web server.
CORS: This allows your API to be accessed from different domains (important for frontend-backend communication).
db: This imports the SQLAlchemy database instance from extension.py (which contains db = SQLAlchemy()).

Why Use extension.py? If you define db inside app.py, you will run into circular imports. Moving db to extension.py avoids this problem.'''
from flask import Flask
from flask_cors import CORS
from extension import db 

def create_app():
    app = Flask(__name__)
    CORS(app)
    '''Flask(__name__): Creates an instance of the Flask app.
     CORS(app): Allows the frontend (e.g., React, Vue, or Angular) to communicate with this backend
     Why Use CORS? Without CORS, browsers may block API requests if the frontend is running on a different port (e.g., frontend on http://localhost:3000, backend on http://127.0.0.1:5000).'''

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///friends.db"
     
    '''SQLALCHEMY_DATABASE_URI: This tells SQLAlchemy where to store the database.
"    sqlite:///friends.db" → Uses SQLite and stores the database in a file named friends.db.'''

     
    db.init_app(app)
    '''his binds the database (db) to the Flask app.
    Without this, the database won’t work with Flask.
     Why Call db.init_app(app) Here?

    This ensures db is connected before creating tables or registering routes.'''

    
    from routes import bp
    app.register_blueprint(bp)
    '''from routes import bp → Imports the bp Blueprint from routes.py.
app.register_blueprint(bp) → Registers the Blueprint, making the routes accessible.
✅ Why Use Blueprints?

Helps organize routes instead of keeping everything in app.py.
Avoids circular imports (since routes are loaded after initializing db).
'''

    with app.app_context():
        db.create_all()
        '''app.app_context() → Creates a temporary application context.
db.create_all() → Creates all tables defined in models.py.
✅ Why Use app.app_context()?

Flask requires an "application context" to interact with the database.
Without it, db.create_all() would fail with an error like'''

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    '''if __name__ == '__main__': → Ensures the script runs only if executed directly.
app = create_app() → Calls the create_app() function to initialize everything.
app.run(debug=True) → Starts the Flask development server with debugging enabled.
✅ Why Use debug=True?

Enables auto-reload (restarts the server when you change code).
Provides detailed error messages when something breaks.
'''
