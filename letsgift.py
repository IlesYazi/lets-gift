database = [
    {"cadeau":"test1", "human":True, "youtuber":False, "movie":True , "original":False, "inventor":True, "1":False},

    {"cadeau": "test2", "human": True, "youtuber": False, "movie": False, "original": True, "inventor": True,"2": False},

    {"cadeau": "test3", "human": True, "youtuber": True, "movie": False, "original": True, "inventor": False,"3": True},

    {"cadeau": "test4", "human": True, "youtuber": True, "movie": False, "original": True, "inventor": False,"4": False},

    {"cadeau": "test5", "human": False, "youtuber": False, "movie": True, "original": False, "inventor": False,"5": False},

    {"cadeau": "test6", "human": True, "youtuber": False, "movie": False, "original": True, "inventor": False,"6": True},

    {"cadeau": "test7", "human": True, "youtuber": False, "movie": False, "original": True, "inventor": True,"7": True},
]

def take_chance(answer, property):
    if answer == "y":
        ans = True
    else:
        ans = False

    to_remove=[]
    for d in database:
        if d[property] != ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

    if len(database) == 1:
        print("Le cadeau parfait est "+database[0]["cadeau"])
        quit()


ans = input("Tu es une fille ?(y,n)")
take_chance(ans, "human")


ans = input("Tu aime manger ?(y,n)")
take_chance(ans, "youtuber")

ans = input("Nouriture exotic ?(y,n)")
take_chance(ans,"movie")

ans = input("Gourmandise préférée(y,n)")
take_chance(ans,"original")

ans = input("Text(y,n)")
take_chance(ans,"inventor")

ans = input("Text(y,n)")
take_chance(ans,"indian")


