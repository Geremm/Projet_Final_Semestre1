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

def print_list(L):
    L = str(L)
    S = L.replace("[", '')
    a = S.replace("]", '')
    b = a.replace("'", '')
    return b
def affiche_nom(List_noms):
    List_noms_sans_doublons = []
    for i in range(len(List_noms)):
        if List_noms[i] not in List_noms_sans_doublons:
            List_noms_sans_doublons.append(List_noms[i])
    return print_list(List_noms_sans_doublons)

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

def remove_ponctuation():
    Ponctuations = {",": '', "-": " ", "'": " ", ".": '', "!": '', "?": '', ":": '', "_": " "}
    for i in range(8):
        txt = ''
        L = list_of_files(".\cleaned", "txt")
        emplacement = "./cleaned/" + L[i]
        with open(emplacement,"r") as file:
            contenu = file.read()
        with open(emplacement,"w") as file:
            for val in contenu:
                if val in Ponctuations:
                    print(Ponctuations[val])
                    val = Ponctuations[val]
                txt += val

            file.write(txt)


# Fonctions TF-IDF


# Création d'une liste pour ouvir chaque fichier dans une boucle

name = ['Chirac1', 'Chirac2', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand1', 'Mitterrand2', 'Sarkozy']
list_of_files = []

for i in name:
    w = f"./cleaned/Nomination_{i}.txt"
    list_of_files.append(w)


# Fonction qui renvoie un dic associant le nombre de fois qu'un mot apparait dans un fichier (TF)
def TF(file):

    #Ajout de chaque mot issue d'un fichier  dans une liste
    with open(file, 'r') as f:
        list_of_word = []
        files = f.read().split()
        for word in files:
            list_of_word.append(word)

    # creation du dic associant le nombre de fois qu'un mot apparait dans un fichier

        nb_word_dic = dict()
        for i in list_of_word:
            if i in nb_word_dic:
                nb_word_dic[i] += 1
            else:
                nb_word_dic[i] = 1

    return nb_word_dic

# Fonction qui renvoie l'IDF d'un mot
def IDF(word):

    # Iteration pour trouver le mot dans chaque doc

    counter = 0
    for i in list_of_files:
        with open(f"{i}", "r") as f:
            files = f.read().split()
            if word in files:
                counter += 1

    # Calcule de la proportion du mot dans chaque doc + score IDF

    proportion_word = counter / len(list_of_files)

    if proportion_word == 0:
        score_IDF = 0
    else:
        score_IDF = math.log(1 / proportion_word)

    return score_IDF

# Fonction qui renvoie un dic associant à chaque mot son IDF
def dic_score_IDF():

    dic_score_IDF = dict()

    for file in list_of_files:
        with open(f"{file}", "r") as f:
            word = f.read().split()
            for word in file:
                score_IDF = IDF(word)
                dic_score_IDF[word] = score_IDF

    return dic_score_IDF


#Fonction qui calcule le score TF-IDF
def TF_IDF(word,file):

    IDF = dic_score_IDF()
    TF = TF(file)
    score_TF_IDF = IDF[word] * TF[word]

    return score_TF_IDF

#Fonction qui renvoie une matrice de tout les scores TF-IDF de chaque mot dans chaque fichier
def Matrice_TF_IDF(list_of_files):


    Matrice_TF_IDF = []

    for file in list_of_files:
        contenu = TF(file)
        M1 = []
        for word in contenu:
            score_idf = TF_IDF(word, file)
            M1.append(score_idf)
        Matrice_TF_IDF.append(M1)

    #Matrice de transposition

    Matrice_TF_IDF_transpose = []

    for i in range(len(Matrice_TF_IDF[0])):
        transpose_line = []
        for j in range(len(Matrice_TF_IDF)):
            transpose_line.append(Matrice_TF_IDF[j][i])
        Matrice_TF_IDF_transpose.append(transpose_line)


    return Matrice_TF_IDF_transpose




directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)
print(affiche_nom(['Chirac', 'Chirac', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Mitterrand', 'Sarkozy']))
print(min())
print(remove_ponctuation())