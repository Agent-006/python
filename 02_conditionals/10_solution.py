species = "Cat"
pet_age = 6
pet_food = None

if (species == "Dog" and pet_age < 2):
    pet_food = "Puppy food"
elif (species == "Cat" and pet_age > 5):
    pet_food = "Senior cat food"
else: 
    pet_food = "regular pet food"

print("AI recommended food for your pet:", pet_food)