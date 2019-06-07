#!/usr/bin/env python3
"""
Created on Sun Mar  3 16:54:44 2019

@author: HaYeonOh
"""
import random 

def DrawBoard():
     Board= [[' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']]
     return Board

def TicTacToeGame():
    #create an empty Board = nested list
    Board = DrawBoard()
   
    row = 0 
    col = 0
    Outcome = 0
    #Print the board
    for row in range(len(Board)):
       for col in range(len(Board[row])):
            print(Board[row][col], end='|')
       print()
       print('-+-+-')
    #flip a coin 
    CoinChoices = ['Human goes first', 'Computer goes first']
    Choice = random.choice(CoinChoices)
    
    print(Choice)
    
    #Start the game: X starts first  
    
    if Choice == 'Human goes first':
    
        while Outcome == 0:
            (row,col) = HumanPlayer('X', Board)
            #update board
            UpdateBoard(Board, row, col, 'X')
            #print board
            for row in range(len(Board)):
                 for col in range(len(Board[row])):
                     print(Board[row][col], end='|')
                 print()
                 print('-+-+-')
            Outcome = Judge(Board)
            ShowOutcome(Outcome)
            
            #computer's turn      
            (row, col) = ComputerPlayer('O', Board)
            UpdateBoard(Board, row, col, 'O')
            #print board
            print('Computer turn')
            print()
            for row in range(len(Board)):
                 for col in range(len(Board[row])):
                     print(Board[row][col], end='|')
                 print()
                 print('-+-+-')
            Outcome = Judge(Board)
            ShowOutcome(Outcome)
            
    else:
        while Outcome == 0:
            print('Computer Turn')
            (row,col) = ComputerPlayer('X', Board)
            #update board
            UpdateBoard(Board, row, col, 'X')
            #print board
            for row in range(len(Board)):
                 for col in range(len(Board[row])):
                     print(Board[row][col], end='|')
                 print()
                 print('-+-+-')
            Outcome = Judge(Board)
            ShowOutcome(Outcome)
           
            #Human's turn   
            print('Human Turn')
            print()
            
            (row, col) = HumanPlayer('O', Board)
            UpdateBoard(Board, row, col, 'O')
            #print board
            for row in range(len(Board)):
                 for col in range(len(Board[row])):
                     print(Board[row][col], end='|')
                 print()
                 print('-+-+-')
            Outcome = Judge(Board)
            ShowOutcome(Outcome)
           
        

    
def HumanPlayer(Tag, Board):
    while 1:
        print('make your choice: 1 or 2 or 3')
        row = input('row = ')

        try:
            row = (int(row)) - 1
            break
        except (TypeError, ValueError):
            print('Oops! that is not a valid number. Try again...') 
                

    while 1:
        print('make your choice: 1 or 2 or 3')
        col = input('col = ')
    
        try:
            col = (int(col)) - 1
            break
        except (TypeError, ValueError):
            print('Oops! that is not a valid number. Try again...'.format(col))
            
    
    if IsSpaceFree(Board, row, col) == 0:
        print('Occupied: please choose another slot')
        #row
        print('make your choice: 1 or 2 or 3')
        row = input('row = ')
        try:
            row = (int(row)) - 1
        
        except (TypeError, ValueError):
            print('Oops! that is not a valid number. Try again...'.format(row))
        #col
        print('make your choice: 1 or 2 or 3')
        col = input('col = ')
    
        try:
            col = (int(col)) - 1
        
        except (TypeError, ValueError):
            print('Oops! that is not a valid number. Try again...'.format(col))
        
    return row, col

def ComputerPlayer(Tag, Board):   
    
    row = random.randint(0,2)
        
    col = random.randint(0,2)
    
    while IsSpaceFree(Board, row, col) == 0:
        #random row
        row = random.randint(0,2)
        
        col = random.randint(0,2)
        
    
    return row, col
     
def Judge(Board):
    # 1 = X wins, 0 = still in process, 2 = O wins, 3 = no winner tie          
   #X on vertical and horizontal
   for col in {0,1,2}:
       if 'X'==Board[0][col] == Board[1][col] == Board [2][col]:
           return 1
       else:
           break
   for row in {0,1,2}:
       if 'X' == Board[row][0] == Board[row][1] == Board [row][2]:
           return 1
       else: 
           break
   #O on vertical and horizontal    
   for col in {0,1,2}:
       if 'O'==Board[0][col] == Board[1][col] == Board [2][col]:
           return 2
       else:
           break
   for row in {0,1,2}:
       if 'O' == Board[row][0] == Board[row][1] == Board [row][2]:
           return 2
       else: 
           break

    #check if previous move was on the main diagonal and caused a win
   if 'X' == Board[0][0] == Board[1][1] == Board [2][2]:
      return 1
   elif 'O' == Board[0][0] == Board[1][1] == Board [2][2]:
      return 2
   #check if previous move was on the secondary diagonal and caused a win
   elif 'X' == Board[0][2] == Board[1][1] == Board [2][0]:
      return 1
   elif 'O' == Board[0][2] == Board[1][1] == Board [2][0]:
      return 2
   #check tie
   count = 0
   for row in range(len(Board)):
       for col in range(len(Board[row])):
            if Board[row][col] == ' ':
                break
            else:
                count+=1
   if count == 9:
    return 3
   else: 
    return 0
        
def IsSpaceFree(Board, row, col):
    if Board[row][col] != ' ':
        return 0
    
def GetNumberOfChessPieces(Board):
    Xcount = 0
    Ocount = 0 
    Emptycount = 0
    
    for row in range(len(Board)):
       for col in range(len(Board[row])):
            if Board[row][col] == 'O':
                Ocount += 1
            elif Board[row][col] == 'X':
                Xcount += 1
            else:
                Emptycount += 1
        
    return Xcount, Ocount, Emptycount
    
def IsBoardFull(Board):
    #1 - true, 0 - false
    for row in range(len(Board)):
       for col in range(len(Board[row])):
            if Board[row][col] == ' ':
                return 0
        
    return 1

def IsBoardEmpty(Board):
    #1 - true, 0 - false
    for row in range(len(Board)):
       for col in range(len(Board[row])):
            if Board[row][col] != ' ':
                return 0
        
    return 1
def UpdateBoard(Board, row, col, tag):
    #void update board
    Board[row][col] = tag
    return

def ShowOutcome(Outcome):
    #void print outcome
    if Outcome == 1:
        print('Human Wins!')
        return
    elif Outcome == 2:
        print('Computer Wins!')
        return
    elif Outcome == 0:
        print('The game is still in progress')
        return
    else:
        print('It is a Tie!')
        return
 
  #play game  
while True:
    TicTacToeGame()
    print('Do you want to play again? (yes/no)')
    if not input().lower().startswith('y'):
        break
print('GameOver')