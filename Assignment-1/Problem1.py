inputString = input("Enter a string: ")             # Take string as list of characters from the console menu

outputString = inputString[2:6]                     # Delete two characters from the string
reversedString = outputString[::-1]                 # Reverse the string

print("\nOutput:" + reversedString)                 # print the string in reverse order
