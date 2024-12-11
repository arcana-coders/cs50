from fpdf import FPDF

def main():
    graduado = input("your amazing name please: ")
    make_shirt(graduado)

def make_shirt(graduado):
    shirt = FPDF(orientation = "P", unit = "mm", format = "A4")
    shirt.add_page()
    shirt.set_font("Arial", size = 24)
    shirt.cell(0,10,"CS50 Shirtificate", align = "C", ln = True)
    shirt.image("shirtificate.png", x=25, y=55, w=150)
    shirt.set_font("Arial", size=18)
    shirt.set_text_color(255,255,255)
    shirt.text(x = 65, y = 110, txt=f"{graduado} pass CS50")
    shirt.output("shirtificate.pdf")

if __name__ == "__main__":
    main()