command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car is already started")
        else:
            started = True
            print("Car started ... ")
    elif command == "stop":
        if not started:
            print("Car is already stopped!!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
        type the following:
        start - to start the car
        stop - to stop the car
        quit - to quit the car
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand this...")
