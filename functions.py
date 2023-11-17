import os

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

directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)
print(affiche_nom(['Chirac', 'Chirac', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Mitterrand', 'Sarkozy']))
print(min())
print(remove_ponctuation())