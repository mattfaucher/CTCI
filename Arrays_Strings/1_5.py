'''
One Away: There are three types of edits that can be performed on
strings: insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit
(or zero edits) away.

EXAMPLE:

pale, ple -> True
pales, pale -> True
pale, bale -> True
pale, bake -> False
'''

def oneAway(string1: str, string2: str):
   # check to make sure lengths are only one apart initially
   if len(string1) == len(string2) or len(string1) == len(string2) + 1 or len(string1) == len(string2) - 1:
      num_same = 0
      
      for char in string2:
         if char in string1:
            num_same += 1
            
      if num_same >= len(string1) - 1:
         return True
      else:
         return False
   
   return False

def main():
   s1, s2 = 'pale', 'ple'
   print(oneAway(s1, s2))
   
   s1, s2 = 'pale', 'pl'
   print(oneAway(s1, s2))
   
   s1, s2 = 'pale', 'plzd'
   print(oneAway(s1, s2))
   
   s1, s2 = 'zap', 'cabado'
   print(oneAway(s1, s2))

if __name__ == "__main__":   
   main()