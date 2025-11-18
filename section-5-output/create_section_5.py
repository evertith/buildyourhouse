#!/usr/bin/env python3
"""
Create all Section 5: FINISH WORK PDFs
Owner-Builder Job Site Binder  
Total: 38 pages across 6 documents
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle, 
                                 Paragraph, Spacer, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfgen import canvas

# Page setup
PAGE_WIDTH, PAGE_HEIGHT = letter
LEFT_MARGIN, RIGHT_MARGIN = 1.5 * inch, 1 * inch
TOP_MARGIN, BOTTOM_MARGIN = 1 * inch, 1 * inch

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        self.page_offset = kwargs.pop('page_offset', 0)
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []
    
    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()
    
    def save(self):
        for i, page in enumerate(self.pages):
            self.__dict__.update(page)
            self.draw_page(i + 1 + self.page_offset)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)
    
    def draw_page(self, page_num):
        self.saveState()
        self.setFont('Helvetica', 10)
        self.drawString(LEFT_MARGIN, PAGE_HEIGHT - 0.5*inch,
                       f"Owner-Builder Job Site Binder | Section 5: Finish Work | Page {page_num}")
        self.setFont('Helvetica', 9)
        self.drawCentredString(PAGE_WIDTH/2, 0.5*inch, str(page_num))
        self.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, 0.5*inch, 
                            "© 2024 Build Your House")
        self.restoreState()

def get_styles():
    styles = getSampleStyleSheet()
    return {
        'title': ParagraphStyle('CustomTitle', parent=styles['Heading1'],
                               fontName='Helvetica-Bold', fontSize=16,
                               textColor=colors.black, spaceAfter=12, alignment=TA_CENTER),
        'heading': ParagraphStyle('CustomHeading', parent=styles['Heading2'],
                                 fontName='Helvetica-Bold', fontSize=13,
                                 textColor=colors.black, spaceAfter=8, spaceBefore=12),
        'subheading': ParagraphStyle('CustomSubHeading', parent=styles['Heading3'],
                                    fontName='Helvetica-Bold', fontSize=11,
                                    textColor=colors.black, spaceAfter=6, spaceBefore=8),
        'normal': ParagraphStyle('CustomNormal', parent=styles['Normal'],
                                fontName='Helvetica', fontSize=11,
                                textColor=colors.black, leading=14)
    }

def make_table(data, col_widths, header_row=True):
    """Helper to create styled tables"""
    table = Table(data, colWidths=col_widths)
    style = [
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11 if header_row else 10),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]
    if header_row:
        style.extend([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ])
    table.setStyle(TableStyle(style))
    return table

print("Creating Section 5 PDFs...")
print("=" * 70)

# Continue script in next command due to character limit
