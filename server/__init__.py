from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import connexion
from flask_cors import CORS
from server.config import HOST, PORT, DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

postgre_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

db = SQLAlchemy()
ma = Marshmallow()


def init_api():
    app = connexion.App(__name__, specification_dir="./swagger/")
    CORS(app.app)
    app.add_api("swagger.yaml", arguments={f"host_with_port": f"{HOST}:{PORT}"})
    app.app.config['SQLALCHEMY_DATABASE_URI'] = postgre_url
    db.init_app(app.app)
    ma.init_app(app.app)
    return app