from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from flask import json


Base = declarative_base()


class MainCategoryProduct(Base):
    __tablename__ = 'main_category_product'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<main_category_product({0})>'.format(self.name)


class CategoryProduct(Base):
    __tablename__ = 'category_product'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True)
    main_category_product_id = Column(Integer)

    def __init__(self, name, main_category_product_id):
        self.name = name
        self.main_category_product_id = main_category_product_id

    def __repr__(self):
        return '<category_product({0}, {1})>'.format(
            self.name, self.main_category_product_id
        )


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    cost = Column(Float)
    category_product_id = Column(Integer)
    parameters = Column(JSONB)
    # тип parameters (JSONB) - привязывает нас к postgresql
    # пока не понял как обратиться через sqlalchemy к вложенному элементу json
    # однако на крайняк можно пользовать raw-sql:
    # r = engine.execute(
    #     "SELECT * FROM product
    #     WHERE product.parameters->'Память и процессор'->'parameters'->'Количество ядер процессора' @> '8';"
    # )
    # Хотя может лучше иметь плоский словарь?..

    def __init__(self, name, cost, category_product_id, parameters):
        self.name = name
        self.cost = cost
        self.category_product_id = category_product_id
        self.parameters = parameters

    def __repr__(self):
        return '<product({0}, {1}, {2}, {3})>'.format(
            self.name, self.cost, self.category_product_id, self.parameters
        )

    def convert_to_dict(self):
        return {
            'name': self.name,
            'cost': self.cost,
            'parameters': self.sorted_parameters(),
        }

    def sorted_parameters(self):
        product_sorted_parameters = sorted(
            self.parameters.items(),
            key=lambda x: x[1].get('priority')
        )
        product_sorted_parameters = (
            (
                category_parameters[0],
                (
                    category_parameters[1].get('main_parameters'),
                    category_parameters[1].get('parameters')
                )
            )
            for category_parameters in product_sorted_parameters
        )
        return product_sorted_parameters

    def flat_parameters(self):

        pass


# TODO: параметры базы надо брать из конфига
engine = create_engine(
    'postgresql://flask:coiw2IS8ph@10.0.3.143:5432/flask_market',
    json_serializer=json.dumps,
    echo=True,
)
Session = sessionmaker(bind=engine)
session = Session()
