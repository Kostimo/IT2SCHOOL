d = {
    1: 4,
    2: 12,
    3: 11,
    4: 20,
    5: 25
}
d_items = d.items()
lst = [k*v for k, v in d_items]
print(lst)