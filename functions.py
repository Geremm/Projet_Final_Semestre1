import os
import math
def list_of_files(directory, extension):    #Fonction qui renvoie la liste des fichier présent dans le repertoire directory
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def extractnames(file):    #Fonction qui extrait les noms des présidents dans les noms des fichiers

    #Séparation du .txt du reste de la chaine de caractère
    name = file.split(".")

    #Séparation du Nomation_ du nom du président
    name = name[0].split("_")

    #Si il y a un numéro après le nom du président, il l'enlève et mets le nom du président dans une variable,
    if name[-1][-1] >= "0" and name[-1][-1] <= "9":
        NomPresident = name[-1].replace(name[-1][-1],'')

    #Sinon le programme mets juste le nom du président dans une variable
    else:
        NomPresident = name[-1]

    #Ajoute le nom du président a la liste du nom des présidents
    return NomPresident

def prenom_presidents(Nom):

    #Dictionnaire qui associe un nom de président a son prénom
    Nom_Prenom = {"Chirac":"Jacques", "Giscard dEstaing": "Valery", "Holland": "François", "Macron":"Emannuel", "Mitterand": "François", "Sarkozy": "Nicolas"}
    return Nom_Prenom[Nom]
def print_list(L):   #Fonction pour afficher une liste sans les crochets ni les guillets
    L = str(L)
    S = L.replace("[", '')
    a = S.replace("]", '')
    b = a.replace("'", '')
    return b

def min():
    for i in range(8):
        text = ""
        L = list_of_files(".\speeches", "txt")
        emplacement = "./speeches/" + L[i]
        emplacement_cleaned = "./cleaned/" + L[i]
        print(emplacement_cleaned)
        print(emplacement)
        with open(emplacement,"r") as file:
            contenu = file.read()
            with open(emplacement_cleaned,"w") as file_cleaned:
                for char in contenu:
                    ascii = ord(char)
                    if ascii in range(65, 91):
                        text += chr(ascii + 32)
                    else:
                        text += char
                file_cleaned.write(text)

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

def AddDic(d1,d2):
    D = {}
    for cle in set(d1.keys()) & set(d2.keys()):
        D[cle] = d1[cle] + d2[cle]
    for cle in d1.keys():
        if cle not in D:
            D[cle] = d1[cle]
    for cle in d2.keys():
        if cle not in D:
            D[cle] = d2[cle]

    return D


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

def Matrice_TF_IDF(Directory):

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
