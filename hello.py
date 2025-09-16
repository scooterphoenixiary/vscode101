from datetime import date

def say_hello(name):
    print("Hello, " + name)

say_hello("vs code")
def say_day_of_week(day):
    print("Today is " + str(day) + ", " + str(day.strftime("%A")))

say_day_of_week(date.today())