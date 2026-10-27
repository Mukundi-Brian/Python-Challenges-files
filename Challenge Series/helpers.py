# helpers.py
# Phase 2 practice series: Modules

def body_mass_index(weight_kg, height_m):
    """A function that calculates BMI based on Weight in Kg and Height in Meters"""
    height_m /= 100
    bmi = round(weight_kg/height_m ** 2, 2)
    return bmi

def convert_temp(temp_in_fahrenheit):
    """A function that converts temp from fahrenheit to celsius"""
    temp_in_celsius = round((temp_in_fahrenheit - 32) * 5/9, 2)
    return f"{temp_in_celsius}°C"

if __name__ == "__main__":    
    my_bmi = body_mass_index(60, 170)
    print(f"Your BMI is: {my_bmi}")
    print(f"The temp im celsius is: {convert_temp(100)}")
    print("Running helpers directly!")

else:
    print("Running practice.py")
