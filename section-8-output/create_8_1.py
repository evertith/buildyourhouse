#!/usr/bin/env python3
"""
Generate 8.1 Residential Code Quick Reference (3 pages)
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
    filename = "/Users/evertith/Repositories/2025/nexarune/buildyourhouse/build-your-house/section-8-output/8.1-residential-code-quick-reference.pdf"

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

    # Title
    elements.append(Paragraph("8.1 RESIDENTIAL CODE QUICK REFERENCE", title_style))
    elements.append(Spacer(1, 0.2*inch))

    # Introduction
    intro_text = """This quick reference guide contains the most commonly referenced residential building code requirements.
Always verify with your local jurisdiction as requirements may vary. Local amendments may be more restrictive than
the International Residential Code (IRC)."""
    elements.append(Paragraph(intro_text, body_style))
    elements.append(Spacer(1, 0.2*inch))

    # PAGE 1: STAIRS AND GUARDRAILS
    elements.append(Paragraph("STAIRS AND HANDRAILS", heading_style))

    # Stairs table
    stairs_data = [
        ['Requirement', 'Minimum/Maximum', 'Notes'],
        ['Maximum Riser Height', '7.75 inches', 'Height from one tread to next'],
        ['Minimum Tread Depth', '10 inches', 'Measured horizontally'],
        ['Maximum Riser Variance', '3/8 inch', 'Between tallest/shortest risers'],
        ['Maximum Tread Variance', '3/8 inch', 'Between deepest/shallowest'],
        ['Minimum Stair Width', '36 inches', 'Clear width, not including handrails'],
        ['Minimum Headroom', '6 feet 8 inches', 'Measured vertically above nosing'],
        ['Handrail Height', '34-38 inches', 'Measured from nosing'],
        ['Handrail Required', 'When 4+ risers', 'At least one side required'],
        ['Handrail Graspability', '1.25-2 inches', 'Perimeter or grip size'],
        ['Handrail Clearance', '1.5 inches minimum', 'From wall to handrail'],
    ]

    stairs_table = Table(stairs_data, colWidths=[2.2*inch, 1.8*inch, 2.0*inch])
    stairs_table.setStyle(TableStyle([
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
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))

    elements.append(stairs_table)
    elements.append(Spacer(1, 0.15*inch))

    # Guardrails
    elements.append(Paragraph("GUARDRAILS", heading_style))

    guardrails_data = [
        ['Requirement', 'Minimum/Maximum', 'Notes'],
        ['Required When', 'Drop exceeds 30 inches', 'Porches, decks, landings, balconies'],
        ['Minimum Height', '36 inches residential', 'Measured from deck/floor surface'],
        ['Sphere Test', '4 inch maximum opening', 'No gaps allowing 4" sphere to pass'],
        ['Triangle Test', '6 inch max opening', 'For stair guardrail triangular openings'],
        ['Load Requirements', '200 lbs concentrated', 'At top rail in any direction'],
        ['Intermediate Rails', 'Spaced to prevent 4" sphere', 'Balusters, pickets, or mesh'],
    ]

    guardrails_table = Table(guardrails_data, colWidths=[2.2*inch, 1.8*inch, 2.0*inch])
    guardrails_table.setStyle(TableStyle([
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
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))

    elements.append(guardrails_table)

    # PAGE 2: ELECTRICAL AND SMOKE DETECTORS
    elements.append(PageBreak())

    elements.append(Paragraph("ELECTRICAL OUTLETS AND CIRCUITS", heading_style))

    electrical_data = [
        ['Location', 'Requirement', 'Additional Notes'],
        ['Wall Outlets - Spacing', 'Maximum 12 feet apart', 'No point more than 6 feet from outlet'],
        ['Wall Outlets - Doors', 'Maximum 6 feet from door', 'Measured along wall'],
        ['Kitchen Counter Outlets', 'Maximum 4 feet apart', 'Must be above counter height'],
        ['Kitchen Islands', 'One outlet required', 'Island 24" x 12" or larger'],
        ['Bathroom Outlets', 'One within 3 feet of sink', 'Must be GFCI protected'],
        ['Garage Outlets', 'At least one', 'GFCI protected'],
        ['Exterior Outlets', 'Front and back required', 'GFCI protected, weather-resistant'],
        ['Basement Outlets', 'At least one', 'GFCI if unfinished'],
        ['Hallways', 'One if 10+ feet long', 'Measured along centerline'],
    ]

    electrical_table = Table(electrical_data, colWidths=[2.0*inch, 2.2*inch, 1.8*inch])
    electrical_table.setStyle(TableStyle([
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
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))

    elements.append(electrical_table)
    elements.append(Spacer(1, 0.15*inch))

    # GFCI Requirements
    elements.append(Paragraph("GFCI PROTECTION REQUIRED:", subheading_style))
    gfci_text = """• All bathroom outlets<br/>
