from server.services import vendor_service


def post_vendor(body):
    return vendor_service.create_vendor(body)

def get_vendor(id):
    return vendor_service.get_vendor(id)

def put_vendor(id, body):
    return vendor_service.update_vendor(id, body)

def delete_vendor(id):
    return vendor_service.delete_vendor(id)