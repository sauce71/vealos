import os

from flask import Flask

from flask_login import LoginManager
login_manager = LoginManager()

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "vealos.db"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # register the database commands
    from . import db
    db.init_app(app)

    
    login_manager.init_app(app) # app is a Flask object


    # apply the blueprints to the app
    from application import auth, user, top, page, index


    app.register_blueprint(auth.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(top.bp)
    app.register_blueprint(page.bp)
    app.register_blueprint(index.bp)
  

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    #app.add_url_rule("/", endpoint="index")

    return app

app = create_app()