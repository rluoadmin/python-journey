import os

source = "1.jpg"
destination = "./temp"

if not os.path.exists(destination):
    os.makedirs(destination)

with open(source, "rb") as f, open(os.path.join(destination, "2.jpg"), "wb") as f2:
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        f2.write(chunk)
