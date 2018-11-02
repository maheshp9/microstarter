# services/apiservice/core/__init__.py

import os

from flask import Flask
from flask_cors import CORS

def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
   
    # register blueprints
    from core.api.entity import entity_blueprint
    app.register_blueprint(entity_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app}

    return app
