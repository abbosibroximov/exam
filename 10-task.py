def add(a,b):
    try:
        return a+b
    except TypeError:
        return int(a)+int(b)
    finally:
        print("Strni ham hisoblaydi!")
result=add(100,"100")
print(result)
