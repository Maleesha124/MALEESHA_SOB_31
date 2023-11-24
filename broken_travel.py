# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year == int(input("Greetings! What is your year of origin? ")) #add a bracket after int and corrected the single quote to double quotes

if year <= 1900: #added a colon after the condition
    print ('Woah, that's the past!')
elif year > 1900 && year < 2020:
    print ("That's totally the present!")
elif:
    print ("Far out, that's the future!!")
