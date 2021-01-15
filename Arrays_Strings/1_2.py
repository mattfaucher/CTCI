'''
Check Permutation: Given two strings, write a method to 
determine if one is a permutation of the other
'''

def checkPermutation(string1: str, string2: str):
   """Function to check if a string is a permutation
   of the other

   Args:
       string1 (str): input string
       string2 (str): input string
   Returns: 
       bool: true if permutation
   """
   
   if len(string1) != len(string2):
      return False
   else:
      for char in string1:
         if char not in string2:
            return False
         else:
            continue
   return True
   
def main():
   s = 'man'
   ss = 'nam'
      
   s1 = 'joeb'
   ss1 = 'bake'
      
   print(checkPermutation(s, ss))
   print(checkPermutation(s1, ss1))
      
      
if __name__ == "__main__":
   main()