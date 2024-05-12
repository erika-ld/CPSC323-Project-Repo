import lexical_analyzer
import assembly_code_generator

def main():
    input_file_one = "test_case_one.txt"
    output_file_one = "test_case_one_output.txt"
    lexical_analyzer.main(input_file_one, output_file_one)

    input_file_two = "test_case_two.txt"
    output_file_two = "test_case_two_output.txt"
    lexical_analyzer.main(input_file_two, output_file_two)

    input_file_three = "test_case_three.txt"
    output_file_three = "test_case_three_output.txt"
    lexical_analyzer.main(input_file_three, output_file_three)

    return 0


if __name__ == "__main__":
    main()