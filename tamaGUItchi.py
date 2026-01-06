from sys import exit
import datetime as dt
import json
import os
from nicegui import ui 
from PIL import Image
# global cas_hladu
# cas_hladu = dt.datetime.now() + dt.timedelta(seconds=10)


zprava = None
obrazek = None
spritesheet = Image.open("cat.png")


def load_data():
    global beta
    if os.path.isfile("tamagotchi.json"):
        with open("tamagotchi.json", "r", encoding="utf-8") as f:
            beta = json.load(f)
    else:
        print("Chyba při načítání souboru")
        beta = {
            "jméno": "Adolf",
            "hlad": 50,
            "žízeň":0,
            "barva": "bílá",
            "životy":100,
            "čisota":100,
            "energie":90,
            "žije": True,
            "věk":0,
            "nešťastnost": False,
            "nemoc":False,


}
        save_data()
    # print("a")
    

    

def save_data():

    global beta
    with open("tamagotchi.json", "w", encoding="utf-8") as f:
        f = json.dump(beta, f, ensure_ascii=False, indent = 4)

def reset():
    global beta
    beta = {
        "jméno": "Adolf",
        "hlad": 50,
        "žízeň":0,
        "barva": "bílá",
        "životy":100,
        "čisota":100,
        "energie":90,
        "žije": True,
        "věk":0,
        "nešťastnost": False,
        "nemoc":False,


}
    save_data()
    zprava.text = "Reset dokončen"

def status():
    # for i in beta:
    #     print(f"{i} : {beta[i]}")
    print(f"""
Hlad je {beta['hlad']}
Žízeň je {beta['žízeň']}
Energie je {beta['energie']}

""")#dopsat podmínku
    zprava.content = f"""
Hlad je {beta['hlad']}<br>
Žízeň je {beta['žízeň']}<br>
Energie je {beta['energie']}

"""
    

def hra():
    beta["nešťastnost"] = False
    beta["energie"] -= 20
    beta["žízeň"] += 20
    beta["hlad"] += 20
    zprava.content = "Zahráno"
    print(f"Právě sis hrál s Adolfem a je šťastný. \nEnergie({beta['energie']})\nŽízeň({beta['žízeň']})\nHlad({beta['hlad']})")

def spánek():
    beta["energie"] = 100
    print(f"Adolf se vyspal. \nEnergie({beta['energie']})")
    obrazek.source = vystrihni_obrazek(0,45)

def nakrmit():
    
    if beta["hlad"]<= -50 or beta["hlad"] >= 150:
        beta["životy"] -=20
        beta["hlad"] -= 10
        print(f"odebral jsem 20 životů({beta['životy']}), \nodebral jsem 10 hladu{beta['hlad']}")
        kontroluj_status()
        ui.notify("Nakrmeno")
    else:
        beta["hlad"] -= 10
        if beta["životy"] < 100:
            beta["životy"] +=1
    print(f"Adolfův hlad je:{beta["hlad"]}")

def kontroluj_status():
    if beta["životy"] <= 0:
        beta["žije"] == False
        print("Adolf umřel!")
        
        ui.shutdown()
        exit()
    if beta["věk"] > 5:
        beta["žije"] == False
        print("Adolf umřel")
        
        ui.shutdown()
        exit()
        
def hladoveni():
    beta["hlad"] += 10
    if beta["hlad"] >= 150:
        beta["životy"] -=20
        print(f"odebral jsem 20 životů({beta['životy']})")
        kontroluj_status()
    print(f"Adolf má hlad! - ({beta["hlad"]})")
def starnuti():
    beta["věk"] += 0

def vystrihni_obrazek(x, y):
    x= x*64
    y= y*64
    return spritesheet.crop((x, y, x+64, y+64))

def main():
    global obrazek, zprava
    #


    print("Vítej")
    print("""  
      /\\
    _/./
 ,-'    `-:..-'/
: o )      _  (
"`-....,--; `-.\\
    `'
  """)
    print("Pro ukončení napišš konec\n")


    #taky stare
    tlacitka = {
        "Nakmit": nakrmit,
        "Hrát": hra, 
        "spát": spánek,
        "status": status, 
        "reset": reset, 
    }
    with ui.element("div").classes("w-full h-screen flex items-center justify-center flex-col flex gap-5"):
        # zprava = ui.label("ahaaaoj")
        ui.label("nadpis").classes("text-4xl")
        
        print(zprava)
        obrazek = ui.image(vystrihni_obrazek(2,4)).classes("h-32 w-32")
        with ui.element("div").classes("w-100 h-50 border-2 border-solid border-black grid grid-cols-3 gap-y- gap-x-2 place-items-center"):
            for jmeno, funkce in tlacitka.items():
                ui.button(jmeno, on_click=funkce).classes("w-30 h-20")
        with ui.element("div").classes("w-100 h-25 border-2 border-black border-solid"):
            with ui.element("div").classes("place-items-center"):
                ui.label("Status").classes("text-lg underline")
            with ui.element("div").classes("place-items-center"):
                zprava = ui.markdown("výpis")
                
    cas_hladu = dt.datetime.now() + dt.timedelta(seconds=10)
    cas_stari = dt.datetime.now() + dt.timedelta(minutes=1)

    beta = load_data()
    # while True:
    #     print("Looop")
    #     uziv_input = input("\n: ")
    #     aktual = dt.datetime.now()
    #     if aktual >= cas_hladu:
    #         hladoveni()
    #         cas_hladu = dt.datetime.now() + dt.timedelta(seconds=10)
    #     if aktual >= cas_stari:
    #         starnuti()
    #         cas_stari = dt.datetime.now() + dt.timedelta(minutes=1)
        
    #     if uziv_input.lower() == "konec":
    #         print("Konec programu... Auf wiedersehen")
    #         save_data()
    #         break
    #     elif uziv_input.lower() == "k":
    #         nakrmit()
    #     elif uziv_input.lower() == "h":
    #         hra()
    #     elif uziv_input.lower() == "s":
    #         spánek()
    #     elif uziv_input.lower() == "p":
    #         status()
    #     elif uziv_input.lower() == "r":
    #         reset()

            
    #     save_data()
    #STARÉ - PRO KOMUNIKACI S TERMINÁLEM
    save_data()
    ui.run()
    
        
        
# if __name__ == "__main__":
    
main()
    


