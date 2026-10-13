def main():

    t = int(input())
    for i in range(t):
        n = int(input())
        print(f"Case #{i+1}: {n*pow(2 , n-1 , 1000000007)%1000000007}")

if __name__ == "__main__":
    main()
