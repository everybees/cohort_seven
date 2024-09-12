import tea_bot
import calculator

if _name_ == "__main__":
    while True:
        prompt = int(input("Press 1 or 2: "))
        if prompt == 1:
            tea_bot.do_something()
        else:
            print("enter 1")
