s = input("enter your string: ")

def palindrome(string):
    if len(string) == 1:
       return True
    if string[0] != string[len(string)-1]:
        return False
    else:
        print(string[1:len(string)-1])
        return palindrome(string[1:len(string)-1])

       
       
if palindrome(s):
    print('its a palindrome')
else:
    print('its not a palindrome')
