from flask import render_template, request
from werkzeug.utils import redirect

from app import app, login
from flask_login import login_user
import dao


@app.route('/')
def index():
    categories = dao.load_categories()
    products = dao.load_products(cate_id=request.args.get('category_id'), kw=request.args.get('keyword'))

    return render_template('index.html', categories=categories, products=products)

@login.user_loader
def load_user(user_id):
    return dao.load_user_by_id(user_id)

@app.route("/login")
def login_view():
    return render_template('login.html')

@app.route("/register")
def register_view():
    return render_template('register.html')

@app.route("/login", methods=['POST'])
def login_process():
    username = request.form.get("username")
    password = request.form.get("password")

    user = dao.auth_user(username, password)

    if user:
        login_user(user=user)

    return redirect('/admin')


if __name__ == '__main__':
    from admin import admin

    app.run(debug=True)
