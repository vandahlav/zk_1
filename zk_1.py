#defining function for counting the number of vowels and consonants
def getNumberofVowelsAndConsonants(input):
    counter_v = 0
    counter_c = 0
    counter_o = 0
    vowels = "aeiyouáéíýóúů"
    consonants = "qwrtzplkjhgfdsxcvbnmřťžpščň"

    try: 
        for character in input:
            if character in vowels:
                counter_v += 1
            if character in consonants:
                counter_c += 1
            else:
               counter_o += 1
        print(f"Your text contains {counter_v} vowels, {counter_c} consonants and {counter_o} other characters.")
    except ValueError:
        print("Program cannot process your input.")
        quit()

#running the fuction
getNumberofVowelsAndConsonants(input = str(input("Enter the text: ")).lower())