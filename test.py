from online_shop.main import Product,Person,Store
#
item_1 = Product("s24", "samsang", 1100,5)
item_2 = Product("s25", "samsang", 1200, 5)
person_1 = Person("arsham", "hajeb", 22)
person_2 = Person("arsh", "haj", 19)

Store.buy_product("arsham", "s24", 4)
Product.show_products()
Store.show_purchases()
