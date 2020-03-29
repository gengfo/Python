def main():
    fo = open("test.txt", "r+")

    fnew = open("new.txt", "w")
    fnew.write("this is test")
    fnew.close()

    print(fo)

if __name__ == "__main__":
    main()
