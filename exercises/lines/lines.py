filename = input("What is the filename? ")
with open(filename) as file:
    lines = file.readlines()
    count = 0
    for line in lines:
        if line.strip() and not line.startswith("#"):
            count += 1
print(count)