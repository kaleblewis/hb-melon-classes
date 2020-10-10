"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
        
    shipped = False

    def __init__(self, species, qty , country_code = "US"):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code  #"US" #FIXME:
        #self.shipped = False


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "government":#govt order
            return total

        elif self.country_code != "US" and self.qty < 10 and self.species == 'Christmas':
            return (total + 3) * 1.5
        
        elif self.country_code != "US" and self.qty < 10:
            return total + 3
        
        elif self.species == 'Christmas':
            return total * 1.5
            
        else:   
            return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order from the government."""
    order_type = "government"
    passed_inspection = False
    tax = 0.00

    def mark_inspection_passed(self, passed):
        self.passed_inspection = passed

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, country_code)


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
