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


print("Welcome to the pysino! Let's play some Blackjack!")
print("=================================================")
number_of_players = input("How many players are there today? (1-3): ")
while True:
    if number_of_players in '123':
        number_of_players = int(number_of_players)
        break
    else:
        number_of_players = input("How many players are there today? (1-3): ")

        
if number_of_players > 0:
    player_one = input("Enter player one's name: ")
    if number_of_players > 1:
        player_two = input("Enter player two's name: ")
        if number_of_players > 2:
            player_three = input("Enter player three's name: ")

    