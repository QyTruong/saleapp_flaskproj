from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.saleapp import app, db
from models import Product, Category


admin = Admin(app=app)
admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(Category, db.session))