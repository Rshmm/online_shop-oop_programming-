class Product:
    products = []

    def __init__(self, name, brand, price, count):
        try:
            assert str(name) and float(price) > 0 and int(count) >= 0
            self.name = name
            self.price = price
            self.count = count
            self.brand = brand
            Product.products.append(self)
        except AssertionError:
            print("there is a problem in the values")

    def __repr__(self):
        return f"name = {self.name} ,brand = {self.brand} ,price = {self.price}, count = {self.count}"

    @classmethod
    def show_products(cls):
        print("products")
        for product in cls.products:
            print(product)

    @classmethod
    def edit_product(cls, name, new_name, new_brand, new_price, new_count):
        found = False
        for product in cls.products:
            if name.lower() == product.name.lower():
                found = True
                if new_name:
                    product.name = new_name
                if new_brand:
                    product.brand = new_brand
                if new_price:
                    product.price = new_price
                if new_count:
                    product.count = new_count
                print("Product edited successfully")
                break
        if not found:
            print("not found")

    @classmethod
    def remove_product(cls, name):
        found = False
        for product in cls.products:
            if name.lower() == product.name.lower():
                found = True
                Product.products.remove(product)
                print("Product removed successfully")
        if not found:
            print("not found")


class Person:
    persons = []

    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

        if self.age >= 18:
            Person.persons.append(self)
        else:
            print(f"your age is under 18 {self.name} ")

    def __repr__(self):
        return f"full name = {self.name + ' ' + self.family} , age = {self.age}"

    @classmethod
    def show_persons(cls):
        print("persons")
        for person in cls.persons:
            print(person)

    @classmethod
    def edit_person(cls, name, new_name, new_family):
        found = False
        for person in cls.persons:
            if name.lower() == person.name.lower():
                found = True
                if new_name:
                    person.name = new_name
                if new_family:
                    person.family = new_family
                print("Person edited successfully")
            if not found:
                print("not found")

    @classmethod
    def remove_person(cls, name):
        found = False
        for person in cls.persons:
            if name.lower() == person.name.lower():
                found = True
                Person.persons.remove(person)
                print("Person removed successfully")
        if not found:
            print("not found")

class Store:
    purchases = []

    @classmethod
    def buy_product(cls, buyer_name, product_name, quantity):
        buyer = None
        product = None

        for person in Person.persons:
            if buyer_name.lower() == person.name.lower():
                buyer = person
                break

        if not buyer:
            print("❌ Buyer not found!")
            return


        for p in Product.products:
            if product_name.lower() == p.name.lower():
                product = p
                break

        if not product:
            print("❌ Product not found!")
            return


        if product.count < quantity:
            print(f"❌ Not enough stock for {product_name}. Available: {product.count}")
            return

        product.count -= quantity
        cls.purchases.append({"buyer": buyer.name, "product": product.name, "quantity": quantity})
        print(f"✅ {buyer.name} bought {quantity} {product.name}(s) successfully!")

    @classmethod
    def show_purchases(cls):
        print("\n🛒 Purchase History:")
        if not cls.purchases:
            print("No purchases yet.")
        for purchase in cls.purchases:
            print(f"👤 {purchase['buyer']} bought {purchase['quantity']} x {purchase['product']}")
        print("\n")
