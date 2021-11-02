def run():
    # myDic = {}
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         myDic[i] = i**3
    # myDic = {i: i**3 for i in range(1,101) if i % 3 != 0}
    myDic = {i: round(i**0.5,2) for i in range(1, 1001)}
    print(myDic)

if __name__ == "__main__":
    run()