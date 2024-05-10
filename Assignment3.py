class SymbolTableEntry:
    def __init__(self, lexeme, memory_location, type):
        self.lexeme = lexeme
        self.memory_location = memory_location
        self.type = type

class SymbolTable:
    def __init__(self):
        self.entries = []

    def check_if_exists(self, lexeme):
        for entry in self.entries:
            if entry.lexeme == lexeme:
                return True
        return False

    def insert_into_table(self, lexeme, memory_location, type):
        if not self.check_if_exists(lexeme):
            self.entries.append(SymbolTableEntry(lexeme, memory_location, type))
        else:
            print(f"Error: Identifier '{lexeme}' already exists in the symbol table.")

    def print_identifiers(self, output_file):
        output_file.write("Symbol Table\n")
        output_file.write("Identifier\tMemoryLocation\tType\n")
        for entry in self.entries:
            output_file.write(f"{entry.lexeme}\t\t{entry.memory_location}\t\t{entry.type}\n")

class AssemblyCodeGenerator:
    def __init__(self):
        self.instructions = []
        self.instr_address = 1

    def generate_instruction(self, op, oprnd=""):
        self.instructions.append((self.instr_address, op, oprnd))
        self.instr_address += 1

    def print_assembly_code_listing(self, output_file):
        output_file.write("Assembly Code Listing\n")
        for instr in self.instructions:
            output_file.write(f"{instr[0]} {instr[1]} {instr[2]}\n")

def parse_rats24(input_code, symbol_table, assembly_generator):
    lines = input_code.split('\n')
    memory_location = 5000

    for line in lines:
        if line.strip() and not line.strip().startswith("[*"):
            tokens = line.strip().split()
            if tokens[0] == "integer":
                for token in tokens[1:]:
                    if token.endswith(";"):
                        lexeme = token[:-1]
                        symbol_table.insert_into_table(lexeme, memory_location, "integer")
                        memory_location += 1
                    else:
                        lexeme = token.strip(",")
                        symbol_table.insert_into_table(lexeme, memory_location, "integer")
                        memory_location += 1
            elif tokens[0] == "scan":
                lexeme = tokens[1][:-1]
                assembly_generator.generate_instruction("SIN")
                symbol_table.insert_into_table(lexeme, memory_location, "integer")
            elif tokens[0] == "while":
                assembly_generator.generate_instruction("LABEL")
            elif tokens[0] == "endwhile":
                assembly_generator.generate_instruction("JUMP", assembly_generator.instructions[-2][0])
            elif tokens[0] == "print":
                lexeme = tokens[1][:-1]
                assembly_generator.generate_instruction("PUSHM", str(symbol_table.entries[0].memory_location))
                assembly_generator.generate_instruction("SOUT")
            elif len(tokens) >= 3 and tokens[1] == "=":
                lexeme = tokens[0]
                if symbol_table.check_if_exists(lexeme):
                    assembly_generator.generate_instruction("POPM", str(symbol_table.entries[0].memory_location))
                else:
                    print(f"Error: Identifier '{lexeme}' is not declared.")
                    return

def generate_code(input_file_path, output_file_path):
    with open(input_file_path, "r") as input_file:
        input_code = input_file.read()

    symbol_table = SymbolTable()
    assembly_generator = AssemblyCodeGenerator()

    parse_rats24(input_code, symbol_table, assembly_generator)

    with open(output_file_path, "w") as output_file:
        assembly_generator.print_assembly_code_listing(output_file)

input_file_path = "test_case_one.txt"
output_file_path = "test_case_one_output.txt"

generate_code(input_file_path, output_file_path)
