from flask import Flask, render_template
from flask import request
from models import session, MainCategoryProduct, Product
from settings import PATH_IMAGES

app = Flask(__name__)


def get_categorys():
    main_categorys = session.query(MainCategoryProduct).all()
    categorys = [
        {
            'main': main_category,
            'sub': main_category.categorys_product,
        }
        for main_category in main_categorys
    ]
    return categorys


@app.route('/')
def index():
    categorys = get_categorys()
    return render_template('index.html', categorys=categorys)


@app.route('/main_category/<int:main_category_id>/')
def show_main_category(main_category_id):
    categorys = get_categorys()
    return render_template('index.html', categorys=categorys)


@app.route('/category/<int:category_id>/')
def show_category(category_id):
    categorys = get_categorys()
    return render_template('index.html', categorys=categorys)


@app.route('/product/<int:product_id>/')
def show_product(product_id):
    categorys = get_categorys()

    product = session.query(Product).filter(Product.id == product_id).first()
    if not product:
        return render_template(
            'product.html', categorys=categorys, product=None
        )
    # main_parameters_name = product.category_product.\
    #     categorys_product_main_parameters
    #
    # main_parameters_name = [
    #     parameter.name for parameter in main_parameters_name
    # ]
    # main_parameters = product.get_flat_main_parameters(main_parameters_name)
    main_parameters = product.get_flat_main_parameters()

    for parameter in main_parameters:
        print(parameter, main_parameters[parameter])

    images_product = [(image.file, image.priority) for image in product.images]
    # Файлы сортируем по приоритету, чем меньше значение приоритета, тем
    # приоритет выше
    images_product = [
        '{}/{}'.format(PATH_IMAGES, file)
        for file, priority in sorted(images_product, key=lambda x: x[1])
    ]

    return render_template(
        'product.html',
        categorys=categorys,
        product=product,
        category_product=product.category_product,
        main_category_product=product.category_product.main_category_product,
        images_product=images_product,
        main_parameters=main_parameters,
    )


@app.route('/api/add_product', methods=['POST'])
def api_add_product():
    print(request.get_json(force=True))
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
