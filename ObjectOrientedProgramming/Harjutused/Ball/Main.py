from Ball import Ball
from InflatableBall import InflatableBall
import random


if __name__ == '__main__':
    balls = []
    for _ in range(60):
        balls.append(Ball(random.randint(15, 30), random.choice(["basketball", "tennis", "football"])))

    for _ in range(40):
        balls.append(InflatableBall(random.randint(10, 25), "beachball", inflated=random.choice([True, False])))

    for ball in balls:
        print(ball.bounce())