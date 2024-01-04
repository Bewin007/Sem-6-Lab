#Write a program to perform token separation for a subset of a programming language.
a = 'if a b c e'#use space for spliting
t = a.split(' ')
Keywords = ['if','while','do']
Identifiers = ['num','a','b','c']
Operators = ['+','-','/','*','>','<','=']
Punctuation = [':',';',',',"'",'''"''','.']

symbol_table = {}

for i in t:
    if i in Keywords:
        print('<keyword ,', i,'>')
        symbol_table[i] = "keyword"
    # if i in Keywords:
    #     print('<keyword ,', i,'>')
    elif i in Identifiers:
        print('<Identifiers ,', i,'>')
        symbol_table[i] = "identifier"
    elif i in Operators:
        print('<Operators ,', i,'>')
        symbol_table[i] = "operator"
    elif i in Punctuation:
        print('<Punctuation ,', i,'>')
        symbol_table[i] = "punctuation"
    


print(symbol_table)

