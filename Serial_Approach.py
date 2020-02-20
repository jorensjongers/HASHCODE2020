from parser import *

def LibScore(daysForScanning, signupForLib, bookScores, nbBookinLib, booksPerDay):
    count = daysForScanning - signupForLib
    score = 0
    scannedbooks = 0
    while ((count >0) and  (nbBookinLib>0)):       
        count -= 1    
        for book in range(min(booksPerDay, nbBookinLib)):
            #print(book)
            score += bookScores[nbBookinLib -1]
            nbBookinLib -= 1
            scannedbooks +=1
    return score, scannedbooks

def optimalLibrary(daysForScanning, lstLibrary, AllBookScores):
    optScore= 0 
    optLib = None
    for lib in lstLibrary:
        bookscore = sort_book_ids(lib.get("books"), AllBookScores)
        currentScore = libScore(daysforScanning, lib.get("signup_time"), bookscores[1], lib.get("nb_books"), lib.get("books_per_day"))
        if (currentScore[0] > optScore): ## opt
            optScore = currentScore[0]
            optLib = lib
            optOrderedBooks = bookscore[-1:books-1-currentScore[1]: -1] 
    return optLib, optOrderedBooks

def libraryOrder(): 
    deadline = get_deadline()
    libArray = []
    while (deadline > 0) : 
        opt_lib = optimalLibrary(deadline, get_libraries())
        libArray.append(opt_lib)
        deadline -= opt_lib.get("signup_time")
    return libArray


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