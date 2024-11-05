from flask import Flask, render_template, request

import dao

app = Flask(__name__)


@app.route('/')

def index():
    q=request.args.get('q')

    # trangchu=request.args.get('trangchu')
    query = request.args.get('query')

    # Trả về danh sách sản phẩm tìm kiếm theo từ khóa, query và trang hiện tại
    categories = dao.load()
    
    products = dao.LoadProducts(q=q,query= query)
    return render_template('index.html',categories=categories, products=products)

@app.route('/query/<int:id>')
def truyxuat(id):
    categories = dao.load()
    product = dao.LoadProduct_Detail(id)
    return render_template('detailProduct.html', product=product, categories=categories) 





if __name__ == '__main__':
    app.run()


