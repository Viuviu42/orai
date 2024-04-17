class Kolcsonzo:
    def __init__(self,name,ids,sh,sm,eh,em):
        self.name = name
        self.ids = ids 
        self.sh = sh
        self.sm = sm 
        self.eh = eh
        self.em = em

file = open("kolcsonzesek.txt", "rt", encoding="utf-8")
kolcsonzesek = []
kolcson = []



for row in file:
   row = row.strip().split(";")
   kolcsonzesek.append(Kolcsonzo(row[0],row[1], row[2], row[3], row[4], row[5]))

print("5. feladat: Napi kölcsönzések száma:", len(kolcsonzesek)-1)

