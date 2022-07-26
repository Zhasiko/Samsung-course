log = input("Insert login: ")
pas = input("Insert password: ")
users = {
  "user": "qwerty",
  "user2": "qwerty2",
  "user3": "qwerty3"
}

if users.get(log, "incorrect") == pas:
    print("OK")
else:
    print("Incorrect")
