from functions import *

Matrix_tf_idf = Matrice_TF_IDF("./cleaned")
list_file = list_of_files("./cleaned",".txt")

#fonctionalité 1
list_of_non_important_words = []

for i in range(len(Matrix_tf_idf)):
    summ = 0
    for j in range(1, len(Matrix_tf_idf[i])):
        summ += Matrix_tf_idf[i][j]
    if summ == 0:
        list_of_non_important_words.append(Matrix_tf_idf[i][0])


print(list_of_non_important_words)

#fonctionalité 2
Max_TF_idf = []

Max = 0

for i in range(len(Matrix_tf_idf)):
    for j in range(1, len(Matrix_tf_idf[i])):
        if Matrix_tf_idf[i][j] > Max:
            Max = Matrix_tf_idf[i][j]

list_of_biggest_TFIDF = []

for i in range(len(Matrix_tf_idf)):
    for j in range(1, len(Matrix_tf_idf[i])):
        if Matrix_tf_idf[i][j] == Max:
            list_of_biggest_TFIDF.append(Matrix_tf_idf[i][0])


print(list_of_biggest_TFIDF)



#Fonctionalité 3
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



#Fonctionalité 4


Max = 0
list_president_nation = []
list_nation = []

for file in list_file:
    dic_word = TF(file)
    for word in dic_word.keys():
        if word == 'nation':
            list_president_nation.append(file)
            if dic_word['nation'] >= Max:
                Max = dic_word['nation']

for file in list_president_nation:
    president = extractnames(file)
    print(f"{president} à prononcé le mot Nation")

for file in list_president_nation:
    dic_word = TF(file)
    if dic_word['nation'] == Max:
        name = extractnames(file)
        list_nation.append(name)

print(list_nation)

#Fonctionalité 5
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