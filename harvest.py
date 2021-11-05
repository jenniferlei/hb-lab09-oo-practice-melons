############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

        return self.pairings


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.new_code = new_code

        return self.new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
        code="musk",
        first_harvest=1998,
        color="green",
        is_seedless=True,
        is_bestseller=True,
        name="Muskmelon",
    )

    casaba = MelonType(
        code="cas",
        first_harvest=2003,
        color="orange",
        is_seedless=False,
        is_bestseller=False,
        name="Casaba"
    )
    
    crenshaw = MelonType(
        code="cren",
        first_harvest=1996,
        color="green",
        is_seedless=False,
        is_bestseller=False,
        name="Crenshaw"
    )

    yellow_watermelon = MelonType(
        code="yw", 
        first_harvest=2013,
        color="yellow",
        is_seedless=False,
        is_bestseller=True,
        name="Yellow Watermelon"
    )

    musk.add_pairing("mint")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    crenshaw.add_pairing("prosciutto")
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types.extend([musk, casaba, crenshaw, yellow_watermelon])

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")

melon_types = make_melon_types()
# print_pairing_info(melon_types)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon
    
    return melon_dict

print(make_melon_type_lookup(melon_types))

# Create a function called make_melon_type_lookup that takes in a list of MelonType objects as an argument, 
# identical to what make_melon_types returns. 
# This function should return a dictionary whose keys are reporting codes (as strings) and whose values are 
# the appropriate melon type instance for that reporting code.


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
