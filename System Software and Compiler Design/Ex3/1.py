import re

def extract_and_remove_macros(c_code):
    # Regular expression pattern to match #define directives
    pattern = re.compile(r'^\s*#define\s+(\w+)\s*\(([^)]*)\)\s*(.*)$', re.MULTILINE)

    # Find all matches in the C code
    matches = pattern.findall(c_code)

    # Create a dictionary to store macro definitions
    macro_dict = {}

    # Process each match and populate the dictionary
    for match in matches:
        macro_name = match[0]
        macro_value = match[1].strip() if match[1].strip() else match[2].strip()
        macro_dict[macro_name] = macro_value

    # Remove #define lines from the code
    code_without_macros = pattern.sub('', c_code)

    return macro_dict, code_without_macros



def main():
    input_file = "System Software and Compiler Design/Ex3/input.txt"

    try:
        # Read the C code from the input file
        with open(input_file, 'r') as file:
            code = file.read()

        # Extract macros, print the dictionary, and print the code without macros
        macro_dict, code_without_macros = extract_and_remove_macros(code)
        
        print("Macro Dictionary:")
        for macro_name, macro_value in macro_dict.items():
            print(f"{macro_name}: {macro_value}")

        print("\nCode without Macros:")
        print(code_without_macros)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

if __name__ == "__main__":
    main()


    