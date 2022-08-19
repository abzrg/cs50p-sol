"""\
-----------------
CS50 Shirtificate
-----------------

Takes a name and outputs a pdf file (using fpdf2)

- The orientation of the PDF should be Portrait.
- The format of the PDF should be A4, which is 210mm wide by 297mm tall.
- The top of the PDF should “CS50 Shirtificate” as text, centered horizontally.
- The shirt’s image should be centered horizontally.
- The user’s name should be on top of the shirt, in white text.

Source: https://cs50.harvard.edu/python/2022/psets/8/shirtificate/
"""

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        header_y: float = 50.0
        header_x: float = self.epw
        header_font_size: int = 45
        self.set_font("helvetica", "", header_font_size)
        self.cell(header_x, header_y, "CS50 Shirtificate", align="C")


def main() -> int:
    """Main function"""

    pdf: PDF = PDF(orientation="P", unit="mm", format="A4")

    # Disable auto page break
    pdf.set_auto_page_break(False)

    # Create page
    pdf.add_page()

    # Set margin (mm)
    margin: float = 10
    pdf.set_margin(margin)

    # Display image
    image_x: float = margin
    image_y: float = 60.0
    pdf.image("shirtificate.png", x=image_x, y=image_y, w=pdf.epw)

    # Writing text onto shirt
    shirt_font_size: int = 20
    shirt_text: str = "Ali Bozorgzadeh took CS50"
    shirt_text_y: float = 120
    pdf.set_font("helvetica", "", shirt_font_size)
    pdf.set_y(shirt_text_y)
    # Changing text color
    pdf.set_text_color(255,255,255)
    pdf.cell(pdf.epw, 0, shirt_text, align="C")

    pdf.output("shirtificate.pdf")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
