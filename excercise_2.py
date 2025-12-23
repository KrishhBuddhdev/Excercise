# Add new data members “parent”, “display_name”, and “products” (list of product objects) inside the category class.
# Add a new member function to generate “display_name”.
# “display_name” has the text value as below.
#    1.Vehicle category without parent then “Vehicle”
#    2.Car category with “Vehicle” as a parent then “Vehicle > Car”
#    3.Petrol category with “Car” as a parent then “Vehicle > Car > Petrol”
# Create 5 category objects with parent and child relation.
# Create 3 product objects in each category.
# Display Category with its Code, Display Name and all product details inside that category.
# Display product list by category (group by category, order by category name).

# Add new data members “parent”, “display_name”, and “products” (list of product objects) inside the category class.

# Class Category

class Category:
    def __init__(self, name, code, parent=None): # no parent = null -> use None keyword
        self.name = name
        self.code = code
        self.parent = parent
        self.products = [] # make empty list to store all product
        self.display_name = self.generate_display_name() # make an object

# Add a new member function to generate “display_name”

    # def display(self):
    #     for p in self.products:
    #         print(p.name, p.code, p.price)


    def generate_display_name(self):
        names = [] # make bank list to fetch names
        current = self
        while current:
            names.append(current.name) # add names dynamically to the list
            current = current.parent
        return " -> ".join(reversed(names)) # concatenate /join string . to show the work flow

# Class product
class Product:
    def __init__(self, name, code, price, category):
        self.name = name
        self.code = code
        self.price = price
        category.products.append(self) # add product dynamically

''' 1.Vehicle category without parent then “Vehicle”
    2.Car category with “Vehicle” as a parent then “Vehicle > Car”
    3.Petrol category with “Car” as a parent then “Vehicle > Car > Petrol”'''


# make objects

vehicle = Category("Vehicle", "11")
car = Category("Car", "12", vehicle)
bike = Category("Bike", "13", vehicle)
petrol= Category("petrol", "15", car)
diesel = Category("diesel", "16", car)

categories = [vehicle, car, bike , petrol , diesel ]

# create product list

product=[
        Product("Truck", 101, 500000, vehicle),
        Product("Bus", 102, 800000, vehicle),
        Product("van", 103, 600000, vehicle),

        Product("Sedan", 201, 1200000, car),
        Product("SUV", 202, 1800000, car),
        Product("Hatchback", 203, 900000, car),

        Product("hunter", 301, 150000, bike),
        Product("classic", 302, 80000, bike),
        Product("meateor", 303, 220000, bike),

        Product("toyota", 401, 1300000, diesel),
        Product("lexsus", 402, 1900000, diesel),
        Product("virtus", 403, 1000000, diesel),

        Product("ryubicon", 501, 1600000, petrol),
        Product("defender", 502, 2200000, petrol),
        Product("discovery", 503, 1100000, petrol),


]

# vehicle.display()
# car.display()
# bike.display()
# petrol.display()
# diesal.display()

# loop to show the value automatically in to the assign variables
for c in categories: # create object
    print("__________________")
    print("__________________")
    print("\nCategory Code :", c.code)

    print("Display Name  :", c.display_name)

    print("Products:")

    for p in c.products:
        print(p.name, p.code, p.price)



