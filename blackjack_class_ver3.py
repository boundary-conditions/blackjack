#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:33:26 2020

@author: keenan
"""
import random


class Cards:
    def __init__(self, bank = 500, decks = 1):
        self.bank = bank #amount to initialize bank with
        self.decks = decks #how many decks to play with
        self.cards = '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',') * (self.decks * 4) #create deck
        self.hands = {} #will contain player keys with hands values as tuples
        self.ledger = {} # will contain player keys with balance values as integers
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, tot_players):
        self.tot_players = tot_players
        for player in range(tot_players):
            new_hand = [self.cards[player], self.cards[player + tot_players]]
            self.hands[player] = {"player cards": new_hand, "score": 0}
        self.cards = self.cards[tot_players*2:]
        
    def hit(self, player):
        self.player = player
        self.hands[player]["player cards"] += [self.cards[0]]
        self.cards = self.cards[1:]
        #self.hands[player][2] = self.hands[player][2]
            
            #take the number of players including dealer, multiply by two, then set that number as a range
            #then iterate over the range taking 
            
            #THIS WORKS
            

    
class Player:
    def __init__(self, cards_var, player_name, player_number = 1, buy_in = 100):
        self.cards_var = cards_var
        self.player_name = player_name
        self.player_number = player_number
    
    def display_hand(self):
        hand = self.cards_var.hands[self.player_number]["player cards"]
        score = self.cards_var.hands[self.player_number]["score"]
        if len(hand) == 2:
            print(f"{self.player_name} has {hand} for {add_hand(hand, score)}")
        else:
            print(f"{self.player_name} has {hand}")
        

        
class Dealer:
    def __init__(self, cards_var, player_name = "Dealer", player_number = 0):
        self.cards_var = cards_var
        self.player_name = player_name
        self.player_number = player_number
    
    def display_hand(self, hole = True):
        self.hole = hole
        hand = self.cards_var.hands[self.player_number]["player cards"]
        score = self.cards_var.hands[self.player_number]["score"]
        if self.hole:
            print(f"{self.player_name} has {hand[0]} with a card in the hole.")
        else:
            print(f"{self.player_name} has {hand} for {add_hand(hand, score, is_dealer = True)}")
        
def add_hit(hand):
    pass
    
     
        
    
    
def add_hand(hand, score, is_dealer=False): #has to go after each deal/hit
    total = 0
    if is_dealer:
        aces = 0
        for i in hand:
            if i in "JQK":
                i = 10
                total += i
            elif i in "23456789":
                total += int(i)
            else:
                aces += 1
        if aces == 1 and total < 11:
            total += 11
        elif aces == 1 and total >= 11:
            total += 1
        elif aces == 2:
            total += 12
    else:
        for i in hand:
            if i == 'A':
                print(f"Player has {hand}...")
                ace = input("Ace high? y/n: ").strip().lower()
                if ace == 'y':
                    i = '11'
                else:
                    i = '1'
            try:
                total += int(i)
            except:
                total += 10
    if total < 21:
        score = [total]
        return total
    elif total == 21:
        score = [total]
        return "{total} Blackjack!"
    else:
        score = [total]
        return f"{total}, Bust!"
    
        


print("Let's play blackjack!")



deck = Cards()
deck.shuffle()
charles = Player(deck, 'Charles')
colleen = Player(deck, 'Colleen', 2)
dealer = Dealer(deck)
deck.deal(3)
charles.display_hand()
colleen.display_hand()
dealer.display_hand()


