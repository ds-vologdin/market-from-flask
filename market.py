from flask import Flask, render_template
from flask import request
from models import session, MainCategoryProduct, Product
from settings import PATH_IMAGES

app = Flask(__name__)


def get_categorys():
    main_categorys = session.query(MainCategoryProduct).all()
    categorys = []
    for main_category in main_categorys:
        sub_categorys = main_category.categorys_product
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
    categorys = get_categorys()

    product = session.query(Product).filter(Product.id == product_id).first()
    if not product:
        return render_template(
            'product.html', categorys=categorys, product=None
        )

    product_dict = product.convert_to_dict()
    print(product_dict.get('parameters'))
    category_product = product.category_product.name
    main_category_product = product.category_product.main_category_product.name
    images_product = [(image.file, image.priority) for image in product.images]
    # Файлы сортируем по приоритету, чем меньше значение приоритета, тем
    # приоритет выше
    images_product = [
        '{}/{}'.format(PATH_IMAGES, file)
        for file, priority in sorted(images_product, key=lambda x: x[1])
    ]
    print(images_product)
    return render_template(
        'product.html',
        categorys=categorys,
        product=product_dict,
        category_product=category_product,
        main_category_product=main_category_product,
        images_product=images_product,
    )


@app.route('/api/add_product', methods=['POST'])
def api_add_product():
    print(request.get_json(force=True))
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
