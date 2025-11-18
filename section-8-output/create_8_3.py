#!/usr/bin/env python3
"""
Generate 8.3 Material Calculators (2 pages)
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfgen import canvas

# Page dimensions
LEFT_MARGIN = 1.5 * inch
RIGHT_MARGIN = 1 * inch
TOP_MARGIN = 1 * inch
BOTTOM_MARGIN = 1 * inch

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_elements(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_elements(self, page_count):
        self.setFont("Helvetica", 9)

        # Header
        header_text = f"Owner-Builder Job Site Binder | Section 8: Quick Reference Guides | Page {self._pageNumber}"
        self.drawString(LEFT_MARGIN, letter[1] - 0.5*inch, header_text)

        # Footer - page number (center)
        self.drawCentredString(letter[0]/2, 0.5*inch, str(self._pageNumber))

        # Footer - copyright (right)
        self.drawRightString(letter[0] - RIGHT_MARGIN, 0.5*inch, "© 2024 Build Your House")

def create_pdf():
    filename = "/Users/evertith/Repositories/2025/nexarune/buildyourhouse/build-your-house/section-8-output/8.3-material-calculators.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN
    )

    # Container for elements
    elements = []

    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        textColor=colors.black,
        spaceAfter=12,
        alignment=TA_CENTER
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        textColor=colors.black,
        spaceAfter=10,
        spaceBefore=12
    )

    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=12,
        textColor=colors.black,
        spaceAfter=6,
        spaceBefore=8
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        textColor=colors.black,
        leading=14
    )

    formula_style = ParagraphStyle(
        'FormulaStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        textColor=colors.black,
        leading=16,
        leftIndent=20,
        spaceAfter=6
    )

    # Title
    elements.append(Paragraph("8.3 MATERIAL CALCULATORS", title_style))
    elements.append(Spacer(1, 0.2*inch))

    intro_text = """Use these formulas and calculators to estimate material quantities for your project.
Always add 5-15% extra for waste, cuts, and mistakes. Order materials in standard sizes and quantities to minimize cost."""
    elements.append(Paragraph(intro_text, body_style))
    elements.append(Spacer(1, 0.2*inch))

    # CONCRETE CALCULATOR
    elements.append(Paragraph("CONCRETE CALCULATOR", heading_style))

    concrete_formula = """Cubic Yards = (Length × Width × Thickness in inches) ÷ 324"""
    elements.append(Paragraph(concrete_formula, formula_style))
    elements.append(Spacer(1, 0.1*inch))

    concrete_example_text = """<b>Example:</b> For a 20' × 30' slab that is 4" thick:<br/>
(20 × 30 × 4) ÷ 324 = 2,400 ÷ 324 = 7.4 cubic yards<br/>
Order 8 cubic yards (rounded up for waste)"""
    elements.append(Paragraph(concrete_example_text, body_style))
    elements.append(Spacer(1, 0.1*inch))

    # Concrete quick reference table
    concrete_data = [
        ['Slab Thickness', 'Square Feet per Cubic Yard'],
        ['4 inches', '81 sq ft'],
        ['5 inches', '65 sq ft'],
        ['6 inches', '54 sq ft'],
        ['8 inches', '40 sq ft'],
    ]

    concrete_table = Table(concrete_data, colWidths=[2.0*inch, 2.5*inch])
    concrete_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(concrete_table)
    elements.append(Spacer(1, 0.15*inch))

    # DRYWALL CALCULATOR
    elements.append(Paragraph("DRYWALL CALCULATOR", heading_style))

    drywall_formula = """Sheets Needed = Total Area ÷ 32 (for 4' × 8' sheets)"""
    elements.append(Paragraph(drywall_formula, formula_style))
    elements.append(Spacer(1, 0.1*inch))

    drywall_example_text = """<b>Example:</b> For a room with 800 sq ft of wall and ceiling area:<br/>
