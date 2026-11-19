def dollars_to_float(d):
    return float(d.replace("$", ""))

def percent_to_float(p):
    return float(p.replace("%", "")) / 100
dollars = input("How much was the meal? ")
percent = input("What percentage would you like to tip? ")

tip = dollars_to_float(dollars) * percent_to_float(percent)
print(f"Leave ${tip:.2f}")