import os.path
if os.path.isfile("individualpizzacosts.txt"):
    print("yes")
    file2 = open("individualpizzacosts.txt", "a")
else:
    print("no")
    file2 = open("individualpizzacosts.txt", "x")
file2.write("pizzacost\n");