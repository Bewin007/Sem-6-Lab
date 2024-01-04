# a = 'Write a program to perform token separation for a subset of a programming language.'
# t = a.split(' ')
# Keywords = {'if', 'while', 'do'}
# Identifiers = {'num', 'a', 'b', 'c'}
# Operators = {'+', '-', '/', '*', '>', '<', '='}
# Punctuation = {':', ';', ',', "'", '"', '.'}

# symbol_table = {}

# def hash_function(identifier):
#     return hash(identifier) % 10

# for i in t:
#     i_cleaned = i.strip('.').lower()
#     # print(i_cleaned)
#     if i_cleaned in Keywords:
#         print('<keyword,', i_cleaned, '>')
#     elif i_cleaned in Identifiers:
#         print('<Identifiers,', i_cleaned, '>')
        
#         # Adding to symbol table
#         hash_value = hash_function(i_cleaned)
#         print(hash_value)
#         symbol_table.setdefault(hash_value, set()).add(i_cleaned)
        
#     elif any(op in i_cleaned for op in Operators):
#         print('<Operators,', i_cleaned, '>')
#     elif any(p in i_cleaned for p in Punctuation):
#         print('<Punctuation,', i_cleaned, '>')

# # Displaying the symbol table
# print('\nSymbol Table:')
# for key, value in symbol_table.items():
#     print(f'Hash {key}: {value}')


a = 'Write a program to perform token separation for a subset of a programming language.'
t = a.split(' ')
Keywords = {'if', 'while', 'do'}
Identifiers = {'num', 'a', 'b', 'c'}
Operators = {'+', '-', '/', '*', '>', '<', '='}
Punctuation = {':', ';', ',', "'", '"', '.'}

symbol_table = {}

def hash_function(identifier):
    return hash(identifier) % 10

for i in t:
    i_cleaned = i.strip('.').lower()
    
    if i_cleaned in Keywords:
        print('<keyword,', i_cleaned, '>')
    elif i_cleaned in Identifiers:
        print('<Identifiers,', i_cleaned, '>')
        
        # Adding to symbol table
        hash_value = hash_function(i_cleaned)
        symbol_table.setdefault(hash_value, set()).add(i_cleaned)
        
    elif any(op in i_cleaned for op in Operators):
        print('<Operators,', i_cleaned, '>')
    elif any(p in i_cleaned for p in Punctuation):
        print('<Punctuation,', i_cleaned, '>')

# Displaying the symbol table
print('\nSymbol Table:')
for key, value in symbol_table.items():
    print(f'Hash {key}: {value}')
