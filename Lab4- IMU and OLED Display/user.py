#execfile("lab4task4.py")

with open("lab4task5.py", "rb") as source_file:
    code = compile(source_file.read(), "lab4task5.py", "exec")
exec(code)