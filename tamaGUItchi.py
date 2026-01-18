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
BASE_DIR = os.path.dirname(__file__) 
spritesheet = Image.open(os.path.join(BASE_DIR, "fish.png"))

beta = {}


def load_data():
    global beta
    if os.path.isfile("tamagotchi.json"):
        if os.path.getsize("tamagotchi.json") == 0: 
            print("Soubor je prázdný, vytvářím nový...") 
            return create_default()
        else:
            with open("tamagotchi.json", "r", encoding="utf-8") as f:
                beta = json.load(f)
                return beta
    else:
        print("Chyba při načítání souboru")
        beta = {
            "jméno": "Adolf",
            "hlad": 50,
            "voda":100,
            "barva": "bílá",
            "životy":100,
            "čisota":100,
            "energie":90,
            "žije": True,
            "věk":0,
            "nešťastnost": 0,
            "nemoc":False,
    


}
        create_default()
        save_data()
        return beta
 
    

def create_default():
    global beta
    beta = {
        "jméno": "Adolf",
        "hlad": 50,
        "voda": 100,
        "barva": "bílá",
        "životy": 100,
        "čisota": 100,
        "energie": 90,
        "žije": True,
        "věk": 0,
        "nešťastnost": 0,
        "nemoc": False,
    }
    save_data()
    return beta


def save_data():

    
    global beta
    with open("tamagotchi.json", "w", encoding="utf-8") as f:
        json.dump(beta, f, ensure_ascii=False, indent=4)


def reset():
    global beta
    beta = {
        "jméno": "Adolf",
        "hlad": 50,
        "voda":100,
        "barva": "bílá",
        "životy":100,
        "čisota":100,
        "energie":90,
        "žije": True,
        "věk":0,
        "nešťastnost": 0,
        "nemoc":False,


}
    save_data()
    zprava.content = "Reset dokončen"
    obrazek.source = os.path.join(BASE_DIR, "fish_0.png")

def status():
    # for i in beta:
    #     print(f"{i} : {beta[i]}")
    print(f"""
Hlad je {beta['hlad']}
Kvalita vody je {beta['voda']}
Energie je {beta['energie']}

""")#dopsat podmínku
    zprava.content = f"""
Hlad je {beta['hlad']}<br>
Kvalita vody je {beta['voda']}<br>
Energie je {beta['energie']}<br>
Životy....? 

"""
    

def hra():
    global obrazek
    beta['nešťastnost'] -= 50
    beta['energie'] -= 20
    zhorseni_vody()
    hladoveni()
    if beta['nešťastnost'] <0:
        beta['nešťastnost'] = 0
    zprava.content = f"""Právě sis hrál s Adolfem a je šťastný. <br>Energie({beta['energie']}) <br>Kvalita vody:({beta['voda']})<br>Hlad({beta['hlad']})"""
    
    obrazek.source = os.path.join(BASE_DIR, "fish_3.png")
    kontroluj_status()
def spánek():
    global obrazek
    beta['energie'] = 100
    
    zprava.content = f"Adolf se vyspal. \nEnergie({beta['energie']})"
    
    zprava.content = f"Adolf se vyspal. \nEnergie({beta['energie']})"
    obrazek.source = os.path.join(BASE_DIR, "fish_1.png")

def nakrmit():
    global obrazek
    if beta['hlad']<= -50 or beta['hlad'] >= 150:
        beta['životy'] -=20
        beta['hlad'] -= 10
        zprava.content = "Adolf je přežraný!"
       
        
    else:
        beta["hlad"] -= 10
        if beta["životy"] < 100:
            beta["životy"] +=5
    
    obrazek.source = os.path.join(BASE_DIR, "fish_2.png")
    zprava.content = f"Nakrmil jsi adolfa! (hlad: {beta['hlad']})"
    kontroluj_status()

def voda():
    zprava.content = "Voda vyměněna!<br>Adolf je šťastnější.."
    beta['voda'] += 50
    if beta['voda'] > 120:
        beta['voda'] =100
        zprava.content = f"Moc měniš vodu...."
        beta['životy'] -= 10
    beta['životy'] +=50
    if beta['životy'] > 100:
        beta['životy'] =100
    beta['nešťastnost'] -= 25
    if beta['nešťastnost'] <0:
        beta['nešťastnost'] = 0
    
    
