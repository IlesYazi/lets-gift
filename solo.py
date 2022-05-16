import random

########## Base de donnees ##########

branche1 = [
    {"objet":"GAGNER", "femme":True, "enfant":True, "jouet":True, "test":True},

    {"objet":"drone", "femme":False, "enfant":False, "jouet":True, "test":True},

    {"objet":"voiture télécomandé", "femme":False, "enfant":True, "jouet":False, "test":True},

    {"objet":"poupé", "femme":True, "enfant":True, "jouet":True, "test":False},

    {"objet":"playstation", "femme":False, "enfant":False, "jouet":False, "test":True},

    {"objet":"xbox", "femme":False, "enfant":False, "jouet":False, "test":True},

    {"objet":"album de musique kpop", "femme":True, "enfant":False, "jouet":False, "test":True},

    {"objet":"ablum de musique rap", "femme":False, "enfant":False, "jouet":False, "test":True},

    {"objet":"bracelet", "femme":True, "enfant":True, "jouet":False, "test":True},

    {"objet":"rouge à levre", "femme":True, "enfant":False, "jouet":False, "test":True},

    #{"objet":"crampons de foot", "femme":None, "enfant":True, "jouet":False, "test":True},
    {"objet":"crampons de foot", "femme":False, "enfant":True, "jouet":False, "test":True},
    {"objet":"crampons de foot", "femme":True, "enfant":True, "jouet":False, "test":True},     

    {"objet":"cliché", "femme":False, "enfant":False, "jouet":True, "test":True},

    {"objet":"plus d'idee", "femme":True, "enfant":False, "jouet":True, "test":True},
]

########## Programmes ##########

def rep_question(reponse, key,tableau:list):
    if reponse == "oui" or reponse == "non" or reponse == "jsp":
        if reponse == "oui":
            question=True
        elif reponse == "non":
            question=False
        else: ## pour le "jsp"
            question=None
    else:
        print("\n \t\t/!\ ERREUR /!\ \n /!\ Repondre par oui ou par non ou par jsp en toute lettre /!\ \n")
        #input(reponse)  
    
    branche2 = []
    for i in tableau:
        if i[key] !=question:
            branche2.append(i)

    for j in branche2:
        tableau.remove(j) 

    return tableau



########## Questions ##########


def pose_question(key,tableau:list, a:int, b:int):
    question = 0
    for i in range(10):
        random.randint(a, b)
        

    return question




print ("\n /!\ Repondre par oui ou par non en toute lettre /!\ \n")

#Question 1
reponse = input("Le cadeau que tu recherches est pour une personne de sexe féminin ?")

question1= rep_question(reponse,"femme",branche1)

rep_question(reponse,"femme",branche1)

print(question1)


#Question 2
print("\n")
reponse = input("Le cadeau que tu recherches est pour un(e) enfant ?")
question2=rep_question(reponse,"enfant",question1)
rep_question(reponse,"enfant",question1)
print(question2)

#Question 3
print("\n")
reponse = input("Le cadeau que tu recherches est un jouet ?")
question3=rep_question(reponse,"jouet",question2)
rep_question(reponse,"jouet",question2)
print(question3)

#Question 4
print("\n")
reponse = input("Fin ?")
question4=rep_question(reponse,"test",question3)
rep_question(reponse,"test",question3)
print(question4)

