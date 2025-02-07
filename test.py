class Product:
    def __init__(self,name,price,stock):
        self.__name=name
        self.__price=price
        self.__stock=stock
    
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def purchase(self,quant):
        if quant<=self.__stock:
            self.__stock-=quant
            print(quant)
            print(self.__stock)
        else:
            print("not enough stock for the selected product. pls try again after sometime!!!")
    def get_stock(self):
        return self.__stock




class Costomer:
    def __init__(self,name,email):
        self.__name=name
        self.__email=email

    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def ordered_products(self,product,quantity):
        if quantity<=product.get_stock():
            
            print("Your order for ",product.get_name()," is successfull") 
        else:
            print("The selected quantities are not available. retry with lesser quantities")

product1=Product("MOBILE PHONE",15000,1)
Costomer1=Costomer("Abhijith","abc@gmail.com")
Costomer1.ordered_products(product1,2)