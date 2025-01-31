import parser 

def libScore(daysForScanning, signupForLib, bookScores, nbBookinLib, booksPerDay):
    count = daysForScanning - signupForLib
    score = 0
    scannedbooks = 0
    while ((count >0) and  (nbBookinLib>0)):       
        count -= 1    
        for book in range(min(booksPerDay, nbBookinLib)):
            score += bookScores[nbBookinLib -1]
            nbBookinLib -= 1
            scannedbooks +=1
    return score, scannedbooks

#scores = alles scores van alle boeken
def sort_book_ids(books, scores):
    scores_for_lib = []
    for book in books:
        scores_for_lib.append(scores[book])
    return ([x for y,x in sorted(zip(scores_for_lib, books))], [y for y,x in sorted(zip(scores_for_lib, books))])



def optimalLibrary(daysForScanning, lstLibrary, AllBookScores, usedBooks):
    optScore= 0 
    optLib = None
    optOrderedBooks = []
    for lib in lstLibrary:
        books = [x for x in lib.get("books") if x not in usedBooks]
        bookscore = sort_book_ids(books, AllBookScores)
        books = len(lib.get("books"))
        currentScore = libScore(daysForScanning, lib.get("signup_time"), bookscore[1], lib.get("nb_books"), lib.get("books_per_day"))
        if (currentScore[0] > optScore): ## opt
            optScore = currentScore[0]
            optLib = lib
            optOrderedBooks = bookscore[-1:books-1-currentScore[1]: -1] 
    return optLib, optOrderedBooks

def libraryOrder(libs, deadline, scores): 
    libArray = []

    while (deadline > 0 and len(libs) > 0) : 
        opt_lib,_ = optimalLibrary(deadline, libs, scores)
        if opt_lib is None:
            break
        libArray.append(opt_lib)
        libs.remove(opt_lib)
        deadline -= opt_lib.get("signup_time")
    return libArray


#test1
scores = [3,5,9]
days = 7
signp = 2
r1 = libScore(days, signp, scores, 3, 1)

#test2
scores = [3,5,9]
days = 3
signp = 2
r = libScore(days, signp, scores, 3, 2)