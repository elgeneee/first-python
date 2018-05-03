var = str(input("Hi what's your name?"))
print("Hi {}!".format(var))


def test():
    try:
        var2 = int(input("How old are you?"))
        if var2 > 30:
            return("you should get a job")
        else:
            return("you should finish your study")
    except ValueError:
        return("This is not a number")
    else:
        return("Hi {}, so your age is {}. Confirm?".format(var, var2))

test()
23
