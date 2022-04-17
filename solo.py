branche1 = [
    {"objet":"GAGNER", "femme":True, "enfant":True, "jouet":True},

    {"objet":"drone", "femme":False, "enfant":False, "jouet":True},

    {"objet":"voiture télécomandé", "femme":False, "enfant":True, "jouet":False},

    {"objet":"poupé", "femme":True, "enfant":True, "jouet":True},

    {"objet":"playstation", "femme":False, "enfant":False, "jouet":False},

    {"objet":"xbox", "femme":False, "enfant":False, "jouet":False},

    {"objet":"album de musique kpop", "femme":True, "enfant":False, "jouet":False},

    {"objet":"ablum de musique rap", "femme":False, "enfant":False, "jouet":False},

    {"objet":"bracelet", "femme":True, "enfant":True, "jouet":False},

    {"objet":"rouge à levre", "femme":True, "enfant":False, "jouet":False},

    {"objet":"crampons de foot", "femme":False, "enfant":True, "jouet":False},
    {"objet":"crampons de foot", "femme":True, "enfant":True, "jouet":False},

    {"objet":"cliché", "femme":False, "enfant":False, "jouet":True},

    {"objet":"plus d'idee", "femme":True, "enfant":False, "jouet":True},
]


def rep_question(reponse, key,question_pose):
    if reponse == "oui" or "o":
        question=True
    if reponse =="non" or "n":
        question=False
    else:
        print("erreur vous n'avez pas repondu par oui ou non")
        quit()

    branche2 = []
    for i in branche1:
        if i[key] !=question:
            branche2.append(i)

    for j in branche2:
        branche1.remove(j) 

    if question_pose==2: #en fonction du nombre de question
        print(branche1)


print ("\n /!\ Repondre par oui ou par non en toute lettre /!\ \n")

#Question 1
question = input("Le cadeau que tu recherches est pour une personne de sexe féminin ?")
rep_question(question,"femme",1)

#Question 2
question = input("Le cadeau que tu recherches est pour un(e) enfant ?")
rep_question(question,"enfant",2)

#Question 3
#question = input("Le cadeau que tu recherches est un jouet ?")
#rep_question(question,"enfant",3)

