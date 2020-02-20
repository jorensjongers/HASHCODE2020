import parser

FILE_NAME = "a_example.in"
OUTPUT_FILE = "submission_landscape.txt"




f = open(FILE_NAME, "r")
out = parser.parse_input(f)
print(out)