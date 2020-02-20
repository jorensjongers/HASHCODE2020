def parse_input(file):
    list = [line.split(' ') for line in file.read().split('\n')]
    return list

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


