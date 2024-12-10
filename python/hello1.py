def Main ():
    name = input("What's your name : ").title().capitalize().split()
    hello(name)


def hello(to):
    print("hello,", to)



Main()
