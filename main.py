from pathlib import Path
from PIL import Image, ImageFilter
import csv


def proc1():
    temp = Path("output")
    temp.mkdir(parents=True, exist_ok=True)
    for image_path in Path("resourses").glob("*.jpg"):
        outp_dir = Path("output", "new_" + image_path.name)

        with Image.open(image_path) as img:
            img.load()
            new_img = img.filter(ImageFilter.FIND_EDGES)
            new_img.save(outp_dir)
            img.close()


def proc2():
    file = open(Path("resourses", "list.csv"))
    data = list(csv.reader(file, delimiter="|"))
    print("Order:")
    sum: float = 0
    for i in data:
        print(f"{i[0]}- Amount:{i[1]}, cost {i[2]} rub.")
        sum += float(i[2]) * int(i[1])
    print(f"Price: {sum} rub.")
    file.close()


proc1()