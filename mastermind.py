import random
import time


#### Partie 1 : Version impérative #### 

# Dictionnaire des couleurs
# rouge, vert, bleu, orange, jaune, rose, blanc, noir

color_dic = {
    1:'rouge',
    2:'vert',
    3:'bleu',
    4:'orange',
    5:'jaune',
    6:'rose',
    7:'blanc',
    8:'noir'
}

# Nombre d'essais possibles : 12 comme dans le mastermind original
max_nb_try = 12
chiffres = '12345678'
str_col = " | ".join([f"{key} : {value}" for (key, value) in color_dic.items()])

def translate(combi, dic=color_dic):
    return [dic[nombre] for nombre in combi]

def gen_rnd_combination(dic=color_dic):
    return [random.choice(list(dic.keys())) for _ in range(4)]

def main():
    print("")
    start=input("Bienvenue sur Mastermind !\nVoulez-vous débuter une partie ? (y/n) : ")
    if start!='y':
        print("Au revoir !")
    else:
        print('-'*100)
        # générer la combinaison de l'ordinateur
        computer_combi = gen_rnd_combination()
        # ne pas oublier que c'est un tuple
        print("L'ordinateur est en train de choisir sa combinaison...")
        for _ in range(3):
            time.sleep(0.5)
            print("...")
        time.sleep(1)
        print("L'ordinateur a choisi !")

        # le jeu
        found = False
        nb_try=0
        while found==False and nb_try < max_nb_try:
            answer=" "
            is_num=False
            while len(answer) != 4 or is_num==False:
                print("Saisissez une combinaison de 4 couleurs à l'aide des chiffres :\n" + str_col)
                print("")
                answer = input("Combinaison : ")
                is_num = True
                for char in answer:
                    try:
                        int(char)
                        if char not in chiffres:
                            is_num=False
                    except:
                        is_num=False
                if len(answer) != 4 or is_num==False:
                    print("")
                    print("!!! Erreur. Veuillez saisir 4 CHIFFRES de la liste !!!")
                    print("")
            nb_try += 1
            user_combi = [int(num) for num in answer]
            print(f"Vous avez choisi la combinaison : {', '.join(translate(user_combi))}.")
            # couleurs bien placées
            good_place = 0
            for i in range(4):
                if user_combi[i] == computer_combi[i]:
                    good_place+=1
            print(f"Il y a {good_place} " + ("couleurs bien placées." if good_place>1 else "couleur bien placée."))        
            # utiliser un opérateur pour ajouter seulement le s si condition (bool ? str1:str2) idée de floshock
            # found=True

            # couleurs mal placées
            good_col= 0
            temp_combi = computer_combi.copy()
            for num in user_combi:
                if num in temp_combi:
                    good_col+=1
                    temp_combi.remove(num)
            good_col-=good_place
            print(f"Il y a {good_col} " + ("couleurs mal placées." if good_col>1 else "couleur mal placée."))
            print("")
            if good_place == 4:
                found=True
                print(f"Vous avez gagné en {nb_try} essais !")
        if nb_try >= max_nb_try and found==False:
            print("")
            print("Vous avez dépassé le nombre maximum d'essais ! Dommage...")
            print(f"L'ordinateur avait choisi {', '.join(translate(computer_combi))} {computer_combi} comme combinaison.")
            print("À bientôt !")

#### Partie 2 : Version orientée objet #### 

class Mastermind():
    def __init__(self):
        self.color_dic = {
                        1:'rouge',
                        2:'vert',
                        3:'bleu',
                        4:'orange',
                        5:'jaune',
                        6:'rose',
                        7:'blanc',
                        8:'noir'
                        }
        self.history = []
        self.chiffres = '12345678'
        self.__combinaison = [random.choice(list(self.color_dic.keys())) for _ in range(4)]
        self.found = False
        self.nb_try = 0
        self.__max_nb_try = 12
    
    def translate(self, combi):
        return [self.color_dic[nombre] for nombre in combi]

    def print_dic(self):
        print(" | ".join([f"{key} : {value}" for (key, value) in self.color_dic.items()]))

    def ask_user(self):
        answer=" "
        is_num=False
        while len(answer) != 4 or is_num==False:
            print("Saisissez une combinaison de 4 couleurs à l'aide des chiffres :")
            self.print_dic()
            print("")
            answer = input("Combinaison : ")
            is_num = True
            for char in answer:
                try:
                    int(char)
                    if char not in self.chiffres:
                        is_num=False
                except:
                    is_num=False
            if len(answer) != 4 or is_num==False:
                print("")
                print("!!! Erreur. Veuillez saisir 4 CHIFFRES de la liste !!!")
                print("")
        output = [int(num) for num in answer]
        return output

    def place_col(self, user_combi):
        # couleurs bien placées
        good_place = 0
        for i in range(4):
            if user_combi[i] == self.__combinaison[i]:
                good_place+=1
        print(f"Il y a {good_place} " + ("couleurs bien placées." if good_place>1 else "couleur bien placée."))        

        # couleurs mal placées
        good_col= 0
        temp_combi = self.__combinaison.copy()
        for num in user_combi:
            if num in temp_combi:
                good_col+=1
                temp_combi.remove(num)
        good_col-=good_place

        print(f"Il y a {good_col} " + ("couleurs mal placées." if good_col>1 else "couleur mal placée."))
        if good_place == 4:
            self.found=True
            print(f"Vous avez gagné en {self.nb_try} essais !")

    def print_history(self):
        if self.nb_try > 0:
            print("Combinaisons déjà rentrées :")
            for combi in self.history:
                print(combi, self.translate(combi))

    def play(self):
        print("")
        start=input("Bienvenue sur Mastermind !\nVoulez-vous débuter une partie ? (y/n) : ")
        if start!='y':
            print("Au revoir !")
        else:
            print('-'*100)
            print("L'ordinateur est en train de choisir sa combinaison...")
            for _ in range(3):
                time.sleep(0.5)
                print("...")
            time.sleep(1)
            print("L'ordinateur a choisi !")

            # le jeu

            while self.found==False and self.nb_try < self.__max_nb_try:
                answer=self.ask_user()
                self.history.append(answer)
                self.nb_try += 1
                self.print_history()               
                print(f"Vous avez choisi la combinaison : {', '.join(self.translate(answer))}.")
                self.place_col(user_combi=answer)
                print("")

            if self.nb_try >= self.__max_nb_try and self.found==False:
                print("")
                print("Vous avez dépassé le nombre maximum d'essais ! Dommage...")
                print(f"L'ordinateur avait choisi {', '.join(self.translate(self.__combinaison))} {self.__combinaison} comme combinaison.")
                print("À bientôt !")

if __name__ == "__main__":
    jeu = Mastermind()
    jeu.play()