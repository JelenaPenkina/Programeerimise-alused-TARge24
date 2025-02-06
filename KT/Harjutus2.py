clients = int(input("Sisesta klientide arv: "))
flowers = 0
i = 1

while i <= clients:
    flowers += i
    i += 2  # Suureneb paaritute arvude kaupa

print(f"Kokku kingiti {flowers} lille.")
