#!/usr/bin/python3


def main():
    LIM = 51
    con = 1

    while con < LIM:
        if con % 2 == 0:
            print(f"El numero {con} es par")
        con += 1



if __name__=="__main__":
    main()
