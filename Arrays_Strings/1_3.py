'''
URLify: write a method to replace all spaces in a string with %20
You may assume that the string has sufficient space at the end to
hold the additional characters, and that you are given the 'true'
length of the string. 

EXAMPLE: Input: "Mr John Smith ", 13
         Output: "Mr%20John%20Smith"
'''

def URLify(string: str, len: int):
   string = string.replace(" ", "%20")
   return string

def main():
   string = "Mr John Smith"
   n = 13
   
   print(URLify(string, n))

if __name__ == "__main__":
    main()