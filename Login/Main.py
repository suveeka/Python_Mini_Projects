import DatabaseQueries

tries = 0

while tries < 3:
 uname = input("Username: ")
 passwd = input("Password: ")
 rpass = DatabaseQueries.users.get(uname)
 if rpass == None:
     print("You are not a registered user")
     tries += 1
 elif passwd == rpass:
     print("Welcome {} you are logged in!".format(uname))
     break
 else:
     print("You entered the wrong password")
     tries += 1
else:
 print("Your Tries are Exhausted")