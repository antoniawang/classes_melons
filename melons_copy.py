"""This file should have our melon-type classes in it."""

class Melon(object):
    def get_base_price(self):
        return 5.0

class WatermelonOrder(Melon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if qty >= 3:
            total = 0.75 * (qty * self.get_base_price())   # TODO, calculate the real amount!
        else:
            total = qty * self.get_base_price()   
        return float(total)

class CantaloupeOrder(Melon):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if qty >= 5:
            total = 0.5 * (qty * self.get_base_price())   # TODO, calculate the real amount!
        else:
            total = qty * self.get_base_price() 
        return float(total)

class CasabaOrder(Melon):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        
        total = 1.5 * (qty * (self.get_base_price() + 1))   # TODO, calculate the real amount!
        return float(total)

class SharlynOrder(Melon):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 1.5 * qty * self.get_base_price()   # TODO, calculate the real amount!
        return float(total)

class Santa_ClausOrder(Melon):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 1.5 * self.get_base_price() * qty   # TODO, calculate the real amount!
        return float(total)

class ChristmasOrder(Melon):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = qty * self.get_base_price()   # TODO, calculate the real amount!
        return float(total)

class Horned_MelonOrder(Melon):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 1.5 * qty * self.get_base_price()   # TODO, calculate the real amount!
        return float(total)

class XiguaOrder(Melon):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 1.5 * qty * self.get_base_price()   # TODO, calculate the real amount!
        return float(total)

class OgenOrder(Melon):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = qty * (self.get_base_price() + 1)   # TODO, calculate the real amount!
        return float(total)