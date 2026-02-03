# HANGMAN GAME

import random
print('H A N G M A N\n')
L1 = ['APPLE','BANANA','ORANGE','GRAPE','MANGO']
L2 = ['LION','TIGER','ELEPHANT','DEER','BEAR']
L3 = ['MOBILE','COMPUTER','TABLE','BAG','MAT']

while True:
    print('Topics:\n1. FRUITS\n2. ANIMALS\n3. THINGS\n')
    s = input('Enter a choice: ')
    if s == '1':
        ch = random.choice(L1)
        break
    elif s == '2':
        ch = random.choice(L2)
        break
    elif s == '3':
        ch = random.choice(L3)
        break
    else:
        print('ENTER A VALID CHOICE')
    print()

print()
n = len(ch)
w = ['_']*n
print('The length of your word is: ',' '.join(w))
print()
print(' O')
print('/|\\')
print('/ \\')
print()

def hang(cnt):
    if cnt == 0:
        print()
        print(' O')
        print('/|\\')
        print('/ \\')
        print()
    elif cnt == 1:
        print()
        print(' O')
        print('/|\\')
        print('/ ')
        print()
    elif cnt == 2:
        print()
        print(' O')
        print('/|\\')
        print()
    elif cnt == 3:
        print()
        print(' O')
        print('/|')
        print()
    elif cnt == 4:
        print()
        print(' O')
        print(' |')
        print()

cnt = 0
s = []
while True:
    c = input('Guess a letter: ').upper()
    if c.isalpha() and len(c) == 1:
        if c not in s:
            s.append(c)
            if c in ch:
                print('CORRECT CHOICE!!!\n')
                for i in range(n):
                    if ch[i] == c:
                        w[i] = c
                print(' '.join(w))
                
            else:
                print('!!!WRONG CHOICE!!!\n')
                cnt += 1
                if cnt != 5:
                    hang(cnt)
                else:
                    print('=='*50)
                    print('!!! GAME OVER !!!')
                    print('!!! YOU LOSE !!!')
                    print('The correct word is: ',ch)
                    print()
                    break
        else:
            print(f'YOU ALREADY GUESSED THE LETTER "{c}"')
        if '_' not in w:
            print('=='*25)
            print('!!! CONGRATULATIONS !!!')
            print('!!! YOU WON !!!')
            print()
            break
    else:
        print('ENTER A VALID ALPHABET')
    print()

print('THANK (^-^)/ YOU')



