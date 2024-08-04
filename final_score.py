from pypdf import PdfWriter
from pypdf.constants import PageLabelStyle

score_file = "01 - Full score - D'un soir triste.pdf"
notes_file = "soir_triste_commentary.pdf"
output_file = "Boulanger - D'un soir triste.pdf"

def main():
    writer = PdfWriter()
    for filename in (score_file, notes_file):
        writer.append(filename)
    writer.add_outline_item("Cover", 0)
    writer.add_outline_item("Full Score", 2)
    writer.add_outline_item("Editorial Commentary", 24)
    writer.set_page_layout("/TwoPageRight")
    writer.set_page_label(0, 0, prefix="Cover")
    writer.set_page_label(1, 1, prefix="Instrumentation")
    writer.set_page_label(2, 26, style=PageLabelStyle.DECIMAL)
    writer.write(output_file)

if __name__ == "__main__":
    main()