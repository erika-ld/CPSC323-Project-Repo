import lexical_analyzer
import assembly_code_generator

def main():
    #Get the lexical analysis of test case one. Result is output to test_case_one_output.txt
    input_file_one = "test_case_one.txt"
    output_file_one = "test_case_one_output.txt"
    lexical_analyzer.main(input_file_one, output_file_one)

    print("\nSuccessful lexical analysis: test_case_one\n\n")

    #Get the assembly code from test case one. 
    #Input file is output file from lexical analysis of test case one.
    #Result is output to test_case_one_assembly.txt
    input_file_one = "test_case_one_output.txt"
    output_file_one = "test_case_one_assembly.txt"
    assembly_code_generator.main(input_file_one, output_file_one)

    print('\nFile successfully parsed: test_case_one\n\n')

    #Get the lexical analysis of test case two. Result is output to test_case_two_output.txt
    input_file_two = "test_case_two.txt"
    output_file_two = "test_case_two_output.txt"
    lexical_analyzer.main(input_file_two, output_file_two)

    print("Successful lexical analysis: test_case_two\n\n")

    #Get the assembly code from test case two. 
    #Input file is output file from lexical analysis of test case two.
    #Result is output to test_case_two_assembly.txt
    input_file_two = "test_case_two_output.txt"
    output_file_two = "test_case_two_assembly.txt"
    assembly_code_generator.main(input_file_two, output_file_two)

    print('\nFile successfully parsed: test_case_two\n\n')


    #Get the lexical analysis of test case three. Result is output to test_case_three_output.txt
    input_file_three = "test_case_three.txt"
    output_file_three = "test_case_three_output.txt"
    lexical_analyzer.main(input_file_three, output_file_three)

    print("Successful lexical analysis: test_case_three\n\n")

    #Get the assembly code from test case three. 
    #Input file is output file from lexical analysis of test case three.
    #Result is output to test_case_three_assembly.txt
    input_file_three = "test_case_three_output.txt"
    output_file_three = "test_case_three_assembly.txt"
    assembly_code_generator.main(input_file_three, output_file_three)

    print('\nFile successfully parsed: test_case_three\n\n')



    return 0


if __name__ == "__main__":
    main()