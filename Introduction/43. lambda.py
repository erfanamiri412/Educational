def f(): return "hello"
f = lambda: "hello"
print(f())

# answer = hello


def f(x): return 2*x
f = lambda x:2*x
print(f(10))

# answer = 20


def f(x,y): return x+y
f = lambda x,y: x+y
print(f(10, 20))

# answer = 30


def f(x,y,z): return x+y+z
f = lambda x,y,z: x+y+z
print(f(10,20,30))

# answer = 60