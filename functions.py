import os
import math
from random import *
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

def remove_punctuation_directory(directory):    #Fonction qui retire tt les ponctuation et les remplace par des espces si besoins

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

def remove_punctuation(str):

    # Initialisation du dictionnaire avec toutes les ponctutations concernées en clé et la valeurs est sois un espace sois rien
    Ponctuations = {",": '', "-": " ", "'": " ", ".": '', "!": '', "?": '', ":": '', "_": " "}

    #Initialisation du str final
    txt = ''

    # Parcour du fichier via contenu
    for char in str:

        # Si le charactère est dans le Dictionnaire ponctuation on le remplace par sa valeur
        if char in Ponctuations:
            char = Ponctuations[char]

        # On ajoute le caractère dans txt
        txt += char
    return txt


def AddDic(d1,d2):   #Fonction qui permet de fusionner deux dictionnaires entre eux

    #Initialisaton du dictionnaire finale
    D = {}

    #On prend toute les cle communes des deux tableau et on additionne leur valeurs
    for cle in set(d1.keys()) & set(d2.keys()):
        D[cle] = d1[cle] + d2[cle]
    #On rajoute au dictionnaire final les clefs et les valeurs qui ne sont pas dans D
    for cle in d1.keys():
        if cle not in D:
            D[cle] = d1[cle]
    #De même avec d2
    for cle in d2.keys():
        if cle not in D:
            D[cle] = d2[cle]

    return D


def list_of_word(directory,stop_word):     #Fonction qui fait la liste de tout les mots de tout les documents

    #Initialisation de la list de tout les fichiers et du tableua qui va contenir tout les mots
    list = list_of_files(directory, ".txt")
    list_word = []

    #On fait une boucle qui parcour tout les fichiers
    for file in list:

        #On utilise la fonction TF pour avoir la list de tout les mots dans un document
        Tf = TF(file)

        #On ajoute tout les mots du fichiers dans list_word en vérifiant que le mot n'y est pas deja
        for word in Tf.keys():
            if word not in list_word and word not in stop_word:
                list_word.append(word)

    return list_word

def stop_word():
    with open("stop_word.txt", "r", encoding="utf-8") as f:
        content = f.read()
        content = content.split("-")
    return content

def mot_non_important(Matrix):
    non_important = []
    for i in  range(len(Matrix)):
        s = 0
        for j in range(1, len(Matrix[i])):
            s += Matrix[i][j]
        if s == 0:
            non_important.append(Matrix[i][0])
    return non_important




#============================= Fonctions TF-IDF

def TF(file):    #Fonction TF
    Dic_contracte = {"l": ["le", "la"], "qu": ["que", "qui"], "n": ["ne"], "d": ["de"], "s": ["se", "sa"], "j": ["je"], "aujourd": ["aujourdhui"], "jusqu": ["jusque"], "hui": [""], "m": ["me", "ma"]}
    #Ouvertuire du fichier étudié
    with open(f"./cleaned/{file}", 'r', encoding="utf-8") as f:

        #Initialisation de la list de tout les mots du fichier et du dictionnaire final
        list_word = f.read().split()
        nb_word_dic = dict()

        #On parcours les mots et si il sont deja dans le dictionnaire on ajoute 1, sinon on initialise la valeur du mot à 1
        for i in list_word:
            if i in Dic_contracte:
                r = randint(0, len(Dic_contracte[i]) - 1)
                i = Dic_contracte[i][r]
            if i in nb_word_dic:
                nb_word_dic[i] += 1
            else:
                nb_word_dic[i] = 1

        return nb_word_dic

def IDF(directory):     #Fonction qui fiat le score IDF de tout les mots d'un répertoire

    #Initialisation de la list des fichiers et du dictionnaire final
    file_list = list_of_files(directory, ".txt")
    nb_word_dic = dict()

    #Parcours de tout les fichiers et utilisation de TF pour avoir tout les mots d'un fichier sans doublon
    for file in file_list:
        nb_word = TF(file)

        #Parcours de tout les mots du fichier, si le mot est dans le dictionnaire on mets + 1 sinon on l'initialise a 1
        for i in nb_word:
            if i in nb_word_dic:
                nb_word_dic[i] += 1
            else:
                nb_word_dic[i] = 1
    #On parcours le dictionnaire final pour appliquer la formule de l'IDF
    for cle, val in nb_word_dic.items():
        nb_word_dic[cle] = math.log10((len(file_list) / val))

    return nb_word_dic

