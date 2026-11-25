class Bird:
    def eat(self):
        print("Bird is eating")


class FlyingBird(Bird):
    def fly(self):
        print("Bird is flying")


class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow is flying")


class Penguin(Bird):
    def swim(self):
        print("Penguin is swimming")


def make_bird_fly(bird: FlyingBird):
    bird.fly()


def main():
    sparrow = Sparrow()
    penguin = Penguin()

    for bird in (sparrow, penguin):
        bird.eat()
    make_bird_fly(sparrow)
    penguin.swim()


if __name__ == "__main__":
    main()