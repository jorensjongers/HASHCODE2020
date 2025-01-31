import parser
import Serial_Approach

FILE_NAMES = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt", "d_tough_choices.txt"]
OUTPUT_FILES = ["submission_a.txt", "submission_b.txt", "submission_c.txt", "submission_e.txt", "submission_f.txt", "submission_d.txt"]

for name,out in zip(FILE_NAMES, OUTPUT_FILES):
    f = open(name, "r")    
    input = parser.parse_input(f)
    libs = parser.get_libraries(input)
    scores = parser.get_scores(input)
    deadline = parser.get_deadline(input)

    lib_order = Serial_Approach.libraryOrder(libs, deadline, scores)
    parser.output(lib_order, out)




