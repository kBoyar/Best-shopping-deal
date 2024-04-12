class Stores:
    def __init__(self, name, location, items):
        self.name = name
        self.location = location
        self.items = items

    def lowerprice(self, given):
        for i in range(len(self.items)):
            if given == self.items[i].name:
                return self.items[i].price
        return 0

    def return_name(self, given):
        for i in range(len(self.items)):
            if given == self.items[i].name:
                return self.items[i].name
        return 0


class Items:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def reduce_quantity(self, given):
        self.quantity = self.quantity - given

    def return_name(self, given):
        for i in range(len(self.name)):
            if given == self.name[i].name:
                return self.name[i].name
        return 0


def sort_price(stores, given):
    for i in range(len(stores)-1):
        swapped = False
        for j in range(0, len(stores)-i-1):
            if stores[j].lowerprice(given) > stores[j + 1].lowerprice(given):
                swapped = True
                stores[j], stores[j + 1] = stores[j + 1], stores[j]
        if not swapped:
            return stores


def count_store(stores, given):
    count = 0
    for i in range(len(stores)):
        for j in range(len(stores[i].items)):
            if stores[i].items[j].name == given:
                count += 1
    return count


s1items = []
s1items.append(Items("apple", 10, 476))
s1items.append(Items("sandwich", 2, 199))
s1items.append(Items("olive bread", 3, 299))
s1items.append(Items("milk", 7, 125))
s1items.append(Items("egg", 40,78))
s1items.append(Items("candy", 4, 51))

s2items = []
s2items.append(Items("bargain phone", 2, 20000))
s2items.append(Items("s phone", 4, 65000))
s2items.append(Items("fruit phone", 2, 70000))

s3items = []
s3items.append(Items("milk", 30, 200))
s3items.append(Items("egg", 2, 50))
s3items.append(Items("candy", 6, 100))
s3items.append(Items("soda", 5, 156))
s3items.append(Items("bargain phone", 3, 18500))

s4items = []
s4items.append(Items("candy", 10, 85))
s4items.append(Items("soda", 4, 150))
s4items.append(Items("sandwich", 3, 299))

s1 = Stores("Local Grocery ", "East Lansing", s1items)
s2 = Stores("Electronics R Here", "Ann arbon", s2items)
s3 = Stores("Corner Store", "East Lansing", s3items)
s4 = Stores("Sparty's", "East Lansing", s4items)

stores = []
stores.append(s1)
stores.append(s2)
stores.append(s3)
stores.append(s4)

items_set = set()
items_map = {}
print("\n\x1B[1;4m" + "Store Related Information" + "\x1B[0m")
print(f"There are {len(stores)} Store(s).")
for i in range(len(stores)):
    print(f"{stores[i].name} has {len(stores[i].items)} distinct items.")

print("\n\x1B[1;4m" + "Item Related Information" + "\x1B[0m")
for i in range(len(stores)):
    for j in range(len(stores[i].items)):
        items_set.add(stores[i].items[j].name)
print(f"There are {len(items_set)} distinct item(s) available for purchase.")
for x in items_set:
    items_map.update({x: 0})
count_items = 0
for i in range(len(stores)):
    for j in range(len(stores[i].items)):
        if stores[i].items[j].name in items_map:
            items_map[stores[i].items[j].name] += stores[i].items[j].quantity
for x in sorted(items_map):
    print(f"There are {items_map[x]} {x}(s).")

mylist = []
print("\n\x1B[1;4m" + "Create list" + "\x1B[0m")
while True:
    ent = input("Enter quantity and product:").lower()
    mylist.append(ent)

    a = input("Do you want to add more?Y/N \n").lower()
    while a != "y" and a != "n":
        if a != "y" and a != "n":
            a = input("Please enter (Y/N)!").lower()
        else:
            break

    if a == "n":
        break

minprice = 3000.00
total_value_all = 0
output = []
i = x = 0
count = 0
saved_store_info = []
print("\n\x1B[1;4m" + "Shopping results" + "\x1B[0m")
for x in range(len(mylist)):
    output.clear()
    saved_store_info.clear()
    total_value_item = 0
    quantity, product = mylist[x].split(" ", 1)
    quantity = int(quantity)
    sort_price(stores, product)
    count = count_store(stores, product)
    output.append(f"\nTrying to order {quantity} {product}(s).")
    output.append(f"{count} Store(s) sell {product}.")
    while True:
        if stores[0].lowerprice(product) == 0:
            stores = stores[1:] + [stores[0]]
        else:
            break
    for i in range(len(stores)):
        for j in range(len(stores[i].items)):
            if quantity == 0:
                break
            if product == stores[i].items[j].name:
                if stores[i].items[j].quantity >= quantity:
                    total_value_item = (int(total_value_item) + (quantity * stores[i].items[j].price))
                    saved_store_info.append(f"Order {quantity} from {stores[i].name} in {stores[i].location}.")
                    break
                else:
                    total_value_item = (int(total_value_item) + (stores[i].items[j].quantity * stores[i].items[j].price))
                    saved_store_info.append(f"Order {stores[i].items[j].quantity} "
                                            f"from {stores[i].name} "
                                            f"in {stores[i].location}.")
                quantity = quantity - stores[i].items[j].quantity
        else:
            continue
        break
    total_value_all = total_value_all + total_value_item
    total_value_item = "%.2f" % float(total_value_item/100)
    output.append(f"Total price:${total_value_item}")

    for i in range(len(saved_store_info)):
        output.append(f"{saved_store_info[i]}")

    for i in range(len(output)):
        print(output[i])

total_value_all = "%.2f" % float(total_value_all/100)
print(f"\nBe sure to bring {total_value_all} when you leave for the stores")