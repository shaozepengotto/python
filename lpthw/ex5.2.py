name = 'shaozepeng'
age = 27 # not a lie
height =65 # inches
weight = 165 # lbs
centimeters = height * 2.54  # cm
kilograms = weight * 0.45359237 # kg
eyes = 'black'
teeth = 'White'
hair = 'black'

print(f"Let's talk about {name}.")
print(f"He's {centimeters} cm tall.")
print(f"He's {kilograms} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")