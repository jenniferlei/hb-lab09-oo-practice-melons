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

        self.code = new_code

        return self.code


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

# print(make_melon_type_lookup(melon_types))

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
    def __init__(self, melon_type, shape_rating, color_rating, harvest_field, harvester):
        """Initialize a melon."""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvester = harvester
    
    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvest_field != 3:
            return True
        return False


# All melons should be able to be categorized as sellable or not sellable. 
# This logic might change over time. 
# Currently, a melon is able to be sold if both its shape and color ratings are greater than 5, 
# and it didn’t come from field 3, which was found to have poisonous fertilizer planted by a competing melon farm.

# my_melon = Melon('yw', 7, 10, 4, 'Sheila')
# print(my_melon.is_sellable())


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)

    melon1 = Melon(
        melon_type=melons_by_id['yw'], 
        shape_rating=8, 
        color_rating=7, 
        harvest_field=2, 
        harvester='Sheila'
    )

    melon2 = Melon(
        melon_type=melons_by_id['yw'], 
        shape_rating=3, 
        color_rating=4, 
        harvest_field=2, 
        harvester='Sheila'
    )

    melon3 = Melon(
        melon_type=melons_by_id['yw'], 
        shape_rating=9, 
        color_rating=8, 
        harvest_field=3, 
        harvester='Sheila'
    )

    melon4 = Melon(
        melon_type=melons_by_id['cas'], 
        shape_rating=10, 
        color_rating=6, 
        harvest_field=35, 
        harvester='Sheila'
    )

    melon5 = Melon(
        melon_type=melons_by_id['cren'], 
        shape_rating=8, 
        color_rating=9, 
        harvest_field=35, 
        harvester='Michael'
    )

    melon6 = Melon(
        melon_type=melons_by_id['cren'], 
        shape_rating=8, 
        color_rating=2, 
        harvest_field=35, 
        harvester='Michael'
    )

    melon7 = Melon(
        melon_type=melons_by_id['cren'], 
        shape_rating=2, 
        color_rating=3, 
        harvest_field=4, 
        harvester='Michael'
    )
    melon8 = Melon(
        melon_type=melons_by_id['musk'], 
        shape_rating=6, 
        color_rating=7, 
        harvest_field=4, 
        harvester='Michael'
    )

    melon9 = Melon(
        melon_type=melons_by_id['yw'], 
        shape_rating=7, 
        color_rating=10, 
        harvest_field=3, 
        harvester='Sheila'
    )

    all_melons = [melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9]

    return all_melons

# melon_types = make_melon_types()
# print(make_melons(melon_types))

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # def print_pairing_info(melon_types):
    # """Prints information about each melon type's pairings."""

    # for melon in melon_types:
    #     print(f"{melon.name} pairs with")
    #     for pairing in melon.pairings:
    #         print(f"- {pairing}")
    for melon in melons:
        if melon.is_sellable():
            print(f"Harvested by {melon.harvester} from field {melon.harvest_field} (CAN BE SOLD)")

        else:
            print(f"Harvested by {melon.harvester} from field {melon.harvest_field} (NOT SELLABLE)")

melon_types = make_melon_types()
melons = make_melons(melon_types)
get_sellability_report(melons)

# melon_type, shape_rating, color_rating, harvest_field, harvester

# Harvested by Sheila from Field 2 (CAN BE SOLD)
# Harvested by Sheila from Field 2 (NOT SELLABLE)
# Harvested by Sheila from Field 3 (NOT SELLABLE)
# Harvested by Sheila from Field 35 (CAN BE SOLD)
# Harvested by Michael from Field 35 (CAN BE SOLD)
# Harvested by Michael from Field 35 (NOT SELLABLE)
# Harvested by Michael from Field 4 (NOT SELLABLE)
# Harvested by Michael from Field 4 (CAN BE SOLD)
# Harvested by Michael from Field 3 (NOT SELLABLE)

