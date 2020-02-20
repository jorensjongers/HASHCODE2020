def LibScore(daysForScanning, signupForLib, bookScores, nbBookinLib, booksPerDay):
    count = daysForScanning - signupForLib
    score = 0

    while ((count >0) and  (nbBookinLib>0)):       
        count -= 1    
        for book in range(min(booksPerDay, nbBookinLib)):
            print(book)
            score += bookScores[nbBookinLib -1]
            nbBookinLib -= 1
    return score


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