#__________Import des extensions__________
import random
import time
import sys


#__________Objectifs du projets__________
def cahier_des_charges():   
    print('''
    Modifier les lettres des phrases données
    Rendre le plus difficile possible de décoder sans ce programme
    Pour cela:
    Une clé aléatoire sera choisie au moment de coder chaque message,
    Ensuite, la clé est modifié de maniére alétoire
    Cette nouvelle clé est rentrée dans une fonction choisie aléatoirement   
    La valeur de sortie est la postion dans l'alphabet de la nouvelle lettre, 
    

    Évolution:

    V1.0: Programme originale
    
    V1.1: Ajout des majuscules, des chiffres et ce 47 autres caractères
        Amélioration:
            Nbr de caractères traduit:
                27 --> 112
    
    V1.2: Optimisation du programme:
        Amélioration:
            Taille maximale d'un texte à traduire:
                10 --> 1 023
    
    V1.3: Mise en place d'une boucle permettant de répéter le programme sans avoir à le stopper
        Amélioration:
            Boucle:
                False --> True
    
    V1.4: Ajout de nouvelles fonctions/modificateur de clé/clé
        Amélioration:
            Nbr de combinaisons possible de fonctions/modificateur de clé/clé:
                300 --> 1 000 000
    ''')
#__________Boucle principal__________
loop = 1 #Permet à la boucle de ce lancer sans utiliser True au cas où on voudrait le stopper
while loop == 1: #La boucle relance le script en continue
    clear = ("\n\n\n") #Saute 3 ligne
    print(clear)
    
    
    #__________Message d'acceuil__________
    print("Bonjour !\nBienvenue sur la version 1.4 de Enigma\n")
    print('''Il est préférable de coder et décoder des phrases sans:
    saut de ligne,

    \nCaractères acceptés:
    Toutes les lettres de l'alphabet en minuscule + majuscule,
    Les chiffres, 
    Certains caractères tel que:
    ! # $ % & ( ) * + , - . ' " / : ; > < = ? @ [ ] ^ _ { } ~ € é è ê à â ç ù ô û É È À Â Ç Ù Ô Â Û

        \nQue voulez-vous faire ?
        \n1. Décodez un message
        \n2. Encodez un message
        \n3. Info
        \n4. Quitter
        \n\n\n''')
    
    
    #__________Initialisation des variables__________
    menu_choice = int(input("Choix: ")) #Demande à l'utilisateur ce qu'il veut faire
    print(clear)
    code_key = random.randint(1, 9999) #Génére une clé aléatoire
    key_choice = random.randint(1, 20) #Genere aléatoirement un modificateur de clé
    fonction = random.randint(1, 20) #Génére aléatoirement une fonction affine
    uncoded = str("NULL") 
    lettre = 0
    key = 0
    final_message = [] 
    coded_solved_message = [] 
    final_text = str()
    real_key1 = code_key * 5 + 2
    real_key2 = code_key * 8 + 3
    real_key3 = code_key * 3 + 4
    real_key4 = code_key * 9 + 5
    real_key5 = code_key * 8 + 12
    real_key6 = code_key * 7 + 2
    real_key7 = code_key * 6 + 17
    real_key8 = code_key * 9 + 6
    real_key9 = code_key * 10 + 7
    real_key10 = code_key * 13 + 4
    real_key11 = code_key * 12 + 8
    real_key12 = code_key * 11 + 14
    real_key13 = code_key * 15 + 13
    real_key14 = code_key * 16 + 22
    real_key15 = code_key * 18 + 25
    real_key16 = code_key * 17 + 21
    real_key17 = code_key * 19 + 9
    real_key18 = code_key * 20 + 4
    real_key19 = code_key * 24 + 32
    real_key20 = code_key * 22 + 21
    useless = str("Cette variable est pas vraiment utile mais c'est surtout que ça sert à rien de l'initialiser mais je me fais chier donc j'éris de la merde au lieu de faire mes exos de physique... Putin mais pourquoi je fais ce script en plus XD Y'a grave moyen que qq est déjà fait pareil duc n dirait juste que je le copier mais le pire que c'est que j'ai pas meme pas copier un seul morceau de code alors que ça aurait été tellement plus vite xD, si qq (autre que moi-meme hein !) lis-ça et bah passes une bonen journée ! (PASSEZ une bonne journée si c'est un adulte qui regadre ça)")

    # Modifie la clé inital en fonction du modificateur de clé généré
    if key_choice == 1:
        key = real_key1
    elif key_choice == 2:
        key = real_key2
    elif key_choice == 3:
        key = real_key3
    elif key_choice == 4:
        key = real_key4
    elif key_choice == 5:
        key = real_key5
    elif key_choice == 6:
        key = real_key6
    elif key_choice == 7:
        key = real_key7
    elif key_choice == 8:
        key = real_key8
    elif key_choice == 9:
        key = real_key9
    elif key_choice == 10:
        key = real_key10
    elif key_choice == 11:
        key = real_key11
    elif key_choice == 12:
        key = real_key12
    elif key_choice == 13:
        key = real_key13
    elif key_choice == 14:
        key = real_key14
    elif key_choice == 15:
        key = real_key15
    elif key_choice == 16:
        key = real_key16
    elif key_choice == 17:
        key = real_key17
    elif key_choice == 18:
        key = real_key18
    elif key_choice == 19:
        key = real_key19
    elif key_choice == 20:
        key = real_key20

    #__________Définition des fonction__________
    def encoding(lettre, key): #Fonction utilisée pour encoder un message
        #Donne pour chaque caractères, sa place dans l'alphabet
        if lettre == "a":
            lettre = 1
        elif lettre =="b":
            lettre = 2  
        elif lettre =="c":
            lettre = 3
        elif lettre =="d":
            lettre = 4
        elif lettre =="e":
            lettre = 5
        elif lettre =="f":
            lettre = 6
        elif lettre =="g":
            lettre = 7
        elif lettre =="h":
            lettre = 8
        elif lettre =="i":
            lettre = 9
        elif lettre =="j":
            lettre = 10
        elif lettre =="k":
            lettre = 11
        elif lettre =="l":
            lettre = 12
        elif lettre =="m":
            lettre = 13
        elif lettre =="n":
            lettre = 14
        elif lettre =="o":
            lettre = 15
        elif lettre =="p":
            lettre = 16
        elif lettre =="q":
            lettre = 17
        elif lettre =="r":
            lettre = 18
        elif lettre =="s":
            lettre = 19
        elif lettre =="t":
            lettre = 20
        elif lettre =="u":
            lettre = 21
        elif lettre =="v":
            lettre = 22
        elif lettre =="w":
            lettre = 23
        elif lettre =="x":
            lettre = 24
        elif lettre =="y":
            lettre = 25
        elif lettre =="z":
            lettre = 26
        elif lettre ==" ":
            lettre = 27
        elif lettre =="A":
            lettre = 28
        elif lettre =="B":
            lettre = 29
        elif lettre =="C":
            lettre = 30
        elif lettre =="D":
            lettre = 31
        elif lettre =="E":
            lettre = 32
        elif lettre =="F":
            lettre = 33
        elif lettre =="G":
            lettre = 34
        elif lettre =="H":
            lettre = 35
        elif lettre =="I":
            lettre = 36
        elif lettre =="J":
            lettre = 37
        elif lettre =="K":
            lettre = 38
        elif lettre =="L":
            lettre = 39
        elif lettre =="M":
            lettre = 40
        elif lettre =="N":
            lettre = 41
        elif lettre =="O":
            lettre = 42
        elif lettre =="P":
            lettre = 43
        elif lettre =="Q":
            lettre = 44
        elif lettre =="R":
            lettre = 45
        elif lettre =="S":
            lettre = 46
        elif lettre =="T":
            lettre = 47
        elif lettre =="U":
            lettre = 48
        elif lettre =="V":
            lettre = 49
        elif lettre =="W":
            lettre = 50
        elif lettre =="X":
            lettre = 51
        elif lettre =="Y":
            lettre = 52
        elif lettre =="Z":
            lettre = 53
        elif lettre=="!":
            lettre = 54
        elif lettre=="#":
            lettre = 55
        elif lettre=="$":
            lettre = 56
        elif lettre=="%":
            lettre = 57
        elif lettre=="&":
            lettre = 58
        elif lettre=="(":
            lettre = 59
        elif lettre==")":
            lettre = 60
        elif lettre=="*":
            lettre = 61
        elif lettre=="+":
            lettre = 62
        elif lettre=="'":
            lettre = 63
        elif lettre=="-":
            lettre = 64
        elif lettre==".":
            lettre = 65
        elif lettre=="/":
            lettre = 66
        elif lettre=="0":
            lettre = 67
        elif lettre=="1":
            lettre = 68
        elif lettre=="2":
            lettre = 69
        elif lettre=="3":
            lettre = 70
        elif lettre=="4":
            lettre = 71
        elif lettre=="5":
            lettre = 72
        elif lettre=="6":
            lettre = 73
        elif lettre=="7":
            lettre = 74
        elif lettre=="8":
            lettre = 75
        elif lettre=="9":
            lettre = 76
        elif lettre==":":
            lettre = 77
        elif lettre==";":
            lettre = 78
        elif lettre==">":
            lettre = 79
        elif lettre=="<":
            lettre = 80
        elif lettre=="=":
            lettre = 81
        elif lettre=="?":
            lettre = 82
        elif lettre=="@":
            lettre = 83
        elif lettre=="[":
            lettre = 84
        elif lettre=="]":
            lettre = 85
        elif lettre=="§":
            lettre = 86
        elif lettre=="^":
            lettre = 87
        elif lettre=="_":
            lettre = 88
        elif lettre=="{":
            lettre = 89
        elif lettre=="}":
            lettre = 90
        elif lettre=="~":
            lettre = 91
        elif lettre=="€":
            lettre = 92
        elif lettre=="é":
            lettre = 93
        elif lettre=="è":
            lettre = 94
        elif lettre=="ê":
            lettre = 95
        elif lettre=="à":
            lettre = 96
        elif lettre=="â":
            lettre = 97
        elif lettre=="ç":
            lettre = 98
        elif lettre=="ù":
            lettre = 99
        elif lettre=="ô":
            lettre = 100
        elif lettre=="É":
            lettre = 101
        elif lettre=="È":
            lettre = 102
        elif lettre=="À":
            lettre = 103
        elif lettre=="Â":
            lettre = 104
        elif lettre=="Ç":
            lettre = 105
        elif lettre=="Ù":
            lettre = 106
        elif lettre=="Ô":
            lettre = 107
        elif lettre=="û":
            lettre = 108
        elif lettre=="Û":
            lettre = 109
        elif lettre==",":
            lettre = 110
        elif lettre =="£":
            lettre = 111
        elif lettre =='"':
            lettre = 112
        while key > 112:
            key = key - 112
        lettre = lettre + key #Fait la somme entre la postion du caractères et la clé
        while lettre > 112: #Réduit la valeur lettre pour qu'elle puisse etre égal à un caractères
            lettre = lettre - 112
        # Transforme la nouvel valeur en caractères en fonction de sa place dans l'alphabet
        if lettre == 1:
            lettre = "a"
        elif lettre ==2:
            lettre = "b" 
        elif lettre ==3:
            lettre = "c"
        elif lettre ==4:
            lettre = "d"
        elif lettre ==5:
            lettre = "e"
        elif lettre ==6:
            lettre = "f"
        elif lettre ==7:
            lettre = "g"
        elif lettre ==8:
            lettre = "h"
        elif lettre ==9:
            lettre = "i"
        elif lettre ==10:
            lettre = "j"
        elif lettre ==11:
            lettre = "k"
        elif lettre ==12:
            lettre = "l"
        elif lettre ==13:
            lettre = "m"
        elif lettre ==14:
            lettre = "n"
        elif lettre ==15:
            lettre = "o"
        elif lettre ==16:
            lettre = "p"
        elif lettre ==17:
            lettre = "q"
        elif lettre ==18:
            lettre = "r"
        elif lettre ==19:
            lettre = "s"
        elif lettre ==20:
            lettre = "t"
        elif lettre ==21:
            lettre = "u"
        elif lettre ==22:
            lettre = "v"
        elif lettre ==23:
            lettre = "w"
        elif lettre ==24:
            lettre = "x"
        elif lettre ==25:
            lettre = "y"
        elif lettre ==26:
            lettre = "z"
        elif lettre ==27:
            lettre = " "
        elif lettre ==28:
            lettre = "A"
        elif lettre ==29:
            lettre = "B"
        elif lettre ==30:
            lettre = "C"
        elif lettre ==31:
            lettre = "D"
        elif lettre ==32:
            lettre = "E"
        elif lettre ==33:
            lettre = "F"
        elif lettre ==34:
            lettre = "G"
        elif lettre ==35:
            lettre = "H"
        elif lettre ==36:
            lettre = "I"
        elif lettre ==37:
            lettre = "J"
        elif lettre ==38:
            lettre = "K"
        elif lettre ==39:
            lettre = "L"
        elif lettre ==40:
            lettre = "M"
        elif lettre ==41:
            lettre = "N"
        elif lettre ==42:
            lettre = "O"
        elif lettre ==43:
            lettre = "P"
        elif lettre ==44:
            lettre = "Q"
        elif lettre ==45:
            lettre = "R"
        elif lettre ==46:
            lettre = "S"
        elif lettre ==47:
            lettre = "T"
        elif lettre ==48:
            lettre = "U"
        elif lettre ==49:
            lettre = "V"
        elif lettre ==50:
            lettre = "W"
        elif lettre ==51:
            lettre = "X"
        elif lettre ==52:
            lettre = "Y"
        elif lettre ==53:
            lettre = "Z"
        elif lettre ==54:
            lettre = "!"
        elif lettre ==55:
            lettre = "#"
        elif lettre ==56:
            lettre = "$"
        elif lettre ==57:
            lettre = "%"
        elif lettre ==58:
            lettre = "&"
        elif lettre ==59:
            lettre = "("
        elif lettre ==60:
            lettre = ")"
        elif lettre ==61:
            lettre = "*"
        elif lettre ==62:
            lettre = "+"
        elif lettre ==63:
            lettre = "'"
        elif lettre ==64:
            lettre = "-"
        elif lettre ==65:
            lettre = "."
        elif lettre ==66:
            lettre = "/"
        elif lettre ==67:
            lettre = "0"
        elif lettre ==68:
            lettre = "1"
        elif lettre ==69:
            lettre = "2"
        elif lettre ==70:
            lettre = "3"
        elif lettre ==71:
            lettre = "4"
        elif lettre ==72:
            lettre = "5"
        elif lettre ==73:
            lettre = "6"
        elif lettre ==74:
            lettre = "7"
        elif lettre ==75:
            lettre = "8"
        elif lettre ==76:
            lettre = "9"
        elif lettre ==77:
            lettre = ":"
        elif lettre ==78:
            lettre = ";"
        elif lettre ==79:
            lettre = ">"
        elif lettre ==80:
            lettre = "<"
        elif lettre ==81:
            lettre = "="
        elif lettre ==82:
            lettre = "?"
        elif lettre ==83:
            lettre = "@"
        elif lettre ==84:
            lettre = "["
        elif lettre ==85:
            lettre = "]"
        elif lettre ==86:
            lettre = "§"
        elif lettre ==87:
            lettre = "^"
        elif lettre ==88:
            lettre = "_"
        elif lettre ==89:
            lettre = "{"
        elif lettre ==90:
            lettre = "}"
        elif lettre ==91:
            lettre = "~"
        elif lettre ==92:
            lettre = "€"
        elif lettre ==93:
            lettre = "é"
        elif lettre ==94:
            lettre = "è"
        elif lettre ==95:
            lettre = "ê"
        elif lettre ==96:
            lettre = "à"
        elif lettre ==97:
            lettre = "â"
        elif lettre ==98:
            lettre = "ç"
        elif lettre ==99:
            lettre = "ù"
        elif lettre ==100:
            lettre = "ô"
        elif lettre ==101:
            lettre = "É"
        elif lettre ==102:
            lettre = "È"
        elif lettre ==103:
            lettre = "À"
        elif lettre ==104:
            lettre = "Â"
        elif lettre ==105:
            lettre = "Ç"
        elif lettre ==106:
            lettre = "Ù"
        elif lettre ==107:
            lettre = "Ô"
        elif lettre ==108:
            lettre = "û"
        elif lettre ==109:
            lettre = "Û"
        elif lettre ==110:
            lettre = ","
        elif lettre ==111:
            lettre = "£"
        elif lettre ==112:
            lettre = '"'
        return(lettre) #Renvoie le caractères 
    def function(key, key_choice, fonction): #Fonction utilisée pour modifier une clé
        #La clé est modifié par la fonction choisie au hasard à l'initialisation des variables
        if fonction == 1:
            key = key * 2 + 3
        elif fonction == 2:
            key = key * 4 + 6
        elif fonction == 3:
            key = key * 5 + 2
        elif fonction == 4:
            key = key * 3 + 4
        elif fonction == 5:
            key = key * 4 + 10
        elif fonction == 6:
            key = key * 8 + 12
        elif fonction == 7:
            key = key * 7 + 17
        elif fonction == 8:
            key = key * 9 + 43
        elif fonction == 9:
            key = key * 12 + 34
        elif fonction == 10:
            key = key * 14 + 18
        elif fonction == 11:
            key = key * 11 + 73
        elif fonction == 12:
            key = key * 18 + 14
        elif fonction == 13:
            key = key * 27 + 95
        elif fonction == 14:
            key = key * 28 + 37
        elif fonction == 15:
            key = key * 21 + 24
        elif fonction == 16:
            key = key * 19 + 16
        elif fonction == 17:
            key = key * 8 + 36
        elif fonction == 18:
            key = key * 13 + 79
        elif fonction == 19:
            key = key * 22 + 83
        elif fonction == 20:
            key = key * 23 + 62
        return key #Renvoie la nouvel clé
    def decoding(lettre, real_coded_key): #Fonction utilisée pour décoder un message
        #Donne pour chaque caractères, sa place dans l'alphabet
        if lettre == "a":
            lettre = 1
        elif lettre =="b":
            lettre = 2  
        elif lettre =="c":
            lettre = 3
        elif lettre =="d":
            lettre = 4
        elif lettre =="e":
            lettre = 5
        elif lettre =="f":
            lettre = 6
        elif lettre =="g":
            lettre = 7
        elif lettre =="h":
            lettre = 8
        elif lettre =="i":
            lettre = 9
        elif lettre =="j":
            lettre = 10
        elif lettre =="k":
            lettre = 11
        elif lettre =="l":
            lettre = 12
        elif lettre =="m":
            lettre = 13
        elif lettre =="n":
            lettre = 14
        elif lettre =="o":
            lettre = 15
        elif lettre =="p":
            lettre = 16
        elif lettre =="q":
            lettre = 17
        elif lettre =="r":
            lettre = 18
        elif lettre =="s":
            lettre = 19
        elif lettre =="t":
            lettre = 20
        elif lettre =="u":
            lettre = 21
        elif lettre =="v":
            lettre = 22
        elif lettre =="w":
            lettre = 23
        elif lettre =="x":
            lettre = 24
        elif lettre =="y":
            lettre = 25
        elif lettre =="z":
            lettre = 26
        elif lettre ==" ":
            lettre = 27
        elif lettre =="A":
            lettre = 28
        elif lettre =="B":
            lettre = 29
        elif lettre =="C":
            lettre = 30
        elif lettre =="D":
            lettre = 31
        elif lettre =="E":
            lettre = 32
        elif lettre =="F":
            lettre = 33
        elif lettre =="G":
            lettre = 34
        elif lettre =="H":
            lettre = 35
        elif lettre =="I":
            lettre = 36
        elif lettre =="J":
            lettre = 37
        elif lettre =="K":
            lettre = 38
        elif lettre =="L":
            lettre = 39
        elif lettre =="M":
            lettre = 40
        elif lettre =="N":
            lettre = 41
        elif lettre =="O":
            lettre = 42
        elif lettre =="P":
            lettre = 43
        elif lettre =="Q":
            lettre = 44
        elif lettre =="R":
            lettre = 45
        elif lettre =="S":
            lettre = 46
        elif lettre =="T":
            lettre = 47
        elif lettre =="U":
            lettre = 48
        elif lettre =="V":
            lettre = 49
        elif lettre =="W":
            lettre = 50
        elif lettre =="X":
            lettre = 51
        elif lettre =="Y":
            lettre = 52
        elif lettre =="Z":
            lettre = 53
        elif lettre=="!":
            lettre = 54
        elif lettre=="#":
            lettre = 55
        elif lettre=="$":
            lettre = 56
        elif lettre=="%":
            lettre = 57
        elif lettre=="&":
            lettre = 58
        elif lettre=="(":
            lettre = 59
        elif lettre==")":
            lettre = 60
        elif lettre=="*":
            lettre = 61
        elif lettre=="+":
            lettre = 62
        elif lettre=="'":
            lettre = 63
        elif lettre=="-":
            lettre = 64
        elif lettre==".":
            lettre = 65
        elif lettre=="/":
            lettre = 66
        elif lettre=="0":
            lettre = 67
        elif lettre=="1":
            lettre = 68
        elif lettre=="2":
            lettre = 69
        elif lettre=="3":
            lettre = 70
        elif lettre=="4":
            lettre = 71
        elif lettre=="5":
            lettre = 72
        elif lettre=="6":
            lettre = 73
        elif lettre=="7":
            lettre = 74
        elif lettre=="8":
            lettre = 75
        elif lettre=="9":
            lettre = 76
        elif lettre==":":
            lettre = 77
        elif lettre==";":
            lettre = 78
        elif lettre==">":
            lettre = 79
        elif lettre=="<":
            lettre = 80
        elif lettre=="=":
            lettre = 81
        elif lettre=="?":
            lettre = 82
        elif lettre=="@":
            lettre = 83
        elif lettre=="[":
            lettre = 84
        elif lettre=="]":
            lettre = 85
        elif lettre=="§":
            lettre = 86
        elif lettre=="^":
            lettre = 87
        elif lettre=="_":
            lettre = 88
        elif lettre=="{":
            lettre = 89
        elif lettre=="}":
            lettre = 90
        elif lettre=="~":
            lettre = 91
        elif lettre=="€":
            lettre = 92
        elif lettre=="é":
            lettre = 93
        elif lettre=="è":
            lettre = 94
        elif lettre=="ê":
            lettre = 95
        elif lettre=="à":
            lettre = 96
        elif lettre=="â":
            lettre = 97
        elif lettre=="ç":
            lettre = 98
        elif lettre=="ù":
            lettre = 99
        elif lettre=="ô":
            lettre = 100
        elif lettre=="É":
            lettre = 101
        elif lettre=="È":
            lettre = 102
        elif lettre=="À":
            lettre = 103
        elif lettre=="Â":
            lettre = 104
        elif lettre=="Ç":
            lettre = 105
        elif lettre=="Ù":
            lettre = 106
        elif lettre=="Ô":
            lettre = 107
        elif lettre=="û":
            lettre = 108
        elif lettre=="Û":
            lettre = 109
        elif lettre==",":
            lettre = 110
        elif lettre =="£":
            lettre = 111
        elif lettre =='"':
            lettre = 112
        while real_coded_key > 112 : #Diminue la clé déduite pour quel corresponde à un caractères
            real_coded_key = real_coded_key - 112
        lettre = lettre - real_coded_key #Déduit la clé de la valeur lettre
        if lettre <= 0: #Fait en sorte que si la valeur est négative / égal à zéro, on ajoute le nombre de termes pour redevenir positif
            lettre = lettre + 112
        # On fait correspondre chaque valeur à un caractères
        if lettre == 1:
            lettre = "a"
        elif lettre ==2:
            lettre = "b" 
        elif lettre ==3:
            lettre = "c"
        elif lettre ==4:
            lettre = "d"
        elif lettre ==5:
            lettre = "e"
        elif lettre ==6:
            lettre = "f"
        elif lettre ==7:
            lettre = "g"
        elif lettre ==8:
            lettre = "h"
        elif lettre ==9:
            lettre = "i"
        elif lettre ==10:
            lettre = "j"
        elif lettre ==11:
            lettre = "k"
        elif lettre ==12:
            lettre = "l"
        elif lettre ==13:
            lettre = "m"
        elif lettre ==14:
            lettre = "n"
        elif lettre ==15:
            lettre = "o"
        elif lettre ==16:
            lettre = "p"
        elif lettre ==17:
            lettre = "q"
        elif lettre ==18:
            lettre = "r"
        elif lettre ==19:
            lettre = "s"
        elif lettre ==20:
            lettre = "t"
        elif lettre ==21:
            lettre = "u"
        elif lettre ==22:
            lettre = "v"
        elif lettre ==23:
            lettre = "w"
        elif lettre ==24:
            lettre = "x"
        elif lettre ==25:
            lettre = "y"
        elif lettre ==26:
            lettre = "z"
        elif lettre ==27:
            lettre = " "
        elif lettre ==28:
            lettre = "A"
        elif lettre ==29:
            lettre = "B"
        elif lettre ==30:
            lettre = "C"
        elif lettre ==31:
            lettre = "D"
        elif lettre ==32:
            lettre = "E"
        elif lettre ==33:
            lettre = "F"
        elif lettre ==34:
            lettre = "G"
        elif lettre ==35:
            lettre = "H"
        elif lettre ==36:
            lettre = "I"
        elif lettre ==37:
            lettre = "J"
        elif lettre ==38:
            lettre = "K"
        elif lettre ==39:
            lettre = "L"
        elif lettre ==40:
            lettre = "M"
        elif lettre ==41:
            lettre = "N"
        elif lettre ==42:
            lettre = "O"
        elif lettre ==43:
            lettre = "P"
        elif lettre ==44:
            lettre = "Q"
        elif lettre ==45:
            lettre = "R"
        elif lettre ==46:
            lettre = "S"
        elif lettre ==47:
            lettre = "T"
        elif lettre ==48:
            lettre = "U"
        elif lettre ==49:
            lettre = "V"
        elif lettre ==50:
            lettre = "W"
        elif lettre ==51:
            lettre = "X"
        elif lettre ==52:
            lettre = "Y"
        elif lettre ==53:
            lettre = "Z"
        elif lettre ==54:
            lettre = "!"
        elif lettre ==55:
            lettre = "#"
        elif lettre ==56:
            lettre = "$"
        elif lettre ==57:
            lettre = "%"
        elif lettre ==58:
            lettre = "&"
        elif lettre ==59:
            lettre = "("
        elif lettre ==60:
            lettre = ")"
        elif lettre ==61:
            lettre = "*"
        elif lettre ==62:
            lettre = "+"
        elif lettre ==63:
            lettre = "'"
        elif lettre ==64:
            lettre = "-"
        elif lettre ==65:
            lettre = "."
        elif lettre ==66:
            lettre = "/"
        elif lettre ==67:
            lettre = "0"
        elif lettre ==68:
            lettre = "1"
        elif lettre ==69:
            lettre = "2"
        elif lettre ==70:
            lettre = "3"
        elif lettre ==71:
            lettre = "4"
        elif lettre ==72:
            lettre = "5"
        elif lettre ==73:
            lettre = "6"
        elif lettre ==74:
            lettre = "7"
        elif lettre ==75:
            lettre = "8"
        elif lettre ==76:
            lettre = "9"
        elif lettre ==77:
            lettre = ":"
        elif lettre ==78:
            lettre = ";"
        elif lettre ==79:
            lettre = ">"
        elif lettre ==80:
            lettre = "<"
        elif lettre ==81:
            lettre = "="
        elif lettre ==82:
            lettre = "?"
        elif lettre ==83:
            lettre = "@"
        elif lettre ==84:
            lettre = "["
        elif lettre ==85:
            lettre = "]"
        elif lettre ==86:
            lettre = "§"
        elif lettre ==87:
            lettre = "^"
        elif lettre ==88:
            lettre = "_"
        elif lettre ==89:
            lettre = "{"
        elif lettre ==90:
            lettre = "}"
        elif lettre ==91:
            lettre = "~"
        elif lettre ==92:
            lettre = "€"
        elif lettre ==93:
            lettre = "é"
        elif lettre ==94:
            lettre = "è"
        elif lettre ==95:
            lettre = "ê"
        elif lettre ==96:
            lettre = "à"
        elif lettre ==97:
            lettre = "â"
        elif lettre ==98:
            lettre = "ç"
        elif lettre ==99:
            lettre = "ù"
        elif lettre ==100:
            lettre = "ô"
        elif lettre ==101:
            lettre = "É"
        elif lettre ==102:
            lettre = "È"
        elif lettre ==103:
            lettre = "À"
        elif lettre ==104:
            lettre = "Â"
        elif lettre ==105:
            lettre = "Ç"
        elif lettre ==106:
            lettre = "Ù"
        elif lettre ==107:
            lettre = "Ô"
        elif lettre ==108:
            lettre = "û"
        elif lettre ==109:
            lettre = "Û"
        elif lettre ==110:
            lettre = ","
        elif lettre ==111:
            lettre = "£"
        elif lettre ==112:
            lettre = '"'
        return(lettre) #On renvoie le caractères
    def hell(): #Fonction utilisée pour spammer l'utilisateur 
        while True: #Répéte indéfiniment
            weird_number = random.randint(1000000000000000, 10000000000000000000000000)
            print(weird_number)       
    #__________Code__________

    #__________Décodage__________
    if menu_choice == 1 :
        coded_message = str(input("\n\nMessage: ")) #Demande à l'utilisateur le message à décoder
        coded_fonction = int(input("\nNumber 1: ")) #Demande à l'utilisateur la 1ere valeur (La fonction utilisé)
        coded_create_key = int(input("Number 2: ")) #Demande à l'utilisateur la 2eme valeur (Le modificateur de clé utilisé)
        coded_key = int(input("Number 3: ")) #Demande à l'utilisateur la 3eme valeur (La clé initiale)
        
        # Modifie la clé initiale en fonction du modificateur donné
        if coded_create_key == 1:
            real_coded_key = coded_key * 5 + 2
        elif coded_create_key == 2:
            real_coded_key = coded_key * 8 + 3
        elif coded_create_key == 3:
            real_coded_key = coded_key * 3 + 4
        elif coded_create_key == 4:
            real_coded_key = coded_key * 9 + 5
        elif coded_create_key == 5:
            real_coded_key = coded_key * 8 + 12
        elif coded_create_key == 6:
            real_coded_key = coded_key * 7 + 2
        elif coded_create_key == 7:
            real_coded_key = coded_key * 6 + 17
        elif coded_create_key == 8:
            real_coded_key = coded_key * 9 + 6
        elif coded_create_key == 9:
            real_coded_key = coded_key * 10 + 7
        elif coded_create_key == 10:
            real_coded_key = coded_key * 13 + 4
        elif coded_create_key == 11:
            real_coded_key = coded_key * 12 + 8
        elif coded_create_key == 12:
            real_coded_key = coded_key * 11 + 14
        elif coded_create_key == 13:
            real_coded_key = coded_key * 15 + 13
        elif coded_create_key == 14:
            real_coded_key = coded_key * 16 + 22
        elif coded_create_key == 15:
            real_coded_key = coded_key * 18 + 25
        elif coded_create_key == 16:
            real_coded_key = coded_key * 17 + 21
        elif coded_create_key == 17:
            real_coded_key = coded_key * 19 + 9
        elif coded_create_key == 18:
            real_coded_key = coded_key * 20 + 4
        elif coded_create_key == 19:
            real_coded_key = coded_key * 24 + 32
        elif coded_create_key == 20:
            real_coded_key = coded_key * 22 + 21
        
        for i in range(len(coded_message)): #Cette boucle se répéte pour chaque lettre du message
            lettre = str(coded_message[i]) #Prends une lettre (La 1ere si c'est le 1er tour de la boucle etc ...)
            lettre = decoding(lettre, real_coded_key) #Passes la lettre dans la fonction decoding(lettre, real_coded_key)
            coded_solved_message.append(str(lettre)) #Rajoutes la lettre dans la liste qui contiendra le message décoder
            real_coded_key = function(real_coded_key, coded_create_key, coded_fonction) #Modifie la clé grace à la fonction function(real_coded_key, coded_create_key, coded_fonction) 
            while real_coded_key > 10000: # Réduit la taille de la clé si celle-ci est trop grande (OPTIMISATION)
                real_coded_key = real_coded_key - 10000
        final_text = ''.join(coded_solved_message) # Regroupe chaque charachtères de la liste en un str
        print("\nMessage décodé:") 
        print("'", final_text, "'") #Envoie le message décodé entre guillemets
        useless = input("\n\n\nAppuyer sur entrée pour revenir au menu") #Renvoie au menu

    #__________Encodage__________
    elif menu_choice == 2 :
        uncoded = str(input("Message: ")) #Demande à l'utilisateur le message à coder
        
        # Renvoie à l'utilisateur 3 valeurs (Respectivement: La fonction utilisé, le modificateur de clé, la clé initiale)
        print("\n\nNombre 1:") 
        print(fonction)
        print("\n\nNombre 2:")
        print(key_choice)
        print("\n\nNombre 3:")
        print(code_key)
        print("\n\n")
        
        ####

        ####
        for i in range(len(uncoded)): #Cette boucle se répéte pour chaque lettre du message
            lettre = str(uncoded[i]) #Prends une lettre (La 1ere si c'est le 1er tour de la boucle etc ...)
            lettre = encoding(lettre, key) #Passes la lettre dans la fonction encoding(lettre, key)
            final_message.append(lettre) #Rajoutes la lettre dans la liste qui contiendra le message coder
            key = function(key, key_choice, fonction) #Modifie la clé grace à la fonction function(real_coded_key, coded_create_key, coded_fonction)
            while key > 10000: # Réduit la taille de la clé si celle-ci est trop grande (OPTIMISATION)
                key = key - 10000
        final_text = ''.join(final_message) # Regroupe chaque charachtères de la liste en un str
        print("Message encodé:")
        print("'"final_text+"'") #Envoie le message codé entre guillemets
        useless = input("\n\n\nAppuyer sur entrée pour revenir au menu") #Renvoie au menu
