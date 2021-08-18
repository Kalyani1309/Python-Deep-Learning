def string_alternative(inputstring):              # Define a function to print the alternative characters
    output_string = inputstring[::2]              # Create a output string with alternate characters starting with first
    print("\nOutput String: " + output_string)


if __name__ == '__main__':
    string_alternative(input("Enter a String: "))  # Get a input string from user and call the function
