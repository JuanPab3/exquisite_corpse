#  \|°~°|/  \|°~°|/  \|°~°|/  \|°~°|/  \|°~°|/  \|°~°|/  \|°~°|/  \|°~°|/  

# C E L L U L A R     A U T O M A T A     R U L E S :
#     - Each word must have at least one word as a possible succesor.
#     
#     - Every member of the succesors_list (for each word) must have a
#       probaility equal or greater than zero.
#     
#     - The sum of those elements must sum one (for each word).
#     
#     - The word that follows each is choosen by random, but taking into account
#       their probability value.
#
#     - The amount of words is decided with the 'markovit_words(n)' function. 
#
#     -

# M U S T    D O :
#     - Read a file type = '.txt'     |YES|
#     
#     - Create an algorithm that returns a type = dic that contains each word
#       with their next word probability.    |YES|
#     
#     - Create an algorithm that interacts with the dictionary to make
#       predictions of the word that follows according to the rules.    |YES|
#     
#     - Create a fuction that using the previews two algorithms  creates an
#       Exquisite corpse.      |YES|
#     
#     - Save the Exquisite corpse into a new file.     |YES|

#  \|°~°|/  \|°~°|/  \|°~°|/  \|°~°|/  \|°~°|/  \|°~°|/  \|°~°|/  \|°~°|/ 

from random import randint
from cleanWW import *


person_n = 'dave'
file_name = f'clean_chats/{person_n}_chat.txt'


#/\/\/\/\/\/\/\/\USING_GRAMS/\/\/\/\/\/\/\/\/\

order = 4
ngrams = dict()


def setup_grams(file_name):
    with open(file_name,'r') as f:
        for i in f:
            for j in range(len(i)-order):
                gram = i[j:j+order]
                if gram not in ngrams.keys():
                    ngrams[gram] =  []
                ngrams[gram].append(i[j+order:j+(2*order):])

def markovit_grams(num:int):
    with open(f'exquisite_corpses/g_exquisite_corpse_{person_n}.txt','w') as f:
        current_gram = list(ngrams.keys())[randint(0,len(ngrams.keys()))]
        for i in range(num):
            f.write(current_gram)
            possibilities = ngrams[current_gram]
            next_gram = possibilities[randint(0,len(possibilities)-1)]
            current_gram = next_gram


#/\/\/\/\/\/\/\/\USING_WORDS/\/\/\/\/\/\/\/\/\

text_list = []
words_dict = dict()

def setup_words(file_name):
    with open(file_name,'r') as f:
        for i in f:
            text_list.extend(i.split(" "))

        for j in range(len(text_list)):
            word = text_list[j]
            if word not in words_dict.keys():
                words_dict[word] = []
            try:
                words_dict[word].append(text_list[j+1])
            except IndexError:
                words_dict[word].append(text_list[j-1])


def markovit_words(num:int):
    with open(f'exquisite_corpses10/w_exquisite_corpse_{person_n}.txt','w') as f:
        current_word = list(words_dict.keys())[randint(0,len(words_dict.keys()))]
        for i in range(num):
            f.write(f'{current_word} ')
            possibilities = words_dict[current_word]
            next_word = possibilities[randint(0,len(possibilities)-1)]
            current_word = next_word


def pretty_doc(person_n):
    words = []
    with open(f'exquisite_corpses/w_exquisite_corpse_{person_n}.txt','r') as f:
        for i in f:
            lines = i.split(" ")
            for j in lines:
                words.append(j)

    with open(f'exquisite_corpses/w_exquisite_corpse_{person_n}.txt','w') as f2:
        count = 0
        for j in lines:
            f2.write(f'{j} ')
            count += 1
            if count == 20:
                f2.write('\n')
                count = 0


def main():
    if person_n != 'clau':
        clean_chat(person_n)
    else:
        clean_clau(person_n)
    setup_words(file_name)
    markovit_words(25)
    pretty_doc(person_n)

if __name__ == '__main__':
    main()
