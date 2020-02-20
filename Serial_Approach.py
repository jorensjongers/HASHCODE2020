from parser import *

def LibScore(daysForScanning, signupForLib, bookScores, nbBookinLib, booksPerDay):
    count = daysForScanning - signupForLib
    score = 0

    while ((count >0) and  (nbBookinLib>0)):       
        count -= 1    
        for book in range(min(booksPerDay, nbBookinLib)):
            #print(book)
            score += bookScores[nbBookinLib -1]
            nbBookinLib -= 1
    return score


def optimalLibrary(daysForScanning, lstLibrary, AllBookScores):
    optScore= 0 
    optLib = None
    for lib in lstLibrary:
        bookscore = sort_book_ids(lib.get("books"), AllBookScores)[1]
        currentScore = libScore(daysforScanning, lib.get("signup_time"), bookscores, lib.get("nb_books"), lib.get("books_per_day"))
        if (currentScore > optScore): ## opt
            optScore = currentScore
            optLib = lib
    return optLib

def libraryOrder(): 
    deadline = get_deadline()

    while (deadline > 0) : 
        opt_lib = optimalLibrary(deadline, get_libraries())

    return 


#test1
scores = [3,5,9]
days = 7
signp = 2
r1 = LibScore(days, signp, scores, 3, 1)

#test2
scores = [3,5,9]
days = 3
signp = 2
r = LibScore(days, signp, mean(scores), 3, 2)