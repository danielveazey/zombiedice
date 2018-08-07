#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint, shuffle

class Die(object):
    def __init__(self, color, sides):
        self.color = color
        self.sides = sides
    def roll(self):
        return self.sides[randint(0,5)]

class Player(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def take_turn(self):
        print()
        print(self.name + "'s turn")
        self.temp_score = {'brains': 0, 'shotgun blast': 0}
        self.my_dice = make_dice()
        self.rolled_dice = []
        the_decision = 'y'
        while self.temp_score['shotgun blast'] < 3 and the_decision == 'y' and len(self.my_dice) > 0:
            self.rolled_dice = self.choose_dice(self.rolled_dice)
            quick_results = self.roll_the_dice(self.rolled_dice)
            quick_results, self.rolled_dice = self.separate_the_dice(quick_results, self.rolled_dice)
            if self.temp_score['shotgun blast'] >= 3:
                print("Too many shotgun blasts!")
                self.temp_score['brains'] = 0
                break
            the_decision = self.make_decision()
        self.score += self.temp_score['brains']

    def choose_dice(self, dice_in_hand):
        while len(dice_in_hand) < 3:
            dice_in_hand.append(self.my_dice.pop())
        return dice_in_hand

    def roll_the_dice(self, dice_in_hand):
        roll_results = []
        basic_results = []
        for each_die in dice_in_hand:
            basic_results.append(each_die.roll())
            roll_results.append(each_die.color + ' ' + basic_results[-1])
        print(roll_results)
        return basic_results

    def separate_the_dice(self, dice_in_hand, dice_objects):
        for i in range(2, -1, -1):
            if dice_in_hand[i] != "runner":
                self.temp_score[dice_in_hand[i]] += 1
                dice_in_hand.pop(i)
                dice_objects.pop(i)
        return dice_in_hand, dice_objects

    def make_decision(self):
        decide = ''
        print(self.temp_score)
        while decide != 'y' and decide != 'n':
            decide = input('Keep rolling (y/n)? ')
        return decide

def make_dice():
    red = Die('Red', ['shotgun blast', 'shotgun blast', 'shotgun blast', 'runner', 'runner', 'brains'])
    yellow = Die('Yellow', ['shotgun blast', 'shotgun blast', 'runner', 'runner', 'brains', 'brains'])
    green = Die('Green', ['shotgun blast', 'runner', 'runner', 'brains', 'brains', 'brains'])
    made_dice = [red, red, red, yellow, yellow, yellow, yellow, green, green, green, green, green, green]
    shuffle(made_dice)
    return made_dice

def game_round(turn_takers):
    for each_player in turn_takers:
        each_player.take_turn()
    print()
    print("That's the end of the round.")
    display_score(turn_takers)
    return turn_takers

def make_players():
    total_players = int(input("How many players? "))
    players = []
    for i in range(1, total_players+1):
        pname = input("Player %s name: " %i)
        this_player = Player(pname, 0)
        players.append(this_player)
    shuffle(players)
    print()
    print("Random order of play:")
    for i in range(len(players)):
        print(i+1, ':', players[i].name)
    print()
    return players

def display_score(scorers):
    print("The score is:")
    for i in range(len(scorers)):
        print(scorers[i].name, scorers[i].score)
    print()

def main():
    players = make_players()
    game_over = False
    while game_over == False:
        game_round(players)
        for each_player in players:
            if each_player.score >= 13:
                game_over = True
    print("Game over. Final score:")
    for each_player in players:
        print(each_player.name, each_player.score)
    return 0

if __name__ == '__main__':
	main()
