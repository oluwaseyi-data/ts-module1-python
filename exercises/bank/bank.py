greetings = input("Greetings: ").lower().strip()
if greetings.lower() == "hello":
    print("$0")
elif greetings.lower().startswith("h"):
    print("$20")
else:
    print("$100")