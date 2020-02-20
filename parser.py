
import main as m
FILE_NAME = "b_lovely_landscapes.txt"
OUTPUT_FILE = "submission_landscape.txt"

f = open(FILE_NAME, "r")
H = []
V = []

def parse_input(file):
    list = [line.split(' ') for line in file.read().split('\n')]
    return list

def output(slideshow):
    submission= open(OUTPUT_FILE,"w+")
    c = len(slideshow)
    submission.write("%d \n" % c)
    for i in range(0,c):
        if isinstance(slideshow[i][0] , int):
            submission.write("%d \n" % slideshow[i][0])
        else:
            submission.write("%d" % slideshow[i][0][0])
            submission.write(" %d \n" % slideshow[i][0][1])

final = ""
output(final)
