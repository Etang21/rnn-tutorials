import csv
wordlist = open('wordlist-dict.txt', 'r')
out = open('wordlist.csv', 'w')
writer = csv.writer(out)
for line in wordlist.readlines():
    tokens = line.split()
    # Some checking for correct verbs
    if tokens[1] == "V:" and len(tokens) >= 3 and tokens[0][0] != '-':
        writer.writerow([tokens[0], tokens[2]])
