

def g():
	print("hello")


def main():
	x = []
	m = 5
	for i in range(10000):
		x.append(i)
		m += 1
	for i in x:
		m += 1
	print("Hello World")
	print("Hello World")
	g()

