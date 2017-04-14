"""Classes for melon orders."""

import random

import datetime
import time

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        def get_base_price():
            """Uses random integer to get base price"""
            base_price = random.randint(5, 9)

            print base_price

            i = datetime.datetime.now()
            today = datetime.date.today()
            day_of_week = datetime.date.weekday(today)
            hour_now = i.hour

            if day_of_week in range(0, 5) and hour_now in range(8, 12):
                base_price += 4

            print today
            print day_of_week
            print hour_now

            return base_price

        base_price = get_base_price()

        if self.species == "christmas melon":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Adds international fee to the total"""
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3

        return total

class GovernmentMelonOrder(AbstractMelonOrder):
    """US Government melon orders."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(GovernmentMelonOrder, self).__init__(species, qty, "domestic", 0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Record the fact that the melon has passed inspection."""

        self.passed_inspection = passed