800 ÷ 32 = 25 sheets<br/>
Order 28 sheets (add 10% for waste and cuts)"""
    elements.append(Paragraph(drywall_example_text, body_style))
    elements.append(Spacer(1, 0.1*inch))

    drywall_tips = """<b>Drywall Tips:</b><br/>
• Use 4' × 8' sheets for walls, 4' × 12' for ceilings if possible<br/>
• 1 gallon joint compound per 100 sq ft of drywall<br/>
• 1 roll of tape per 100 linear feet of seams<br/>
• 1 pound of screws per 8 sheets (1,000 screws approx)"""
    elements.append(Paragraph(drywall_tips, body_style))
    elements.append(Spacer(1, 0.15*inch))

    # PAINT CALCULATOR
    elements.append(Paragraph("PAINT CALCULATOR", heading_style))

    paint_formula = """Gallons Needed = Total Area ÷ 350 (per coat)"""
    elements.append(Paragraph(paint_formula, formula_style))
    elements.append(Spacer(1, 0.1*inch))

    paint_example_text = """<b>Example:</b> For 1,200 sq ft of wall area with 2 coats:<br/>
1,200 ÷ 350 = 3.4 gallons per coat<br/>
3.4 × 2 coats = 6.8 gallons total<br/>
Order 7 gallons (round up)"""
    elements.append(Paragraph(paint_example_text, body_style))
    elements.append(Spacer(1, 0.1*inch))

    # Paint coverage table
    paint_data = [
        ['Surface Type', 'Coverage per Gallon'],
        ['Smooth drywall/plaster', '400 sq ft'],
        ['Textured drywall', '350 sq ft'],
        ['Rough wood/concrete', '300 sq ft'],
        ['Primer on new drywall', '300 sq ft'],
    ]

    paint_table = Table(paint_data, colWidths=[2.2*inch, 2.3*inch])
    paint_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(paint_table)

    # PAGE 2
    elements.append(PageBreak())

    # FLOORING CALCULATOR
    elements.append(Paragraph("FLOORING CALCULATOR", heading_style))

    flooring_formula = """Square Feet Needed = (Length × Width) × 1.10 (waste factor)"""
    elements.append(Paragraph(flooring_formula, formula_style))
    elements.append(Spacer(1, 0.1*inch))

    flooring_example_text = """<b>Example:</b> For a 12' × 15' room:<br/>
12 × 15 = 180 sq ft<br/>
180 × 1.10 = 198 sq ft<br/>
Order 200 sq ft (round up to nearest package size)"""
    elements.append(Paragraph(flooring_example_text, body_style))
    elements.append(Spacer(1, 0.1*inch))

    # Flooring waste factors
    waste_data = [
        ['Flooring Type', 'Recommended Waste Factor'],
        ['Carpet, sheet vinyl', '5-10% (1.05 - 1.10)'],
        ['Hardwood, straight pattern', '10-15% (1.10 - 1.15)'],
        ['Tile, diagonal pattern', '15-20% (1.15 - 1.20)'],
        ['Laminate, complex room', '10-15% (1.10 - 1.15)'],
    ]

    waste_table = Table(waste_data, colWidths=[2.3*inch, 2.7*inch])
    waste_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(waste_table)
    elements.append(Spacer(1, 0.15*inch))

    # SIDING CALCULATOR
    elements.append(Paragraph("SIDING CALCULATOR", heading_style))

    siding_formula = """Square Feet = (Total Wall Area) - (Window/Door Areas)"""
    elements.append(Paragraph(siding_formula, formula_style))
    elements.append(Spacer(1, 0.1*inch))

    siding_example_text = """<b>Example:</b> For a wall 40' long × 10' high with two 3' × 5' windows:<br/>
Wall area: 40 × 10 = 400 sq ft<br/>
Window area: 2 × (3 × 5) = 30 sq ft<br/>
Net siding: 400 - 30 = 370 sq ft<br/>
With 10% waste: 370 × 1.10 = 407 sq ft"""
    elements.append(Paragraph(siding_example_text, body_style))
    elements.append(Spacer(1, 0.1*inch))

    siding_tips = """<b>Siding Material Tips:</b><br/>
