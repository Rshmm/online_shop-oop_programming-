from online_shop.main import Product,Person,Store

while True:

    print("1- Add products")
    print("2- Show products")
    print("3- edit products")
    print("4- Remove products")
    print("5- Add person")
    print("6- Show person")
    print("7- Edit person")
    print("8- Remove person")
    print("9- buy products")
    print("10- show buy products")
    print("0- EXIT")

    choice = int(input("Enter your choice : "))

    match choice:
        #  Add products
        case 1:
            name = input("Enter products name : ")
            brand = input("Enter products brand : ")
            price = input("Enter products price : ")
            count = int(input("Enter products count : "))
            Product(name,brand,price,count)


        # Show products
        case 2:
            Product.show_products()


        # edit products
        case 3:
            Product.show_products()
            name = input("Enter product name that you wants to edit : ")
            new_name = input("Enter new name for product (if you dont want to change it enter nothing) : ")
            new_brand = input("Enter new brand for product (if you dont want to change it enter nothing) : ")
            new_price = input("Enter new price for product (if you dont want to change it enter nothing) : ")
            new_count = int(input("Enter new count for product (if you dont want to change it enter nothing) : "))
            Product.edit_product(name,new_name,new_brand,new_price,new_count)


        # Remove products
        case 4:
            Product.show_products()
            name = input("Enter product name that you wants to remove : ")
            Product.remove_product(name)

        # Add person
        case 5:
            name = input("Enter person name : ")
            family = input("Enter person family : ")
            age = int(input("Enter person age : "))
            Person(name,family,age)

        # Show person
        case 6:
            Person.show_persons()

        # Edit person
        case 7:
            Person.show_persons()
            name = input("Enter person name that you wants to edit : ")
            new_name = input("Enter new name for person (if you dont want to change it enter nothing) : ")
            new_family = input("Enter new family  for person (if you dont want to change it enter nothing) : ")
            Person.edit_person(name,new_name,new_family)

        # Remove person
        case 8:
            Person.show_persons()
            name = input("Enter person name that you wants to remove : ")
            Person.remove_person(name)

        case 9:
            Person.show_persons()
            buyer_name = input("Enter person who wants to buy : ")
            Product.show_products()
            product_name = input("Enter product which you want to buy : ")
            quantity = int(input("Enter product count you wants to buy : "))
            Store.buy_product(buyer_name,product_name,quantity)

        case 10:
            Store.show_purchases()

        case 0:
            exit()

