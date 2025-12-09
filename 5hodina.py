import random
seznam_zvirat = ["pes", "Rybička", "prase", "gorila", "plejtvák obecný"]
seznam_sloves = ["potrhalo", "sežralo", "ukradlo", "použilo jako potravinu pro trávení", "pochcalo"]
seznam_veci = ["Domácí úkol", "žákovskou", "ISIC", "Telefon", "mě"]
seznam_aktivit = ["spal", "hrál na pc", "nebyl doma", "ten předmět používal", "byl ve škole"]
def generator_vymluv(a,b,c,d):
    
    for i in range(3):
        score = 0
        cislo1 = random.randint(0,4)
        cislo2 = random.randint(0,4)
        cislo3 = random.randint(0,4)
        cislo4 = random.randint(0,4)
        cislo_a = 0
        for i in a:
            cislo_a += len(i)
        cislo_a = cislo_a/len(a)

        cislo_b = 0
        for i in b:
            cislo_b += len(i)
        cislo_b = cislo_b/len(b)

        cislo_c = 0
        for i in c:
            cislo_c += len(i)
        cislo_c = cislo_c/len(c)
        
        cislo_d = 0
        for i in d:
            cislo_d += len(i)
        cislo_d = cislo_d/len(d)
        if cislo_a < len(a[cislo1]):
            score +=1
        if cislo_b < len(b[cislo2]):
            score +=1
        if cislo_c < len(c[cislo3]):
            score +=1
        if cislo_d < len(d[cislo4]):
            score +=1
        

        print(f"Přišel jsem pozdě protože {a[cislo1]} {b[cislo2]} moji {c[cislo3]} zatímco jsem {d[cislo4]}")
        if score == 4:
            print(f"Score je maximální({score}), tuto výmluvu použij!")
        if score >2:
            print(f"score je {score} ze 4. Výmluva je slušná")
        else:
            print(f"Výmluva stojí za .... score je: {score}")
    #rating
    
    
        

    


generator_vymluv(seznam_zvirat, seznam_sloves, seznam_veci, seznam_aktivit)


