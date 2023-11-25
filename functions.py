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

def min(directory):   #Fonction qui passe touts les caractère alphabétique d'une liste de fichier en minuscule
    L = list_of_files(directory, "txt")

    #Boucle pour pour appliquer la fonction a tout les fichiers du répertoire
    for i in range(len(L)):

        #Initialisation des variables utiles:
            #text est la variable qui sera utilié pour contenir le texte transformer en minuscule

        text = ""
            #emplacement et emplacement_cleaned sont les deux variable utilisé pour contenir les deux adresses utiles
        emplacement = directory + "/" + L[i]
        emplacement_cleaned = "./cleaned/" + L[i]

        #Ouverture du fichier avec des majuscules
        with open(emplacement,"r") as file:

            #Récuperation de son contenu dans la variable contenu
            contenu = file.read()

        #Ouverture du fichier sans majuscules
        with open(emplacement_cleaned,"w") as file_cleaned:

            #Parcour de chaque carcatères
            for char in contenu:

                #Récupération du code ascii de chaque caractères pour voir si c'est une majuscule ou pas
                ascii = ord(char)
                if ascii in range(65, 91):

                    #Si c'est le cas on la passe en minuscule et on l'ajoute a text
                    text += chr(ascii + 32)
                else:
                    #Sinon on la laisse en minuscule et on la stock
                    text += char
            #Ajout de text dans le fichier cleaned
            file_cleaned.write(text)

# Fonction pour afficher une liste sans doublons
def affiche_nom(List_noms):
    List_noms_sans_doublons = list(set(List_noms))
    print(List_noms_sans_doublons)

def remove_punctuation(directory):    #Fonction qui retire tt les ponctuation et les remplace par des espces si besoins

    #Initialisation du dictionnaire avec toutes les ponctutations concernées en clé et la valeurs est sois un espace sois rien
    Ponctuations = {",": '', "-": " ", "'": " ", ".": '', "!": '', "?": '', ":": '', "_": " "}
    #Initialisation de la list de tout les fichiers
    L = list_of_files(directory, "txt")

    #Boucle pour pour parcourir tous les fichiers
    for i in range(len(L)):

        #Initialisations des variable utiles, txt pour contenir le texte sans ponctuations et emplacement pour avoir l'adresse du répertoire
        txt = ''
        emplacement = directory + "/" + L[i]

        #Ouverture du fichier étudié et récupération de son contenus dans la variable contenu
        with open(emplacement,"r") as file:
            contenu = file.read()

        #Reouverture du fichier mais en w ce coups ci pour pour enlever les ponctuations
        with open(emplacement,"w") as file:

            #Parcour du fichier via contenu
            for char in contenu:

                #Si le charactère est dans le Dictionnaire ponctuation on le remplace par sa valeur
                if char in Ponctuations:
                    char = Ponctuations[char]

                #On ajoute le caractère dans txt
                txt += char

            #On écrit dans le fichier en mettant le texte sans les ponctuation
            file.write(txt)

def AddDic(d1,d2):   #Fonction qui permet de fusionner deux dictionnaires entre eux

    #Initialisaton du dictionnaire finale
    D = {}

    #
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
        nb_word_dic[cle] = math.log((len(file_list) / val) + 1)

    return nb_word_dic

def TF_IDF(word, idf, list_files):
    TF_IDF_LIST =[word]

    for i in range(len(list_files)):
        tf = TF(list_files[i])
        if word in tf and word in idf:
            TF_IDF = tf[word] * idf[word]
        else:
            TF_IDF = 0.0
        TF_IDF_LIST.append(TF_IDF)

    return TF_IDF_LIST

def Matrice_TF_IDF(directory):
    idf = IDF(directory)
    list_word = list_of_word()
    list_files = list_of_files(directory,".txt")

    Matrix = []

    for word in list_word:
        tf_idf = TF_IDF(word, idf, list_files)
        Matrix.append(tf_idf)

    return Matrix

Matrix = Matrice_TF_IDF("./cleaned")
for row in Matrix:
    print(row)