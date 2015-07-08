"""This file should have our melon-type classes in it."""

# from data.py import melons

class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if qty >= 3:
            total = 0.75 * (qty * 5.0)   # TODO, calculate the real amount!
        else:
            total = qty * 5    
        return float(total)

class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if qty >= 5:
            total = 0.5 * (qty * 5)   # TODO, calculate the real amount!
        else:
            total = qty * 5 
        return float(total)

class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        
        total = 1.5 * (qty * 6)   # TODO, calculate the real amount!
        return float(total)

class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 1.5 * qty * 5   # TODO, calculate the real amount!
        return float(total)

class Santa_ClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 1.5 * 5 * qty   # TODO, calculate the real amount!
        return float(total)

class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = qty * 5   # TODO, calculate the real amount!
        return float(total)

class Horned_MelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 1.5 * qty * 5   # TODO, calculate the real amount!
        return float(total)

class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 1.5 * qty * 5   # TODO, calculate the real amount!
        return float(total)

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = qty * 6   # TODO, calculate the real amount!
        return float(total)