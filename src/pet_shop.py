# WRITE YOUR FUNCTIONS HERE

# Returns Name of Pet Shop
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# Returns Total Cash 
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# Add cash/remove cash
def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

# Pets sold
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# Increase Pets Sold
def increase_pets_sold(pet_shop, pet_num_sold):
    pet_shop["admin"]["pets_sold"] += pet_num_sold

# List Stock
def get_stock_count(pet_shop):
  return len(pet_shop["pets"])


