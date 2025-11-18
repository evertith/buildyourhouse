#!/usr/bin/env python3
"""
Create all Section 5: FINISH WORK PDFs
Owner-Builder Job Site Binder
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfgen import canvas

# Page dimensions
PAGE_WIDTH, PAGE_HEIGHT = letter
LEFT_MARGIN = 1.5 * inch
RIGHT_MARGIN = 1 * inch
TOP_MARGIN = 1 * inch
BOTTOM_MARGIN = 1 * inch

def create_header_footer(canvas_obj, doc, section_title, page_num):
    """Add header and footer to each page"""
    canvas_obj.saveState()

    # Header
    canvas_obj.setFont('Helvetica', 10)
    header_text = f"Owner-Builder Job Site Binder | Section 5: Finish Work | Page {page_num}"
    canvas_obj.drawString(LEFT_MARGIN, PAGE_HEIGHT - 0.5 * inch, header_text)

    # Footer - page number center, copyright right
    canvas_obj.setFont('Helvetica', 9)
    canvas_obj.drawCentredString(PAGE_WIDTH / 2, 0.5 * inch, str(page_num))
    canvas_obj.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, 0.5 * inch, "© 2024 Build Your House")

    canvas_obj.restoreState()

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        self.section_title = kwargs.pop('section_title', '')
        self.page_offset = kwargs.pop('page_offset', 0)
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for i, page in enumerate(self.pages):
            self.__dict__.update(page)
            self.draw_page(i + 1 + self.page_offset)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page(self, page_num):
        create_header_footer(self, None, self.section_title, page_num)

def get_custom_styles():
    """Return custom paragraph styles"""
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

    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=11,
        textColor=colors.black,
        spaceAfter=6,
        spaceBefore=8
    )

    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        textColor=colors.black,
        leading=14
    )

    return title_style, heading_style, subheading_style, normal_style

def create_5_1_drywall_completion_checklist():
    """5.1 Drywall Completion Checklist (6 pages)"""
    filename = "5.1-drywall-completion-checklist.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN
    )

    story = []
    title_style, heading_style, subheading_style, normal_style = get_custom_styles()

    # Title
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("DRYWALL COMPLETION CHECKLIST", title_style))
    story.append(Spacer(1, 0.2 * inch))

    # Project info
    project_data = [
        ["Project Name:", "_" * 60],
        ["Address:", "_" * 60],
        ["Inspector/Supervisor:", "_" * 40, "Date:", "_" * 20]
    ]

    project_table = Table(project_data, colWidths=[1.5*inch, 3*inch, 0.6*inch, 1.2*inch])
    project_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica', 11),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(project_table)
    story.append(Spacer(1, 0.25 * inch))

    # SECTION 1: DRYWALL HANGING
    story.append(Paragraph("SECTION 1: DRYWALL HANGING INSPECTION", heading_style))
    story.append(Spacer(1, 0.1 * inch))

    hanging_data = [
        ["Item", "Check", "Notes/Location"],
        ["All walls covered with drywall", "☐", "_" * 50],
        ["All ceilings covered with drywall", "☐", "_" * 50],
        ["Proper screw spacing (12\" o.c. walls, 12\" o.c. ceilings)", "☐", "_" * 50],
        ["No screws proud of surface (all dimpled)", "☐", "_" * 50],
        ["Corner bead installed on all outside corners", "☐", "_" * 50],
        ["Corner bead straight and secure", "☐", "_" * 50],
        ["Cutouts for electrical boxes correct and clean", "☐", "_" * 50],
        ["Cutouts for mechanical vents correct", "☐", "_" * 50],
        ["Cutouts for plumbing access correct", "☐", "_" * 50],
        ["HVAC register openings cut accurately", "☐", "_" * 50],
        ["Recessed lighting openings cut properly", "☐", "_" * 50],
        ["Joints staggered (no four-way intersections)", "☐", "_" * 50],
        ["Proper moisture-resistant drywall in wet areas", "☐", "_" * 50],
        ["Proper fire-rated drywall where required", "☐", "_" * 50],
        ["No gaps larger than 1/4\" at joints", "☐", "_" * 50],
    ]

    hanging_table = Table(hanging_data, colWidths=[4.2*inch, 0.4*inch, 2*inch])
    hanging_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(hanging_table)
    story.append(Spacer(1, 0.15 * inch))

    # Additional hanging notes
    story.append(Paragraph("Additional Hanging Notes:", subheading_style))
    for i in range(4):
        story.append(Paragraph("_" * 110, normal_style))

    story.append(PageBreak())

    # SECTION 2: TAPING AND FINISHING - FIRST COAT
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("SECTION 2: TAPING AND FINISHING", heading_style))
    story.append(Spacer(1, 0.1 * inch))

    story.append(Paragraph("First Coat (Tape and Embed):", subheading_style))

    first_coat_data = [
        ["Item", "Check", "Notes/Location"],
        ["All joints taped with paper or mesh tape", "☐", "_" * 50],
        ["Tape embedded in joint compound", "☐", "_" * 50],
        ["No bubbles or wrinkles in tape", "☐", "_" * 50],
        ["Corner bead coated", "☐", "_" * 50],
        ["Inside corners taped and embedded", "☐", "_" * 50],
        ["All screw dimples filled", "☐", "_" * 50],
        ["No ridges or high spots", "☐", "_" * 50],
        ["Compound feathered at edges", "☐", "_" * 50],
        ["Adequate drying time allowed (24+ hours)", "☐", "_" * 50],
    ]

    first_coat_table = Table(first_coat_data, colWidths=[4.2*inch, 0.4*inch, 2*inch])
    first_coat_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(first_coat_table)
    story.append(Spacer(1, 0.15 * inch))

    story.append(Paragraph("First Coat Completion Date: _______________ Inspector: _______________", normal_style))
    story.append(Spacer(1, 0.2 * inch))

    # SECOND COAT
    story.append(Paragraph("Second Coat (Fill and Feather):", subheading_style))

    second_coat_data = [
        ["Item", "Check", "Notes/Location"],
        ["All joints covered with wider coat", "☐", "_" * 50],
        ["Screw dimples filled again if needed", "☐", "_" * 50],
        ["Feathered edges 2-3\" wider than first coat", "☐", "_" * 50],
        ["Corner beads coated smoothly", "☐", "_" * 50],
        ["Inside corners smooth and even", "☐", "_" * 50],
        ["Any imperfections from first coat corrected", "☐", "_" * 50],
        ["No trowel marks or ridges", "☐", "_" * 50],
        ["Smooth transition from joint to field", "☐", "_" * 50],
        ["Adequate drying time allowed (24+ hours)", "☐", "_" * 50],
    ]

    second_coat_table = Table(second_coat_data, colWidths=[4.2*inch, 0.4*inch, 2*inch])
    second_coat_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(second_coat_table)
    story.append(Spacer(1, 0.15 * inch))

    story.append(Paragraph("Second Coat Completion Date: _______________ Inspector: _______________", normal_style))

    story.append(PageBreak())

    # THIRD COAT
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("Third Coat (Final Skim/Finish Coat):", subheading_style))

    third_coat_data = [
        ["Item", "Check", "Notes/Location"],
        ["Final skim coat applied to all joints", "☐", "_" * 50],
        ["Feathered edges 4-6\" wider than second coat", "☐", "_" * 50],
        ["All screw dimples completely invisible", "☐", "_" * 50],
        ["Corners perfectly smooth", "☐", "_" * 50],
        ["No visible ridges or imperfections", "☐", "_" * 50],
        ["Smooth transition - can't see/feel joints", "☐", "_" * 50],
        ["Entire surface ready for texture/paint", "☐", "_" * 50],
        ["Adequate drying time allowed (24+ hours)", "☐", "_" * 50],
    ]

    third_coat_table = Table(third_coat_data, colWidths=[4.2*inch, 0.4*inch, 2*inch])
    third_coat_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(third_coat_table)
    story.append(Spacer(1, 0.15 * inch))

    story.append(Paragraph("Third Coat Completion Date: _______________ Inspector: _______________", normal_style))
    story.append(Spacer(1, 0.2 * inch))

    # SANDING
    story.append(Paragraph("Sanding:", subheading_style))

    sanding_data = [
        ["Item", "Check", "Notes/Location"],
        ["All joints sanded smooth", "☐", "_" * 50],
        ["No high spots or ridges remain", "☐", "_" * 50],
        ["Corners sanded carefully (not oversanded)", "☐", "_" * 50],
        ["Entire surface smooth to touch", "☐", "_" * 50],
        ["Dust cleaned from all surfaces", "☐", "_" * 50],
        ["Dust vacuumed from floors", "☐", "_" * 50],
        ["Light test performed (no shadows/defects)", "☐", "_" * 50],
        ["Touch-up areas identified and listed below", "☐", "_" * 50],
    ]

    sanding_table = Table(sanding_data, colWidths=[4.2*inch, 0.4*inch, 2*inch])
    sanding_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(sanding_table)
    story.append(Spacer(1, 0.15 * inch))

    story.append(Paragraph("Sanding Completion Date: _______________ Inspector: _______________", normal_style))

    story.append(PageBreak())

    # TEXTURE APPLICATION
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("Texture Application (if applicable):", subheading_style))
    story.append(Spacer(1, 0.1 * inch))

    story.append(Paragraph("Texture Type: ☐ Orange Peel  ☐ Knockdown  ☐ Skip Trowel  ☐ Smooth  ☐ Other: _______________", normal_style))
    story.append(Spacer(1, 0.15 * inch))

    texture_data = [
        ["Item", "Check", "Notes/Location"],
        ["Surface properly primed before texture", "☐", "_" * 50],
        ["Texture pattern consistent throughout", "☐", "_" * 50],
        ["Texture density/coverage uniform", "☐", "_" * 50],
        ["Knockdown timing consistent (if applicable)", "☐", "_" * 50],
        ["Corners and edges textured properly", "☐", "_" * 50],
        ["Ceiling texture matches walls (if same)", "☐", "_" * 50],
        ["No drips or runs in texture", "☐", "_" * 50],
        ["Sample approved before full application", "☐", "_" * 50],
        ["Adequate drying time before painting", "☐", "_" * 50],
    ]

    texture_table = Table(texture_data, colWidths=[4.2*inch, 0.4*inch, 2*inch])
    texture_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(texture_table)
    story.append(Spacer(1, 0.15 * inch))

    story.append(Paragraph("Texture Completion Date: _______________ Applicator: _______________", normal_style))
    story.append(Spacer(1, 0.2 * inch))

    # TOUCH-UP AREAS
    story.append(Paragraph("Touch-Up Areas Needed:", subheading_style))

    touchup_data = [
        ["Location/Room", "Issue", "Corrected", "Date"],
        ["_" * 25, "_" * 35, "☐", "_" * 12],
        ["_" * 25, "_" * 35, "☐", "_" * 12],
        ["_" * 25, "_" * 35, "☐", "_" * 12],
        ["_" * 25, "_" * 35, "☐", "_" * 12],
        ["_" * 25, "_" * 35, "☐", "_" * 12],
        ["_" * 25, "_" * 35, "☐", "_" * 12],
        ["_" * 25, "_" * 35, "☐", "_" * 12],
        ["_" * 25, "_" * 35, "☐", "_" * 12],
    ]

    touchup_table = Table(touchup_data, colWidths=[2*inch, 2.8*inch, 0.8*inch, 1*inch])
    touchup_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(touchup_table)

    story.append(PageBreak())

    # SECTION 3: PROBLEM AREAS
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("SECTION 3: PROBLEM AREAS DOCUMENTATION", heading_style))
    story.append(Spacer(1, 0.1 * inch))

    story.append(Paragraph("Cracks Noted:", subheading_style))

    cracks_data = [
        ["Location", "Length", "Width", "Cause", "Repair Method", "Repaired"],
        ["_" * 18, "_" * 10, "_" * 10, "_" * 18, "_" * 18, "☐"],
        ["_" * 18, "_" * 10, "_" * 10, "_" * 18, "_" * 18, "☐"],
        ["_" * 18, "_" * 10, "_" * 10, "_" * 18, "_" * 18, "☐"],
        ["_" * 18, "_" * 10, "_" * 10, "_" * 18, "_" * 18, "☐"],
        ["_" * 18, "_" * 10, "_" * 10, "_" * 18, "_" * 18, "☐"],
        ["_" * 18, "_" * 10, "_" * 10, "_" * 18, "_" * 18, "☐"],
    ]

    cracks_table = Table(cracks_data, colWidths=[1.4*inch, 0.8*inch, 0.8*inch, 1.4*inch, 1.4*inch, 0.8*inch])
    cracks_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 10),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 9),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (5, 0), (5, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(cracks_table)
    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Nail Pops Noted:", subheading_style))

    nailpops_data = [
        ["Location/Room", "Number of Pops", "Cause (if known)", "Repaired", "Date"],
        ["_" * 22, "_" * 15, "_" * 22, "☐", "_" * 12],
        ["_" * 22, "_" * 15, "_" * 22, "☐", "_" * 12],
        ["_" * 22, "_" * 15, "_" * 22, "☐", "_" * 12],
        ["_" * 22, "_" * 15, "_" * 22, "☐", "_" * 12],
        ["_" * 22, "_" * 15, "_" * 22, "☐", "_" * 12],
        ["_" * 22, "_" * 15, "_" * 22, "☐", "_" * 12],
    ]

    nailpops_table = Table(nailpops_data, colWidths=[1.8*inch, 1.2*inch, 1.8*inch, 0.8*inch, 1*inch])
    nailpops_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 10),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (3, 0), (3, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(nailpops_table)
    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Other Repairs Needed:", subheading_style))

    repairs_data = [
        ["Location", "Description of Issue", "Priority", "Completed", "Date"],
        ["_" * 18, "_" * 35, "☐ High ☐ Med ☐ Low", "☐", "_" * 10],
        ["_" * 18, "_" * 35, "☐ High ☐ Med ☐ Low", "☐", "_" * 10],
        ["_" * 18, "_" * 35, "☐ High ☐ Med ☐ Low", "☐", "_" * 10],
        ["_" * 18, "_" * 35, "☐ High ☐ Med ☐ Low", "☐", "_" * 10],
        ["_" * 18, "_" * 35, "☐ High ☐ Med ☐ Low", "☐", "_" * 10],
        ["_" * 18, "_" * 35, "☐ High ☐ Med ☐ Low", "☐", "_" * 10],
    ]

    repairs_table = Table(repairs_data, colWidths=[1.4*inch, 2.5*inch, 1.3*inch, 0.6*inch, 0.8*inch])
    repairs_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 10),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 9),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (3, 0), (3, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(repairs_table)

    story.append(PageBreak())

    # FINAL APPROVAL
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("SECTION 4: FINAL APPROVAL", heading_style))
    story.append(Spacer(1, 0.2 * inch))

    approval_data = [
        ["Quality Check", "Pass/Fail", "Notes"],
        ["Overall drywall installation quality", "☐ Pass  ☐ Fail", "_" * 40],
        ["Taping and finishing quality", "☐ Pass  ☐ Fail", "_" * 40],
        ["Texture application (if applicable)", "☐ Pass  ☐ Fail  ☐ N/A", "_" * 40],
        ["All repairs completed satisfactorily", "☐ Pass  ☐ Fail", "_" * 40],
        ["Surface ready for priming/painting", "☐ Pass  ☐ Fail", "_" * 40],
        ["Acceptable for next phase of work", "☐ Yes  ☐ No", "_" * 40],
    ]

    approval_table = Table(approval_data, colWidths=[2.5*inch, 1.5*inch, 2.6*inch])
    approval_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(approval_table)
    story.append(Spacer(1, 0.3 * inch))

    story.append(Paragraph("Overall Comments/Observations:", subheading_style))
    for i in range(6):
        story.append(Paragraph("_" * 110, normal_style))

    story.append(Spacer(1, 0.3 * inch))

    # Signature section
    signature_data = [
        ["Inspector/Supervisor Signature:", "_" * 40, "Date:", "_" * 15],
        ["", "", "", ""],
        ["Owner/Builder Signature:", "_" * 40, "Date:", "_" * 15],
    ]

    signature_table = Table(signature_data, colWidths=[2*inch, 2.8*inch, 0.6*inch, 1.2*inch])
    signature_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica', 11),
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(signature_table)
    story.append(Spacer(1, 0.3 * inch))

    story.append(Paragraph("Items to be Completed Before Next Phase:", subheading_style))
    for i in range(4):
        story.append(Paragraph("☐ _" + "_" * 105, normal_style))

    # Build PDF
    doc.build(story, canvasmaker=lambda *args, **kwargs: NumberedCanvas(*args, section_title="Drywall", page_offset=0, **kwargs))
    print(f"✓ Created {filename}")

# Continue with remaining functions in next part due to length...
# This file will be split into multiple parts

if __name__ == "__main__":
    print("Creating Section 5: FINISH WORK PDFs...")
    print("=" * 60)
    create_5_1_drywall_completion_checklist()
    print("\nPart 1 of 6 complete. Continue with remaining files...")
