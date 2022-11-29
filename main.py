# GAINCHE Andrea 27/10/2021 Algo-Prog final project

from pylab import *


class chro():
    def __init__(self):
        self.chromosome = []
        self.bonnePlace = 0
        self.justeDedans = 0
        self.match = 0
        self.distance = 9999

    def fitness1(self, PM1):
        # fonction qui test combien caractere sont a la bonne place et combien son dans la liste pas a la bonne place
        # PM la phase mystere et c un chromosome
        mot = PM1.copy()  # on copy la phrase mystere pour ne pas la modifier
        c = self.chromosome.copy()
        self.match = 0
        self.bonnePlace = 0
        self.justeDedans = 0
        for i in range(len(mot)):  # on parcourt le chromosome
            if c[i] == mot[i]:
                # on regarde si le caractere est du chromosome est le meme que celui de la phrase mystere
                supprime(c[i], mot)  # Si ce sont les mêmes on le retire du chromosome et de la PM
                supprime(c[i], c)
                self.bonnePlace += 1  # on incrémente la variable associé a la bonne place d'un caractere
        for j in range(
                len(mot)):  # on reparcourt le chromosome pour trouver si il y a des caractères mal placer mais dans la PM
            if c[j] in mot and c[j] != -1:
                # si le caracter est dans la phrase mystere et n as pas deja ete note comme dedans (-1)
                supprime(c[j], mot)  # on l enleve de la PM
                self.justeDedans += 1  # on incrémente la variable associé
        self.match = self.bonnePlace + self.justeDedans * 0.1

    def fitness2(self, PM1):
        # fonction qui calcule la distance entre chaque caractere du chromosome
        mot = PM1.copy()
        c = self.chromosome.copy()
        self.distance = 0
        for i in range(len(mot)):  # on parcourt chaque caractere du chromosome
            self.distance += (mot[i] - c[i]) * (
                    mot[i] - c[i])  # on calcule le carre de chaque distance pour etre positif


def inputPhraseMystere():  # renvoie une liste d int qui est l ascci de la chaine de caractere entree par l utilisateur
    chaine = input("Entrez la phrase mystere : ")
    chaine = list(chaine)
    for i in range(len(chaine)):
        chaine[i] = ord(chaine[i])
    return chaine


def chaineToInt(chaine):
    # renvoie une liste d int qui est l ascci de la chaine de caractere mise en entree de la fonction
    chaine = list(chaine)
    for i in range(len(chaine)):
        chaine[i] = ord(chaine[i])
    return chaine


def intToChaine(chaine):  # il y a en entre une list d int qu on convertit en str correspondant a l ascii de chaque int
    string = ""
    for i in chaine:
        string += str(chr(i))
    return string


def supprime(n, liste):  # remplace le caractère n par un -1 pour ne pas le redétecté par la suite
    for i in range(len(liste)):
        if liste[i] == n:
            liste[i] = -1
            return liste


def printPop(pop):  # fonction qui print chaque chromosome de la population
    for i in pop:
        print(i.chromosome)


def premierePopulation(PM, N):  # cree la premiere population de taille N et de taille de chromosome taille de PM
    pop = []
    i = 0
    while i < N:  # population de la taille N
        c = chro()
        c.chromosome = []
        for j in range(len(PM)):  # chaque chromosome de taille de PM
            c.chromosome = c.chromosome + [np.random.randint(0, 255)]
        pop.append(c)
        i += 1
    return pop


def triInsertion(pop):  # range la population par rapport a leur parametre match
    for i in range(0, len(pop)):
        valeur = pop[i]
        j = i - 1
        while j >= 0 and valeur.match < pop[j].match:
            pop[j + 1] = pop[j]
            j -= 1
        pop[j + 1] = valeur
    return pop


def triInsertion2(pop):  # range la population par rapport a leur parametre distance
    for i in range(0, len(pop)):
        valeur = pop[i]
        j = i - 1
        while j >= 0 and valeur.distance > pop[j].distance:
            pop[j + 1] = pop[j]
            j -= 1
        pop[j + 1] = valeur
    return pop


def selectionMeilleur(pop, TS, typeDeJeu):  # en entrée la population en entier et resort la pop en ranger et coupe
    mediane = int(len(pop) * TS)  # calcule combien d'element de la pop on garde pour la prochaine generation
    if typeDeJeu == 1:
        pop = triInsertion(pop)
    elif typeDeJeu == 2:
        pop = triInsertion2(pop)
    pop = pop[(-1 * mediane):]
    return pop


