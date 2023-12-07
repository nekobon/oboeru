from fpdf import FPDF
from pathlib import Path
import typing as tp
import math


        # if(unit=='pt'):
        #     self.k=1
        # elif(unit=='mm'):
        #     self.k=72/25.4
        # elif(unit=='cm'):
        #     self.k=72/2.54
        # elif(unit=='in'):
        #     self.k=72.
        # else:
        #     self.error('Incorrect unit: '+unit)
        # # Page format
        # if(isinstance(format,basestring)):
        #     format=format.lower()
        #     if(format=='a3'):
        #         format=(841.89,1190.55)
        #     elif(format=='a4'):
        #         format=(595.28,841.89)
        #     elif(format=='a5'):
        #         format=(420.94,595.28)
        #     elif(format=='letter'):
        #         format=(612,792)
        #     elif(format=='legal'):
        #         format=(612,1008)

# to be parameters
size = 'letter'
orientation = 'P' # or 'L'
font = 'Arial'
font_size = 20
rows = 12
cols = 4
margin = 10 # 1 cm
input_fp = 'input.txt'
border = 1


pdf = FPDF(orientation, 'mm', size)
pdf.set_margins(margin, margin, margin)
pdf.set_font(font, 'B', font_size)
pdf.set_auto_page_break(False)

class Card(tp.NamedTuple):
    front: str
    back: str

def read_input(fp: Path) -> tp.List[Card]:
    cards = list()
    with fp.open('r') as f:
        for line in f:
            front, back = line.strip().split('\t')
            cards.append(Card(front, back))
    return cards

def add_one_page(pdf: FPDF, cards: tp.List[Card], rows: int, cols: int, front: bool) -> None:
    cell_width = (pdf.w - 2*margin)/ cols
    cell_height = (pdf.h - 2*margin) / rows
    pdf.add_page()
    for i in range(len(cards)):
        card = cards[i] if front else  cards[cols-1-i%cols + i//cols*cols]
        face = card.front if front else card.back
        # if ln is True, then the next cell will be placed below the current one, if false, then on the right
        pdf.cell(cell_width, cell_height, face, align='C', border=border, ln=((i+1)%cols)==0)

cards = read_input(Path(input_fp))
num_face_pages = math.ceil(len(cards) / (rows * cols))

for p in range(num_face_pages):
    cards_one_page = cards[p * rows * cols : (p+1) * rows * cols]
    add_one_page(pdf, cards_one_page, rows, cols, True)
    add_one_page(pdf, cards_one_page, rows, cols, False)




    # for i, card in enumerate(cards):
        # pdf.cell(cell_width, cell_height, card.front, align='C', border=1, ln=((i+1)%cols)==0)

# for i in range(1, 19):
#     pdf.cell(cell_width, cell_height, f'cat', align='C', border=1, ln=(i%cols)==0)

pdf.output('tuto1.pdf', 'F')
