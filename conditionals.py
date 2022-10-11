# using conditions to control the flow of our program
product_price: int = 300


if product_price == 600:
    print("The product price is 600 SAR")
    print("Another operation")
elif product_price > 400:
    print("The product is expensive!")
elif product_price < 400:
    print("The product is cheap")
else:
    print("")

username: str = "ahemd"
password: str = "563520Adhdsk"

if username == "ahemd" and password == "563520Adhdsk":
    print("Welcome to the website")
else:
    print("Your credentials are not correct")
