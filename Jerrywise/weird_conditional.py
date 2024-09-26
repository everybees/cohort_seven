n_int = int(input("Enter a nnumber: "))

if n_int % 2 != 0:
    print("weird")
if n_int % 2 == 0 and 2 <= n_int <= 5:
    print("not weird")
if n_int % 2== 0 and 6<= n_int <= 20:
    print("not weird")
if n_int % 2 == 0 and n_int >= 20:
    print("not weirld")