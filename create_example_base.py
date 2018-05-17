from models import MainCategoryProduct, CategoryProduct, Product, Base, \
    session, engine


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    main_category_product_list = [
        'Электроника',
        'Бытовая техника',
        'Детские товары',
        'Зоотовары',
        'Дом, дача, ремонт',
        'Одежда и обувь',
        'Красота и здоровье',
        'Авто',
    ]
    for category in main_category_product_list:
        main_category_product = MainCategoryProduct(name=category)
        session.add(main_category_product)

    main_category_product = session.query(MainCategoryProduct).filter_by(
        name='Электроника'
    ).first()

    category_product_list_list = [
        ('мобильные телефоны', main_category_product.id),
        ('смартфоны', main_category_product.id),
        ('планшеты', main_category_product.id),
        ('mp3-плееры', main_category_product.id),
    ]
    for category in category_product_list_list:
        category_product = CategoryProduct(*category)
        session.add(category_product)

    category_product = session.query(CategoryProduct).filter_by(
        name='смартфоны'
    ).first()

    products_list = [
        (
            'Xiaomi Redmi 5 Plus 4/64GB',
            13290.00,
            category_product.id, {
                'Общие характеристики': {
                    'Операционная система': 'Android',
                    'Материал корпуса': 'металл',
                    'Количество SIM-карт': 2,
                    'Режим работы нескольких SIM-карт': 'Попеременный',
                    'Вес': 180,
                    'Размеры (ШxВxТ)': '75.45x158.5x8.05',
                },
                'Экран': {
                    'Тип экрана': ('цветной', 'сенсорный'),
                    'Тип сенсорного экрана': ('мультитач', 'емкостный'),
                    'Диагональ': '5.99',
                    'Размер изображения': '2160x1080',
                    'Число пикселей на дюйм (PPI)': 403,
                    'Соотношение сторон': '18:9',
                },
                'Мультимедийные возможности': {
                    'Тыловая фотокамера': 12.0,
                    'Фотовспышка': ('тыльная', 'светодиодная'),
                    'Функции тыловой фотокамеры': 'автофокус',
                    'Диафрагма тыловой фотокамеры': 'F/2.2',
                    'Макс. разрешение видео': '1920x1080',
                    'Фронтальная камера': '5 млн пикс.',
                },
                'Связь': {
                    'Стандарт': ('GSM 900/1800/1900', '3G', '4G LTE'),
                    'Интерфейсы': ('Wi-Fi 802.11n', 'Wi-Fi Direct',
                                   'Bluetooth 4.2', 'USB'),
                    'Спутниковая навигация': ('GPS', 'ГЛОНАСС', 'BeiDou'),
                    'Cистема A-GPS': True,
                },
                'Память и процессор': {
                    'Процессор': 'Qualcomm Snapdragon 625 MSM8953, 2000 МГц',
                    'Количество ядер процессора': 8,
                    'Видеопроцессор': 'Adreno 506 ',
                    'Объем встроенной памяти': 64,
                    'Объем оперативной памяти': 4,
                    'Слот для карт памяти': True,
                },
                'Питание': {
                    'Емкость аккумулятора': 4000
                },
            }
        )
    ]
    for product_tuple in products_list:
        product = Product(*product_tuple)
        session.add(product)
    session.commit()
