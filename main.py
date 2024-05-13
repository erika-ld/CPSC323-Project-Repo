import lexical_analyzer
import assembly_code_generator

def main():
    input_file_one = "test_case_one.txt"
    output_file_one = "test_case_one_output.txt"
    lexical_analyzer.main(input_file_one, output_file_one)

    print("\nSuccessful lexical analysis: test_case_one\n\n")

    input_file_one = "test_case_one_output.txt"
    output_file_one = "test_case_one_assembly.txt"
    assembly_code_generator.main(input_file_one, output_file_one)

    print('\nFile successfully parsed: test_case_one\n\n')

    input_file_two = "test_case_two.txt"
    output_file_two = "test_case_two_output.txt"
    lexical_analyzer.main(input_file_two, output_file_two)

    print("Successful lexical analysis: test_case_two\n\n")

    input_file_two = "test_case_two_output.txt"
    output_file_two = "test_case_two_assembly.txt"
    assembly_code_generator.main(input_file_two, output_file_two)

    print('\nFile successfully parsed: test_case_two\n\n')


    input_file_three = "test_case_three.txt"
    output_file_three = "test_case_three_output.txt"
    lexical_analyzer.main(input_file_three, output_file_three)

    print("Successful lexical analysis: test_case_three\n\n")

    input_file_three = "test_case_three_output.txt"
    output_file_three = "test_case_three_assembly.txt"
    assembly_code_generator.main(input_file_three, output_file_three)

    print('\nFile successfully parsed: test_case_three\n\n')



    return 0


if __name__ == "__main__":
    main()