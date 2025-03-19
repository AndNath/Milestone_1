# Variables
int_userMoney = int(input("Enter how much money you want to have. (after this, program will start)"))
max_speed = 51
int_userSpeed = int(input("Do you know how fast you were going?"))

# The main program
if int_userSpeed < max_speed:
  print("Sorry for wasting your time.")
elif int_userSpeed > max_speed and int_userSpeed <= 60:
    print("Thats over the speed limit, im going to have to fine $30 you for that.\nAfter paying the ticket, you now have ${}".format(int_userMoney - 30))
elif int_userSpeed > max_ + 11 and int_userSpeed <= max_speed + 15:
    print("Thats over the speed limit, im going to have to fine $60 you for that.\nAfter paying the ticket, you now have ${}".format(int_userMoney - 60))
