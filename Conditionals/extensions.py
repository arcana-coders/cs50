def main ():
    sufix = input("Gimme the file name  ")
    sufix = sufix.replace(" ","").lower()
    sufix = sufix.replace(".", " ")
    if sufix.endswith("gif"):
        print("image/gif")
    elif sufix.endswith("jpg"):
        print("image/jpeg")
    elif sufix.endswith("jpeg"):
        print("image/jpeg")
    elif sufix.endswith("png"):
        print("image/png")
    elif sufix.endswith("pdf"):
        print("application/pdf")
    elif sufix.endswith("txt"):
        print("text/plain")
    elif sufix.endswith("zip"):
        print("application/zip")
    else:
        print("application/octet-stream")    


    
main ()