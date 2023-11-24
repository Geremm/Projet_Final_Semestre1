import os
import math

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def extract_names(L):
    T = []
    for i in range(len(L)):
        L[i] = L[i].split(".")
        L[i][0] = L[i][0].split("_")
        if L[i][0][-1][-1] >= "0" and L[i][0][-1][-1] <= "9":
            a = L[i][0][-1].replace(L[i][0][-1][-1],'')
        else:
            a = L[i][0][-1]
        T.append(a)
    return T

def prenom_presidents(List_noms):
    Nom_Prenom = {"Chirac":"Jacques", "Giscard dEstaing": "Valery", "Holland": "François", "Macron":"Emannuel", "Mitterand": "François", "Sarkozy": "Nicolas"}

# Fonction pour afficher une liste sans doublons
def affiche_nom(List_noms):
    List_noms_sans_doublons = list(set(List_noms))
    print(List_noms_sans_doublons)

def remove_punctuation():
    Ponctuations = {",": '', "-": " ", "'": " ", ".": '', "!": '', "?": '', ":": '', "_": " "}
    for i in range(8):
        txt = ''
        L = list_of_files("./cleaned", "txt")
        emplacement = "./cleaned/" + L[i]
        with open(emplacement,"r") as file:
            contenu = file.read()
        with open(emplacement,"w") as file:
            for val in contenu:
                if val in Ponctuations:
                    val = Ponctuations[val]
                txt += val

            file.write(txt)

# Fonctions TF-IDF
def TF(file):
    with open(f"./cleaned/{file}", 'r') as f:
        list_of_word = f.read().split()

        nb_word_dic = dict()

        for i in list_of_word:
            if i in nb_word_dic:
                nb_word_dic[i] += 1
            else:
                nb_word_dic[i] = 1

        return nb_word_dic

def IDF(directory):
    file_list = list_of_files(directory, ".txt")

    nb_word_dic = dict()

    for file in file_list:
        nb_word = TF(file)
        for i in nb_word:
            if i in nb_word_dic:
                nb_word_dic[i] += 1
            else:
                nb_word_dic[i] = 1

    for cle, val in nb_word_dic.items():
        nb_word_dic[cle] = math.log((len(file_list) / val))

    return nb_word_dic

def TF_IDF(word, file):

    tf = TF(file)
    idf = IDF("./cleaned")
    TF_IDF = tf[word] * idf[word]

    return TF_IDF

def Str_file(file):
    with open(f"./cleaned/{file}", 'r') as f:
        contenu = f.read()
        return contenu
def Matrix_TF_IDF(directory):


    Matrix_tf_idf = []

    file_list = list_of_files(directory, "txt")

    for i in range(len(file_list)):
        if i == 4:
            pass
        Matrix_tf_idf.append([])
        file = file_list[i]
        dic_file = TF(file)
        for word in dic_file:
            tf_idf = TF_IDF(word, file)
            Matrix_tf_idf[i].append(word + " : " + str(tf_idf))
        """
        StrDoc = Str_file(file).split()
        print(StrDoc)
        print(len(Matrix_tf_idf[i]), len(StrDoc))
        """
    return Matrix_tf_idf


def Transpose_Matrix(matrice):
    #Initialisation du nombre de ligne et de colonnes
    nombre_lignes = len(matrice)
    nombre_colonnes = max(len(ligne) for ligne in matrice)

    #Initialiser de la matrice transposée
    matrice_transposee = [[] for i in range(nombre_colonnes)]

    #Remplissage de la matrice
    for i in range(nombre_lignes):
        for j in range(len(matrice[i])):
            matrice_transposee[j].append(matrice[i][j] if j < len(matrice[i]) else None)
    return matrice_transposee

def transfo_dic_list(dic):
    T = []
    for key in dic.keys():
        T.append(key)
    return T
def Mot_via_scoreTFIDF(directory,i,j):
    list = list_of_files(directory, "txt")
    file = list[j]
    tf = TF(file)
    tf = transfo_dic_list(tf)
    print(tf, "\n", len(tf), i, file)
    mot = tf[i]
    return mot
#print(Mot_via_scoreTFIDF("./cleaned",3,4))

Matrix = Matrix_TF_IDF("./cleaned")
for i in range(len(Matrix)):
    print(Matrix[i])

"""
Matrix = Matrix_TF_IDF("./cleaned")
Matrix_Transposee = Transpose_Matrix(Matrix)

print("\n")

for ligne in Matrix_Transposee:
    print(ligne)
    """