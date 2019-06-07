#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 21:33:14 2019

@author: HaYeonOh
"""
import random
import sys
#Assignment 1 rock paper scissor game 
def PlayGame():
    print("Welcome to rock-paper-scissors !")
    #Create an empty game record:
    List1 = []
    List2 = []
    List3 = []
    
    GameRecord = [[List1],[List2],[List3]]
    
    Human = "game"
    NumRound = 0
    HumanScore = 0
    ComputerScore = 0
    
    while NumRound >= 0:
        print("let's play ................................")
        Human = HumanPlayer(GameRecord)
        
        if Human in ["r","rock","p","paper","scissors","s"]:
            if Human == "r":
                 Human = "rock"
            elif Human == "s":
                 Human = "scissors"
            elif Human == "p":
                 Human = "paper"
                 
            List1.append(Human)
    
            Computer = ComputerPlayer(GameRecord) 
             
                        
            if Computer == "r":
                 Computer = "rock"
            elif Computer == "s":
                 Computer = "scissors"
            elif Computer == "p":
                 Computer = "paper"
                 
            List2.append(Computer)
            
                 
            Outcome = Judge(Human, Computer)
            if Outcome == 2:
                HumanScore += 1
            elif Outcome == 1: 
                ComputerScore += 1
                
            List3.append(Outcome)
    
            UpdateGameRecord(GameRecord, List1, List2, List3)
            NumRound += 1
            
        elif Human in ["g", "game"]:
            print("--------Record of the Game-------")
            print("The Number of Rounds are", NumRound)
            print("Human wins ",HumanScore," rounds")
            print("Computer wins ",ComputerScore," rounds")
            for item in GameRecord:
                for x in item:
                    print(x)
                print 
        else:
            sys.exit()

def HumanPlayer(GameRecord):
    
    
        print("rock(r), paper(p), scissors(s) ?")
        print("or you want to see the record of the game(g) ?")
        print("or you want to quit(q) ?")
            
        Choice = input("please make your choice now: ")
            
        if Choice in ["r","rock","p","paper","scissors","s","g","game","q","quit"]: 
            return Choice           
        else: 
            print("The computer cannot understand your input")
            print("--------------Try Again---------------")
            HumanPlayer(GameRecord)
            
        
    
def ComputerPlayer(GameRecord):
    #options for computer 
    CompChoices = ["rock", "paper", "scissors"] 
    #random choice
    Choice = random.choice(CompChoices)      
       
    return(Choice)
    
        
def Judge(Human,Computer):
    
    
    if Human =="rock" and Computer == "scissors":
        
        Outcome = 2
        
        print("-----------------Outcome-------------------")
        print("Human wins: Human chose "+ Human +" Computer chose "+ Computer)
        print("-------------------------------------------")
        
    elif Human == "scissors" and Computer == "paper":
       
        Outcome = 2
        
        print("-----------------Outcome-------------------")
        print("Human wins: Human chose "+ Human +" Computer chose "+ Computer)
        print("-------------------------------------------")
    elif Human == "paper" and Computer == "rock":
        Outcome = 2
         
        print("-----------------Outcome-------------------")
        print("Human wins: Human chose "+ Human +" Computer chose "+ Computer)
        print("-------------------------------------------")
    elif Human == Computer :
        
        Outcome = 0
            
        print("-----------------Outcome-------------------")
        print("It is a tie: Human chose "+ Human +" Computer chose "+ Computer)
        print("-------------------------------------------")
    else: 
        Outcome = 1

        print("-----------------Outcome-------------------")
        print("Computer wins: Human chose "+ Human +" Computer chose "+ Computer)
        print("-------------------------------------------")
    return(Outcome)
    
def UpdateGameRecord(GameRecord, List1, List2, List3):

     GameRecord = [[List1],[List2],[List3]]      
     return