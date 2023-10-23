# Q1: Sort the word in alphabetical order

sentence = "this is a python program"
tests = sentence.split()
sorted_tests = sorted(tests)

for word in sorted_tests:
    print(word)


#Q2:  Check weather an year is leap year or not:

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):git
        return True
    else:
        return False

year =int(input("Check year leap or not:"))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#Q3: Check if string is a number or float:

number1 = input("Enter a word or a number:")
def float_check(number1):
    try:
        float(number1)
        return True
    except:
        return False
print(float_check(number1))