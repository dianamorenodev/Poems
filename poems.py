from time import sleep
vcount = 0
ccount = 0
nlines = int(input("How many lines will there be? "))
while True:
    poem = input("Please enter one line for your poem:")
    print(nlines)
    poem = poem.lower()
    for i in range(0, len(poem)):
        if poem[i] in ('a', "e", "i", "o", "u"):
            vcount = vcount + 1
        elif (poem[i] >= 'a' and poem[i] <= 'z'):
            ccount = ccount + 1
        nlines = nlines - 1
        print(nlines)
        if(nlines == 0):
            print("Number of Vowels: ", vcount)
            print("Number of Consonants: ", ccount)
            sleep(4)
            break
