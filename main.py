# Importation des fonctions depuis le module functions
from functions import *

# Obtention de la matrice TF-IDF à partir des fichiers nettoyés
Matrix_tf_idf = Matrice_TF_IDF("./cleaned")
list_file = list_of_files("./cleaned", ".txt")

# Lecture du contenu du fichier "./Project_Presentation"
with open("./Project_Presentation", "r") as f:
    content = f.read()
    print(content)

# Initialisation de la variable de fin du programme
end = False

# Boucle principale du programme
while not end:
    # Saisie de la fonctionnalité choisie par l'utilisateur
    func = input("Saisir la fonctionnalité de votre choix (numéros de la fonctionnalité (Ex : 1) ) : ")

    if func == "1":
        # Fonctionnalité 1 : Mots les moins importants
        f1 = input("Voulez-vous savoir quels sont les mots les moins importants dans tous les discours : (y) or (n) ")
        f1.lower()
        if f1 == "y":
            list_of_non_important_words = []

            # Parcours de chaque ligne de la matrice
            for i in range(len(Matrix_tf_idf)):
                summ = 0
                # Calcul de la somme des scores TF-IDF pour chaque mot
                for j in range(1, len(Matrix_tf_idf[i])):
                    summ += Matrix_tf_idf[i][j]
                # Si la somme est nulle, le mot est ajouté à la liste des mots moins importants
                if summ == 0:
                    list_of_non_important_words.append(Matrix_tf_idf[i][0])

            print("Voici le(s) mot(s) le(s) moins important dans tous les discours :")

            # Affichage des mots moins importants
            for row in list_of_non_important_words:
                print(row, ",", end=" ")

    elif func == "2":
        # Fonctionnalité 2 : Mot avec le plus grand score TF IDF
        f2 = input("Voulez-vous savoir quel(s) est/sont le(s) mot(s) avec le plus grand score TF IDF ? : (y) or (n) ")
        f2 = f2.lower()
        if f2 == "y":
            Max_TF_idf = []
            Max = 0

            # Parcours de chaque ligne de la matrice
            for i in range(len(Matrix_tf_idf)):
                # Parcours de chaque score TF-IDF dans la ligne
                for j in range(1, len(Matrix_tf_idf[i])):
                    # Recherche du score TF-IDF le plus élevé
                    if Matrix_tf_idf[i][j] > Max:
                        Max = Matrix_tf_idf[i][j]

            list_of_biggest_TFIDF = []

            # Recherche des mots avec le score TF-IDF le plus élevé
            for i in range(len(Matrix_tf_idf)):
                for j in range(1, len(Matrix_tf_idf[i])):
                    if Matrix_tf_idf[i][j] == Max:
                        list_of_biggest_TFIDF.append(Matrix_tf_idf[i][0])

            print("Le(s) mot(s) qui a/ont le score TF-IDF le plus élevé est/sont :")

            # Affichage des mots avec le score TF-IDF le plus élevé
            for row in list_of_biggest_TFIDF:
                print(row)

    elif func == "3":
        # Fonctionnalité 3 : Mot le plus prononcé par un président
        f3 = input("Souhaitez-vous voir le mot le plus prononcé par le président de votre choix ? (y) or (n) : ")
        f3 = f3.lower()
        if f3 == "y":
            president = input("Quel président voulez-vous choisir ? : ")
            name = ' '
            stopword = stop_word()
            non_important = mot_non_important(Matrix_tf_idf)
            i = 0

            # Recherche du président spécifié dans les noms de fichiers
            while name != president:
                name = extractnames(list_file[i])

                if name == president and list_file[i] != list_file[i + 1]:
                    T = []
                    max = 0
                    DicTxt = TF(list_file[i])

                    # Recherche du mot le plus prononcé dans le discours du président
                    for cle, val in DicTxt.items():
                        if max < val and cle not in non_important and cle not in stopword:
                            print(cle)
                            T = []
                            max = val
                            T.append(cle)
                        elif max == val and val not in non_important and cle not in stopword:
                            T.append(cle)

                    # Affichage du mot le plus prononcé
                    if len(T) > 1:
                        print(f"{president} a prononcé le plus de fois le mot : {T[0]}")
                        for i in range(1, len(T)):
                            print(f"ainsi que le mot : {T[i]}")
                    else:
                        print(f"{president} a prononcé le plus de fois le mot : {T[0]}")

                # Recherche du mot le plus prononcé dans le discours du président (Si il y a 2 fichiers du même president
                elif name == president and list_file[i] == list_file[i + 1]:
                    file1 = f"{list_file[i]}"
                    file2 = f"{list_file[i + 1]}"

                    DicTxt1 = TF(file1)
                    DicTxt2 = TF(file2)
                    Dic_merge = AddDic(DicTxt1, DicTxt2)

                    T = []
                    max = 0

                    for cle, val in Dic_merge.items():
                        if max < val and cle not in non_important and cle not in stopword:
                            T = []
                            max = val
                            T.append(cle)
                        elif max == val and cle not in non_important and cle not in stopword:
                            T.append(cle)

                    # Affichage du mot le plus prononcé
                    if len(T) > 1:
                        print(f"{president} a prononcé le plus de fois le mot : {T[0]}")
                        for i in range(1, len(T)):
                            print(f"ainsi que le mot : {T[i]}")
                    else:
                        print(f"{president} a prononcé le plus de fois le mot : {T[0]}")

                else:
                    i += 1

    elif func == "4":
        # Fonctionnalité 4 : Noms du président et répétition d'un mot
        f4 = input(
            "Voulez-vous savoir quel est/sont le(s) nom(s) du (des) président(s) qui a (ont) parlé du mot de votre choix ainsi que celui qui l’a répété le plus de  fois ? (y) or (n) : ")
        f4 = f4.lower()
        if f4 == "y":
            word_search = input("Quel mot voulez-vous chercher ? : ")
            word_search = word_search.lower()
            Max = 0
            M = []

            # Recherche du mot spécifié dans chaque discours
            for file in list_file:
                dic_word = TF(file)

                # Recherche de la répétition du mot et mise à jour du maximum
                for word in dic_word.keys():
                    if word == word_search:
                        M.append(file)
                        if dic_word[word_search] >= Max:
                            Max = dic_word[word_search]

            if Max == 0:
                print("Aucun président n'a prononcé le mot recherché")
            else:
                M2 = []
                i = 0

                # Recherche des noms des présidents
                for file in M:
                    name = extractnames(file)
                    if name in M2:
                        continue
                    else:
                        M2.append(name)

                if len(M2) > 1:
                    for i in range(len(M2) - 1):
                        if M2[i] != M2[i + 1]:
                            print(f"{M2[i]} a prononcé le mot : {word_search}")
                        elif M2[i] == M2[i + 1]:
                            print(f"{M2[i + 1]} a prononcé le mot: {word_search}")

                    w = input(
                        f"Voulez-vous savoir quel(s) président(s) a/ont répété le plus de fois le mot : {word_search} ? (y) or (n) : ")
                    w = w.lower()

                    if w == 'y':
                        M3 = []

                        # Recherche des présidents ayant répété le plus le mot
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

                else:
                    print(
                        f"{M2[0]} est le seul a avoir prononcé le mot: {word_search}, {M2[0]} l'a prononcé {Max} fois.")

    elif func == "5":
        # Fonctionnalité 5 : Premier président à prononcer un mot
        f5 = input("Voulez-vous chercher un mot afin de trouver quel président l'a énoncé en premier ? (y) or (n) :")
        if f5 == "y":
            mot = input("Entrez le mot souhaité : ")
            mot = mot.lower()
            find = False
            i = 0

            # Recherche du mot dans chaque discours
            while not find:
                tf = TF(list_file[i])

                # Vérification de la présence du mot et affichage du premier président
                for cle in tf.keys():
                    if cle == mot:
                        find = True
                        name = extractnames(list_file[i])
                        print(f"C'est {name} qui a énoncé le mot {mot} en premier !")
                i += 1

                # Si le mot n'est pas trouvé dans tous les discours
                if i >= len(list_file):
                    print("Aucun président n'a prononcé ce mot")
                    find = True

    else:
        print("La fonctionnalité n'existe pas ")

    # Demande à l'utilisateur s'il souhaite voir d'autres fonctionnalités
    print()
    stop = input("Voulez-vous voir d'autres fonctionnalités ? (y) or (n) ")
    stop = stop.lower()

    if stop == "n":
        end = True

# Fin du programme
print("Fin du programme")
