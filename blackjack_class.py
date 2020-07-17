#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:33:26 2020

@author: keenan
"""
import random


class Cards:
    def __init__(self, decks = 1):
        
        self.decks = decks
        self.cards = '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',') * (self.decks * 4)
        #self.hands = {} can i make this work?
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, player_hand, new_card):
        self.player_hand = player_hand
        self.new_card = new_card
        player_hand.append(new_card)
        return player_hand
            
            

class Bank:
    def __init__(self, bank):
        self.bank = bank #amount to initialize bank with
        self.ledger = {}
    
class Player:
    def __init__(self, bank_var, cards_var, player_name  )
        


print("Let's play blackjack!")



deck = Cards()

charles_hand = []
deck.deal(charles_hand, deck.cards.pop())
print(charles_hand)
dealer_hand = []
deck.deal(dealer_hand, deck.cards.pop())
print(dealer_hand)
deck.deal(charles_hand, deck.cards.pop())
deck.deal(dealer_hand, deck.cards.pop())
print(charles_hand)
print(dealer_hand)


        


