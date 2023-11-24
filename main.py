from functions import *

#Matrix = Matrice_TF_IDF("./cleaned")
file1 = "Nomination_Chirac1.txt"
file2 = "Nomination_CHirac2.txt"
DicTxt1 = TF(file1)
DicTxt2 = TF(file2)
DicChirac = AddDic(DicTxt1,DicTxt2)
T = []
max = 0
for cle, val in DicChirac.items():
    if max < val:
        T = []
        max = val
        T.append(cle)
    elif max == val:
        T.append(cle)
print(T)
print(max)

mot = "climat"
Trouve = False
i = 0
list_files = list_of_files("./cleaned",".txt")
while not Trouve:
    tf = TF(list_files[i])
    for cle in tf.keys():
        if cle == mot:
            Trouve = True
            print(list_files[i])
    i += 1