import parser

FILE_NAME = "a_example.txt"
OUTPUT_FILE = "submission.txt"

f = open(FILE_NAME, "r")
input = parser.parse_input(f)





libs = parser.get_libraries(input)
print(libs)