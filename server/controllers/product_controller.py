from server.services import product_service


def post_product(body):
    return product_service.create_product(body)


def get_product(id):
    return product_service.get_product(id)


def get_products():
    return product_service.get_products()


def put_product(id, body):
    return product_service.update_product(id, body)


def delete_product(id):
    return product_service.delete_product(id)