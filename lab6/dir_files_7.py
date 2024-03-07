f1 = input("Copy from:")
f2 = input("Paste to:")
with open(f1, "r") as f1:
    with open(f2, "w") as f2:
        f2.write(f1.read())
