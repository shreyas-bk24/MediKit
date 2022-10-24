from flask import render_template

from MediKit import app
from MediKit.models import Products, CategoryTable

@app.route('/baby_care')
def baby_care():
    baby = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                          Products.image).filter_by(category="Baby Care").all()
    count = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                           Products.image).filter_by(category="Baby Care").count()
    return render_template('category.html',products=baby,res="Baby Care",count=count)


@app.route('/personal_care')
def personal_care():
    personal_pros = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                                   Products.image).filter_by(category="Personal care").all()
    count = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                           Products.image).filter_by(category="Personal care").count()

    return render_template('category.html',products=personal_pros,res="Personal care",count=count)


@app.route('/BP')
def BP():
    BP = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                        Products.image).filter_by(category="BP").all()
    count = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                           Products.image).filter_by(category="BP").count()

    return render_template('category.html', products=BP, res="BP", count=count)


@app.route('/cold_and_cough')
def cold_and_cough():
    cold = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                          Products.image).filter_by(category="Cold and cough").all()
    count = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                           Products.image).filter_by(category="Cold and cough").count()

    return render_template('category.html', products=cold, res="Cold and Cough", count=count)


@app.route('/ayurvedic')
def ayurvedic():
    ayurvedic = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                               Products.image).filter_by(category="Ayurvedic").all()
    count = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                           Products.image).filter_by(category="Ayurvedic").count()

    return render_template('category.html', products=ayurvedic, res="Ayurvedic", count=count)


@app.route('/first_aid')
def first_aid():
    FA = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                        Products.image).filter_by(category="First aid").all()
    count = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                           Products.image).filter_by(category="First aid").count()

    return render_template('category.html', products=FA, res="First Aid", count=count)


@app.route('/diabetic_needs')
def diabetic_needs():
    diabetic = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                              Products.image).filter_by(category="Diabitic needs").all()
    count = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                           Products.image).filter_by(category="Diabitic needs").count()

    return render_template('category.html', products=diabetic, res="Diabetic needs", count=count)


@app.route('/house_hold')
def house_hold():
    House = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                           Products.image).filter_by(category="Household").all()
    count = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                           Products.image).filter_by(category="Household").count()

    return render_template('categoty.html', products=House, res="House Hold", count=count)


@app.route('/others')
def others():
    oth = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                         Products.image).filter_by(category="Others").all()
    count = Products.query.join(CategoryTable).add_columns(CategoryTable.category, Products.product_name, Products.id,
                                                           Products.image).filter_by(category="Others").count()

    return render_template('category.html', products=oth, res="BP", count=count)

