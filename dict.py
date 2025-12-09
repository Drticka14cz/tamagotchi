#dictionary - slovník, je soubor zpárovaných klíčů a honot (key - value)
tel_sez = {
    "Radek": "+420 111 111 111",
    "mohamed": "+alžírsko 222 222 222",
    "pferd": "+420 333 333 333",
}
print(tel_sez["Radek"])
cat = {
    "jméno": "erika",
    "věk": "86",
    "barva": "černá",
    "žije?": False, 
    "oblíbené jídlo": "eintopf",
    "Kámoši": ["beran", "kavka"]


}
print(cat["barva"])
for key in cat:
    print(key)
for key, hodnota in cat.items():
    print(f"{key}: {hodnota}")

for klic in cat:
    print(cat[klic])

for hodnota in cat.values():
    print(hodnota)