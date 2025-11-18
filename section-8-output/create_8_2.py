#!/usr/bin/env python3
"""
Generate 8.2 Span Tables (3 pages)
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
    filename = "/Users/evertith/Repositories/2025/nexarune/buildyourhouse/build-your-house/section-8-output/8.2-span-tables.pdf"

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

    note_style = ParagraphStyle(
        'NoteStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        textColor=colors.black,
        leading=11,
        leftIndent=20
    )

    # Title
    elements.append(Paragraph("8.2 SPAN TABLES", title_style))
    elements.append(Spacer(1, 0.15*inch))

    # Introduction
    intro_text = """These span tables are based on typical residential construction using No. 2 grade lumber and standard loading conditions.
<b>Always verify with your local building department and engineer's specifications for your specific project.</b> Spans are in feet-inches."""
    elements.append(Paragraph(intro_text, body_style))
    elements.append(Spacer(1, 0.15*inch))

    # PAGE 1: FLOOR JOISTS
    elements.append(Paragraph("FLOOR JOISTS - 40 PSF Live Load, 10 PSF Dead Load", heading_style))
    elements.append(Paragraph("No. 2 Grade Lumber, Deflection Limited to L/360", subheading_style))

    # 2x8 Floor Joists
    floor_2x8_data = [
        ['Joist Size: 2x8', '12" O.C.', '16" O.C.', '19.2" O.C.', '24" O.C.'],
        ['Southern Pine', "13'-3\"", "12'-0\"", "11'-2\"", "9'-11\""],
        ['Douglas Fir-Larch', "12'-8\"", "11'-6\"", "10'-8\"", "9'-6\""],
        ['Hem-Fir', "12'-2\"", "11'-0\"", "10'-3\"", "9'-1\""],
        ['Spruce-Pine-Fir', "11'-10\"", "10'-9\"", "10'-0\"", "8'-11\""],
    ]

    floor_2x8_table = Table(floor_2x8_data, colWidths=[1.6*inch, 1.1*inch, 1.1*inch, 1.1*inch, 1.1*inch])
    floor_2x8_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
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
    elements.append(floor_2x8_table)
    elements.append(Spacer(1, 0.1*inch))

    # 2x10 Floor Joists
    floor_2x10_data = [
        ['Joist Size: 2x10', '12" O.C.', '16" O.C.', '19.2" O.C.', '24" O.C.'],
        ['Southern Pine', "16'-11\"", "15'-4\"", "14'-3\"", "12'-8\""],
        ['Douglas Fir-Larch', "16'-2\"", "14'-8\"", "13'-7\"", "12'-1\""],
        ['Hem-Fir', "15'-6\"", "14'-1\"", "13'-1\"", "11'-7\""],
        ['Spruce-Pine-Fir', "15'-1\"", "13'-8\"", "12'-9\"", "11'-4\""],
    ]

    floor_2x10_table = Table(floor_2x10_data, colWidths=[1.6*inch, 1.1*inch, 1.1*inch, 1.1*inch, 1.1*inch])
    floor_2x10_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
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
    elements.append(floor_2x10_table)
    elements.append(Spacer(1, 0.1*inch))

    # 2x12 Floor Joists
    floor_2x12_data = [
        ['Joist Size: 2x12', '12" O.C.', '16" O.C.', '19.2" O.C.', '24" O.C.'],
        ['Southern Pine', "20'-7\"", "18'-8\"", "17'-4\"", "15'-5\""],
        ['Douglas Fir-Larch', "19'-8\"", "17'-10\"", "16'-7\"", "14'-9\""],
        ['Hem-Fir', "18'-10\"", "17'-1\"", "15'-11\"", "14'-1\""],
        ['Spruce-Pine-Fir', "18'-4\"", "16'-8\"", "15'-6\"", "13'-9\""],
    ]

    floor_2x12_table = Table(floor_2x12_data, colWidths=[1.6*inch, 1.1*inch, 1.1*inch, 1.1*inch, 1.1*inch])
    floor_2x12_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
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
    elements.append(floor_2x12_table)
    elements.append(Spacer(1, 0.12*inch))

    # Notes
    notes_text = """<b>Notes:</b><br/>
• O.C. = On Center (spacing between joist centers)<br/>
• Spans assume single span with bearing at ends only<br/>
• For cantilevers, maximum overhang = 1/4 of back span<br/>
• Add blocking or bridging at mid-span for joists over 8 feet"""
    elements.append(Paragraph(notes_text, note_style))

    # PAGE 2: CEILING JOISTS AND RAFTERS
    elements.append(PageBreak())

    elements.append(Paragraph("CEILING JOISTS - 10 PSF Live Load, 5 PSF Dead Load", heading_style))
    elements.append(Paragraph("No. 2 Grade Lumber, Not Supporting Habitable Space", subheading_style))

    # 2x6 Ceiling Joists
    ceiling_2x6_data = [
        ['Joist Size: 2x6', '12" O.C.', '16" O.C.', '19.2" O.C.', '24" O.C.'],
        ['Southern Pine', "17'-4\"", "15'-9\"", "14'-8\"", "13'-0\""],
        ['Douglas Fir-Larch', "16'-7\"", "15'-1\"", "14'-0\"", "12'-5\""],
        ['Hem-Fir', "15'-11\"", "14'-5\"", "13'-5\"", "11'-11\""],
        ['Spruce-Pine-Fir', "15'-6\"", "14'-1\"", "13'-1\"", "11'-8\""],
    ]

    ceiling_2x6_table = Table(ceiling_2x6_data, colWidths=[1.6*inch, 1.1*inch, 1.1*inch, 1.1*inch, 1.1*inch])
    ceiling_2x6_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
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
    elements.append(ceiling_2x6_table)
    elements.append(Spacer(1, 0.1*inch))

    # 2x8 Ceiling Joists
    ceiling_2x8_data = [
        ['Joist Size: 2x8', '12" O.C.', '16" O.C.', '19.2" O.C.', '24" O.C.'],
        ['Southern Pine', "22'-11\"", "20'-9\"", "19'-4\"", "17'-2\""],
        ['Douglas Fir-Larch', "21'-11\"", "19'-11\"", "18'-6\"", "16'-5\""],
        ['Hem-Fir', "21'-0\"", "19'-1\"", "17'-9\"", "15'-9\""],
        ['Spruce-Pine-Fir', "20'-6\"", "18'-7\"", "17'-4\"", "15'-5\""],
    ]

    ceiling_2x8_table = Table(ceiling_2x8_data, colWidths=[1.6*inch, 1.1*inch, 1.1*inch, 1.1*inch, 1.1*inch])
    ceiling_2x8_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
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
    elements.append(ceiling_2x8_table)
    elements.append(Spacer(1, 0.1*inch))

    # 2x10 Ceiling Joists
    ceiling_2x10_data = [
        ['Joist Size: 2x10', '12" O.C.', '16" O.C.', '19.2" O.C.', '24" O.C.'],
        ['Southern Pine', "Max Span", "26'-6\"", "24'-8\"", "21'-11\""],
        ['Douglas Fir-Larch', "Max Span", "25'-5\"", "23'-8\"", "21'-0\""],
        ['Hem-Fir', "26'-10\"", "24'-4\"", "22'-8\"", "20'-2\""],
        ['Spruce-Pine-Fir', "26'-2\"", "23'-9\"", "22'-1\"", "19'-8\""],
    ]

    ceiling_2x10_table = Table(ceiling_2x10_data, colWidths=[1.6*inch, 1.1*inch, 1.1*inch, 1.1*inch, 1.1*inch])
    ceiling_2x10_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
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
    elements.append(ceiling_2x10_table)
    elements.append(Spacer(1, 0.15*inch))

    # RAFTERS
    elements.append(Paragraph("COMMON RAFTERS - 30 PSF Live Load, 10 PSF Dead Load", heading_style))
    elements.append(Paragraph("No. 2 Grade Lumber, Snow Load Areas", subheading_style))

    # 2x6 Rafters
    rafter_2x6_data = [
        ['Rafter Size: 2x6', '12" O.C.', '16" O.C.', '24" O.C.'],
        ['Southern Pine', "13'-7\"", "12'-4\"", "10'-11\""],
        ['Douglas Fir-Larch', "13'-0\"", "11'-10\"", "10'-6\""],
        ['Hem-Fir', "12'-6\"", "11'-4\"", "10'-1\""],
        ['Spruce-Pine-Fir', "12'-2\"", "11'-1\"", "9'-10\""],
    ]

    rafter_2x6_table = Table(rafter_2x6_data, colWidths=[2.0*inch, 1.3*inch, 1.3*inch, 1.4*inch])
    rafter_2x6_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
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
    elements.append(rafter_2x6_table)
    elements.append(Spacer(1, 0.1*inch))

    # 2x8 Rafters
    rafter_2x8_data = [
        ['Rafter Size: 2x8', '12" O.C.', '16" O.C.', '24" O.C.'],
        ['Southern Pine', "17'-11\"", "16'-3\"", "14'-5\""],
        ['Douglas Fir-Larch', "17'-2\"", "15'-7\"", "13'-10\""],
        ['Hem-Fir', "16'-6\"", "14'-11\"", "13'-3\""],
        ['Spruce-Pine-Fir', "16'-0\"", "14'-7\"", "12'-11\""],
    ]

    rafter_2x8_table = Table(rafter_2x8_data, colWidths=[2.0*inch, 1.3*inch, 1.3*inch, 1.4*inch])
    rafter_2x8_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
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
    elements.append(rafter_2x8_table)
    elements.append(Spacer(1, 0.1*inch))

    # 2x10 Rafters
    rafter_2x10_data = [
        ['Rafter Size: 2x10', '12" O.C.', '16" O.C.', '24" O.C.'],
        ['Southern Pine', "22'-10\"", "20'-9\"", "18'-5\""],
        ['Douglas Fir-Larch', "21'-11\"", "19'-11\"", "17'-8\""],
        ['Hem-Fir', "21'-0\"", "19'-1\"", "16'-11\""],
        ['Spruce-Pine-Fir', "20'-6\"", "18'-7\"", "16'-6\""],
    ]

    rafter_2x10_table = Table(rafter_2x10_data, colWidths=[2.0*inch, 1.3*inch, 1.3*inch, 1.4*inch])
    rafter_2x10_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
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
    elements.append(rafter_2x10_table)

    # PAGE 3: HEADERS AND DECK JOISTS
    elements.append(PageBreak())

    elements.append(Paragraph("HEADERS - Load Bearing Walls", heading_style))
    elements.append(Paragraph("Building Width 24 feet, One Story Above", subheading_style))

    # Headers table
    headers_data = [
        ['Opening Width', 'Single Story', 'Two Stories', 'Three Stories'],
        ['Up to 3 feet', '2x6', '2x8', '2x10'],
        ['4 feet', '2x8', '2x10', '2x12'],
        ['5 feet', '2x10', '2x12', '2-2x12'],
        ['6 feet', '2x12', '2-2x10', '2-2x12'],
        ['8 feet', '2-2x10', '2-2x12', '3-2x12'],
        ['10 feet', '2-2x12', '3-2x12', '4-2x12'],
        ['12 feet', '3-2x12', '4-2x12', 'Engineered Beam'],
    ]

    headers_table = Table(headers_data, colWidths=[1.5*inch, 1.5*inch, 1.5*inch, 1.5*inch])
    headers_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
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
    elements.append(headers_table)
    elements.append(Spacer(1, 0.12*inch))

    # Header notes
    header_notes = """<b>Notes:</b><br/>
• Headers must be installed on edge with crown up<br/>
• Use solid blocking or cripple studs below header<br/>
• King studs and jack studs required on both sides<br/>
• For wider openings or different conditions, consult engineer"""
    elements.append(Paragraph(header_notes, note_style))
    elements.append(Spacer(1, 0.15*inch))

    # DECK JOISTS
    elements.append(Paragraph("DECK JOISTS - 40 PSF Live Load, 10 PSF Dead Load", heading_style))
    elements.append(Paragraph("Southern Pine or Douglas Fir-Larch No. 2 Grade", subheading_style))

    # 2x6 Deck Joists
    deck_2x6_data = [
        ['Joist Size: 2x6', '12" O.C.', '16" O.C.', '24" O.C.'],
        ['Maximum Span', "9'-9\"", "8'-10\"", "7'-10\""],
    ]

    deck_2x6_table = Table(deck_2x6_data, colWidths=[2.0*inch, 1.3*inch, 1.3*inch, 1.4*inch])
    deck_2x6_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
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
    elements.append(deck_2x6_table)
    elements.append(Spacer(1, 0.1*inch))

    # 2x8 Deck Joists
    deck_2x8_data = [
        ['Joist Size: 2x8', '12" O.C.', '16" O.C.', '24" O.C.'],
        ['Maximum Span', "12'-10\"", "11'-8\"", "10'-4\""],
    ]

    deck_2x8_table = Table(deck_2x8_data, colWidths=[2.0*inch, 1.3*inch, 1.3*inch, 1.4*inch])
    deck_2x8_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
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
    elements.append(deck_2x8_table)
    elements.append(Spacer(1, 0.1*inch))

    # 2x10 Deck Joists
    deck_2x10_data = [
        ['Joist Size: 2x10', '12" O.C.', '16" O.C.', '24" O.C.'],
        ['Maximum Span', "16'-5\"", "14'-11\"", "13'-3\""],
    ]

    deck_2x10_table = Table(deck_2x10_data, colWidths=[2.0*inch, 1.3*inch, 1.3*inch, 1.4*inch])
    deck_2x10_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
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
    elements.append(deck_2x10_table)
    elements.append(Spacer(1, 0.1*inch))

    # 2x12 Deck Joists
    deck_2x12_data = [
        ['Joist Size: 2x12', '12" O.C.', '16" O.C.', '24" O.C.'],
        ['Maximum Span', "20'-0\"", "18'-2\"", "16'-1\""],
    ]

    deck_2x12_table = Table(deck_2x12_data, colWidths=[2.0*inch, 1.3*inch, 1.3*inch, 1.4*inch])
    deck_2x12_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
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
    elements.append(deck_2x12_table)
    elements.append(Spacer(1, 0.15*inch))

    # Deck notes
    deck_notes = """<b>Deck Construction Notes:</b><br/>
• Joist spans measured from face of ledger to centerline of beam<br/>
• Use pressure-treated or naturally decay-resistant lumber<br/>
• Install joist hangers at ledger connections<br/>
• Maximum cantilever = 1/4 of joist span<br/>
• Check local codes for additional requirements"""
    elements.append(Paragraph(deck_notes, note_style))
    elements.append(Spacer(1, 0.15*inch))

    # Important disclaimer
    disclaimer_text = """<b>IMPORTANT DISCLAIMER:</b> These tables are for general reference only and represent common residential construction conditions.
Actual span requirements may vary based on lumber species, grade, moisture content, load duration, and local code requirements.
Always consult with your building department and structural engineer for your specific application. Engineered lumber products
(I-joists, LVL, etc.) have different span capabilities - refer to manufacturer's specifications."""
    elements.append(Paragraph(disclaimer_text, body_style))

    # Build PDF
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"Created: {filename}")

if __name__ == "__main__":
    create_pdf()
