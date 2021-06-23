# Birth Year Calculator

- The goal of this task is to produce a calculator that effectively takes in a persons age, checks it to make sure it's valid. Then display it along with a message including the persons name.

- This was Achieved by having the user input an age then use a `While loop` and `if statement` to validate.

```python
while True:
    age = input("What is your age?")
    if age.isdigit() == True and int(age) > 0 and int(age) < 150:
        break
    print("enter valid birth year please")
```
- User then inputted there name, and the message was formatted as well as printed to the console.

```python
name = input("What is your name?")
birth_year = 2021 - int(age);
print("OMG {}, you are {} years old so you were born in {}.".format(name.capitalize(), age, birth_year))
```



## Extra

- This one line, tells the user how long they have been alive for in hours

```python
print("You have been alive for {} hours".format(int(age) * 8760))
```
## Extra ++

- This uses the time module in python to calculate how old the user is. User types in there birth year so that there age can be calulated.
```
from datetime import date

birth_year = input("what year were you born?")
today = date.today()
gap = today.year - birth_year

print("Using the Time Module,  you are {}".format(gap))
```