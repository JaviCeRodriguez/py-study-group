each_cons = lambda lst, n: [lst[section: section + n] for section in range(0, len(lst) - n + 1)]

def each_cons(lst, n):
    cascaded = []
    for section in range(0, len(lst) - n + 1):
        cascaded.append(lst[section:section + n])
    return cascaded
