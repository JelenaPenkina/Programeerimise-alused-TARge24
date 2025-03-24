"""
Tee uus fail luuletus.txt ning lisa sinna järgmine luuletus:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.
Koosta programm, mis kuvab ekraanile luuletuse read, kuid lisab nende ette
rea järjekorranumbri ja iga rea järele sulgudesse reas asuvate sümbolite arvu e. rea pikkuse.
"""

file_name = 'luuletus.txt'

with open(file_name, 'w') as f:
    f.write("""Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.
""")

with open(file_name) as f:
    for nr, line in enumerate(f):
        line = line.strip()
        print(f'{nr + 1} {line}({len(line) - 1})')