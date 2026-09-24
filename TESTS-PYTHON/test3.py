def motlepluslong (a: list):
    b = ""
    for i in a:
        if len(i) >= len(b):
            b = i
    return b


print(motlepluslong(["snob","bonjour", "virtuel", "chat"]))

            