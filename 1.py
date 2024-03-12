import csv

def vstavka(data):
    pass


with open ('0students.csv') as f, open('student_new.csv', 'a') as nf:
    data = list(csv.reader(f, delimiter=';'))
    print(*data, sep = '\n')


