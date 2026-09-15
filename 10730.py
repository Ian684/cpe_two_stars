def main():
	while True:
		line = input()
		if line == "0":break
		line = line.split()
		n = int(line[0][:-1])
		arr = list(map(int , line[1:]))
		pos = {}
		for i in range(n):
			pos[arr[i]] = i
		flag = False
		for l in range(n-2):
			for r in range(l + 2 , n):
				if arr[l] + arr[r] & 1:continue
				if l < pos[(arr[l] + arr[r]) // 2] < r:
					flag = True
					break
			if flag:break		
		if flag:
			print("no")
		else:
			print("yes")
			
		


if __name__ == "__main__":
	main()	