def kontroluj_status():
    if not beta['žije']:
        zprava.content = "Resetuji hru, protože Adolf umřel"
        obrazek.source = os.path.join(BASE_DIR, "fish_5.png")
        
        ui.timer(10.0, reset)
        return

    
    if beta["životy"] <= 0:
        zprava.content = "Zhebl"
        beta["žije"] = False
        return
        
       
        
        
        
    if beta["věk"] > 5:
        beta["žije"] = False
        
        zprava.content = "Adolf umřel..... D:"
        obrazek.source = os.path.join(BASE_DIR, "fish_5")
        print("umrel")
        return
        
        
    if beta['nešťastnost'] > 100:
        beta['životy'] -= 1
        ui.timer(10.0, kontroluj_status)
        zprava.content = f"Adolf je smutný..."
    if beta['energie'] < -50:
        beta['životy'] -=50
        ui.timer(25.0,kontroluj_status)
    

def hladoveni():
    beta["hlad"] += 10
    
    if beta["hlad"] >= 150:
        beta["životy"] -=20
        
        zprava.content= f"Adolf má hlad!!! <br>Odebral jsem 20 životů({beta['životy']})"
        obrazek.source = os.path.join(BASE_DIR, "fish_4.png")
        kontroluj_status()
    if beta["hlad"] >100:
        

        
        zprava.content = f"Adolf má hlad! - ({beta['hlad']})"
    else:
        zprava.content = f"Adolf tráví své jídlo..."
def zhorseni_vody():
    global pozadi
    
    beta['voda'] -= 15
    if beta["voda"] <= -150:
        beta["životy"] -=20
        
        zprava.content= f"Adolf má špatnou vodu!!! <br>Odebral jsem 20 životů({beta['životy']})"
        obrazek.source = os.path.join(BASE_DIR, "fish_4.png")
        pozadi.style("background-color: green")
        kontroluj_status()
    elif beta["voda"] <20:
        pozadi.style("background-color: #38B2AC")
        

        
        zprava.content = f"Adolf má špatnou vodu! - ({beta['voda']})"
    
    else:
        zprava.content = f"Zhoršuje se voda..."
        pozadi.style("background-color: skyblue")
def starnuti():
    beta["věk"] += 1
    zprava.content = f"Adolf mí narozky! je mu {beta['věk']}!"

def smutek():
    beta['nešťastnost'] +=5



def random_event():
    if beta["žije"] == False: 
        return
    else:

        zprava.content = f"BLO blo "
        obrazek.source = os.path.join(BASE_DIR, "fish_0.png")
def main():
    global obrazek, zprava, tlacitka, pozadi
    #

    print("Spuštím...")


    #taky stare
    tlacitka = {
        "Nakmit": nakrmit,
        "Hrát": hra, 
        "spát": spánek,
        "Doplnit vodu": voda, 
        "status": status, 
        "reset hry": reset, 
    }
    ui.timer(3600.0, starnuti)
    ui.timer(60.0, hladoveni)
    ui.timer(35.0, smutek)
    ui.timer(42.0, zhorseni_vody)
    ui.timer(25.0, random_event)
    ui.timer(60.0, kontroluj_status)
    pozadi = ui.query("body")
    pozadi.style("background-color: skyblue")
    with ui.element("div").classes("w-full h-screen flex items-center justify-center flex-col flex gap-5 ").style(" width: 100vw; height: 100vh; "):# background-color: skyblue;
        # zprava = ui.label("ahaaaoj")
        ui.label("nadpis").classes("text-4xl")
        
        
        with ui.element("div").classes("h-32 w-32 "):
            
            obrazek = ui.image(os.path.join(BASE_DIR, "fish_0.png")).classes("h-32 w-32")
            


        with ui.element("div").classes("w-100 h-50 border-2 border-solid border-black grid grid-cols-3 gap-y- gap-x-2 place-items-center"):
            for jmeno, funkce in tlacitka.items():
                ui.button(jmeno, on_click=funkce).classes("w-30 h-20")
        with ui.element("div").classes("w-100 h-38 border-2 border-black border-solid"):
            with ui.element("div").classes("place-items-center"):
                ui.label("Status").classes("text-lg underline")
            with ui.element("div").classes("place-items-center"):
                zprava = ui.markdown("")
                
    # cas_hladu = dt.datetime.now() + dt.timedelta(seconds=10)
    # cas_stari = dt.datetime.now() + dt.timedelta(minutes=1)


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
    beta = load_data()
    save_data()
    
    ui.run()
    
    #dadawdawawd
        
# if __name__ == "__main__":
    
main()
    


