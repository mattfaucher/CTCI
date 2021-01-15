'''
Palindrome Permutation: Given a string, write a function to check if it is
a permutation of a palindrome. A palindrome is a word or phrase that is 
the same forwards as it is backwards. A permutation is a rearrangement of 
letters. The palindrome does not need to be limited to just dictionary words.
You can ignore casing and non-letter characters.

EXAMPLE: Input: Tact Coa
         Output: True (permutations: 'taco cat", atco cta", etc.)
'''

def palPermutation(string: str):
   # can i create a palindrome given the string
   # all palindromes have an even number of letters
   # one letter will be odd value
   
   # create dict
   letter_freq = {}
   # clean up the whitespace
   string = string.replace(" ", "")
   
   # build dict
   for char in string:
      counter = 0
      if char in letter_freq.keys():
         letter_freq[char] += 1
      else:
         letter_freq[char] = 1
   
   # count the 
   odd_count = 0
   for k, v in letter_freq.items():
      # if odd and odd_count is 0
      if v % 2 != 0 and odd_count == 0:
         odd_count += 1
      # if odd and odd_count isn't 0
      elif v % 2 != 0 and odd_count != 0:
         return False
      
   return True
      

def main():
   s = 'tact coa'
   s2 = 'ababaccde'
   
   print(palPermutation(s))
   print(palPermutation(s2))

if __name__ == "__main__":
   main()