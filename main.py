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


f2 = input("Voulez-vous savoir quel(s) est/sont le(s) mot(s) avec le plus grand score TF IDF ? : (y) or (n) ")
f2 = f2.lower()

if f2 == "y":

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

    print("Le(s) mot(s) qui a/ont le score TF-IDF le plus élevé est/sont :")

    for row in list_of_biggest_TFIDF:
        print(row)




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

word_search = input("Quel mot voulez-vous chercher ? : ")
word_search = word_search.lower()

Max = 0
M = []

for file in list_file:
    dic_word = TF(file)
    for word in dic_word.keys():
        if word == word_search:
            M.append(file)
            if dic_word[word_search] >= Max:
                Max = dic_word[word_search]
if Max == 0:
    print("Aucun président n'a prononcé le mot recherché")
else:
    M2 = []
    for file in M:
        name = extractnames(file)
        M2.append(name)
    for i in range(len(M2) - 1):
        if M2[i] != M2[i + 1]:
            print(f"{M2[i]} a prononcé le mot : {word_search}")

if Max == 0:
    w = 0
else:
    w = input(f"Voulez-vous savoir quel(s) président(s) a/ont répété le plus de fois le mot : {word_search} ? (y) or (n) : ")
    w = w.lower()

    if w == 'y':
        M3 = []
        for file in M:
            dic_word = TF(file)
            if dic_word[word_search] == Max:
                name = extractnames(file)
                M3.append(name)
        if len(M3) > 1:
            print(f"c'est {M3[0]} qui a repeté le plus de fois ce mot")
            print("Ainsi que")
            for i in range(1, len(M3)):
                print(M3[i])
        else:
            print(f"c'est {M3[0]} qui a repeté le plus de fois ce mot")



#Fonctionalité 5


mot = input("Quel mot voulez-vous chercher")
find = False
i = 0
list_files = list_of_files("./cleaned",".txt")

while not find:
    tf = TF(list_files[i])
    for cle in tf.keys():
        if cle == mot:
            find = True
            print(list_files[i])
    i += 1
