import random # Importera modulen random för att generera slumpmässiga tal
dice_list = [] # Skapa en tom lista för tärningarna
points = int(0) # Skapa en variabel för poäng
time = 0 # Skapa en variabel för vems tur det är
turn_timer = 0 # Visar vilken tur det är

def dice(): # tärningen
    for i in range(amount_dice): #Starta en loop som ska upprepa ett visst antal gånger, bestämt av amount_dice.
        dice_throw = random.randint(1,6) # Slå en tärning och lagra resultatet i dice_throw
        dice_list.append(dice_throw) # Lägg till resultatet i listan dice_list

def dice_choice(): # Denna funktion tar användarens inmatning för att bestämma vilka tärningar som ska kastas om. Den tar bort de valda tärningarna från listan, kastar om dem och visar resultatet för användaren.
    global amount_dice
    while True:
        try:
            rerolling_dice = input("Which dice/dices would you like to throw again?: ")
        except ValueError:
            print("That is not one of your dice.")
        rerolling_dice_list = rerolling_dice.split() # Dela upp användarens inmatning i en lista av tärningsnummer. 
        if len(rerolling_dice_list) < 6:
            for i in range(len(rerolling_dice_list)):
                dice_value = int(rerolling_dice_list[i]) # Konvertera varje inmatat tärningsnummer till heltal.
                dice_list.remove(dice_value)
            break
        else:
            print("You have chosen more dices than you have.")
    amount_dice = len(rerolling_dice_list)
    dice()
    print("Your new dices are:", dice_list)
    return dice_list

def player_selection():
    global number_of_players
    global players
    players = {}
    global player_id
    player_id = {}
    time_for_player_selection = 0
    while True:
        try:
            number_of_players = int(input("How many players are there? (Choose between 2 and 4): "))
            if (number_of_players >= 2 and number_of_players <= 4):
                for _ in range(number_of_players):
                    time_for_player_selection += 1
                    player_tag = ("Player" + str(time_for_player_selection))
                    name = input("What is your name?: ")
                    players.update({name: points})
                    player_id.update({player_tag: name})
                break
            else:
                print("Amount of players are not between 2 and 4.")
        except ValueError:
            print("That is not an appropriate character.")

def turn():
    dice_list.clear()
    global amount_dice
    amount_dice = 5 # Ange antalet tärningar
    global time
    time += 1
    global turn_timer
    if time == 1:
        turn_timer += 1
    global current_player
    current_player = player_id.get("Player" + str(time))
    print("----------------------------------------Turn " + str(turn_timer) + "----" + current_player + "------------------------------------------------------")
    print(players)
    print(current_player + " you throw your dice and get these values:")
    dice()
    print(dice_list)
    while True:
        try:
            for i in range(3):
                if i < 2:
                    dice_choice_answer = input("If you want to throw some dice again press 1, if not press 2: ") # Användaren uppmanas att ange vilka tärningar de vill kasta om.
                    if dice_choice_answer == "1":
                        dice_choice()
                    elif dice_choice_answer == "2":
                        break
                else:
                    break
            break
        except ValueError:
            print("That is not one of the options.")
    point_protocol()

def point_protocol():
    print("----------------------------------------Points Protocol--------------------------------------------------")
    print("You have thrown your dice three times and the result is:", dice_list)
    print("You are able to chooce these options for your dices:")
    if 1 in dice_list:
        print("Option 1 is the total value of you ones.")
    if 2 in dice_list:
        print("Option 2 is the total value of you twos.")
    if 3 in dice_list:
        print("Option 3 is the total value of you threes.")
    if 4 in dice_list:
        print("Option 4 is the total value of you fours.")
    if 5 in dice_list:
        print("Option 5 is the total value of you fivess.")
    if 6 in dice_list:
        print("Option 6 is the total value of you sixes.")
    print("Option 7 is the total value of all your dices.")
    choice_of_pointsline = input("What is your prefered option?: ")
    if (choice_of_pointsline == "1" and 1 in dice_list):
        points_for_round = dice_list.count(1)
    elif (choice_of_pointsline == "2" and 2 in dice_list):
        points_for_round = 2*dice_list.count(2)
    elif (choice_of_pointsline == "3" and 3 in dice_list):
        points_for_round = 3*dice_list.count(3)
    elif (choice_of_pointsline == "4" and 4 in dice_list):
        points_for_round = 4*dice_list.count(4)
    elif (choice_of_pointsline == "5" and 5 in dice_list):
        points_for_round = 5*dice_list.count(5)
    elif (choice_of_pointsline == "6" and 6 in dice_list):
        points_for_round = 6*dice_list.count(6)
    elif choice_of_pointsline == "7":
        points_for_round = sum(dice_list)
    elif choice_of_pointsline == "8":
        print("Not done")

    players_previous_points = players.get(current_player)
    players_total_points = players_previous_points + points_for_round
    players.update({current_player: players_total_points})
    print(current_player + " you now have " + str(players_total_points) + " points.")

player_selection()

for i in range(3*number_of_players):
    turn()
    if time == number_of_players:
        time = 0

print(players)

print("End of test")