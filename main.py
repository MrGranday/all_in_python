import random


def get_choice():
    the_choices_for_computer = ["rock", "paper", "scissors"]
    player_choice = input("Enter your choice (rock, paper, scissors):")
    computer_choice = random.choice(the_choices_for_computer)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win():
