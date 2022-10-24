from datetime import date
from flask_login import UserMixin
from flask_migrate import Migrate
from flask_security import RoleMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from MediKit import app

db = SQLAlchemy(app)

# here migration is used to alter the database columns
migrate = Migrate(app, db, render_as_batch=True)


# category table consist of data about the categories only

class CategoryTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(250), unique=True)
    product = relationship("Products", backref='category_table', lazy=True)


# this table consist the data and login credentials of the vendor
class Vendor(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Integer, unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    vendor_id = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    products = relationship("Products", backref='vendor', lazy="select")


# user table consist of user credentials
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    super_user = db.Column(db.Boolean(), default=False)

    address = relationship('AddressTable', backref='users', lazy=True)
    # complaints table
    comp = relationship('Complaints', backref='users', lazy=True)
    cart = relationship('Cart', backref='users', lazy=True)
    order_tab = relationship('Order', backref='users', lazy=True)


# this table consist the product information
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(250), nullable=False, unique=True)
    image = db.Column(db.String(2500), nullable=True)
    price = db.Column(db.Float(2), nullable=False)
    Discount = db.Column(db.Float(2), nullable=False)
    no_of_pieces = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(1000), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey("category_table.id"))
    vendor_id = db.Column(db.Integer, db.ForeignKey("vendor.id"))
    #
    categoryID = relationship("CategoryTable",
                              primaryjoin="and_(CategoryTable.id==Products.category_id)",
                              backref="products",
                              viewonly=True)
    vendorID = relationship("Vendor",
                            primaryjoin="and_(Vendor.id==Products.vendor_id)",
                            overlaps='vendor,products')

    def __repr__(self):
        return f'Product : {self.product_name}'


# this table consists of address details of the user
class AddressTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250))
    email = db.Column(db.String(250), nullable=False)
    ph_no = db.Column(db.String(10), nullable=False)
    house_no = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(250), nullable=False)
    city = db.Column(db.String(250), nullable=False)
    town = db.Column(db.String(250), nullable=False)
    sub_district = db.Column(db.String(250), nullable=False)
    district = db.Column(db.String(250), nullable=False)
    pincode = db.Column(db.String(10), nullable=False)
    state = db.Column(db.String(100), nullable=False)

    user_tab = relationship("Users", primaryjoin="and_(Users.id==AddressTable.user_id)", overlaps="address,users")


# cart page show the list of products in the cart
class Cart(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    quantity = db.Column(db.Integer, default=1)
    # order = relationship("Orders", backref='cart', lazy=True)

    productID = relationship("Products",
                             primaryjoin="and_(Products.id==Cart.product_id)",
                             backref="Products",
                             overlaps="products,cart")
    UID = relationship("Users",
                       primaryjoin="and_(Users.id==Cart.user_id)",
                       backref="users",
                       viewonly=True)


# it will show the order details of the user
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pro_id = db.Column(db.Integer)
    qty = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey("cart.order_id"))
    total_amt = db.Column(db.Float)
    discount = db.Column(db.Float)
    orderd_on = db.Column(db.DateTime())
    pay_mode = db.Column(db.String(100))
    orderID = relationship("Cart",
                           primaryjoin="and_(Cart.order_id==Order.order_id)",
                           backref="cart",
                           overlaps="Cart,Order")

    userID = relationship("Users",
                          primaryjoin="and_(Users.id==Order.user_id)",
                          backref="Users",
                          viewonly=True)


class Complaints(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    email = db.Column(db.String(250))
    rating = db.Column(db.Integer)
    response = db.Column(db.String(5000))
    posted_on = db.Column(db.DateTime(), nullable=False)
    is_resolved = db.Column(db.Boolean, default=False)
