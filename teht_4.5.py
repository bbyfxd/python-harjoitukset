print('Enter correct username and password combo to continue')
count=0
while count < 5:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Rules' and username=='Python':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1