from flask import Blueprint, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from Forms_model import ProductForm

from extensions import db
from Models import Product

store = Blueprint("store", __name__)


@store.route('/product_register', methods=['GET', 'POST'])
def product_register():

    form = ProductForm()

    if form.validate_on_submit():
        admin_password = form.admin_password.data

        if admin_password == "0537":
            name = form.name.data
            description = form.description.data
            price = form.price.data
            stock = form.stock.data

            image = secure_filename(name + "_" + form.image.data.filename)
            form.image.data.save("static/products_image/" + image)

            new_product = Product(name, description, price, stock, image)
            db.session.add(new_product)
            db.session.commit()

            return render_template("product_register.html", form=form, errors=form.errors, message="Produto %s cadastrado com sucesso" % name)
        else:
            return render_template("product_register.html", form=form, errors=form.errors, error="Senha de adimistrador errada")

    return render_template("product_register.html", form=form, errors=form.errors)
