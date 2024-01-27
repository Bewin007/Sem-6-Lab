import re

a = 'int a,b,c;'
t = re.findall(r'\b\w+\b|[^\w\s]', a)
Keywords = ['if', 'while', 'do','int']
Operators = ['+', '-', '/', '*', '>', '<', '=']
Punctuation = [':', ';', ',', "'", '"', '.']

Keywords_count =0
Identifiers_count = 0

for i in t:
    if i in Keywords:
        print('<keyword ,', i, '>')
        Keywords_count+=1
    elif i in Operators:
        print('<Operators ,', i, '>')
    elif i in Punctuation:
        print('<Punctuation ,', i, '>')
    else:
        if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', i):
            print('<Identifier ,', i, '>')
            Identifiers_count+=1
        elif re.match(r'^[0-9]+$', i):
            print('<Value ,', i, '>')


print('Total Keywords: ',Keywords_count)
print('Total Identifiers: ',Identifiers_count)

