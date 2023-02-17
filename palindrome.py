from ast import List
from email.charset import SHORTEST
from json.encoder import INFINITY
from operator import index
from pickle import NONE

# Coding Practicum 1 
# Hannah Peluso
# CS 452
# November 2, 2022
# I have abided by the JMU Honor Code. 


def main():
    print("Enter a string: \n")
    str = input()
    longest_palindromic_subsequence(str)
    shortest_palindromic_supersequence(str)
    split_into_palindromes(str)
   
   
# helper method to check if a string is a palindrome
def isPalindrome(str):
    return str == str[::-1] 
    
    
#prints the longest palindromic subsequence of str
def longest_palindromic_subsequence(str):
    if isPalindrome(str):
        print("Longest palindromic subsequence: " + str)
    else:
        p = str[0]
        l = 1
        for i in range(len(str)):
            for j in range(len(str), 0, -1):
                if isPalindrome(str[i:j + 1]):
                    if len(str[i:j + 1]) > l:
                        p = str[i:j + 1]
                        l = len(str[i:j + 1])
        print("Longest palindromic subsequence: " + p)
          
# prints the number of insertions needed to make str the shortest palindrome possible
def shortest_pal(str, i, j):
    if (i == j):
        return 0
    if (i == j - 1):
        return 0 if(str[i] == str[j]) else 1
    if(str[i] == str[j]):
        return shortest_pal(str, i + 1, j - 1)
    else:
        return 1 + min(shortest_pal(str, i, j - 1), shortest_pal(str, i + 1, j))
        # return (min(shortest_pal(str, i, j - 1), shortest_pal(str, i + 1, j)) + 1)

def shortest_palindromic_supersequence(st):
    print("Shortest palindromic supersequence for '" + st + "' takes " + str(shortest_pal(st, 0, len(st) - 1)) + " character(s) inserted to make a palindrome.")
    

#splits the string into the fewest number of palindromes possible and returns as a list of strings.  
def split_into_palindromes(str): 
    print("Input split into palindromes: ")
    s = [None] * len(str)
    for i in range(len(str) - 1, -1, -1):
        if isPalindrome(str[i: len(str)]):
            s[i] = 1 # type: ignore
        else:
            best = INFINITY
            for j in range(i, len(str) - 1, 1):
                if isPalindrome(str[i:j]):
                    splitHere =  s[j + 1] + 1 # type: ignore
                    best = min(best, splitHere) # type: ignore
            s[i] = best   # type: ignore
    
    print(s)        


main()