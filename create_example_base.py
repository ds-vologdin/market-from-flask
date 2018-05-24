from models import MainCategoryProduct, CategoryProduct, Product, \
    ImagesProduct, CategoryProductMainParameters, User, Feedback, \
    Base, session, engine


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

    main_category_product = MainCategoryProduct.query.filter(
        MainCategoryProduct.name == 'Электроника'
    ).first()

    category_product_list = [
        ('мобильные телефоны', main_category_product.id),
        ('смартфоны', main_category_product.id),
        ('планшеты', main_category_product.id),
        ('mp3-плееры', main_category_product.id),
    ]
    for category in category_product_list:
        category_product = CategoryProduct(*category)
        session.add(category_product)

    category_product = CategoryProduct.query.filter(
        CategoryProduct.name == 'смартфоны'
    ).first()

    category_product_main_parameters_list = [
        'Операционная система',
        'Количество SIM-карт',
        'Диагональ',
        'Тыловая фотокамера',
        'Фронтальная камера',
        'Стандарт',
        'Интерфейсы',
        'Спутниковая навигация',
    ]
    for parameter in category_product_main_parameters_list:
        category_product_main_parameters = CategoryProductMainParameters(
            parameter, category_product.id
        )
        session.add(category_product_main_parameters)

    products_list = [
        (
            'Xiaomi Redmi 5 Plus 4/64GB',
            'Хороший телефон, бери не пожалеешь...',
            13290.00,
            category_product.id,
            {
                'Общие характеристики': {
                        'priority': 0,
                        # priority используем для сортировки категорий
                        # характеристик
                        'parameters': {
                            'Материал корпуса': 'металл',
                            'Режим работы нескольких SIM-карт': 'Попеременный',

                        },
                        'main_parameters': {
                            'Операционная система': 'Android',
                            'Количество SIM-карт': 2,
                            'Вес': 180,
                            'Размеры (ШxВxТ)': '75.45x158.5x8.05',
                        },
                },
                'Экран': {
                    'priority': 1,
                    'parameters': {
                        'Тип экрана': ('цветной', 'сенсорный'),
                        'Тип сенсорного экрана': ('мультитач', 'емкостный'),
                        'Число пикселей на дюйм (PPI)': 403,
                        'Соотношение сторон': '18:9',
                    },
                    'main_parameters': {
                        'Диагональ': '5.99',
                        'Размер изображения': '2160x1080',
                    },
                },
                'Мультимедийные возможности': {
                    'priority': 2,
                    'parameters': {
                        'Фотовспышка': ('тыльная', 'светодиодная'),
                        'Функции тыловой фотокамеры': 'автофокус',
                        'Диафрагма тыловой фотокамеры': 'F/2.2',
                        'Макс. разрешение видео': '1920x1080',
                    },
                    'main_parameters': {
                        'Тыловая фотокамера': 12.0,
                        'Фронтальная камера': 5,
                    },
                },
                'Связь': {
                    'priority': 3,
                    'parameters': {
                        'Cистема A-GPS': True,
                    },
                    'main_parameters': {
                        'Стандарт': ('GSM 900/1800/1900', '3G', '4G LTE'),
                        'Интерфейсы': ('Wi-Fi 802.11n', 'Wi-Fi Direct',
                                       'Bluetooth 4.2', 'USB'),
                        'Спутниковая навигация': ('GPS', 'ГЛОНАСС', 'BeiDou'),

                    },
                },
                'Память и процессор': {
                    'priority': 4,
                    'parameters': {
                        'Слот для карт памяти': True,
                    },
                    'main_parameters': {
                        'Процессор':
                            'Qualcomm Snapdragon 625 MSM8953, 2000 МГц',
                        'Количество ядер процессора': 8,
                        'Видеопроцессор': 'Adreno 506 ',
                        'Объем встроенной памяти': 64,
                        'Объем оперативной памяти': 4,
                    },
                },
                'Питание': {
                    'priority': 5,
                    'parameters': {},
                    'main_parameters': {
                        'Емкость аккумулятора': 4000,
                    },
                },
            },
            4
        ),
        (
            'Xiaomi Redmi 5 Plus 4/32GB',
            'Хороший телефон, бери не пожалеешь...',
            10290.00,
            category_product.id,
            {
                'Общие характеристики': {
                        'priority': 0,
                        # priority используем для сортировки категорий
                        # характеристик
                        'parameters': {
                            'Материал корпуса': 'металл',
                            'Режим работы нескольких SIM-карт': 'Попеременный',

                        },
                        'main_parameters': {
                            'Операционная система': 'Android',
                            'Количество SIM-карт': 2,
                            'Вес': 180,
                            'Размеры (ШxВxТ)': '75.45x158.5x8.05',
                        },
                },
                'Экран': {
                    'priority': 1,
                    'parameters': {
                        'Тип экрана': ('цветной', 'сенсорный'),
                        'Тип сенсорного экрана': ('мультитач', 'емкостный'),
                        'Число пикселей на дюйм (PPI)': 403,
                        'Соотношение сторон': '18:9',
                    },
                    'main_parameters': {
                        'Диагональ': '5.99',
                        'Размер изображения': '2160x1080',
                    },
                },
                'Мультимедийные возможности': {
                    'priority': 2,
                    'parameters': {
                        'Фотовспышка': ('тыльная', 'светодиодная'),
                        'Функции тыловой фотокамеры': 'автофокус',
                        'Диафрагма тыловой фотокамеры': 'F/2.2',
                        'Макс. разрешение видео': '1920x1080',
                    },
                    'main_parameters': {
                        'Тыловая фотокамера': 12.0,
                        'Фронтальная камера': 5,
                    },
                },
                'Связь': {
                    'priority': 3,
                    'parameters': {
                        'Cистема A-GPS': True,
                    },
                    'main_parameters': {
                        'Стандарт': ('GSM 900/1800/1900', '3G', '4G LTE'),
                        'Интерфейсы': ('Wi-Fi 802.11n', 'Wi-Fi Direct',
                                       'Bluetooth 4.2', 'USB'),
                        'Спутниковая навигация': ('GPS', 'ГЛОНАСС', 'BeiDou'),

                    },
                },
                'Память и процессор': {
                    'priority': 4,
                    'parameters': {
                        'Слот для карт памяти': True,
                    },
                    'main_parameters': {
                        'Процессор':
                            'Qualcomm Snapdragon 625 MSM8953, 2000 МГц',
                        'Количество ядер процессора': 8,
                        'Видеопроцессор': 'Adreno 506 ',
                        'Объем встроенной памяти': 32,
                        'Объем оперативной памяти': 4,
                    },
                },
                'Питание': {
                    'priority': 5,
                    'parameters': {},
                    'main_parameters': {
                        'Емкость аккумулятора': 4000,
                    },
                },
            },
            4
        )
    ]
    for product_tuple in products_list:
        product = Product(*product_tuple)
        session.add(product)

    product = session.query(Product.id).filter(
        Product.name == 'Xiaomi Redmi 5 Plus 4/64GB'
    ).first()
    product_id = product[0]
    images = [
        (product_id, 'd2543e0e-5c2d-11e8-81fa-2089846029f1.jpeg', 0),
        (product_id, '4d41d5d4-5c30-11e8-b708-2089846029f1.jpeg', 1),
    ]
    for image in images:
        image_product = ImagesProduct(*image)
        session.add(image_product)

    users = [
        ('terminator', 'Вася', 'Москва'),
        ('gingema', 'Катя', 'Хабаровск'),
        ('cheburator', 'Толя', 'Курск'),
    ]
    for user in users:
        user_market = User(*user)
        session.add(user_market)

    terminator = User.query.filter(User.login == 'terminator').first()
    feedback = Feedback(
        'Очень хороший телефон. Рекомендую.',
        5, terminator.id, product_id
    )
    session.add(feedback)
    gingema = User.query.filter(User.login == 'gingema').first()
    feedback = Feedback(
        'не понравился...',
        3, gingema.id, product_id
    )
    session.add(feedback)
    cheburator = User.query.filter(User.login == 'cheburator').first()
    feedback = Feedback(
        'Через месяц поменял экран, хрупкий',
        4, cheburator.id, product_id
    )
    session.add(feedback)

    session.commit()
