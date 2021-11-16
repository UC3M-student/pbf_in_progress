import pandas as pd
import numpy as np
from pydtmc import *


def variables (file):
    df = pd.read_excel(file)
    matrix = np.array([[0,0],[0,0]])
    size = len(df)
    results = df.iloc[0:size,7]
    n = 0
     
    try:
        while n < size: 
            n += 1
            t = n - 1
            if results[n] == "W" and results[t] == "L":
                a = np.array([[0,1],[0,0]])
                matrix = matrix + a
            elif results[n] == "L" and results[t] == "W":
                b = np.array([[0,0],[1,0]])
                matrix = matrix + b
            elif results[n] == results[t] == "W":
                c = np.array([[1,0],[0,0]])
                matrix = matrix + c
            elif results[n] == results[t] == "L":
                d = np.array([[0,0],[0,1]])
                matrix = matrix + d
            else:
                continue 
    except KeyError:
        print("value error")
        
    first0_0 = matrix[0,0]/(matrix[0,0] + matrix[0,1]) 
    first0_1 = matrix[0,1]/(matrix[0,0] + matrix[0,1])
    first1_0 = matrix[1,0]/(matrix[1,0] + matrix[1,1])
    first1_1 = matrix[1,1]/(matrix[1,0] + matrix[1,1])

    matrix_probailities = np.array([[first0_0,first0_1],[first1_0,first1_1]])
        
    return matrix_probailities
     
def last_win_or_lose (file):
    df = pd.read_excel(file)
    results = df.iloc[(len(df)-1):len(df),7]
    return results

def in_a_row(last_win_or_lose) : #probabilities in a row
    if last_win_or_lose == "W":
        two_wins_in_a_row = first[0,0] #next win
        three_wins_in_a_row = first[0,0]**2
        four_wins_in_a_row = first[0,0]**3
        five_wins_in_a_row = first[0,0]**4
        six_wins_in_a_row = first[0,0]**5
        seven_wins_in_a_row = first[0,0]**6
        eight_wins_in_a_row = first[0,0]**7
        nine_wins_in_a_row = first[0,0]**8
        ten_wins_in_a_row = first[0,0]**9
        
        database =pd.DataFrame({ "2" : [two_wins_in_a_row ],
                                "3" : [three_wins_in_a_row],
                                "4": [four_wins_in_a_row],
                                "5" : [ five_wins_in_a_row],
                                "6": [ six_wins_in_a_row],
                                "7": [seven_wins_in_a_row],
                                "8": [eight_wins_in_a_row],
                                "9": [nine_wins_in_a_row],
                                "10": [ten_wins_in_a_row]})
        
    elif last_win_or_lose == "L":
        two_lose_in_a_row = 1 - first[1,1] #next win 
        three_lose_in_a_row = 1 - first[1,1]**2
        four_lose_in_a_row = 1 - first[1,1]**3
        five_lose_in_a_row = 1 - first[1,1]**4
        six_lose_in_a_row = 1 - first[1,1]**5
        seven_lose_in_a_row = 1 - first[1,1]**6
        eight_lose_in_a_row = 1 - first[1,1]**7
        nine_lose_in_a_row = 1 - first[1,1]**8
        ten_lose_in_a_row = 1 - first[1,1]**9
        
        database =pd.DataFrame({ "2" : [two_lose_in_a_row ],
                                "3" : [three_lose_in_a_row],
                                "4": [four_lose_in_a_row],
                                "5" : [ five_lose_in_a_row],
                                "6": [ six_lose_in_a_row],
                                "7": [seven_lose_in_a_row],
                                "8": [eight_lose_in_a_row],
                                "9": [nine_lose_in_a_row],
                                "10": [ten_lose_in_a_row]})
    
    else:
        print("error in the probability matrix")
        
    return database        
    
    
    
       
 
    
first = variables("D:\VSCODE projects\Golden State Warriors\Excell data\Wolden State Warriors.xls")


second = last_win_or_loose("D:\VSCODE projects\Golden State Warriors\Excell data\Wolden State Warriors.xls")
print(second)
