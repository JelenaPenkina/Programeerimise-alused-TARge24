"""Class bed"""
import random
import BunkBed
import Bed

if __name__ == '__main__':

    bed1 = Bed(200, 200, is_made=True)
    print(bed1.accommodates_people())
    print(bed1.get_is_made())
    print(bed1.get_size())
    bed2 = BunkBed(110, 200, is_made=True, floors=3)
    print(bed2.bunk_bed_accommodates_people())
    print(bed2.get_is_made())
    print(bed2.get_size())

    all_beds = []
    bunkBeds = int(100 * 0.4)
    beds = 100 - bunkBeds

    for _ in range(beds):
        length = random.randint(180, 220)
        width = random.randint(80, 240)
        is_made = random.choice([True, False])
        all_beds.append(Bed(length, width, is_made=is_made))

    for _ in range(bunkBeds):
        length = random.randint(180, 220)
        width = random.randint(80, 200)
        floors = random.choice([2, 3])
        is_made = random.choice([True, False])
        all_beds.append(BunkBed(length, width, is_made=is_made, floors=floors))

for i, bed in enumerate(all_beds):
    print(f"Voodi {i + 1}: {bed.accommodates_people()}")
    print(f"Voodi {i + 1}: {bed}")