#using coditions to control the flow of our program


product_price : int = 300


if product_price == 600:
    print("the product price is 600 SAR")
    print("another operation")
elif product_price > 400:
    print("The product is expensive!")
elif product_price < 400:
    print("The  product is cheap")



username : str = "ahmed"
password : str = "563520Adhdsk"

if username == "ahmegd" or password == "5s63520Adhdsk":
    print("Welcome to the website")
else:
    print("Your credentials are not correct")