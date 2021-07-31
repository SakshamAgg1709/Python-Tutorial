"""Problems Of ages"""
import time

instant = time.time()
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


year2 = int(input("Enter the year for which you want to know your age\n"))
print(your_age(year2))


instant2 = time.time()
print(instant2-instant)



"""Harry Bhai's Solution"""

yearAge = int(input("What is your Age/Year of birth\n"))
isAge = False
isYear = False

if len(str(yearAge)) == 4:
    isYear = True

else:
    isAge = True

if(yearAge<1900 and isYear):
    print("You seem to be the oldest person alive")
    exit()

if(yearAge>2019):
    print("You are not yet born")
    exit()

if isAge:
    yearAge = 2019 - yearAge

print(f"You will be 100 years old in {yearAge + 100}")

interestedYear = int(input("Enter the year you want to know your age in\n"))

print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")


