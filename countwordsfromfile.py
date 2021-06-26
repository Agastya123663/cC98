def countwordsfromfile():
    filename = input('Enter the file name : ')
    numberofwords = 0
    file = open(filename,'r')
    for line in file:
        print(line)
        words = line.split()
        numberofwords = numberofwords + len(words)
    print('no of words',numberofwords)

countwordsfromfile()
    
