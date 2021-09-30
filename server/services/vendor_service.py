from server.models.vendor import Vendor, VendorSchema
from server import db

def create_vendor(body):
    vendor = Vendor()
    vendor.Name = body.get("Name")
    vendor.City = body.get('City')
    vendor.CNPJ = body.get('CNPJ')

    try:
        db.session.add(vendor)
        db.session.commit()
    except:
        db.session.rollback()
    rett = VendorSchema(many=False).jsonify(vendor)

    return rett


def get_vendor(id):
    vendor = Vendor()
    vendor = vendor.query.get(id)
    rett = VendorSchema(many=False).jsonify(vendor)
    return rett

def update_vendor(id, body):
    vendor = Vendor()
    vendor = vendor.query.get(id)

    vendor.Name = body.get('Name')
    vendor.City = body.get('City')
    vendor.CNPJ = body.get('CNPJ')

    try:
        db.session.add(vendor)
        db.session.commit()
    except:
        db.session.rollback()

    rett = VendorSchema(many=False).jsonify(vendor)
    return rett


def delete_vendor(id):
    vendor = Vendor()
    vendor = vendor.query.get(id)
    db.session.delete(vendor)
    db.session.commit()
    return ""


def get_vendors():
    vendor = Vendor()
    vendor = vendor.query.all()
    rett = VendorSchema(many=True).jsonify(vendor)
    return rett