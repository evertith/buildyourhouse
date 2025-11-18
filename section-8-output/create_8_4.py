#!/usr/bin/env python3
"""
Generate 8.4 Emergency Contacts (1 page)
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
    filename = "/Users/evertith/Repositories/2025/nexarune/buildyourhouse/build-your-house/section-8-output/8.4-emergency-contacts.pdf"

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
        spaceBefore=10
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
    elements.append(Paragraph("8.4 EMERGENCY CONTACTS", title_style))
    elements.append(Spacer(1, 0.15*inch))

    intro_text = """Keep this list updated and posted visibly at your job site. Include after-hours contact numbers where available.
In case of emergency, call 911 first, then notify the appropriate contacts below."""
    elements.append(Paragraph(intro_text, body_style))
    elements.append(Spacer(1, 0.15*inch))

    # EMERGENCY SERVICES
    elements.append(Paragraph("EMERGENCY SERVICES", heading_style))

    emergency_data = [
        ['Service', 'Phone Number'],
        ['Emergency (Fire/Medical/Police)', '911'],
        ['Poison Control Center', '1-800-222-1222'],
        ['Police (Non-Emergency)', '_' * 40],
        ['Fire Department (Non-Emergency)', '_' * 40],
        ['Hospital/Urgent Care', '_' * 40],
    ]

    emergency_table = Table(emergency_data, colWidths=[2.2*inch, 3.8*inch])
    emergency_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(emergency_table)
    elements.append(Spacer(1, 0.15*inch))

    # BUILDING OFFICIALS & INSPECTORS
    elements.append(Paragraph("BUILDING DEPARTMENT & INSPECTORS", heading_style))

    officials_data = [
        ['Contact', 'Name', 'Phone Number'],
        ['Building Inspector', '_' * 25, '_' * 25],
        ['Electrical Inspector', '_' * 25, '_' * 25],
        ['Plumbing Inspector', '_' * 25, '_' * 25],
        ['Mechanical Inspector', '_' * 25, '_' * 25],
        ['Building Dept Main Line', '_' * 25, '_' * 25],
    ]

    officials_table = Table(officials_data, colWidths=[1.8*inch, 2.0*inch, 2.2*inch])
    officials_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(officials_table)
    elements.append(Spacer(1, 0.15*inch))

    # UTILITY COMPANIES
    elements.append(Paragraph("UTILITY COMPANIES", heading_style))

    utility_data = [
        ['Utility', 'Company Name', 'Phone Number'],
        ['Electric Company', '_' * 22, '_' * 22],
        ['Gas Company', '_' * 22, '_' * 22],
        ['Water/Sewer Company', '_' * 22, '_' * 22],
        ['Telephone/Internet', '_' * 22, '_' * 22],
        ['Utility Location Service (811)', 'Call Before You Dig', '811'],
    ]

    utility_table = Table(utility_data, colWidths=[1.8*inch, 2.0*inch, 2.2*inch])
    utility_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(utility_table)
    elements.append(Spacer(1, 0.15*inch))

    # INSURANCE & PROJECT CONTACTS
    elements.append(Paragraph("INSURANCE & PROJECT CONTACTS", heading_style))

    insurance_data = [
        ['Contact Type', 'Name/Company', 'Phone Number'],
        ['Homeowner\'s Insurance Agent', '_' * 22, '_' * 22],
        ['Builder\'s Risk Insurance', '_' * 22, '_' * 22],
        ['Project Architect/Engineer', '_' * 22, '_' * 22],
        ['General Contractor (if any)', '_' * 22, '_' * 22],
    ]

    insurance_table = Table(insurance_data, colWidths=[2.0*inch, 2.0*inch, 2.0*inch])
    insurance_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(insurance_table)
    elements.append(Spacer(1, 0.15*inch))

    # SUBCONTRACTOR EMERGENCY CONTACTS
    elements.append(Paragraph("SUBCONTRACTOR EMERGENCY CONTACTS", heading_style))

    sub_data = [
        ['Trade', 'Company/Name', 'Primary Phone', 'After-Hours Phone'],
        ['Excavation', '_' * 16, '_' * 16, '_' * 16],
        ['Foundation', '_' * 16, '_' * 16, '_' * 16],
        ['Framing', '_' * 16, '_' * 16, '_' * 16],
        ['Electrical', '_' * 16, '_' * 16, '_' * 16],
        ['Plumbing', '_' * 16, '_' * 16, '_' * 16],
        ['HVAC', '_' * 16, '_' * 16, '_' * 16],
        ['Roofing', '_' * 16, '_' * 16, '_' * 16],
        ['Drywall', '_' * 16, '_' * 16, '_' * 16],
        ['Flooring', '_' * 16, '_' * 16, '_' * 16],
        ['Other: _________', '_' * 16, '_' * 16, '_' * 16],
    ]

    sub_table = Table(sub_data, colWidths=[1.2*inch, 1.6*inch, 1.6*inch, 1.6*inch])
    sub_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(sub_table)
    elements.append(Spacer(1, 0.15*inch))

    # Important note
    note_text = """<b>IMPORTANT:</b> Keep a copy of this page in your vehicle and with your project documents.
Update immediately when contact information changes. Post a copy at the job site entrance."""
    elements.append(Paragraph(note_text, body_style))

    # Build PDF
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"Created: {filename}")

if __name__ == "__main__":
    create_pdf()
