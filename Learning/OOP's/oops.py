import csv

class Item:

    # Class attribute for Discounted Price
    disc_price = 0.8

    # To view all items
    view_all = []

    def __init__(self, name: str, price: float, quantity=0):

        # Run validation
        assert price >= 0, f"Written price = {price}, must be greater than or equal to Zero"
        assert quantity >= 0, f"Written quantity = {quantity}, must be greater than or equal to Zero"

        # Assign to self obejct
        self.name = name
        self.price = price
        self.quantity = quantity

        # To view all 
        Item.view_all.append(self)

    # To calculate whole inventory price 
    def calc_total_price(self):
        return self.price * self.quantity
    
    # For discounted price
    def apply_discount(self):
        self.price = self.price * self.disc_price

    # To load from csv file
    @classmethod
    def load_from_csv(cls):
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    # For View all
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
    

Item.load_from_csv()
print(Item.view_all)