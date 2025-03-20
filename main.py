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
    print("Thats over the speed limit, im going to have to fine $80 you for that.\nAfter paying the ticket, you now have ${}".format(int_userMoney - 80))
elif int_userSpeed > max_ + 15 and int_userSpeed <= max_speed + 20:
    print("Thats pretty high over the speed limit, im going to have to fine $120 you for that.\nAfter paying the ticket, you now have ${}".format(int_userMoney - 120))
elif int_userSpeed > max_ + 20 and int_userSpeed <= max_speed + 25:
    print("Thats pretty high over the speed limit, im going to have to fine $170 you for that.\nAfter paying the ticket, you now have ${}".format(int_userMoney - 170))
elif int_userSpeed > max_ + 25 and int_userSpeed <= max_speed + 30:
    print("Thats high over the speed limit, im going to have to fine $220 you for that.\nAfter paying the ticket, you now have ${}".format(int_userMoney - 220))
elif int_userSpeed > max_ + 30 and int_userSpeed <= max_speed + 39:
    print("Thats high over the speed limit, im going to have to fine $350 you for that.\nAfter paying the ticket, you now have ${}".format(int_userMoney - 350))
elif int_userSpeed > max_ + 39 and int_userSpeed <= max_speed + 49:
    print("Thats very high over the speed limit, im going to have to fine $450 and take your licence for 28 days.\nAfter paying the ticket, you now have ${} and lost your licence for 28 days".format(int_userMoney - 450))
else:
    print("Thats extremely high over the speed limit, im going to have to fine $630 and take your licence for 60 days.\nAfter paying the ticket, you now have ${} and lost your licence for 60 days".format(int_userMoney - 630))
