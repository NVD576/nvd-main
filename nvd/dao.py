import json

def load():
    with open('data/categories.json', encoding= 'utf-8') as f:
        categories=json.load(f)

    return categories
    

def LoadProducts(q=None, query=None):
    with open('data/products.json', encoding= 'utf-8') as f:
        products=json.load(f)
        if q:
            products = [p for p in products if q.lower() in p["name"].lower()]
        if query:
            products = [p for p in products if  p["category_id"].__eq__(int(query))]

        return products

def LoadProduct_Detail(id):
    with open('data/products.json', encoding= 'utf-8') as f:
        products=json.load(f)
        for p in products:
            if p["id"]==int(id):
                return p
