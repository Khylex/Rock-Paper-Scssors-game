from random import choice
while True:
    # take input from the user
  player_select = input("Choose a Letter  'R', 'P' or 'S': ")

    # getplayer_select from computer
  choices = ['R', 'P', 'S', ]
  comp_choice = str(choice(choices))

    # check if player_select is one of the four options
  if player_select in ('R', 'P', 'S'):
    if (player_select == 'R' and comp_choice == 'S') or (player_select == 'S' and comp_choice == 'P') or (player_select == 'P' and comp_choice == 'R'):
        print("You Win !!! " + " Player " + (player_select) +
                  " and CPU " + comp_choice)
        break
    elif player_select == comp_choice:
        print("It's a Draw !!! " + " Player " + player_select +
                  " and  CPU " + comp_choice)
    else:
        print("You Lose !!! " + " Player " + player_select +
                  " and  CPU " + comp_choice)
  else:
        print("Invalid Input")
