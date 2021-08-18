inputString = input("Enter a sentence which has 'python' word in it: ")     # Get the input from the user

outputString = inputString.replace("python", "pythons")                     # Replace each occurrence of ‘python’ with ‘pythons’ without using regex

print("\nOutput String: " + outputString)                                   # print the output
