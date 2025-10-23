import random, os, sys, time


#Définition des cartes 
familles = ["♠️", "♥️", "♦️", "♣️"]
cartes = ["As","2","3","4","5","6","7","8","9","10","Valet","Dame","Roi"]

#Création du deck 
deck = [f"{carte} {famille}" for famille in familles for carte in cartes]

#Création du deck joueur et banque
deck_joueur = []
deck_banque = []

#Variable pour cacher la deuxième carte de la banque
carte_cachee = True


random.shuffle(deck)

#cartes sur table
carte_jouee = []

def affichage():
    global carte_cachee
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')
    print("=============================================")
    print("              𝓑𝓵𝓪𝓬𝓴𝓙𝓪𝓬𝓴 𝓡𝓸𝔂𝓪𝓵             ")
    print("=============================================")

    print("Joueur :")
    print(f"Points : {total_points(deck_joueur)}")
    print(f"Cartes : {deck_joueur}")

    print("---------------------------------------------")

    print("Banque :")
    if carte_cachee and len(deck_banque) >= 2:
        print(f"Points : {points(deck_banque[0])} + ?")
        print(f"Cartes : [{deck_banque[0]}, '?']")
    else:
        print(f"Points : {total_points(deck_banque)}")
        print(f"Cartes : {deck_banque}")

    print("=============================================")



def tirage(main: list):
    if len(deck) != 0:
        carte = deck.pop()
        carte_jouee.append(carte)
        main.append(carte)
        return carte
    else:
        print("Il n'y a plus de carte dans le paquet")

        
    

def points(carte: str):
    liste_nombre = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    liste_tête = [ "Valet", "Dame", "Roi"]
    valeur_carte = carte.split()[0]
    if(valeur_carte in liste_nombre):
        return int(valeur_carte)
    elif(valeur_carte in liste_tête):
        return 10
    else :
        return 11


def total_points(main: list):
    total = 0
    nb_as = 0
    for c in main:
        valeur = points(c)
        total += valeur
        if "As" in c:
            nb_as += 1
    while total > 21 and nb_as > 0:
        total -= 10
        nb_as -= 1
    return total



def verification(main: list):
    total = total_points(main)
    if total > 21:
        if main == deck_joueur:
            print("BURST du joueur - La banque gagne !")
        else:
            print("BURST de la banque - Le joueur gagne !")
        return True
    return False
        
def victoire():
        total_joueur = total_points(deck_joueur)
        total_banque = total_points(deck_banque)
        
        ecart_joueur = abs(21 - total_joueur)
        ecart_banque = abs(21 - total_banque)

        if ecart_joueur < ecart_banque:
            print("Joueur gagne !")
        elif ecart_banque < ecart_joueur:
            print("Banque gagne !")
        else:
            print("PUSH !")


def main():
    stop_joueur = 0
    for i in range(2):

        tirage1 = tirage(deck_joueur)
        tirage2 = tirage(deck_banque)
        
    affichage()

    while(stop_joueur != 1):

        print("Hit ou Stay ?")
        reponse = input("Choix > ").strip()

        if(reponse.upper() == "HIT"):
            carte = tirage(deck_joueur)
            affichage()
            if verification(deck_joueur):
                return

        elif(reponse.upper() == "STAY"):
            stop_joueur = 1
            global carte_cachee 
            carte_cachee = False
            affichage()
    
    while(total_points(deck_banque) < 17):
            carte = tirage(deck_banque)
            affichage()
            if verification(deck_banque):
                return
            
            print("\nLa banque tire une carte...")
            time.sleep(1.5)  

    victoire()

main()