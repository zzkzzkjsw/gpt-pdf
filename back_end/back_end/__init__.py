from flask import Flask
from flask_cors import CORS
from .views.chat_views import chat_views
from .views.login_views import login_views
from back_end.extensions import set_extensions
from .config import config

def create_app(config_name):

    app = Flask(__name__)

    # load config
    app.config.from_object(config.get(config_name))
    app.secret_key = b'12313123131241414141241fsfgsfsdfsfs'

    # load extensions
    set_extensions(app)

    # CORS(app,supports_credentials=True)

    @app.route("/index")
    def index():
        return "首页"
    
    app.register_blueprint(chat_views)
    app.register_blueprint(login_views)

    return app

    


