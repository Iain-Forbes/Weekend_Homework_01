# WRITE YOUR FUNCTIONS HERE

# Returns Name of Pet Shop
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# Returns Total Cash 
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# Add or Remove cash
def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

