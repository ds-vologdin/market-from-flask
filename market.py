from flask import Flask, render_template
from flask import request
from models import session, MainCategoryProduct, CategoryProduct, Product

app = Flask(__name__)


def get_categorys():
    main_categorys = session.query(MainCategoryProduct).all()
    categorys = []
    for main_category in main_categorys:
        sub_categorys = session.query(CategoryProduct).filter_by(
            main_category_product_id=main_category.id
        ).all()
        sub_categorys_name = [
            sub_category.name for sub_category in sub_categorys
        ]
        categorys.append({
            'main': main_category.name,
            'sub': sub_categorys_name,
        })
    return categorys


@app.route('/')
def index():
    categorys = get_categorys()
    return render_template('index.html', categorys=categorys)


@app.route('/<int:product_id>/')
def show_product(product_id):
    print(product_id)
    categorys = get_categorys()
    product = session.query(Product).filter_by(id=product_id).first()
    if not product:
        pass
    print(product.convert_to_dict())
    return render_template(
        'product.html', categorys=categorys, product=product.convert_to_dict()
    )


@app.route('/api/add_product', methods=['POST'])
def api_add_product():
    print(request.get_json(force=True))
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
