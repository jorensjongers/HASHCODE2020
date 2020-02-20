import parser

FILE_NAME = "a_example.txt"
OUTPUT_FILE = "submission.txt"

f = open(FILE_NAME, "r")
input = parser.parse_input(f)





libs = [{'lib_id' : 0, 'nb_books' : 2, 'books' : [2, 3]}, {'lib_id' : 1, 'nb_books' : 3, 'books' : [0,1, 3]}]
parser.output(libs, OUTPUT_FILE)