• Kitchen countertop outlets<br/>
• All exterior outlets<br/>
• All garage outlets<br/>
• Unfinished basement outlets<br/>
• Crawl space outlets<br/>
• Laundry room outlets (within 6 feet of sink)<br/>
• Wet bar sink outlets"""
    elements.append(Paragraph(gfci_text, body_style))
    elements.append(Spacer(1, 0.15*inch))

    # Smoke Detectors
    elements.append(Paragraph("SMOKE AND CO DETECTORS", heading_style))

    smoke_data = [
        ['Location', 'Requirement', 'Notes'],
        ['Each Sleeping Room', 'One smoke detector', 'Inside each bedroom'],
        ['Outside Sleeping Areas', 'One per sleeping area', 'In hallway near bedrooms'],
        ['Each Story', 'At least one', 'Including basement, not crawl space'],
        ['Interconnection', 'All must be interconnected', 'When one sounds, all sound'],
        ['Power Source', 'Hardwired with battery backup', 'Or 10-year sealed battery'],
        ['CO Detectors', 'Outside sleeping areas', 'Required if fuel-burning appliances'],
        ['CO Detector - Each Level', 'One per floor minimum', 'Including basement'],
    ]

    smoke_table = Table(smoke_data, colWidths=[2.0*inch, 2.2*inch, 1.8*inch])
    smoke_table.setStyle(TableStyle([
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
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))

    elements.append(smoke_table)

    # PAGE 3: WINDOWS AND CEILING HEIGHTS
    elements.append(PageBreak())

    elements.append(Paragraph("EMERGENCY ESCAPE AND RESCUE OPENINGS (EGRESS WINDOWS)", heading_style))

    egress_data = [
        ['Requirement', 'Minimum/Maximum', 'Notes'],
        ['Required Location', 'Each sleeping room', 'Basements with bedrooms also need egress'],
        ['Minimum Net Clear Opening', '5.7 square feet', 'Actual openable area'],
        ['Minimum Opening Width', '20 inches', 'Clear opening when open'],
        ['Minimum Opening Height', '24 inches', 'Clear opening when open'],
        ['Maximum Sill Height', '44 inches', 'From floor to bottom of opening'],
        ['Window Wells (if req.)', '9 sq ft minimum', 'If window well depth >44 inches'],
        ['Window Well Width', '36 inches minimum', 'Horizontal projection'],
        ['Window Well Ladder', 'Required if >44" deep', 'Permanent ladder or steps'],
        ['Ladder Requirements', 'Max 18" projection', 'Rungs 3" wide, 12" spacing max'],
    ]

    egress_table = Table(egress_data, colWidths=[2.2*inch, 1.8*inch, 2.0*inch])
    egress_table.setStyle(TableStyle([
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
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))

    elements.append(egress_table)
    elements.append(Spacer(1, 0.15*inch))

    # Ceiling Heights
    elements.append(Paragraph("CEILING HEIGHTS", heading_style))

    ceiling_data = [
        ['Room Type', 'Minimum Height', 'Notes'],
        ['Habitable Rooms', '7 feet', 'Living rooms, bedrooms, kitchens'],
        ['Bathrooms', '6 feet 8 inches', 'At fixtures and circulation paths'],
        ['Hallways', '6 feet 8 inches', 'Minimum clear height'],
        ['Kitchens', '6 feet 8 inches', 'At work areas'],
        ['Basements (unfinished)', '6 feet 8 inches', 'Beams may project to 6 feet 4 inches'],
        ['Sloped Ceilings', '50% of room area at min height', 'No portion below 5 feet'],
        ['Furred Ceilings', 'Maintain minimum heights', 'Account for lowered ceiling'],
    ]

    ceiling_table = Table(ceiling_data, colWidths=[2.0*inch, 1.8*inch, 2.2*inch])
    ceiling_table.setStyle(TableStyle([
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
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))

    elements.append(ceiling_table)
    elements.append(Spacer(1, 0.15*inch))

    # Additional Requirements
    elements.append(Paragraph("ADDITIONAL COMMON REQUIREMENTS", heading_style))

    additional_data = [
        ['Item', 'Requirement'],
        ['Tempered Glass', 'Required within 24" of door, bottom edge <60" above floor'],
        ['Bathroom Ventilation', 'Window 3 sq ft (1.5 sq ft openable) OR mechanical fan'],
        ['Mechanical Fan', 'Min 50 CFM intermittent or 20 CFM continuous (bathroom)'],
        ['Stair Lighting', 'Required at top and bottom, 3-way switches if 6+ risers'],
        ['Insulation', 'Meet energy code for climate zone (R-values vary by location)'],
        ['Attic Access', 'Minimum 22" x 30" opening, accessible location'],
        ['Crawl Space Access', 'Minimum 18" x 24" opening'],
    ]

    additional_table = Table(additional_data, colWidths=[2.2*inch, 3.8*inch])
    additional_table.setStyle(TableStyle([
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
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))

    elements.append(additional_table)
    elements.append(Spacer(1, 0.15*inch))

    # Important note
    note_text = """<b>IMPORTANT:</b> This quick reference is based on the International Residential Code (IRC).
Always verify requirements with your local building department as local amendments may differ. When in doubt,
consult with your building inspector before proceeding."""
    elements.append(Paragraph(note_text, body_style))

    # Build PDF
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"Created: {filename}")

if __name__ == "__main__":
    create_pdf()
