counter_v = 0
counter_c = 0

try: 
    input = int(input("Zadejte text: "))
    for character in input:
        if character in "aeiyou":
            counter_v += 1
        if character in "qwrtzplkjhgfdsxcvbnm":
            counter_c += 1
    print(f"Text obsahuje {counter_v} samohlásek a {counter_c} souhlásek.")
except TypeError:
    print("Nebyl zadán text.")