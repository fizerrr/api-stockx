from re import S
from unicodedata import name


class Snkr:
      name = None
      image_url = None
      last_sale = None
      retail_price = None
      def __init__(self, name,image_url,last_sale,retail_price):
        self.name = name
        self.image_url = image_url
        self.last_sale = last_sale
        self.retail_price = retail_price
      def print_name(self):
        print(name)