def run():
    myList = [1,"hello, True, 4.5"]
    myDic = {"firstName": "luis", "lastName": "castilla"}
    
    superList = [
       {"firstName": "luis", "lastName": "castilla"},
       {"firstName": "miguel", "lastName": "torres"},
       {"firstName": "pepe", "lastName": "rodelo"},
       {"firstName": "susana", "lastName": "martinez"},
       {"firstName": "jose", "lastName": "garcia"},
    ]
    
    superDic = {
        "naturalNums":[1,2,3,4,5],
        "integerNums":[-1,-2,0,1,2],
        "floatingNums":[1.1,4.5,6.43]
    }
    
    for key, value in superDic.items():
        print(key, "-", value)




if __name__ == "__main__":
    run()