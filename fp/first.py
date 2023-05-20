def main():
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(to = "KAZAHSTAN"):
    print("SALAM,", to)

main()