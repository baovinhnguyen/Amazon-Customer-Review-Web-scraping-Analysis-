import pandas as pd
dataset = pd.read_csv("review1.csv")
text = ''
for item in dataset['comment']:
    text = text + item

review1 = open("text1.txt","r")
d = dict()
for line in review1:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Split the line into words
    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])

df = pd.DataFrame(data=d, index=[0])

df = (df.T)

print (df)

df.to_excel('dict1.xlsx')
