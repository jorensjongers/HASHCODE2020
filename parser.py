def parse_input(file):
    list = [line.split(' ') for line in file.read().split('\n')]
    print(list)
    return list

def get_nb_books(list):
    return int(list[0][0])

def get_nb_libraries(list):
    return int(list[0][1])

def get_deadline(list):
    return int(list[0][2])

def get_scores(list):
    result = []
    for score in list[1]:
        new_score = int(score)
        result.append(new_score)
    return result

def get_libraries(lst):
    result = []
    for id in range(0, get_nb_libraries(lst) * 2, 2):
        nb_books = int(lst[id+2][0])
        signup_time = int(lst[id+2][1])
        books_per_day = int(lst[id+2][2])
        books = []
        for book in lst[id+3]:
            new_book = int(book)
            books.append(new_book)
        lib = {}
        lib["nb_books"] = nb_books
        lib["signup_time"]=signup_time
        lib["books_per_day"]=books_per_day
        lib["books"] = books
        result.append(lib)
    return result



def output(output_file, slideshow):
    # TODO aanpassen aan opgave, niet zo gebruiken!!!
    submission= open(output_file,"w+")
    c = len(slideshow)
    submission.write("%d \n" % c)
    for i in range(0,c):
        if isinstance(slideshow[i][0] , int):
            submission.write("%d \n" % slideshow[i][0])
        else:
            submission.write("%d" % slideshow[i][0][0])
            submission.write(" %d \n" % slideshow[i][0][1])


