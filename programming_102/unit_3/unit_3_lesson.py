convertables = {"feet", "miles", "meters", "kilometers", "inches", "yards"}

for convertable in convertables:  
    print(convertable)

user_input_unit = input("What is specified unit of distance")
user_input_distance = int(input("What is the distance to convert?"))

convertable_feet =  {user_input_distance: [(user_input_distance * 0.3048)]}
convertable_miles = {user_input_distance: [(user_input_distance * 1609.34)]}
convertable_meters = {user_input_distance: [(user_input_distance)]}
convertable_kilos = {user_input_distance: [(user_input_distance * 1000)]}
convertable_yards = {user_input_distance: [(user_input_distance * 0.9144)]}
convertable_inches = {user_input_distance: [(user_input_distance * 0.0254)]} 

convfefe = str(convertable_feet[user_input_distance])[1:-1]
convmimi = str(convertable_miles[user_input_distance])[1:-1]
convmeme = str(convertable_meters[user_input_distance])[1:-1]
convkiki = str(convertable_kilos[user_input_distance])[1:-1]
convyaya = str(convertable_yards[user_input_distance])[1:-1]
convinin = str((convertable_inches[user_input_distance])[1:-1])

if user_input_unit == "feet":
    print(f"{user_input_distance} feet is {convfefe} meters.")
elif user_input_unit == "miles":
    print(f"{user_input_distance} miles is {convmimi} meters.")
elif user_input_unit == "meters":
    print(f"{user_input_distance} meters is {convmeme} meters.")
elif user_input_unit == "kilometers":
    print(f"{user_input_distance} kilometers is {convkiki} meters.")
elif user_input_unit == "yards":
    print(f"{user_input_distance} kilometers is {convyaya} meters.")
elif user_input_unit == "inches":
    print(f"{user_input_distance} kilometers is {convinin} meters.")