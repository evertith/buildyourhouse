#!/usr/bin/env python3
"""
Generate 8.5 Common Measurements (1 page)
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
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
    filename = "/Users/evertith/Repositories/2025/nexarune/buildyourhouse/build-your-house/section-8-output/8.5-common-measurements.pdf"

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
        fontSize=13,
        textColor=colors.black,
        spaceAfter=8,
        spaceBefore=12
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        textColor=colors.black,
        leading=14
    )

    # Title
    elements.append(Paragraph("8.5 COMMON MEASUREMENTS & CONVERSIONS", title_style))
    elements.append(Spacer(1, 0.15*inch))

    intro_text = """Quick reference for common construction measurements, lumber dimensions, and unit conversions.
Keep this handy for quick calculations on the job site."""
    elements.append(Paragraph(intro_text, body_style))
    elements.append(Spacer(1, 0.15*inch))

    # LUMBER DIMENSIONS
    elements.append(Paragraph("ACTUAL LUMBER DIMENSIONS (Nominal vs. Actual)", heading_style))

    lumber_data = [
        ['Nominal Size', 'Actual Size', 'Common Uses'],
        ['1x2', '3/4" × 1-1/2"', 'Trim, furring strips'],
        ['1x3', '3/4" × 2-1/2"', 'Trim, lattice'],
        ['1x4', '3/4" × 3-1/2"', 'Trim, boards'],
        ['1x6', '3/4" × 5-1/2"', 'Trim, fascia, boards'],
        ['1x8', '3/4" × 7-1/4"', 'Trim, shelving'],
        ['1x10', '3/4" × 9-1/4"', 'Shelving, trim'],
        ['1x12', '3/4" × 11-1/4"', 'Shelving, stair treads'],
        ['2x2', '1-1/2" × 1-1/2"', 'Furring, light framing'],
        ['2x3', '1-1/2" × 2-1/2"', 'Light framing, blocking'],
        ['2x4', '1-1/2" × 3-1/2"', 'Wall framing, blocking'],
        ['2x6', '1-1/2" × 5-1/2"', 'Floor joists, rafters, headers'],
        ['2x8', '1-1/2" × 7-1/4"', 'Floor joists, rafters, headers'],
        ['2x10', '1-1/2" × 9-1/4"', 'Floor joists, beams, headers'],
        ['2x12', '1-1/2" × 11-1/4"', 'Floor joists, beams, headers'],
        ['4x4', '3-1/2" × 3-1/2"', 'Posts, columns'],
        ['4x6', '3-1/2" × 5-1/2"', 'Beams, posts'],
        ['6x6', '5-1/2" × 5-1/2"', 'Large posts, beams'],
    ]

    lumber_table = Table(lumber_data, colWidths=[1.2*inch, 1.3*inch, 3.5*inch])
    lumber_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(lumber_table)
    elements.append(Spacer(1, 0.15*inch))

    # LINEAR CONVERSIONS
    elements.append(Paragraph("LINEAR MEASUREMENTS & CONVERSIONS", heading_style))

    linear_data = [
        ['From', 'To', 'Multiply By', 'Example'],
        ['Inches', 'Feet', '÷ 12', '36" = 3 feet'],
        ['Feet', 'Inches', '× 12', '5 feet = 60"'],
        ['Feet', 'Yards', '÷ 3', '9 feet = 3 yards'],
        ['Yards', 'Feet', '× 3', '2 yards = 6 feet'],
        ['Inches', 'Centimeters', '× 2.54', '12" = 30.48 cm'],
        ['Feet', 'Meters', '× 0.3048', '10 feet = 3.048 m'],
    ]

    linear_table = Table(linear_data, colWidths=[1.1*inch, 1.2*inch, 1.3*inch, 2.4*inch])
    linear_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(linear_table)
    elements.append(Spacer(1, 0.15*inch))

    # AREA AND VOLUME CONVERSIONS
    elements.append(Paragraph("AREA & VOLUME CONVERSIONS", heading_style))

    area_data = [
        ['Measurement', 'Conversion', 'Common Use'],
        ['1 square foot', '144 square inches', 'Area calculations'],
        ['1 square yard', '9 square feet', 'Carpet, concrete'],
        ['1 square (roofing)', '100 square feet', 'Roofing materials'],
        ['1 cubic foot', '1,728 cubic inches', 'Volume calculations'],
        ['1 cubic yard', '27 cubic feet', 'Concrete, soil, gravel'],
        ['1 cubic yard concrete', 'Covers 81 sq ft at 4" thick', 'Slab calculations'],
        ['1 gallon', '128 fluid ounces', 'Paint, liquids'],
        ['1 gallon', '0.1337 cubic feet', 'Liquid volume'],
    ]

    area_table = Table(area_data, colWidths=[1.6*inch, 2.2*inch, 2.2*inch])
    area_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(area_table)
    elements.append(Spacer(1, 0.15*inch))

    # COMMON BUILDING MEASUREMENTS
    elements.append(Paragraph("STANDARD BUILDING DIMENSIONS", heading_style))

    building_data = [
        ['Item', 'Standard Dimension', 'Notes'],
        ['Stud spacing', '16" or 24" O.C.', 'On center measurement'],
        ['Standard ceiling height', '8 feet', 'Residential rooms'],
        ['Door height (interior)', '6\'-8" (80")', 'Standard pre-hung'],
        ['Door height (exterior)', '6\'-8" to 8\'-0"', 'Varies by style'],
        ['Door width (interior)', '24", 28", 30", 32", 36"', 'Common sizes'],
        ['Door width (exterior)', '32", 36"', 'Most common'],
        ['Window rough opening', '+2" width, +2-1/2" height', 'Add to window size'],
        ['Door rough opening', '+2" width, +2-1/2" height', 'Add to door size'],
        ['Countertop height', '36"', 'Kitchen/bathroom standard'],
        ['Countertop depth', '24" to 25"', 'Standard base cabinet'],
        ['Upper cabinet height', '12", 15", 18", 30", 42"', 'Common sizes'],
        ['Stair riser (max)', '7-3/4"', 'Residential code'],
        ['Stair tread (min)', '10"', 'Residential code'],
    ]

    building_table = Table(building_data, colWidths=[1.6*inch, 1.8*inch, 2.6*inch])
    building_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(building_table)
    elements.append(Spacer(1, 0.15*inch))

    # HELPFUL TIPS
    tips_text = """<b>Quick Tips:</b><br/>
• When measuring, always double-check and measure twice before cutting<br/>
• "O.C." means "on center" - measured from center of one member to center of the next<br/>
• Rough openings are larger than actual door/window sizes to allow for shimming and adjustment<br/>
• Always verify local code requirements as they may differ from these standards"""
    elements.append(Paragraph(tips_text, body_style))

    # Build PDF
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"Created: {filename}")

if __name__ == "__main__":
    create_pdf()
