class Kolcsonzo:
    def __init__(self,name,ids,sh,sm,eh,em):
        self.name = name
        self.ids = ids 
        self.sh = sh
        self.sm = sm 
        self.eh = eh
        self.em = em

file = open("kolcsonzesek.txt", "rt")
for row in file:
   row = row.strip().split(";")
   kolcson = Kolcsonzo(row[0],row[1], row[2], row[3], row[4], row[5])
