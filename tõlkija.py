def a(phrase):
    b= ""
    for s in phrase:
        if s in "AEIOUaeiou":
            if s.isupper():
                b=b+"G"
            else:
                b=b+"g"
        else:
            b=b+s
    return b


print(a(input("Sisesta sõna: ")))
        