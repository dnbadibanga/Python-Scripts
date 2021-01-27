word = 'kambucha'
word = 'misunderstanding'
word = 'onomatopoeia'

length = len(word)
vowels = ['a', 'e', 'i', 'o', 'u']

v = 0
c = 0

for i in range(0, length):
    if word[i] in vowels:
        v += 1
    else:
        c += 1

if v > c:
    print(word, ' has more vowels(', v, ') than consonants(', c, ')')
else:
    print(word, ' has more consonants(', c, ') than vowels(', v, ')')
