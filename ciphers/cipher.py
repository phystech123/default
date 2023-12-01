__author__ = 'Riabov Oleg'
# -*- coding: utf8 -*-

class Atbash:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self):
        lowercase_code = {self.alphabet[i]:self.alphabet[-i-1] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():self.alphabet[-i-1].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])
cipher = Atbash()
with open('sh','r') as f:
    with open('s_h','w')as g:
        line = f.readline()
        while line != '.':
            g.write(f'{cipher.encode(line)}\n')
            line = f.readline()




class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        lowercase_code = {self.alphabet[i]:self.alphabet[(i+key)%len(self.alphabet)] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():self.alphabet[(i+key)%len(self.alphabet)].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        Lowercase_code = {self.alphabet[i]:self.alphabet[(i-key)%len(self.alphabet)] for i in range(len(self.alphabet))}
        Uppercase_code= {self.alphabet[i].upper():self.alphabet[(i-key)%len(self.alphabet)].upper() for i in range(len(self.alphabet))}
        self._decode = dict(Lowercase_code)
        self._decode.update(Uppercase_code)

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        if len(line) == 1:
            return self._decode[line] if line in self._decode else line
        else:
            return ''.join([self.decode(char) for char in line])
#поиск ключа
line=input()
for i in range(33):
    key=i
    cipher = Caesar(key)
    print(i,'     ',cipher.decode(line))
#основное
key=14
cipher = Caesar(key)
with open('sh','r') as f:
    with open('s_h','w')as g:
        line = f.readline()
        while line != '.':
            g.write(f'{cipher.decode(line)}\n')
            line = f.readline()





class Monoalphabet:
    #для частотного анализа(не работает)
    # def norm(alp):
    #     o='''
    #     о — 9.28%
    #     а — 8.66%
    #     е — 8.10%
    #     и — 7.45%
    #     н — 6.35%
    #     т — 6.30%
    #     р — 5.53%
    #     с — 5.45%
    #     л — 4.32%
    #     в — 4.19%
    #     к — 3.47%
    #     п — 3.35%
    #     м — 3.29%
    #     у — 2.90%
    #     д — 2.56%
    #     я — 2.22%
    #     ы — 2.11%
    #     ь — 1.90%
    #     з — 1.81%
    #     б — 1.51%
    #     г — 1.41%
    #     й — 1.31%
    #     ч — 1.27%
    #     ю — 1.03%
    #     х — 0.92%
    #     ж — 0.78%
    #     ш — 0.77%
    #     ц — 0.52%
    #     щ — 0.49%
    #     ф — 0.40%
    #     э — 0.17%
    #     ъ — 0.04% 
    #     ё - 0.01%
    #     '''
    #     t=[]
    #     o=list(o)
    #     for i in o:
    #         if i in alp:
    #             t.append(i)
    #     return t
   
    alphabet=list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")

    def __init__(self, keytable):
        lowercase_code = {self.alphabet[i]:keytable[i] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():keytable[i].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        Lowercase_code = {keytable[i]:self.alphabet[i] for i in range(len(self.alphabet))}
        Uppercase_code = {keytable[i].upper():self.alphabet[i].upper() for i in range(len(self.alphabet))}
        self._decode = dict(Lowercase_code)
        self._decode.update(Uppercase_code)

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        if len(line) ==1:
            return self._decode[line] if line in self._decode else line
        else:
            return ''.join([self.decode(char) for char in line])
#тоже для частотного анализа))
# with open('sh','r') as f:
#     alp = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
#     ALP=[i.upper() for i in alp]
#     s=dict()
#     for i in alp:
#         s[i]=0
#     r=list(f.read())
#     for i in r:
#         if i in alp:
#             s[i]+=1
#         elif i in ALP:
#             i=i.lower()
#             s[i]+=1
# keyy=sorted(s.items(), key=lambda item: item[1]) #[i][0] for i in range(len(s))][::-1]
# key=list()
# for i in keyy:
#     key.append(i[0])
qwe='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
key='эьормщднйгычясюцажшбтпвёлеъузхкфи'
key,qwe=list(key),list(qwe)
#print(len(set(key)))

cipher = Monoalphabet(key)
with open('sh','r') as f:
    f.seek(0)
    with open('s_h','w')as g:
        line = f.readline()
        while line != '.':
            g.write(f'{cipher.decode(line)}\n')
            line = f.readline()





class Vigenere:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
      #        "012345678901234567890123456789012"

    def __init__(self, keyword):
        self.alphaindex = {self.alphabet[index]: index for index in range(len(self.alphabet))}
        self.key = [self.alphaindex[letter] for letter in keyword.lower()]
        # print(self.alphabet[self.alphaindex[input()]-self.alphaindex[input()]])

    def caesar(self, letter, shift):
        if letter in self.alphaindex:  # шбжцлюэи ьтчоэ
            index = (self.alphaindex[letter] + shift)%len(self.alphabet)
            cipherletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # йэряэоюэи ьтчоэ
            cipherletter = self.caesar(letter.lower(), shift).upper()
        else:
            cipherletter = letter
        return cipherletter
    
    def oppcaesar(self, letter, shift):
        if letter in self.alphaindex:  # шбжцлюэи ьтчоэ
            index = (self.alphaindex[letter] - shift)%len(self.alphabet)
            origletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # йэряэоюэи ьтчоэ
            origletter = self.oppcaesar(letter.lower(), shift).upper()
        else:
            origletter = letter
        return origletter

    def encode(self, line, key = None):
        if not key:
            key = self.key
        ciphertext = []
        i = 0
        for letter in line:
            shift = key[i]
            cipherletter = self.caesar(letter, shift)
            ciphertext.append(cipherletter)
            i = (i + 1)%len(key)

        return ''.join(ciphertext)

    def decode(self, line):
        origtext = []
        i = 0
        for letter in line:
            shift = self.key[i]
            origletter = self.oppcaesar(letter, shift)
            origtext.append(origletter)
            i = (i + 1)%len(self.key)

        return ''.join(origtext)
keyword = 'столлман'#input('keyword=')
cipher = Vigenere(keyword)

with open('sh','r') as f:
    with open('s_h','w')as g:
        line = f.readline()
        while line != '.':
            g.write(f'{cipher.decode(line)}\n')
            line = f.readline()
