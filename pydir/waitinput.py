print('''This programs demonstrates an waiting input''')

while(True):
    inputstr = input('Please input your message, quit with quit() :')
    if (inputstr != "quit()"):
        print(inputstr)
    else:
        break
