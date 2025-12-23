# category class
class Category:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.no_of_products = 0

    def display(self):
        print(self.name, self.code, self.no_of_products)


# product class
class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        category.no_of_products += 1


# Categories
C1 = Category("Chinese", "011")
C2 = Category("FastFood", "012")
C3 = Category("Beverages", "013")

# Products
products = [
    Product("Burger", 101, C2, 100),
    Product("Pizza", 102, C2, 110),
    Product("Garlic Bread", 103, C2, 120),
    Product("Noodles", 104, C1, 170),
    Product("Momos", 105, C1, 80),
    Product("Coffee", 106, C3, 130),
    Product("Cold Coffee", 107, C3, 160),
    Product("Manchurian", 108, C1, 240),
    Product("Lassi", 109, C3, 90),
    Product("Cold Coco", 110, C3, 75),
]

# Display category info
C1.display()
C2.display()
C3.display()


# 🔹 Sorting (LOW → HIGH)
products_sorted_low = sorted(products, key=lambda p: p.price)

print("\nLow to High:")
for p in products_sorted_low:
    print(p.name, p.price)


# 🔹 Sorting (HIGH → LOW)
products_sorted_high = sorted(products, key=lambda p: p.price, reverse=True)

print("\nHigh to Low:")
for p in products_sorted_high:
    print(p.name, p.price)


# 🔹 Fast Searching using Dictionary
product_by_code = {p.code: p for p in products}

code = int(input("Enter code here: "))
product = product_by_code.get(code)

if product:
    print("\nFound:", product.name, product.price)
else:
    print("\n404 Product Not Found")
