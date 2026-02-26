class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product Name: {self.name}, Price: {self.price}")

class order:
    def __init__(self):
        self.products = []
        self.quantity = 0

    def add_product(self, product, quantity):
        self.products.append(product)
        self.quantity += quantity

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price * self.quantity
        return total
    
if __name__ == "__main__":
    p1 = product("Laptop", 1000)
    p2 = product("Phone", 500)

    order1 = order()
    order1.add_product(p1, 2)
    order1.add_product(p2, 3)

    print("Total Price: ", order1.total_price())