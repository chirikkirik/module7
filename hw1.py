from itertools import product
from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open('products.txt', 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        file = open('products.txt', 'r')
        current_products = self.get_products()
        for product in products:
            if product.name not in current_products:
                file = open('products.txt', 'a')
                file.write(f'{product}\n')
            else:
                print(f'Продукт {product.name} {product.weight} {product.category} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())

