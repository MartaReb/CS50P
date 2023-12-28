from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.add_page()
        self.set_font("helvetica", "B", 40)
        self.cell(0, 60, "CS50 Shirtificate", align="C")
        self.ln(120)
        self.image("shirtificate.png", x=5, y=60, w=200)
        self.set_font("helvetica", "B", 26)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, f"{name} took CS50", align="C")

def main():
    pdf = PDF(input("Name: "))
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
