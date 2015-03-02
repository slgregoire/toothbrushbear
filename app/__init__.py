#defines a function that creates an application instance

from flask import Flask
from app.views.index import index_bp

def create_app():
	app = Flask(__name__)
	app.register_blueprint(index_bp)

	return app 