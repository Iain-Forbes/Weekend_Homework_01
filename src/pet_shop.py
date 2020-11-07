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

# Get Pet by Breed
def get_pets_by_breed(pet_shop, breed):
    found_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_pets.append(pet)
    
    return found_pets

# Find Pet by Name 
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

# Remove Pet by Name
def remove_pet_by_name(pet_shop, name):
    pet_delete = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet_delete)

# Add a Pet to Stock
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append("pets")

# Returns Total Cash 
def get_customer_cash(customers):
    return customers["cash"]

# Remove Customer Cash
def remove_customer_cash(customers, amount):
    customers["cash"] -= amount

# Return Customer Pets

def get_customer_pet_count(customers):
    return len(customers["pets"])

# Add a Pet to Customer

def add_pet_to_customer(customers, pets):
    return customers["pets"].append("pets")

# Can Customer Afford Pet

def  customer_can_afford_pet(customers, pet_shop):
    return customers["cash"] >= pet_shop["price"]