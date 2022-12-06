from flask import Blueprint





LoginUser = Blueprint("login", __name__)

@LoginUser.route("/login", methods=['GET','POST'])
def login():
    return "teste"


@LoginUser.route("/logout", methods=['GET','POST'])
def login_off():
    return "teste"

