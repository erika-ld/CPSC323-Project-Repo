import lexical_analyzer
import assembly_code_generator

def main():
    input_file_current = "test_case_one.txt"
    output_file_current = "test_case_one_output.txt"
    lexical_analyzer.main(input_file_current, output_file_current)

    input_file_current = "test_case_two.txt"
    output_file_current = "test_case_two_output.txt"
    lexical_analyzer.main(input_file_current, output_file_current)

    input_file_current = "test_case_two.txt"
    output_file_current = "test_case_two_output.txt"
    lexical_analyzer.main(input_file_current, output_file_current)

    return 0


if __name__ == "__main__":
    main()