def test(x):
    y = 0
    for i in range(5):
        y+=i
    return y

def main():
    a = test(7)
    print(a)

if __name__ == "__main__":
    main()