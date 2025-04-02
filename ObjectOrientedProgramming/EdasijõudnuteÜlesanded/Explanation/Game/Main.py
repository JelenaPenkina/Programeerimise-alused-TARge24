import Statistics

if __name__ == '__main__':
    stats = Statistics

    print(stats.get("/players"))  # ['Mati', 'Kati', 'Peeter']
    print(stats.get("/games"))  # ['chess', 'poker', 'monopoly']
    print(stats.get("/total"))  # 3
    print(stats.get("/total/winner"))  # 1
    print(stats.get("/player/Mati/amount"))  # 2
    print(stats.get("/player/Mati/won"))  # 1
