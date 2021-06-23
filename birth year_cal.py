from datetime import date

# First Part
age = "age"
name = "James bond"


# Second Part
while True:
    age = input("What is your age?")
    if age.isdigit() == True and int(age) > 0 and int(age) < 150:
        break
    print("enter valid birth year please")
name = input("What is your name?")
birth_year = 2021 - int(age);
print("OMG {}, you are {} years old so you were born in {}.".format(name.capitalize(), age, birth_year))


# Extra
print("You have been alive for {} hours".format(int(age) * 8760))


# Extra ++

today = date.today()
gap = today.year - birth_year

print("Using the Time Module,  you are {}".format(gap))