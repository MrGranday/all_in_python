def get_choice():
  player_choice = input("Enter your choice (rock, paper, scissors):")
  computer_choice = "paper"
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

get_choice1 = get_choice()
print(get_choice1)
