import sys
from PIL import Image, ImageOps

def main():
    
    if len(sys.argv) < 3:
        print("Too few arguments")
        sys.exit(1)
    elif len(sys.argv) > 4:
        print("Too many arguments")
        sys.exit(1)
    extensions = ("jpg", "jpeg", "png")
    
    if not sys.argv[1].endswith(extensions) or not sys.argv[2].endswith(extensions):
        print("your file is not a image")
        sys.exit(1)
    elif not sys.argv[1].endswith("jpg") and sys.argv[2].endswith("jpg"):
        print("both files are not jpg")
        sys.exit(1)
    elif not sys.argv[1].endswith("jpeg") and sys.argv[2].endswith("jpeg"):
        print("both files are not jpeg")
        sys.exit(1)
    elif not sys.argv[1].endswith("png") and sys.argv[2].endswith("png"):
        print("both files are not png")
        sys.exit(1)
    
    filebefore = sys.argv[1]
    fileafter = sys.argv[2]
    process_image(filebefore, fileafter)

def process_image(filebefore, fileafter):
    try:
        image = Image.open(filebefore)
        shirt = Image.open("shirt.png")
        image = ImageOps.fit(image, shirt.size)
        image.paste(shirt, (0,0), shirt)
        image.save(fileafter)

    except FileNotFoundError:
        print("File not found")
        sys.exit(1)




if __name__ == "__main__":
    main()