• Add 10-15% waste for lap siding<br/>
• Add 15-20% waste for diagonal or fancy patterns<br/>
• Vinyl siding sold by "square" (100 sq ft)<br/>
• Account for starter strips, J-channels, and trim"""
    elements.append(Paragraph(siding_tips, body_style))
    elements.append(Spacer(1, 0.15*inch))

    # ROOFING CALCULATOR
    elements.append(Paragraph("ROOFING CALCULATOR", heading_style))

    roofing_formula = """Squares Needed = (Roof Area in sq ft) ÷ 100"""
    elements.append(Paragraph(roofing_formula, formula_style))
    elements.append(Spacer(1, 0.1*inch))

    roofing_example_text = """<b>Example:</b> For a roof with 2,400 sq ft of area:<br/>
2,400 ÷ 100 = 24 squares<br/>
With 10% waste: 24 × 1.10 = 26.4 squares<br/>
Order 27 squares"""
    elements.append(Paragraph(roofing_example_text, body_style))
    elements.append(Spacer(1, 0.1*inch))

    # Roof pitch multipliers
    pitch_data = [
        ['Roof Pitch', 'Multiplier', 'Example: 1,000 sq ft floor'],
        ['Flat to 3:12', '1.03', '1,030 sq ft roof'],
        ['4:12', '1.05', '1,050 sq ft roof'],
        ['5:12', '1.08', '1,080 sq ft roof'],
        ['6:12', '1.12', '1,120 sq ft roof'],
        ['8:12', '1.20', '1,200 sq ft roof'],
        ['10:12', '1.30', '1,300 sq ft roof'],
        ['12:12', '1.41', '1,410 sq ft roof'],
    ]

    pitch_table = Table(pitch_data, colWidths=[1.4*inch, 1.2*inch, 2.4*inch])
    pitch_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(pitch_table)
    elements.append(Spacer(1, 0.1*inch))

    roofing_tips = """<b>Roofing Additional Materials:</b><br/>
• Ridge cap: 1 bundle per 30 linear feet<br/>
• Starter strip: 1 bundle per 100 linear feet<br/>
• Ice and water shield: 2 rolls per 1 square (100 sq ft)<br/>
• Underlayment: 4 squares per roll (400 sq ft coverage)"""
    elements.append(Paragraph(roofing_tips, body_style))
    elements.append(Spacer(1, 0.15*inch))

    # FRAMING LUMBER CALCULATOR
    elements.append(Paragraph("FRAMING LUMBER ESTIMATOR", heading_style))

    framing_data = [
        ['Application', 'Spacing', 'Formula'],
        ['Wall studs', '16" O.C.', '(Linear feet × 0.75) + extras for corners/openings'],
        ['Wall studs', '24" O.C.', '(Linear feet × 0.50) + extras for corners/openings'],
        ['Floor/ceiling joists', '16" O.C.', '(Linear feet × 0.75) + 1'],
        ['Floor/ceiling joists', '24" O.C.', '(Linear feet × 0.50) + 1'],
        ['Plates (top/bottom)', 'Per wall', 'Linear feet × 3 (for top double plate + bottom)'],
    ]

    framing_table = Table(framing_data, colWidths=[1.6*inch, 1.0*inch, 3.4*inch])
    framing_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    elements.append(framing_table)
    elements.append(Spacer(1, 0.15*inch))

    # Final note
    final_note = """<b>IMPORTANT:</b> These calculators provide estimates only. Always verify measurements on-site and consult
with suppliers for material recommendations. Order extra materials for waste, mistakes, and future repairs.
Keep leftover materials labeled and stored properly for warranty and maintenance purposes."""
    elements.append(Paragraph(final_note, body_style))

    # Build PDF
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"Created: {filename}")

if __name__ == "__main__":
    create_pdf()
