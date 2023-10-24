def weekdays(day):
  if day == "Monday" or day =="Tuesday" or day =="Wednesday" or day=="Thursday" or day=="Friday":
    print("It is a weekday.")     #prints it is a weekday if any of the above are input
  elif day == "Saturday" or day == "Sunday":
    print("It's the weekend.")    #prints it is a weekend if any of the above are input
  else:
    print("Invalid day entered")