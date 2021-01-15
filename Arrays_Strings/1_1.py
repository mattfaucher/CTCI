'''
Is Unique: Implement an algo to determine if a string has all unique chars
What if you cannot use additional data structure?
'''

def isUnique(string: str):
   """Function to determine if string has all unique chars

   Args:
       string (str): [description]
   Returns:
       boolean: true if all unique
   """
   
   seen = ""
   
   for char in string:
      if char in seen:
         return False
      else:
         seen += char
         
   return True


def main():
   s = 'abcdeg'
   ss = 'ababa'
   
   print(isUnique(s))
   print(isUnique(ss))

if __name__ == "__main__":
   main()