def fit(pop, PM, typeDeJeu):
    # en entre : la population , et PM on effectue la methode fitness de la classe chro sur chaque element de la pop
    if typeDeJeu == 1:
        for i in pop:
            i.fitness1(PM)
    if typeDeJeu == 2:
        for i in pop:
            i.fitness2(PM)
    return pop


def reproduction(pop, N, decoupage, taille):  # taille longueure de PM
    longueurPOPinicial = len(pop)
    nombreDelement = int(decoupage * taille)
    while len(pop) < N:
        n1, n2 = np.random.randint(0, longueurPOPinicial), np.random.randint(0, longueurPOPinicial)
        c1 = pop[n1 - 1].chromosome[:nombreDelement]
        c2 = pop[n2 - 1].chromosome[(-1 * (taille - nombreDelement)):]
        pop.append(chro())
        pop[len(pop) - 1].chromosome = c1 + c2
    return pop


def mutation(pop, TM):
    # fonction qui donne une chance TM a chaque chromosome de changer pour un autre caractere prix au hasard
    # on prend TM en pourcentage
    for i in pop:
        for j in range(len(i.chromosome)):  # on parcourt chaque caractere de chaque chromosome
            if np.random.randint(0, 100) <= TM:
                # on prend un entier au hasard et si il est plus petit que TM alors ce caractere va changer
                i.chromosome[j] = np.random.randint(0, 255)
    return pop


def fin2(pop):
    if pop[len(pop) - 1].match == len(pop[0].chromosome):
        return False
    else:
        return True


def fin3(pop):
    if pop[len(pop) - 1].distance == 0:  # on regarde quand la distance entre la PM et le meilleur chromosome est de 0
        return False
    else:
        return True


def jeu(TS, N, decoupage, PM, pop,
        TM):  # jeu avec la fonction de fitnesse 1 : celle qui compte le nombre de caractere a la bonne place
    while fin2(pop):
        pop = mutation(pop, TM)
        pop = fit(pop, PM, 1)
        pop = selectionMeilleur(pop, TS, 1)
        pop = reproduction(pop, N, decoupage, len(PM))
        pop = triInsertion(pop)
        print(intToChaine(pop[N - 1].chromosome))
    print("ok")
    return pop


def jeu2(TS, N, decoupage, PM, pop,
         TM):  # jeu avec la fonction de fitnnes 2 qui compte la differrence entre le chromosome et PM
    while fin3(pop):
        pop = mutation(pop, TM)
        pop = fit(pop, PM, 2)
        pop = selectionMeilleur(pop, TS, 2)
        pop = reproduction(pop, N, decoupage, len(PM))
        pop = triInsertion2(pop)
        print(intToChaine(pop[N - 1].chromosome))
        print(pop[N - 1].distance)
    print("ok")
    return pop


if __name__ == '__main__':
    TS = 0.1
    N = 100
    TM = 5
    decoupage = 0.5
    tpsCalcul = []
    PM = inputPhraseMystere()
    """print("debut")
    N=1
    changementN = []
    for i in range(50):
        debut = time()
        pop = premierePopulation(PM, N)
        pop = jeu(TS, N, decoupage, PM, pop, TM)
        fin = time()
        tpsCalcul.append(fin - debut)
        changementN.append(N)
        N = N + i * 10
    print("fin")
    print(tpsCalcul)
    plot(changementN, tpsCalcul)
    show()
"""

    """print("debut")
    TS = 0.05
    changementTS = []
    for i in range(2, 10):  #changment de TS
        debut = time()
        pop = premierePopulation(PM, N)
        pop = jeu(TS, N, decoupage, PM, pop, TM)
        fin = time()
        tpsCalcul.append(fin - debut)
        changementTS.append(TS)
        TS = 0.05 * i
    print("fin")
    print(tpsCalcul)
    plot(changementTS, tpsCalcul)
    show()"""

    """print("debut")
    changementTM = []
    for i in range(50):  #changement de TM
        debut = time()
        pop = premierePopulation(PM, N)
        pop = jeu(TS, N, decoupage, PM, pop, TM)
        fin = time()
        tpsCalcul.append(fin - debut)
        changementTM.append(TM)
        TM = i * 2
    print("fin")
    print(tpsCalcul)
    plot(changementTM, tpsCalcul)
    show()"""

    pop = premierePopulation(PM, N)
    pop = jeu(TS, N, decoupage, PM, pop, TM)