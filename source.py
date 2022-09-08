def f(t, y):
    return 2 * t * y

def Euler1(hi, t = 0, y = 1):
    i = 1
    while (t <= 1):
        y += hi * f(t, y)
        t += hi
        print("%i. %0.3e %0.5e" % (i, t, y))
        i+=1
    print()

def Euler2(hi, t = 0, y = 1):
    i = 1
    while(t <= 1):
        y += 0.5 * hi * (f(t, y) + f(t + hi, y + hi * f(t, y)))
        t += hi
        print("%i. %0.3e %0.5e" % (i, t, y))
        i += 1
    print()

def Euler3(hi, t = 0, y = 1):
    i = 1
    while(t <= 1):
        y += hi * f(t + 0.5 * hi, y + hi * 0.5 * f(t, y))
        t += hi
        print("%i. %0.3e %0.5e" % (i, t, y))
        i += 1
    print()
        


h = [0.1, 0.05, 0.025]
print("Первая схема Эйлера")
for hi in h:
    print(f"step: {hi}")
    Euler1(hi)

print("Вторая схема Эйлера")
for hi in h:
    print(f"step: {hi}")
    Euler2(hi)

print("Третья схема Эйлера")
for hi in h:
    print(f"step: {hi}")
    Euler3(hi)
