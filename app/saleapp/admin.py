from flask_admin import Admin, expose, BaseView
from flask_admin.contrib.sqla import ModelView
from werkzeug.utils import redirect

from app.saleapp import app, db
from models import Product, Category, UserRole
from flask_login import current_user, logout_user

admin = Admin(app=app)

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class ProductView(AdminView):
    column_list = ['id', 'name', 'price', 'active', 'category_id']
    column_searchable_list = ['name']
    column_filters = ['name', 'price', 'id']
    can_export = True
    edit_modal = True
    column_editable_list = ['name', 'price']
    page_size = 3

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect("/admin")

    def is_accessible(self):
        return current_user.is_authenticated

admin.add_view(ProductView(Product, db.session))
admin.add_view(AdminView(Category, db.session))
admin.add_view(LogoutView(name='Logout'))