def TF_IDF(word, idf, list_files):   #Fonction qui le TF IDF de 1 mot dans tout les documents

    #Initialisation de la ligne final avec le mot étudié
    TF_IDF_LIST =[word]

    #Parcour de tout les fichiers initialisation de la variable tf
    for i in range(len(list_files)):
        tf = TF(list_files[i])

        #Si le mot est dans le dictionnaire tf et idf alors on fait le produit du score TF et IDF
        if word in tf and word in idf:
            TF_IDF = tf[word] * idf[word]
        #Sinon le score TF_IDF vaut 0.0
        else:
            TF_IDF = 0.0
        #On ajoute le score TF_IDF de ce mot dans la ligne de score TF IDF
        TF_IDF_LIST.append(TF_IDF)

    return TF_IDF_LIST

def Matrice_TF_IDF(directory):   #Fonction qui fait la matrice TF_IDF

    #Initialisation de la list des stop words
    stop_word_list = stop_word()
    #Initialisation de toutes les varaibles utiles comme le score idf du repertorie, la list de tout les mots dans le répertoire et la list de tout les fichiers et de la Matrice
    idf = IDF(directory)
    list_word = list_of_word(directory, stop_word_list)
    list_files = list_of_files(directory,".txt")
    Matrix = []

    #Parcours de la list contenant tout les mots de tout les fichiers
    for word in list_word:

        #Ajout de la ligne avec le score TF_IDF du mot étudié
        tf_idf = TF_IDF(word, idf, list_files)
        Matrix.append(tf_idf)
    return Matrix

""""==================================================== Partie 2 =================================================================="""""

M = Matrice_TF_IDF("./cleaned")
Matrix_without_Word = []

for i in range(len(M)):
    Matrix_without_Word.append([])
    for j in range(len(M[i])):
        if M[i][j] != M[i][0]:
            Matrix_without_Word[i].append(M[i][j])


def transpose(matrix):
    result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]

    return result


def traitement_question(question):
    question = remove_punctuation(question)
    question = question.split()
    return question

def mot_communs(question, directory):
    list_files = list_of_files(directory, ".txt")
    communs = []
    for file in list_files:
        tf = TF(file)
        for mot in question:
            if mot in tf and mot not in communs:
                communs.append(mot)
    return communs


def TF_IDF_question(question):

    qst = traitement_question(question)
    TF_dic_qst = dict()

    for word in qst:
        if word in TF_dic_qst.keys():
            TF_dic_qst[word] += 1
        else:
            TF_dic_qst[word] = 1

    vector = []
    dic_idf = IDF("./cleaned")

    for word in dic_idf.keys():
        if word in qst:
            val = TF_dic_qst[word] * dic_idf[word]
            vector.append(val)
        else:
            vector.append(0)

    return vector

def Vector_B(numberDoc):

    VectorB = []
    for i in range(len(Matrix_without_Word)):
        if i == numberDoc:
            for j in range(len(Matrix_without_Word[i])):
                VectorB.append(Matrix_without_Word[i][j])

    return VectorB

def dot_product(question, numberdoc):

    dot_product = 0
    VectorA = TF_IDF_question(question)
    VectorB = Vector_B(numberdoc)

    for i in range(len(VectorA)):
        for j in range(len(VectorB)):
            dot_product += VectorA[i] * VectorB[j]

    return dot_product


def norm(vecteur):
    summ = 0
    for val in vecteur:
        summ += val**2
    return math.sqrt(summ)


def cosine_similarity(question,numberdoc):

    VectorA = TF_IDF_question(question)


    VectorB = Vector_B(numberdoc)
    Dot_product = dot_product(question,numberdoc)
    norm1 = norm(VectorA)
    norm2 = norm(VectorB)
    cosine_similarity = Dot_product/(norm1*norm2)


    return cosine_similarity


