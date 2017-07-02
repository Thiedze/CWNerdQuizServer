from unicodedata import category

from cwcategory import Category


class Quiz(object):

    def __init__(self, categories):
        self.categories = dict()
        for key, value in categories.items():
            category = Category(key, value)
            self.categories[key] = category
        