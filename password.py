password = ('1234')
myVar = input("Enter password")
count = 5
for items in myVar:
    if password == myVar:
        print('Good Job!')
        break
    else:
        print('Try again')
        count -= 5
