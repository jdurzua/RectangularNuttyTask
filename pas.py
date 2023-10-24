def pas(password):
  len_password = int(len(password))
  if len_password < 6:
    print("password is too short")
  else:
    print('password length is good')

  if password.isnumeric():
    print('password should contain letters')
  elif password.isalpha():
    print('password should contain numbers')
