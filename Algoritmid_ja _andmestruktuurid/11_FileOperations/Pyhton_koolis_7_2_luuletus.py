""" Tee uus fail luuletus.txt ning lisa sinna järgmine luuletus:
Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.

Koosta programm, mis kuvab ekraanile luuletuse read, kuid lisab nende ette rea järjekorranumbri
ja iga rea järele sulgudesse reas asuvate sümbolite arvu e. rea pikkuse. """

with open("luuletus.txt", encoding="utf8") as file:
    for nr, line in enumerate(file):
        print(f"{nr + 1} {line.rstrip()} {len(line)}")
