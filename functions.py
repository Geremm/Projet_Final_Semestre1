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


def list_of_word():

    list = list_of_files("./cleaned", ".txt")

    list_of_word = []

    for file in list:
        Tf = TF(file)
        for word in Tf.keys():
            if word not in list_of_word:
                list_of_word.append(word)

    return list_of_word


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
    if word in tf and word in idf:
        TF_IDF = tf[word] * idf[word]
    else:
        TF_IDF = 0.0

    return TF_IDF

def Matrice(Directory):

    list_word = list_of_word()
    list_files = list_of_files("./cleaned",".txt")

    Matrix = []

    for i, word in enumerate(list_word):
        row = [word]
        for file in list_files:
            tf_idf = TF_IDF(word, file)
            row.append(tf_idf)
        Matrix.append(row)

    return Matrix





