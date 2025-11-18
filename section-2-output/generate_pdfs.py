#!/usr/bin/env python3
"""
Generate Section 2 PDFs for Owner-Builder Job Site Binder
Contracts & Legal Documents
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import os

# Page setup constants
LEFT_MARGIN = 1.5 * inch
RIGHT_MARGIN = 1.0 * inch
TOP_MARGIN = 1.0 * inch
BOTTOM_MARGIN = 1.0 * inch

def add_header_footer(canvas_obj, doc):
    """Add header and footer to each page"""
    canvas_obj.saveState()

    # Header
    canvas_obj.setFont('Arial', 9)
    header_text = f"Owner-Builder Job Site Binder | Section 2: Contracts & Legal Documents | Page {doc.page}"
    canvas_obj.drawString(LEFT_MARGIN, letter[1] - 0.5*inch, header_text)
    canvas_obj.line(LEFT_MARGIN, letter[1] - 0.6*inch, letter[0] - RIGHT_MARGIN, letter[1] - 0.6*inch)

    # Footer
    canvas_obj.setFont('Arial', 9)
    # Page number (center)
    canvas_obj.drawCentredString(letter[0]/2, 0.5*inch, str(doc.page))
    # Copyright (right)
    canvas_obj.drawRightString(letter[0] - RIGHT_MARGIN, 0.5*inch, "© 2024 Build Your House")
    canvas_obj.line(LEFT_MARGIN, 0.7*inch, letter[0] - RIGHT_MARGIN, 0.7*inch)

    canvas_obj.restoreState()

def create_checkbox():
    """Create a checkbox character"""
    return "☐"

def create_line(width_inches):
    """Create an underline for filling in"""
    return "_" * int(width_inches * 10)

# Create styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontName='Arial-Bold',
    fontSize=16,
    textColor=colors.black,
    spaceAfter=12,
    alignment=TA_CENTER
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontName='Arial-Bold',
    fontSize=12,
    textColor=colors.black,
    spaceAfter=6,
    spaceBefore=12
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontName='Arial',
    fontSize=11,
    textColor=colors.black,
    spaceAfter=6,
    leading=14
)

bold_style = ParagraphStyle(
    'CustomBold',
    parent=styles['Normal'],
    fontName='Arial-Bold',
    fontSize=11,
    textColor=colors.black,
    spaceAfter=6
)

small_style = ParagraphStyle(
    'CustomSmall',
    parent=styles['Normal'],
    fontName='Arial-Italic',
    fontSize=10,
    textColor=colors.black,
    spaceAfter=6
)

def generate_2_1_subcontractor_agreement():
    """2.1 Subcontractor Agreement Template (6 pages)"""
    filename = "2.1-subcontractor-agreement-template.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN
    )

    story = []

    # Title
    story.append(Paragraph("SUBCONTRACTOR AGREEMENT", title_style))
    story.append(Spacer(1, 0.2*inch))

    # Project Information
    story.append(Paragraph("<b>PROJECT INFORMATION</b>", heading_style))
    story.append(Paragraph(f"<b>Project Address:</b> {create_line(8)}", body_style))
    story.append(Paragraph(f"<b>Legal Description:</b> {create_line(7.5)}", body_style))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Owner/General Contractor Information:</b>", bold_style))
    story.append(Paragraph(f"Name: {create_line(10)}", body_style))
    story.append(Paragraph(f"Address: {create_line(9.5)}", body_style))
    story.append(Paragraph(f"City/State/ZIP: {create_line(8)}", body_style))
    story.append(Paragraph(f"Phone: {create_line(4)} Email: {create_line(5)}", body_style))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Subcontractor Information:</b>", bold_style))
    story.append(Paragraph(f"Company Name: {create_line(8)}", body_style))
    story.append(Paragraph(f"License #: {create_line(4)} State: {create_line(2)}", body_style))
    story.append(Paragraph(f"Contact Person: {create_line(7)}", body_style))
    story.append(Paragraph(f"Address: {create_line(9.5)}", body_style))
    story.append(Paragraph(f"City/State/ZIP: {create_line(8)}", body_style))
    story.append(Paragraph(f"Phone: {create_line(4)} Email: {create_line(5)}", body_style))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph(f"<b>Project Description:</b> {create_line(7)}", body_style))
    story.append(Paragraph(create_line(12), body_style))
    story.append(Paragraph(f"<b>Agreement Date:</b> {create_line(3)}", body_style))
    story.append(Paragraph(f"<b>Work Start Date:</b> {create_line(3)}", body_style))
    story.append(Paragraph(f"<b>Substantial Completion Date:</b> {create_line(3)}", body_style))
    story.append(Paragraph(f"<b>Final Completion Date:</b> {create_line(3)}", body_style))

    story.append(PageBreak())

    # Scope of Work
    story.append(Paragraph("<b>SCOPE OF WORK</b>", heading_style))
    story.append(Paragraph("<b>Detailed Description of Work to be Performed:</b>", bold_style))
    for i in range(8):
        story.append(Paragraph(create_line(12), body_style))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Specifications and Standards:</b>", bold_style))
    story.append(Paragraph(f"{create_checkbox()} Work shall comply with all applicable building codes and regulations", body_style))
    story.append(Paragraph(f"{create_checkbox()} Work shall comply with approved plans dated: {create_line(4)}", body_style))
    story.append(Paragraph(f"{create_checkbox()} Work shall meet industry standards for: {create_line(5)}", body_style))
    story.append(Paragraph(f"{create_checkbox()} Other specifications: {create_line(7)}", body_style))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Materials:</b>", bold_style))
    story.append(Paragraph("Materials to be provided by Subcontractor:", body_style))
    for i in range(3):
        story.append(Paragraph(create_line(12), body_style))

    story.append(Paragraph("Materials to be provided by Owner:", body_style))
    for i in range(3):
        story.append(Paragraph(create_line(12), body_style))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Exclusions (Work NOT included in this agreement):</b>", bold_style))
    for i in range(4):
        story.append(Paragraph(create_line(12), body_style))

    story.append(PageBreak())

    # Payment Terms
    story.append(Paragraph("<b>PAYMENT TERMS</b>", heading_style))
    story.append(Paragraph(f"<b>Total Contract Amount:</b> $ {create_line(4)}", body_style))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Payment Schedule:</b>", bold_style))

    # Payment table
    payment_data = [
        ['Draw #', 'Milestone/Completion Point', 'Amount'],
        ['1', create_line(6), f"$ {create_line(2)}"],
        ['2', create_line(6), f"$ {create_line(2)}"],
        ['3', create_line(6), f"$ {create_line(2)}"],
        ['4', create_line(6), f"$ {create_line(2)}"],
        ['5', create_line(6), f"$ {create_line(2)}"],
    ]

    payment_table = Table(payment_data, colWidths=[0.8*inch, 3.5*inch, 1.5*inch])
    payment_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONT', (0, 0), (-1, 0), 'Arial-Bold', 11),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONT', (0, 1), (-1, -1), 'Arial', 11),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))
    story.append(payment_table)

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(f"<b>Retention:</b> {create_line(1.5)} % to be held until final completion and inspection", body_style))
    story.append(Paragraph(f"<b>Retention Amount:</b> $ {create_line(4)}", body_style))
    story.append(Paragraph(f"<b>Payment Terms:</b> Payment due within {create_line(1.5)} days of invoice submission", body_style))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Final Payment Conditions:</b>", bold_style))
    story.append(Paragraph("Final payment shall be made upon:", body_style))
    story.append(Paragraph(f"{create_checkbox()} Completion of all work per specifications", body_style))
    story.append(Paragraph(f"{create_checkbox()} Passing final inspection", body_style))
    story.append(Paragraph(f"{create_checkbox()} Receipt of unconditional lien waiver from Subcontractor", body_style))
    story.append(Paragraph(f"{create_checkbox()} Receipt of lien waivers from all material suppliers", body_style))
    story.append(Paragraph(f"{create_checkbox()} Submission of warranties and operating manuals (if applicable)", body_style))
    story.append(Paragraph(f"{create_checkbox()} Correction of any punch list items", body_style))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Change Orders:</b>", bold_style))
    story.append(Paragraph("All changes to the scope of work must be approved in writing via Change Order Form before work begins. No additional payment will be made for work performed without a signed change order.", body_style))
    story.append(Paragraph("Change orders must include:", body_style))
    story.append(Paragraph("• Detailed description of change", body_style))
    story.append(Paragraph("• Cost impact (materials and labor)", body_style))
    story.append(Paragraph("• Schedule impact", body_style))
    story.append(Paragraph("• Signatures of both parties", body_style))

    story.append(PageBreak())

    # Legal Requirements
    story.append(Paragraph("<b>LEGAL REQUIREMENTS AND RESPONSIBILITIES</b>", heading_style))

    story.append(Paragraph("<b>Insurance Requirements:</b>", bold_style))
    story.append(Paragraph("Subcontractor shall maintain the following insurance coverage throughout the duration of this agreement:", body_style))
    story.append(Paragraph(f"{create_checkbox()} General Liability Insurance: Minimum $ {create_line(2.5)} per occurrence", body_style))
    story.append(Paragraph(f"{create_checkbox()} Workers' Compensation Insurance (if required by state law)", body_style))
    story.append(Paragraph(f"{create_checkbox()} Vehicle Insurance: Minimum $ {create_line(2.5)} per occurrence", body_style))
    story.append(Paragraph("Subcontractor shall provide Certificate of Insurance to Owner before work begins.", body_style))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>License Verification:</b>", bold_style))
    story.append(Paragraph(f"{create_checkbox()} Subcontractor license verified with state licensing board", body_style))
    story.append(Paragraph(f"{create_checkbox()} License in good standing as of: {create_line(3)}", body_style))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Lien Waivers:</b>", bold_style))
    story.append(Paragraph("Subcontractor agrees to provide:", body_style))
    story.append(Paragraph("• Conditional lien waiver with each progress payment request", body_style))
    story.append(Paragraph("• Unconditional lien waiver upon receipt of each progress payment", body_style))
    story.append(Paragraph("• Final unconditional lien waiver upon receipt of final payment", body_style))
    story.append(Paragraph("• Lien waivers from all material suppliers and sub-subcontractors", body_style))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Warranty:</b>", bold_style))
    story.append(Paragraph("Subcontractor warrants that all work shall be:", body_style))
    story.append(Paragraph("• Performed in a workmanlike manner", body_style))
    story.append(Paragraph("• Free from defects in materials and workmanship", body_style))
    story.append(Paragraph("• In compliance with all applicable codes and regulations", body_style))
    story.append(Paragraph("• Performed by qualified personnel", body_style))
    story.append(Paragraph(f"Warranty Period: {create_line(4)} from date of substantial completion", body_style))
    story.append(Paragraph("Subcontractor shall promptly correct any defects in materials or workmanship that appear during the warranty period at no additional cost to Owner.", body_style))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Permits and Inspections:</b>", bold_style))
    story.append(Paragraph(f"{create_checkbox()} Owner responsible for obtaining permits", body_style))
    story.append(Paragraph(f"{create_checkbox()} Subcontractor responsible for obtaining permits", body_style))
    story.append(Paragraph("Subcontractor shall notify Owner at least 48 hours before inspections are required and shall coordinate with inspector to schedule inspections.", body_style))
    story.append(Paragraph("Subcontractor shall correct any work that fails inspection at no additional cost to Owner.", body_style))

    story.append(PageBreak())

    # Dispute Resolution
    story.append(Paragraph("<b>DISPUTE RESOLUTION</b>", heading_style))
    story.append(Paragraph("Any disputes arising under this agreement shall be resolved as follows:", body_style))

    story.append(Paragraph("<b>1. Direct Communication:</b> Parties shall first attempt to resolve disputes through direct communication within 7 days of dispute arising.", body_style))
    story.append(Paragraph("<b>2. Written Notice:</b> If dispute is not resolved, the aggrieved party shall provide written notice detailing the dispute within 14 days.", body_style))
    story.append(Paragraph("<b>3. Meeting:</b> Parties shall meet in person within 14 days of written notice to attempt resolution.", body_style))
    story.append(Paragraph("<b>4. Mediation:</b> If meeting does not resolve dispute, parties agree to participate in mediation with a mutually agreed upon mediator. Cost of mediation shall be split equally.", body_style))
    story.append(Paragraph(f"<b>5. Arbitration/Litigation:</b> If mediation fails, parties may pursue:", body_style))
    story.append(Paragraph(f"   {create_checkbox()} Binding arbitration (check if selected)", body_style))
    story.append(Paragraph(f"   {create_checkbox()} Litigation in courts of {create_line(3)} County, {create_line(1.5)} (State)", body_style))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Termination:</b>", bold_style))
    story.append(Paragraph("<b>By Owner:</b> Owner may terminate this agreement for cause (failure to perform, safety violations, code violations) with 7 days written notice. Owner may terminate without cause with 14 days written notice.", body_style))
    story.append(Paragraph("<b>By Subcontractor:</b> Subcontractor may terminate for non-payment after providing 14 days written notice and opportunity to cure.", body_style))
    story.append(Paragraph("Upon termination, Subcontractor shall be paid for all work completed to date, less any costs incurred by Owner to correct deficiencies.", body_style))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Indemnification:</b>", bold_style))
    story.append(Paragraph("Subcontractor agrees to indemnify and hold harmless Owner from any claims, damages, losses, or expenses (including attorney fees) arising from:", body_style))
    story.append(Paragraph("• Subcontractor's negligent acts or omissions", body_style))
    story.append(Paragraph("• Injury to persons or property caused by Subcontractor or its employees", body_style))
    story.append(Paragraph("• Failure to comply with applicable laws and regulations", body_style))
    story.append(Paragraph("• Claims by Subcontractor's employees, suppliers, or sub-subcontractors", body_style))

    story.append(PageBreak())

    # Additional Terms
    story.append(Paragraph("<b>ADDITIONAL TERMS AND CONDITIONS</b>", heading_style))

    story.append(Paragraph("<b>Site Access and Scheduling:</b>", bold_style))
    story.append(Paragraph(f"Subcontractor shall coordinate work schedule with Owner and other trades. Site access hours: {create_line(4)}", body_style))

    story.append(Paragraph("<b>Cleanup:</b>", bold_style))
    story.append(Paragraph("Subcontractor shall maintain a clean and safe work area and remove all debris and materials at the end of each workday. Final cleanup shall include removal of all tools, equipment, and materials.", body_style))

    story.append(Paragraph("<b>Safety:</b>", bold_style))
    story.append(Paragraph("Subcontractor shall comply with all OSHA regulations and maintain a safe work environment. Subcontractor is responsible for safety of its employees and shall provide all required personal protective equipment.", body_style))

    story.append(Paragraph("<b>Damage to Property:</b>", bold_style))
    story.append(Paragraph("Subcontractor shall be responsible for any damage to existing structures, fixtures, or property caused by Subcontractor or its employees.", body_style))

    story.append(Paragraph("<b>Assignment:</b>", bold_style))
    story.append(Paragraph("This agreement may not be assigned without written consent of both parties.", body_style))

    story.append(Paragraph("<b>Entire Agreement:</b>", bold_style))
    story.append(Paragraph("This agreement constitutes the entire agreement between parties and supersedes all prior negotiations, representations, or agreements. This agreement may only be modified by written amendment signed by both parties.", body_style))

    story.append(Paragraph("<b>Governing Law:</b>", bold_style))
    story.append(Paragraph(f"This agreement shall be governed by the laws of the State of {create_line(4)}.", body_style))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>SIGNATURES</b>", heading_style))
    story.append(Paragraph("By signing below, parties acknowledge they have read, understood, and agree to all terms and conditions of this agreement.", body_style))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>OWNER/GENERAL CONTRACTOR:</b>", bold_style))
    story.append(Paragraph(f"Signature: {create_line(5)} Date: {create_line(2)}", body_style))
    story.append(Paragraph(f"Print Name: {create_line(5)}", body_style))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>SUBCONTRACTOR:</b>", bold_style))
    story.append(Paragraph(f"Signature: {create_line(5)} Date: {create_line(2)}", body_style))
    story.append(Paragraph(f"Print Name: {create_line(5)}", body_style))
    story.append(Paragraph(f"Title: {create_line(5)}", body_style))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>WITNESS (Optional):</b>", bold_style))
    story.append(Paragraph(f"Signature: {create_line(5)} Date: {create_line(2)}", body_style))
    story.append(Paragraph(f"Print Name: {create_line(5)}", body_style))

    doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"Generated: {filename}")
    return filename

# Due to length constraints, I'll create a separate function for each remaining document
# Let me create the script incrementally

if __name__ == "__main__":
    os.chdir("/Users/evertith/Repositories/2025/nexarune/buildyourhouse/build-your-house/section-2-output")
    generate_2_1_subcontractor_agreement()
    print("Document 2.1 completed!")
