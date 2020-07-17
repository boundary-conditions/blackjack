#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:33:26 2020

@author: keenan
"""
import random


class Deck:
    def __init__(self, decks = 1):
        
        self.decks = decks
        self.cards = '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',') * (self.decks * 4)
        #self.cards
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, card = []):
        self.card = card
        try:
            popped = self.cards.pop()
            self.card = popped
            return self.card
        except:
            pass

class Player:
    def __init__(self, name, is_dealer = False, cards = ['','','','','','']):
        self.name = name
        self.cards = cards
        self.is_dealer = is_dealer
        
    def move(self, choice):
        #self.move = choice
        pass
    
    def display_hand(self, is_down = True):
        self.is_down = is_down
        if self.is_dealer and self.is_down:
            return self.cards[0]
        else:
            return self.cards
deal_card = []
        
deck = Deck()
charles = Player('Charles')
dealer = Player('Dealer',is_dealer = True)

deal_card = deck.cards.pop()
print(deal_card)
charles.cards[0] = deal_card
print(deal_card)
print(charles.cards)
deal_card = deck.cards.pop()
print(deal_card)
dealer.cards[0] = deal_card
print(charles.cards)
print(deal_card)
deal_card = deck.cards.pop()
print(deal_card)
charles.cards[1] = deal_card
print(deal_card)
print(charles.cards)
deal_card = deck.cards.pop()
print(deal_card)
dealer.cards[1] = deal_card
print(deal_card)


        


