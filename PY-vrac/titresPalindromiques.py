nbLivre = int(input())

def Palindrome(testpalindrome):
   if testpalindrome[::-1] == testpalindrome: return True

for ar in range(nbLivre):
   phrase = input()
   testpalindrome = phrase
   testpalindrome = "".join(testpalindrome.split()) 
   testpalindrome = testpalindrome.lower()
     
   if Palindrome(testpalindrome):
      print(phrase)