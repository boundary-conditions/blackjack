#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:33:26 2020

@author: keenan
"""
import random


class Cards:
    def __init__(self, decks = 1):
        self.decks = decks #how many decks to play with
        self.cards = '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',') * (self.decks * 4) #create deck
        self.hands = {} # each player key has a dictionary containing cards and score
        
    def shuffle(self, start_game = True): 
        self.start_game = start_game
        if start_game:
            random.shuffle(self.cards)
        else:
            self.cards = self.cards + '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',') * (self.decks * 4)
            random.shuffle(self.cards)
            
    def add_hand(self, hand, is_dealer=False): #has to go after each deal/hit
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
        return total
                
            
    def deal(self, total_players):
        self.total_players = total_players
        for player_number in range(total_players):
            new_hand = [self.cards[player_number], self.cards[player_number + total_players]]
            if player_number == 0:
                self.hands[player_number] = {"player cards": new_hand, 
                                             "score": self.add_hand(new_hand, is_dealer = True)}   
            else:
                self.hands[player_number] = {"player cards": new_hand, 
                                             "score": self.add_hand(new_hand)}
        self.cards = self.cards[total_players*2:]
        
    def hit(self, player_number):
        self.player_number = player_number
        self.hands[player_number]["player cards"] += [self.cards[0]] #adds card to hand
        self.cards = self.cards[1:] #deletes card from deck
        new_hand =  self.hands[player_number]["player cards"] #readable variable for function
        if player_number == 0:
            self.hands[player_number]['score'] = self.add_hand(new_hand, is_dealer = True)  
        else:
            self.hands[player_number]["score"] = self.add_hand(new_hand)
            

            #THIS WORKS
            
class Bank:
    def __init__(self, bank = 500):
        self.bank = bank #amount to initialize bank with
        self.ledger = {} # will contain player keys with balance values as integers
        
    def buy_in(self, player_number, amount):
        self.player_number = player_number
        self.amount = amount
        self.ledger[player_number] = {'balance': self.amount}
     
     
    def bet(self, player_number, amount, is_split = False):
        self.player_number = player_number
        self.amount = amount
        self.ledger[player_number]['balance'] -= self.amount
        if is_split:
            self.ledger[player_number]['split'] = self.amount
        else:
            self.ledger[player_number]['bet'] = self.amount
            
    def double_down(self, player_number):
        original_bet = self.ledger[player_number]['bet']
        self.ledger[player_number]['balance'] -= original_bet
        self.ledger[player_number]['bet'] *= 2
            

    
class Player:
    def __init__(self, cards_var, bank_var, player_name, player_number = 1):
        self.cards_var = cards_var
        self.bank_var = bank_var
        self.player_name = player_name
        self.player_number = player_number

    
    def display_hand(self):
        hand = self.cards_var.hands[self.player_number]["player cards"]
        score = self.cards_var.hands[self.player_number]["score"]
        if len(hand) == 2:
            print(f"{self.player_name} has {hand} for {score}")
        else:
            print(f"{self.player_name} has {hand} for {score}")
            
    
        

        
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
            print(f"{self.player_name} has {hand} for {score}")
        
        


