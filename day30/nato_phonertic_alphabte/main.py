# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    
    word = input("Enter a word: ").upper()
    #Esta es la parte que se va a probar que salga bien, si sale mal vamos a except
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    #En ligar de salir el error en rojo, se le informa al usuario cual fue el error
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    #else, Si todo salio bien con el try, vamos a imprimir lo que desea el usuario 
    else:
        print(output_list)
        
generate_phonetic()


