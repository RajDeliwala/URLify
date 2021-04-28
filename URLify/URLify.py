'''
Cracking the coding interview
Chapter 1 - Arrays and Strings page 90
URLify
Problem Statement: Write a method to replace all spaces in a string with '%20'. You may assume that the string has suffcient space at the end to hold additional characters, and that
you are given the "true" length of the string. 
example: 
    input: "Mr John Smith   ", 13
    output: "Mr%20John%20Smith"
Constraits or Questions you need to ask:

Solution notes:

'''
#Cleaning the end of the string of all it's extra white space
#Then just replace the remaining white spaces in the string with %20 and print
def URLify_solution(string, stringSize):
    new_string = string[:stringSize] + "" + string[stringSize:+1]     
    x = new_string.replace(" ", "%20")
    return print(x)

URLify_solution("Mr John Smith        ", 13)
URLify_solution("ra J        ", 4)
URLify_solution("Checking theCode         ", 16)

