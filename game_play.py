#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 12:41:12 2020

@author: keenan
"""
"""
Some things id like to add to this game are:
*Betting system needed*
1. the ability to choose to have the deck cut or not
2. opening bets, natural blackjack notice on first add_hand, 1.5 payout
3. hit players one at a time until stand/bust/blackjack
4. dealer plays by revealing second card, then hitting one at a time until >=17 or bust
5. split pairs, players cards are divided and played individually, 1x payout for blackjack
6. doubling down when first two cards equal 9 10 or 11, one more card is dealt face down and settled at end of round
7.
"""
import blackjackmodule

bank = blackjackmodule.Bank()

print("Welcome to the pysino! Let's play some Blackjack!")
print("=================================================")


number_of_players = input("How many players are there today? (1-3): ")
while True:
    if number_of_players in '123' and len(number_of_players) == 1:
        number_of_players = int(number_of_players)
        break
    else:
        number_of_players = input("How many players are there today? (1-3): ")

#initialize cards
number_of_decks = input("How many decks should we play with? (1-4): ")
while True:
    if number_of_decks in '1234' and len(number_of_decks) == 1:
        number_of_decks = int(number_of_decks)
        break
    else:
        number_of_decks = input("How many decks should we play with? (1-4): ")
cards = blackjackmodule.Cards(decks = number_of_decks)


player_list = []        
if number_of_players > 0:
    player_one = input("Enter player one's name: ")
    player_one = blackjackmodule.Player(cards, bank, player_one, player_number = 1)
    bank.buy_in(1, 100)
    player_list.append(player_one)
    if number_of_players > 1:
        player_two = input("Enter player two's name: ")
        player_two = blackjackmodule.Player(cards, bank, player_two, player_number = 2)
        bank.buy_in(2, 100)
        player_list.append(player_two)
        if number_of_players > 2:
            player_three = input("Enter player three's name: ")
            player_three = blackjackmodule.Player(cards, bank, player_three, player_number = 3)
            bank.buy_in(3,100)
            player_list.append(player_three)
            
cards.shuffle()

for player in player_list:
    while True:
        amount = input("Place a $ bet. (2, 5, 10 or 20): ")
        if amount in ['2', '5', '10', '20']:
            amount = int(amount)
            bank.bet(player.player_number, amount)
            break




cards.deal(number_of_players +1)
            
            

            



    