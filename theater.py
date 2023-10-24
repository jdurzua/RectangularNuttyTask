def theater(age):
  if age <5:               # prints FREE if age value is less than 5
    print("FREE!!")  
  elif 5 <= age <= 12:         # prints total cost when age is 5 to 12
    print("Total cost is $8")
  elif 13 <= age <= 59:       #prints total cost when age is 13 to 59
    print("Total cost is $12")   
  elif age >=60:
    print("Total cost is $10")  #prints total cost when age is 60 and older
  else:
    print("No prices available")  #prints error if input is invalid
    