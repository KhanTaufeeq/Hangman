import random

data = open('C:/Users/taufe/OneDrive/Documents/words.txt')

for x in data:
    words = x.split()
    
word = random.choice(words)

i = 1
n = 0

temporary = '_'
for p in range(len(word)-1):
    temporary = temporary + '_'
    
def ShowTheWord1(index, character, temp):  
    """ This function is used to show letters guessed by the user.
        It has same length but the unguessed letters are replaced 
        by underscore."""
    lst = list(temp)
    lst[index] = character
    temp = ''.join(lst)
    return temp

def ShowTheWord2(index, character, temp):
    """ This function is used to show letters guessed by the user
        that comes more than once in the secret word."""
    lst = list(temp)
    for num in index:
        lst[num] = character
    temp = ''.join(lst)
    return temp

def is_word_guessed(target, result):
    """ It returns true if the guessed word is same as secret word
        otherwise false."""
    if target == result:
        return True
    else:
        return False
    
print('length of the word is : ', len(word))
print('positioning starts from 0\n')
while i <= len(word):
    x = input('Please guess a letter : ')
    if x in word.lower():
        if word.lower().count(x) > 1:
            c = word.lower().count(x)
            ind = [j for j in range(len(word)) if word.startswith(x,j)]
            temporary = ShowTheWord2(ind, x, temporary)
            print('Good guess : ',temporary)
            i -= 1
            n += c
            if n >= len(word):
                break
        else:
            place = word.lower().index(x)
            temporary = ShowTheWord1(place,x,temporary)
            print('Good guess : ',temporary)
            i -= 1
            n += 1
            if n >= len(word):
                break
    else:
        print('wrong')
        if len(word) - i == 0:
            break
        print('you have only', len(word)-i, 'guesses')
        
    i += 1

if is_word_guessed(word,temporary):
    print('\n')
    print('Congratulations, you won!')
    print('the secret word was : ', word)
    
else:
    print('\n')
    print('Sorry, you ran out of guesses.')
    print('the secret word was : ', word)
        


        