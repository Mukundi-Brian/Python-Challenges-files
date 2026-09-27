# This code converts units from one unit to another infinitely until terminated

# 1. Converting degrees to radians
# 1 degree to radian multiply by pi/180
# 1 radian to degree multiply by 180/pi

# 2. Converting square meters to hectares
# 1 hectares = 10,000 square meters and vice versa

# 3. Converting hectares to acres
# 1 hectares = 2.471 acres and vice versa


from math import pi # Importing pi from math
mistake_count = 0 # Let's add a mistake counter incase the user decides to spam wrong inputs

while True: # The code will ask the question until quit is pressed
    user_choice = input("""Which converter would you like to use?: (A, B, C, D, E, F or Q)
        A: Radians - Degrees
        B: Degrees - Radians
        C: Square Meters - Hectares
        D: Hectares - Square Meters
        E: Acres - Hectares
        F: Hectares - Acres
        Q: Quit
        """).upper()

    # Lets make sure the quit function works first
    if user_choice == "Q":
          print("Exiting Program, have a wonderful day!\n")
          break

    # Lets check for values other than the choices given
    if user_choice not in ("A", "B", "C", "D", "E", "F"):

        mistake_count += 1 # Increase the counter whenever a wrong choice is chosen

        if mistake_count > 4:
            print("Please try again some other time. Good Day!\n")
            break
        else:
            print("That's not a valid response!, Try again.\n")
          
        continue
    
    # Lets check for user value error
    try:
          user_value = float(input("Enter the value you wish to convert: "))
    except ValueError:
          print("That's not a valid response!, Try again.\n")
          continue
    
    # A: Converting from degrees to radians
    if user_choice == "A":
        degrees_to_radians = user_value * pi/180
        print(f"Your value in radians is: {degrees_to_radians}\n")

    # B: Converting from radians to degrees
    elif user_choice == "B":
        radians_to_degrees = user_value * 180/pi
        print(f"Your value in degrees is: {radians_to_degrees}\n")

    # C: Converting from square meters to hectares
    elif user_choice == "C":
        square_meters_to_hectares = user_value / 10000
        print(f"Your value in Hectares is: {square_meters_to_hectares}\n")

    # D: Converting from hectares to square meters
    elif user_choice == "D":
        hectares_to_square_meters = user_value * 10000
        print(f"Your value in Square Meters is: {hectares_to_square_meters}\n")

    # E: Converting from Acres to hectares
    elif user_choice == "E":
        acres_to_hectares = user_value / 2.471
        print(f"Your value in Hectares is: {acres_to_hectares}\n")
    
    # F:Converting from hectares to Acres
    elif user_choice == "F":
        hectares_to_acres = user_value * 2.471
        print(f"Your value in Acres is: {hectares_to_acres}\n")
        
