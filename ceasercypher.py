offset = 1
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def encrypt(text, offset):
   result = ""
   for letter in text:
      position = characters.find(letter)
      if position >= 0:
         result += characters[(position + offset) % len(characters)]
      else:
         result += letter
   return result

def decrypt(text, offset):
    result = ""
    for letter in text:
        position = characters.find(letter)
        if position >= 0:
            result += characters[(position - offset) % len(characters)]
        else:
            result += letter     
    return result

while True:
   print ("1 -- Encrypt a text string") 
   print ("2 -- Decrypt a text string") 
   print ("3 -- Quit") 
   action = input("Select which type of operation you want: ")

   if (action == "1"):
       offset = int(input("Enter the offset value"))
       text = input("Enter a text string to be encrypted: ")
       print ("The encrypted text string is: ", encrypt(text, offset))
   elif (action == "2"):
      offset = int(input("Enter the offset value"))
      text = input("Enter a text string to be decrypted: ")
      print ("The decrypted text string is: ", decrypt(text, offset))
   elif (action == "3"):
      print ("Goodbye")
      break
   else:
      print ("Invalid input -- try again")

   

