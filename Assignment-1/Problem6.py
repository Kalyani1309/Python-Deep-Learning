infile = open("InputFile", "r")             # Read the input file contents
wordCountDict = dict()                      # Create an empty dictionary

for line in infile:                         # Loop through each line of the file
    line = line.strip()                     # Remove the leading spaces and newline character
    line = line.lower()                     # To avoid case mismatch, convert the characters in line to lowercase
    words = line.split(" ")                 # Split the line into words
    for word in words:                      # apply for loop over each word in line
        if word in wordCountDict:           # Check if the word is already present in dictionary
            # Increment count of word by 1
            wordCountDict[word] = wordCountDict[word] + 1
        else:
            # Add the new word to dictionary with count 1
            wordCountDict[word] = 1

infile = open("InputFile", "a")             # Open the input file in Append mode
print("Output - ")                        # Print the contents of dictionary and also
for key in list(wordCountDict.keys()):
    print(key, ":", wordCountDict[key])
    # Append the input file with the output content
    infile.write("\n{} : {}".format(key, wordCountDict[key]))

infile.close()                              # Finally, close the file
