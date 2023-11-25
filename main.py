from functions import *

Matrix_tf_idf = Matrice_TF_IDF("./cleaned")
list_file = list_of_files("./cleaned",".txt")


with open("./Project_Presentation", "r") as f:
    content = f.read()
    print(content)

end = False
while end == False:

    func = input("Saisir la fonctionnalité de votre choix (numéros de la fonctionnalité (Ex : 1) ) : ")

    if func == "1":

        # fonctionalité 1

        f1 = input("Voulez-vous savoir quels sont les mots les moins important dans tous les discours : (y) or (n) ")
        f1.lower()

        if f1 == "y":
            list_of_non_important_words = []

            for i in range(len(Matrix_tf_idf)):
                summ = 0
                for j in range(1, len(Matrix_tf_idf[i])):
                    summ += Matrix_tf_idf[i][j]
                if summ == 0:
                    list_of_non_important_words.append(Matrix_tf_idf[i][0])

            print("Voici le(s) mot(s) le(s) moins important dans tous les discours :")

            for row in list_of_non_important_words:
                print(row)

        stop = input("Voulez-vous voir d'autre d'autre fonctionnalité ? (y) or (n) ")
        stop = stop.lower()

        if stop == "n":
            end = True

    elif func == "2":

        # fonctionalité 2

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

        stop = input("Voulez-vous voir d'autre d'autre fonctionnalité ? (y) or (n) ")
        stop = stop.lower()

        if stop == "n":
            end = True

    elif func == "3":

        # Fonctionalité 3

        f3 = input("Souhaitez-vous voir le mot le plus prononcé par le président de votre choix ? (y) or (n) :")
        f3 = f3.lower()

        if f3 == "y":
            president = input("Quel president voulez-vous choisir ? : ")
            for i in range(len(list_file) - 1):
                name = extractnames(list_file[i])
                if name == president and list_file[i] != list_file:
                    T = []
                    max = 0
                    DicTxt = TF(list_file[i])
                    for cle, val in DicTxt.items():
                        if max < val:
                            T = []
                            max = val
                            T.append(cle)
                        elif max == val:
                            T.append(cle)
                    if len(T) > 1:
                        print(f"{president} a prononcé le plus de fois le mot : {T[0]}")
                        for i in range(1, len(T)):
                            print(f"ainsi que le mot : {T[i]}")
                    else:
                        print(f"{president} a prononcé le plus de fois le mot : {T[0]}")


                elif name == president and list_file[i] == list_file[i + 1]:

                    file1 = f"{list_file[i]}"
                    file2 = f"{list_file[i + 1]}"

                    DicTxt1 = TF(file1)
                    DicTxt2 = TF(file2)
                    Dic_merge = AddDic(DicTxt1, DicTxt2)

                    T = []
                    max = 0

                    for cle, val in Dic_merge.items():
                        if max < val:
                            T = []
                            max = val
                            T.append(cle)
                        elif max == val:
                            T.append(cle)
                    if len(T) > 1:
                        print(f"{president} a prononcé le plus de fois le mot : {T[0]}")
                        for i in range(1, len(T)):
                            print(f"ainsi que le mot : {T[i]}")
                    else:
                        print(f"{president} a prononcé le plus de fois le mot : {T[0]}")


        stop = input("Voulez-vous voir d'autre d'autre fonctionnalité ? (y) or (n) ")
        stop = stop.lower()

        if stop == "n":
            end = True

    elif func == "4":

        # Fonctionalité 4

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
            w = input(
                f"Voulez-vous savoir quel(s) président(s) a/ont répété le plus de fois le mot : {word_search} ? (y) or (n) : ")
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

        stop = input("Voulez-vous voir d'autre d'autre fonctionnalité ? (y) or (n) ")
        stop = stop.lower()

        if stop == "n":
            end = True


    elif func == "5":

        # Fonctionalité 5

        f5 = input("Voulez-vous chercher un mot afin de trouver quel president l'a énoncé en premier ? (y) or (n) :")
        if f5 == "y":

            mot = input("Entrez le mot souhaité : ")
            mot = mot.lower()

            find = False
            i = 0
            list_files = list_of_files("./cleaned", ".txt")

            while not find:
                tf = TF(list_files[i])
                for cle in tf.keys():
                    if cle == mot:
                        find = True
                        name = extractnames(list_files[i])
                        print(f"C'est {name} qui a énoncé le mot {mot} en premier !")
                i += 1

        stop = input("Voulez-vous voir d'autre d'autre fonctionnalité ? (y) or (n) ")
        stop = stop.lower()

        if stop == "n":
            end = True

    else:
        print("La fonctionnalité n'existe pas ")

print("Fin du programme")
