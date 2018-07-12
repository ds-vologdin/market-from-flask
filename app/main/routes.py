from flask import render_template
from flask import request

from app.settings import config
from .blueprint import blueprint
from .models import MainCategoryProduct, Product, CategoryProduct
from .logger import logger


# TODO: Возможно имеет смысл вынести хелперы в отдельный файл
def get_categorys():
    main_categorys = MainCategoryProduct.query.all()
    categorys = [
        {
            'main': main_category,
            'sub': main_category.categorys_product,
        }
        for main_category in main_categorys
    ]
    return categorys


@blueprint.route('/')
def index():
    categorys = get_categorys()
    return render_template('index.html', categorys=categorys)


@blueprint.route('/main_category/<int:main_category_id>/')
def show_main_category(main_category_id):
    categorys = get_categorys()
    main_category = MainCategoryProduct.query.\
        filter(MainCategoryProduct.id == main_category_id).first()
    if not main_category:
        logger.debug('Запрос основной категории по несуществующему id')
        return render_template(
            'subcategory.html',
            categorys=categorys,
            main_category=None,
            sub_category=None,
            )
    return render_template(
        'subcategory.html',
        categorys=categorys,
        main_category=main_category,
        sub_categorys=main_category.categorys_product,
    )


@blueprint.route('/category/<int:category_id>/')
def show_category(category_id):
    categorys = get_categorys()
    category = CategoryProduct.query.\
        filter(CategoryProduct.id == category_id).first()
    if not category:
        logger.debug('Запрос категории по несуществующему id')
        return render_template(
            'subcategory_products.html',
            categorys=categorys,
            products=None,
            )
    products_info = []

    for product in category.products:
        products_info.append({
            'id': product.id,
            'product_name': product.name,
            'rating': product.rating,
            'cost': product.cost,
            'description': product.description,
            'images': product.get_sorted_path_images(
                config.get('PATH_IMAGES')
            ),
        })
    return render_template(
        'subcategory_products.html',
        categorys=categorys,
        products=products_info,
        category=category,
        main_category=category.main_category_product
    )


@blueprint.route('/product/<int:product_id>/')
def show_product(product_id):
    categorys = get_categorys()

    product = Product.query.filter(Product.id == product_id).first()
    if not product:
        logger.debug('Запрос продукта по несуществующему id')
        return render_template(
            'product.html', categorys=categorys, product=None
        )
    # TODO: надо подумать, может в шаблон перенести вызов функции?
    main_parameters = product.get_flat_main_parameters()

    images_product = product.get_sorted_path_images(config.get('PATH_IMAGES'))

    feedbacks = product.feedbacks

    return render_template(
        'product.html',
        categorys=categorys,
        product=product,
        category_product=product.category_product,
        main_category_product=product.category_product.main_category_product,
        images_product=images_product,
        main_parameters=main_parameters,
        feedbacks=feedbacks
    )


@blueprint.route('/api/add_product', methods=['POST'])
def api_add_product():
    logger.debug('Кто-то пытается пользоваться API. ХА-ХА-ХА...')
    print(request.get_json(force=True))
    return 'OK'
