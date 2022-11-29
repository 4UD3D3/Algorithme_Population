def triSelection(stringATrier):
    fini = False
    stringATrier = list(stringATrier)
    while not fini:
        for x in range(len(stringATrier) - 1):
            if stringATrier[x + 1] < stringATrier[x]:
                stringATrier[x + 1], stringATrier[x] = stringATrier[x], stringATrier[x + 1]
                break
        else:
            fini = True
    return stringATrier


def triInsertion(stringATrier):
    stringATrier = list(stringATrier)
    for i in range(1, len(stringATrier)):
        valeur = stringATrier[i]
        j = i - 1
        while j >= 0 and valeur < stringATrier[j]:
            stringATrier[j + 1] = stringATrier[j]
            j -= 1
        stringATrier[j + 1] = valeur

    return stringATrier


def fusion(L1, L2):
    L = []
    i = 0
    j = 0
    while i < len(L1):
        L.append(L1[i])
        i += 1

    while j < len(L2):
        L.append(L2[j])
        j += 1

    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1

    return L


def triFusion(stringATrier):
    if len(stringATrier) < 2:
        return stringATrier[:]
    else:
        m = len(stringATrier) // 2
        liste1 = triFusion(stringATrier[:m])
        liste2 = triFusion(stringATrier[m:])
        return fusion(liste1, liste2)


print(triInsertion(input("chaine a trier : ")))
