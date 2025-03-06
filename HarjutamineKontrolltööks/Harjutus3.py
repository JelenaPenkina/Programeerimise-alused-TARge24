clients = int(input("Sisesta klientide arv: "))
flowers = 0
count = 1
i = 1

while count <= clients:
    flowers += i
    i += 2
    count += 1

print(f"Kokku kingiti {flowers} lille.")

