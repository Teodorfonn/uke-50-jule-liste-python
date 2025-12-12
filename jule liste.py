def lag_onskeliste():
    navn = input("skriv inn navnet ditt: ")
    by = input("hvilken by bor du i: ")

    ønsker =[]
    print("Skriv inn 8–10 ønsker. Skriv 'slutt' hvis du er ferdig.")
    while len(ønsker) <10:
        ønske = input(f"Ønske {len(ønsker) + 1}: ")
        if ønske.lower() == "slutt":
            break
        ønsker.append(ønske)


    with open("onskelister.txt", "a", encoding="utf-8") as fil:
        fil.write(f"{navn};{by};{','.join(ønsker)}\n")


    print("Ønskelisten er lagret!\n")



def hent_sortert_leveringsliste():
     leveranser = {}


     try:
           with open("onskelister.txt", "r", encoding="utf-8") as fil:
              for linje in fil:
                navn, by, _ = linje.strip().split(";")
                if by not in leveranser:
                    leveranser[by] = []
                leveranser[by].append(navn)
     except FileNotFoundError:
        print("Ingen ønskelister funnet.")
        return
     

     print("\nLeveringsliste sortert på sted:" )
     for by in sorted(leveranser.keys()):
        print(f"- {by}: {', '.join(leveranser[by])}")   


while True:
    print("\n1. lag ønskeliste")
    print("2. vis leveringsliste for nissen")
    print("3. avslutt")
    velg = input("velg et tall: ")

    if velg == "1":
        lag_onskeliste()
    elif velg == "2":
        hent_sortert_leveringsliste()
    elif velg == "3":
        break
    else:
        print("ugyldig valg, prøv igjen ")
    
    





           