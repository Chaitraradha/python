with open("f1.txt",'w') as fh:
    fh.write(f"newfile\n:python class")
name=["Anu", "Priya", "Akarsh"]
with open("f1.txt",'a') as fh:
    fh.write(f"{name}\n")

