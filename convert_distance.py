# todo: miles = convert(km)
# formula: mile = 1.6 * km


def convert_miles_to_km(miles):  # the starting of a function
    km = miles * 1.6  # <--- this is a formula.
    print("mile:")
    print(miles)
    print("km:")
    # <--- this is to finish and execute the function, if I leave this line empty or don't write anything, it will show "none" when I run the code.
    return km


# <--- in this line you input a distance(mile).
my_input = convert_miles_to_km(212)
print("The distance:  ")
# <--- in this line the output is converted to km of the written mile distance.
print(my_input)
