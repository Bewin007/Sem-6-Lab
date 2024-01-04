#Write a program to perform token separation for a subset of a programming language.
a = 'if a b c'
t = a.split(' ')
Keywords = ['if','while','do']
Identifiers = ['num','a','b','c']
Operators = ['+','-','/','*','>','<','=']
Punctuation = [':',';',',',"'",'''"''','.']

for i in t:
    if i in Keywords:
        print('<keyword ,', i,'>')
    # if i in Keywords:
    #     print('<keyword ,', i,'>')
    elif i in Identifiers:
        print('<Identifiers ,', i,'>')
    elif i in Operators:
        print('<Operators ,', i,'>')
    elif i in Punctuation:
        print('<Punctuation ,', i,'>')