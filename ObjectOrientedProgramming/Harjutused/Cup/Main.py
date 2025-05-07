from Cup import Cup
from TravelMug import TravelMug
import random

if __name__ == '__main__':
    cups = []
    for _ in range(60):
        cups.append(Cup(random.randint(200, 500), random.choice(["blue", "green", "white"]), random.choice([True, False])))

    for _ in range(40):
        cups.append(TravelMug(random.randint(300, 600), random.choice(["black", "red"]), random.choice([True, False]), lid_on=random.choice([True, False])))

    for i, cup in enumerate(cups):
        print(f"Cup {i+1}: {cup}")