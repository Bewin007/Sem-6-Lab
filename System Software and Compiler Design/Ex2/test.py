import re

def symbol_table(input_file):
    key = ['int','double','char']
    punct = [';',',']
    identifier = re.compile('([a-zA-Z])([a-zA-Z0-9])*')
    symboltable =[]

    with open(input_file,"r") as f:
        lines = f.readlines()

    data_type, return_type = None,None

    for line in lines:
        tokens = re.findall(r'\b\w+\b',line)
        for i,token in enumerate(tokens):
            if token in key:
                data_type,return_type = token,None

                if i + 1 < len(tokens) and tokens[i+1] == '(':
                    return_type = tokens[i]
            elif token in punct:
                continue

            elif re.match(identifier,token):
                entry = {'ID':token,'Data Type':data_type,'ReturnType':None,'InitialValue':'NULL','NoOfParameters': 0,'TypeOfParameters': ''}

                if '=' in line:
                    entry['InitialValue'] = line.split('=')
                elif '(' in line:
                    parameters = line[line.index('(')+1:line.index(')')].strip()

                    if parameters:
                        entry.update({'Data Type':None,'ReturnType': data_type,'NoOfParameters':len(parameters.split(',')),'TypeOfParameters':','.join(p.strip().split()[1] for p in parameters.split(','))})
                symboltable.append(entry)

        print("ID\tData Type\tReturnType\tInitial Value\tNo.of Parameters Type of Parameters")
        for entry in symboltable:
            print(f"{entry['ID']}\t{entry['Data Type']}\t\t\t{entry['ReturnType']}\t\t\t{entry['InitialValue']}\t\t{entry['NoOfParameters']}\t\t{entry['TypeOfParameters']}")

symbol_table("input.txt")