def generate(limit):
	
	mu = [1]*(limit+1)
	mu[0] = 0
	prime = [True]*(limit+1)
	
	for p in range(2 , limit+1):
		if prime[p]:
			for j in range(p , limit+1 , p):
				prime[j] = False
				mu[j] *= -1
			if p*p <= limit:
				for j in range(p*p , limit+1 , p*p):
					mu[j] = 0
	M = [0]*(limit+1)
	for i in range(1 , limit + 1):
		M[i] = M[i-1] + mu[i]

	return mu , M


def main():
	mu , M = generate(1000000)
	while True:
		n = int(input())
		if n == 0:break
		a , b , c = str(n) , str(mu[n]) , str(M[n])
		print(f"{' '*(8-len(a))+a}{' '*(8-len(b))+b}{' '*(8-len(c))+c}")

if __name__ == "__main__":
	main()
