# Robin og Emil
from datetime import date
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from flask import current_app

bp = Blueprint("top", __name__)

@bp.route("/top/")
#@bp.route("/user/<int:user_id>")
def index():  
    return render_template("top.html", **locals())