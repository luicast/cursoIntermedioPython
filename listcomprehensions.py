def run():
    # squares = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    # squares = [i**2 for i in range(1, 101) if i % 3 != 0] 
    #squares = [i for i in range(1, 10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]   
    squares = [i for i in range(1, 10000) if i % 36 == 0]
    print(squares)



if __name__ == "__main__":
    run()