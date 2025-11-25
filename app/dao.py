import hashlib

from models import Category, Product, User

def load_categories():
    return Category.query.all()

def load_products(cate_id=None, kw=None, page=1):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))
    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))

    return query.all()

def load_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

        return User.query.filter(User.username.__eq__(username),
                                 User.password.__eq__(password)).first()
    return None
