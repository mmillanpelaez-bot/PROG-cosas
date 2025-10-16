fails = 0
sucess = False
word = "esternocleidomastoideo"

dashWord = '_' * len(word)

while sucess == False or fails <= 7:
    print ('The word is: '+ dashWord)
    word_str = input('Write the word or a letter: ')
    if len(word_str) != 0:
        if word_str != 0:
            if word_str == word:
                sucess = True
                print('Congratulations! You got the word'+ word +'right.')
            else:
                fails = fails + 1
        else:
            found = False
            for i, character in