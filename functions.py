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

def min_directory(directory):   #Fonction qui passe touts les caractère alphabétique d'une liste de fichier en minuscule
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
    Dic_contracte = {"l": ["le", "la"], "qu": ["que", "qui"], "n": ["ne"], "d": ["de"], "s": ["se", "sa"], "j": ["je"], "aujourd": ["aujourdhui"], "jusqu": ["jusque"], "hui": [""], "m": ["me", "ma"], "c":["cela"]}
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

def IDF(directory, stopword):     #Fonction qui fiat le score IDF de tout les mots d'un répertoire

    #Initialisation de la list des fichiers et du dictionnaire final
    file_list = list_of_files(directory, ".txt")
    nb_word_dic = dict()

    #Parcours de tout les fichiers et utilisation de TF pour avoir tout les mots d'un fichier sans doublon
    for file in file_list:
        nb_word = TF(file)

        #Parcours de tout les mots du fichier, si le mot est dans le dictionnaire on mets + 1 sinon on l'initialise a 1
        for i in nb_word:
            if i in nb_word_dic and i not in stopword:
                nb_word_dic[i] += 1
            elif i not in stopword:
                nb_word_dic[i] = 1
    #On parcours le dictionnaire final pour appliquer la formule de l'IDF
    for cle, val in nb_word_dic.items():
        nb_word_dic[cle] = math.log10((len(file_list)) / val)

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
    idf = IDF(directory,stop_word_list)
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
def Matrice_without_word(directory):
    M = Matrice_TF_IDF(directory)
    Matrix_without_Word = []

    for i in range(len(M)):
        Matrix_without_Word.append([])
        for j in range(len(M[i])):
            if M[i][j] != M[i][0]:
                Matrix_without_Word[i].append(M[i][j])
    return Matrix_without_Word

Matrix_without_Word = Matrice_without_word("./cleaned")
def transpose(matrix):
    result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]

    return result

def min(str):
    txt = ''
    for char in str:
        if ord(char) >= 65 and ord(char) <= 90:
            txt += chr(ord(char) + 32)
        else:
            txt += char

    return txt

def traitement_question(question):
    Dic_contracte = {"l": ["le", "la"], "qu": ["que", "qui"], "n": ["ne"], "d": ["de"], "s": ["se", "sa"], "j": ["je"], "aujourd": ["aujourdhui"], "jusqu": ["jusque"], "hui": [""], "m": ["me", "ma"], "c": ["cela"]}
    indice_remove = []
    stopword = stop_word()
    question = remove_punctuation(question)
    question = min(question)
    question = question.split()
    for i in range(len(question)):
        if question[i] in Dic_contracte:
            r = randint(0, len(Dic_contracte[question[i]]) - 1)
            question[i] = Dic_contracte[question[i]][r]

        if question[i] in stopword:
            indice_remove.append(i)
    for j, i in enumerate(indice_remove):
        question.remove(question[i-j])
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


def TF_IDF_question(question, directory):
    stopword = stop_word()
    TF_dic_qst = dict()

    for word in question:
        if word in TF_dic_qst.keys():
            TF_dic_qst[word] += 1
        else:
            TF_dic_qst[word] = 1

    vector = []
    dic_idf = IDF(directory, stopword)
    for word in dic_idf.keys():
        if word in question:
            val = TF_dic_qst[word] * dic_idf[word]
            vector.append(val)
        else:
            vector.append(0.0)
    return vector

def Vector_B(num):

    Vector = []
    Matrix = transpose(Matrix_without_Word)
    for i in range(len(Matrix)):
        if i == (num - 1):
            for j in range(len(Matrix[i])):
                Vector.append(Matrix[i][j])

    return Vector

def dot_product(VectorA, VectorB):

    dot_product = 0
    for i in range(len(VectorA)):
        dot_product += VectorA[i] * VectorB[i]
    return dot_product


def norm(vecteur):

    summ = 0
    for val in vecteur:
        summ += val**2
    norme = math.sqrt(summ)
    return norme


def cosine_similarity(question,num):

    VectorA = TF_IDF_question(question, "./cleaned")
    VectorB = Vector_B(num)
    Dot_product = dot_product(VectorA,VectorB)
    norm1 = norm(VectorA)
    norm2 = norm(VectorB)
    if norm1*norm2 == 0:
        return 0
    cosine_similarity = Dot_product/(norm1*norm2)


    return cosine_similarity


def most_relevant_doc(question):

    max = 0
    cosin_sim_list = []
    list_file = list_of_files("./cleaned",".txt")

    for i in range(1,len(list_file)+1):
        sim = cosine_similarity(question,i)
        cosin_sim_list.append(sim)

    for i in range(len(cosin_sim_list)):
        if cosin_sim_list[i] > max:
            max = cosin_sim_list[i]

    index = cosin_sim_list.index(max)


    list = list_of_files("./speeches",".txt")

    return list[index]
def TFIDF_Max(question, list_idf):
    List = TF_IDF_question(question, "./cleaned")
    max = List[0]
    index_max = 0
    Change = False
    for i in range(len(List)):
        if List[i] > max:
            max = List[i]
            index_max = i
            Change = True

    if Change == False:
        return False

    return list_idf[index_max]

def traitement_reponse_starter(answer):
    answer = min(answer)
    txt = ''
    alphabet = [chr(char) for char in range(ord('a'), ord('z')+1)]
    i = 0
    while answer[i] not in alphabet:
        i += 1
    for j in range(i, len(answer)):
        txt += answer[j]
    return txt

def traitement_reponse(answer):
    answer = min(answer)
    txt = ''
    alphabet = [chr(char) for char in range(ord('a'), ord('z')+1)]
    i = 0
    while answer[i] not in alphabet:
        i += 1

    txt += chr(ord(answer[i]) - 32)
    for j in range(i + 1, len(answer)):
        txt += answer[j]
    return txt


def reponse(question,stopword):
    question = traitement_question(question)
    dic_idf = IDF("./cleaned", stopword)
    list_idf = [key for key in dic_idf.keys()]
    word = TFIDF_Max(question, list_idf)

    if word == False:
        return "Base de donnée insuffisante pour répondre à cette question."

    doc = most_relevant_doc(question)
    with open(f"./cleaned/{doc}", 'r', encoding="utf-8") as f:
        Find = False
        ligne = -1
        while Find == False:
            ligne += 1
            content = f.readline()
            if word in content[:-1]:
                Find = True
    with open(f"./speeches/{doc}", "r", encoding="utf-8") as f:
        a = f.readlines()
        return a[ligne]

def answer_with_starters(question, stopword):
    question_starters = {"Comment": "Après analyse, ", "Pourquoi": "Car, ", "Peux-tu": "Oui, bien sûr!"}
    list_Question = question.split()
    answer = reponse(question, stopword)
    if answer == "Base de donnée insuffisante pour répondre à cette question.":
        return "Base de donnée insuffisante pour répondre à cette question.\n"

    if list_Question[0] in question_starters.keys():
        Starter = question_starters[list_Question[0]]
        return Starter + " " + traitement_reponse_starter(answer)
    return traitement_reponse(answer)
