"""Problems Of ages"""

age_year = input("Enter you age and the year of birth: Separating \"-\" ; Like-> 21-2000\n")
age = int(age_year.split("-")[0])
year = int(age_year.split("-")[1])

def century(year):
    new_year = year + 100
    return f"In {new_year}, You will be 100 years old "
if age <= 1:
        print("You are too small to use this programm😝")

elif age >= 100:
        print("You seem to be the oldest one alive😝")

elif year >= 2020:
        print("You do not seem to be born yet😝")

elif year <= 1921:
        print("You seem to be the oldest one alive😝")

elif 1<age<100 and 1921<year<2020:
    print(century(year))

def your_age(y):
    y2 = y - year
    if y2 <= 0:
        print("Enter correct year")
    else:
        return f"In {y} , Your age will be {y2}"

print("Wanna play another trivia : Type Y for Yes or N for No\n")
y_n = input()
y_n2 = y_n.capitalize()


if y_n2 == "Y" :
        year2 = int(input("Enter the year for which you want to know your age\n"))
        print(your_age(year2))

elif y_n2 == "N":
        print("Thanks for cooperation")

else:
    print("Enter correct answer: Y for Yes or N for No ")



