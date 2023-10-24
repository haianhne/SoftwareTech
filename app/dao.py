def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }]


def load_products(kw):
    products = [{
        'id': 1,
        'name': 'Iphone 15 ProMax 256',
        'price': 39999990,
        'image': 'https://www.renderhub.com/madmix/apple-iphone-15-pro-max-v2/apple-iphone-15-pro-max-v2-01.jpg'
    }, {
        'id': 1,
        'name': 'Ipad 15 ProMax 256',
        'price': 39999990,
        'image': 'https://www.renderhub.com/madmix/apple-iphone-15-pro-max-v2/apple-iphone-15-pro-max-v2-01.jpg'
    }, {
        'id': 1,
        'name': 'Iphone 15 ProMax 256',
        'price': 39999990,
        'image': 'https://www.renderhub.com/madmix/apple-iphone-15-pro-max-v2/apple-iphone-15-pro-max-v2-01.jpg'
    }, {
        'id': 1,
        'name': 'Iphone 15 ProMax 256',
        'price': 39999990,
        'image': 'https://www.renderhub.com/madmix/apple-iphone-15-pro-max-v2/apple-iphone-15-pro-max-v2-01.jpg'
    }, {
        'id': 1,
        'name': 'Iphone 15 ProMax 256',
        'price': 39999990,
        'image': 'https://www.renderhub.com/madmix/apple-iphone-15-pro-max-v2/apple-iphone-15-pro-max-v2-01.jpg'
    }, {
        'id': 1,
        'name': 'Iphone 15 ProMax 256',
        'price': 39999990,
        'image': 'https://www.renderhub.com/madmix/apple-iphone-15-pro-max-v2/apple-iphone-15-pro-max-v2-01.jpg'
    }, ]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]
    return products
