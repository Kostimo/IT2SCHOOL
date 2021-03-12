with open("text.txt", mode="r") as text:
    nums = list(range(10))
    lines = text.readlines()
    d = {}
    d.fromkeys(nums, None)
    # for i in range(10):
    #     for el in lines:
    #         d[i] = el
            
    print(d)
    # for k, v in d.items():
    #     if v[0] in "euioaEUIOA":
    #         d[k] = v[::-1]
    #     if v[0] in "tpkTPK":
    #         del d[k]
    # print(d)