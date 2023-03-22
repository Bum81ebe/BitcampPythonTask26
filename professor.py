import random
level = ""

def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            level = int(input("Please choose the Level: "))
        except ValueError:
            continue
        if level > 3 and level < 1:
            continue
        else:
            break
    level = int(level)
    return level
        


def generate_integer(level):
   # print("Level is :",level)
    if level == 1:
        point = 10
        attempt = 3
        for i in range(10):
            x = random.randint(1, 9)
            y = random.randint(1, 9)
            n = 0
            while n < 10:
                try:
                    z = int(input(f"{x} + {y} = "))
                except ValueError:
                    continue
                if x + y != z:
                    print("EEE")
                    attempt -= 1
                    if attempt == 0:
                        point -= 1
                        break
                else:
             #       print("Correct!")
                    break
                n += 1
            if attempt == 0:
                print(x, "+" , y , "=" , (x + y))
                attempt = 3
                continue
        print(f"Score: {point}")

    if level == 2:
        point = 10
        attempt = 3
        for i in range(10):
            x = random.randint(11, 99)
            y = random.randint(11, 99)
            n = 0
            while n < 10:
                try:
                    z = int(input(f"{x} + {y} = "))
                except ValueError:
                    continue
                if x + y != z:
                    print("EEE")
                    attempt -= 1
                    if attempt == 0:
                        point -= 1
                        break
                else:
             #       print("Correct!")
                    break
                n += 1
            if attempt == 0:
                print(x, "+" , y , "=" , (x + y))
                attempt = 3
                continue
        print(f"Score: {point}")
    elif level == 3:
        point = 10
        attempt = 3
        for i in range(10):
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            n = 0
            while n < 10:
                try:
                    z = int(input(f"{x} + {y} = "))
                except ValueError:
                    continue
                if x + y != z:
                    print("EEE")
                    attempt -= 1
                    if attempt == 0:
                        point -= 1
                        break
                else:
             #       print("Correct!")
                    break
                n += 1
            if attempt == 0:
                print(x, "+" , y , "=" , (x + y))
                attempt = 3
                continue
        print(f"Score: {point}")

    





if __name__ == "__main__":
    main()