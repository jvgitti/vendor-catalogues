from server.models.product import Product, ProductSchema
from server import db

def create_product(body, schema=True):
    product = Product()
    product.Name = body.get('Name')
    product.Code = body.get('Code')
    product.Price = body.get('Price')
    product.Vendor_Id = body.get('Vendor_Id')

    try:
        db.session.add(product)
        db.session.commit()
    except:
        db.session.rollback()

    if schema:
        rett = ProductSchema(many=False).jsonify(product)
    else:
        rett = product
    return rett


def get_product(id):
    product = Product()
    product = product.query.get(id)
    rett = ProductSchema(many=False).jsonify(product)
    return rett

def update_product(id, body):
    product = Product()
    vendor = product.query.get(id)

    product.Name = body.get('Name')
    product.Code = body.get('Code')
    product.Price = body.get('Price')
    product.VendorId = body.get('VendorId')

    try:
        db.session.add(vendor)
        db.session.commit()
    except:
        db.session.rollback()

    rett = ProductSchema(many=False).jsonify(vendor)
    return rett


def delete_product(id):
    product = Product()
    vendor = product.query.get(id)
    db.session.delete(vendor)
    db.session.commit()
    return ""


def get_products():
    product = Product()
    product = product.query.all()
    rett = ProductSchema(many=True).jsonify(product)
    return rett