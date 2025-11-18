#!/usr/bin/env python3
"""
Generate all Section 2 PDFs for Owner-Builder Job Site Binder
Contracts & Legal Documents - Complete Package
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
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
    canvas_obj.setFont('Helvetica', 9)
    header_text = f"Owner-Builder Job Site Binder | Section 2: Contracts & Legal Documents | Page {doc.page}"
    canvas_obj.drawString(LEFT_MARGIN, letter[1] - 0.5*inch, header_text)
    canvas_obj.line(LEFT_MARGIN, letter[1] - 0.6*inch, letter[0] - RIGHT_MARGIN, letter[1] - 0.6*inch)
    # Footer
    canvas_obj.drawCentredString(letter[0]/2, 0.5*inch, str(doc.page))
    canvas_obj.drawRightString(letter[0] - RIGHT_MARGIN, 0.5*inch, "© 2024 Build Your House")
    canvas_obj.line(LEFT_MARGIN, 0.7*inch, letter[0] - RIGHT_MARGIN, 0.7*inch)
    canvas_obj.restoreState()

def L(inches):
    """Create an underline for filling in"""
    return "_" * int(inches * 10)

CB = "☐"  # Checkbox

# Create styles using Helvetica (standard PDF font)
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
    fontSize=12,
    textColor=colors.black,
    spaceAfter=6,
    spaceBefore=12
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=11,
    textColor=colors.black,
    spaceAfter=6,
    leading=14
)

bold_style = ParagraphStyle(
    'CustomBold',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    textColor=colors.black,
    spaceAfter=6
)

small_style = ParagraphStyle(
    'CustomSmall',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=10,
    textColor=colors.black,
    spaceAfter=6
)

def create_standard_table(data, col_widths=None):
    """Create a standard table with borders"""
    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 11),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))
    return table

print("Starting PDF generation for Section 2...")
print("=" * 60)

# Change to output directory
os.chdir("/Users/evertith/Repositories/2025/nexarune/buildyourhouse/build-your-house/section-2-output")

# Initialize counters
total_pages = 0
files_created = []

# 2.1 - Subcontractor Agreement Template (6 pages)
print("\n[1/8] Generating 2.1-subcontractor-agreement-template.pdf...")
filename = "2.1-subcontractor-agreement-template.pdf"
doc = SimpleDocTemplate(filename, pagesize=letter, leftMargin=LEFT_MARGIN, rightMargin=RIGHT_MARGIN, topMargin=TOP_MARGIN, bottomMargin=BOTTOM_MARGIN)
story = []

story.append(Paragraph("SUBCONTRACTOR AGREEMENT", title_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("PROJECT INFORMATION", heading_style))
story.append(Paragraph(f"<b>Project Address:</b> {L(8)}", body_style))
story.append(Paragraph(f"<b>Legal Description:</b> {L(7.5)}", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>Owner/General Contractor Information:</b>", bold_style))
story.append(Paragraph(f"Name: {L(10)}", body_style))
story.append(Paragraph(f"Address: {L(9.5)}", body_style))
story.append(Paragraph(f"City/State/ZIP: {L(8)}", body_style))
story.append(Paragraph(f"Phone: {L(4)} Email: {L(5)}", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>Subcontractor Information:</b>", bold_style))
story.append(Paragraph(f"Company Name: {L(8)}", body_style))
story.append(Paragraph(f"License #: {L(4)} State: {L(2)}", body_style))
story.append(Paragraph(f"Contact Person: {L(7)}", body_style))
story.append(Paragraph(f"Address: {L(9.5)}", body_style))
story.append(Paragraph(f"City/State/ZIP: {L(8)}", body_style))
story.append(Paragraph(f"Phone: {L(4)} Email: {L(5)}", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph(f"<b>Project Description:</b> {L(7)}", body_style))
story.append(Paragraph(L(12), body_style))
story.append(Paragraph(f"<b>Agreement Date:</b> {L(3)}", body_style))
story.append(Paragraph(f"<b>Work Start Date:</b> {L(3)}", body_style))
story.append(Paragraph(f"<b>Substantial Completion Date:</b> {L(3)}", body_style))
story.append(Paragraph(f"<b>Final Completion Date:</b> {L(3)}", body_style))
story.append(PageBreak())

story.append(Paragraph("SCOPE OF WORK", heading_style))
story.append(Paragraph("<b>Detailed Description of Work to be Performed:</b>", bold_style))
for i in range(8):
    story.append(Paragraph(L(12), body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>Specifications and Standards:</b>", bold_style))
story.append(Paragraph(f"{CB} Work shall comply with all applicable building codes and regulations", body_style))
story.append(Paragraph(f"{CB} Work shall comply with approved plans dated: {L(4)}", body_style))
story.append(Paragraph(f"{CB} Work shall meet industry standards for: {L(5)}", body_style))
story.append(Paragraph(f"{CB} Other specifications: {L(7)}", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>Materials:</b>", bold_style))
story.append(Paragraph("Materials to be provided by Subcontractor:", body_style))
for i in range(3):
    story.append(Paragraph(L(12), body_style))
story.append(Paragraph("Materials to be provided by Owner:", body_style))
for i in range(3):
    story.append(Paragraph(L(12), body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>Exclusions (Work NOT included in this agreement):</b>", bold_style))
for i in range(4):
    story.append(Paragraph(L(12), body_style))
story.append(PageBreak())

story.append(Paragraph("PAYMENT TERMS", heading_style))
story.append(Paragraph(f"<b>Total Contract Amount:</b> $ {L(4)}", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>Payment Schedule:</b>", bold_style))
payment_data = [
    ['Draw #', 'Milestone/Completion Point', 'Amount'],
    ['1', L(6), f"$ {L(2)}"],
    ['2', L(6), f"$ {L(2)}"],
    ['3', L(6), f"$ {L(2)}"],
    ['4', L(6), f"$ {L(2)}"],
    ['5', L(6), f"$ {L(2)}"],
]
story.append(create_standard_table(payment_data, [0.8*inch, 3.5*inch, 1.5*inch]))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph(f"<b>Retention:</b> {L(1.5)} % to be held until final completion and inspection", body_style))
story.append(Paragraph(f"<b>Retention Amount:</b> $ {L(4)}", body_style))
story.append(Paragraph(f"<b>Payment Terms:</b> Payment due within {L(1.5)} days of invoice submission", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>Final Payment Conditions:</b>", bold_style))
story.append(Paragraph("Final payment shall be made upon:", body_style))
story.append(Paragraph(f"{CB} Completion of all work per specifications", body_style))
story.append(Paragraph(f"{CB} Passing final inspection", body_style))
story.append(Paragraph(f"{CB} Receipt of unconditional lien waiver from Subcontractor", body_style))
story.append(Paragraph(f"{CB} Receipt of lien waivers from all material suppliers", body_style))
story.append(Paragraph(f"{CB} Submission of warranties and operating manuals (if applicable)", body_style))
story.append(Paragraph(f"{CB} Correction of any punch list items", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>Change Orders:</b>", bold_style))
story.append(Paragraph("All changes to the scope of work must be approved in writing via Change Order Form before work begins. No additional payment will be made for work performed without a signed change order.", body_style))
story.append(Paragraph("Change orders must include:", body_style))
story.append(Paragraph("• Detailed description of change", body_style))
story.append(Paragraph("• Cost impact (materials and labor)", body_style))
story.append(Paragraph("• Schedule impact", body_style))
story.append(Paragraph("• Signatures of both parties", body_style))
story.append(PageBreak())

story.append(Paragraph("LEGAL REQUIREMENTS AND RESPONSIBILITIES", heading_style))
story.append(Paragraph("<b>Insurance Requirements:</b>", bold_style))
story.append(Paragraph("Subcontractor shall maintain the following insurance coverage throughout the duration of this agreement:", body_style))
story.append(Paragraph(f"{CB} General Liability Insurance: Minimum $ {L(2.5)} per occurrence", body_style))
story.append(Paragraph(f"{CB} Workers' Compensation Insurance (if required by state law)", body_style))
story.append(Paragraph(f"{CB} Vehicle Insurance: Minimum $ {L(2.5)} per occurrence", body_style))
story.append(Paragraph("Subcontractor shall provide Certificate of Insurance to Owner before work begins.", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>License Verification:</b>", bold_style))
story.append(Paragraph(f"{CB} Subcontractor license verified with state licensing board", body_style))
story.append(Paragraph(f"{CB} License in good standing as of: {L(3)}", body_style))
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
story.append(Paragraph(f"Warranty Period: {L(4)} from date of substantial completion", body_style))
story.append(Paragraph("Subcontractor shall promptly correct any defects in materials or workmanship that appear during the warranty period at no additional cost to Owner.", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>Permits and Inspections:</b>", bold_style))
story.append(Paragraph(f"{CB} Owner responsible for obtaining permits", body_style))
story.append(Paragraph(f"{CB} Subcontractor responsible for obtaining permits", body_style))
story.append(Paragraph("Subcontractor shall notify Owner at least 48 hours before inspections are required and shall coordinate with inspector to schedule inspections.", body_style))
story.append(Paragraph("Subcontractor shall correct any work that fails inspection at no additional cost to Owner.", body_style))
story.append(PageBreak())

story.append(Paragraph("DISPUTE RESOLUTION", heading_style))
story.append(Paragraph("Any disputes arising under this agreement shall be resolved as follows:", body_style))
story.append(Paragraph("<b>1. Direct Communication:</b> Parties shall first attempt to resolve disputes through direct communication within 7 days of dispute arising.", body_style))
story.append(Paragraph("<b>2. Written Notice:</b> If dispute is not resolved, the aggrieved party shall provide written notice detailing the dispute within 14 days.", body_style))
story.append(Paragraph("<b>3. Meeting:</b> Parties shall meet in person within 14 days of written notice to attempt resolution.", body_style))
story.append(Paragraph("<b>4. Mediation:</b> If meeting does not resolve dispute, parties agree to participate in mediation with a mutually agreed upon mediator. Cost of mediation shall be split equally.", body_style))
story.append(Paragraph(f"<b>5. Arbitration/Litigation:</b> If mediation fails, parties may pursue:", body_style))
story.append(Paragraph(f"   {CB} Binding arbitration (check if selected)", body_style))
story.append(Paragraph(f"   {CB} Litigation in courts of {L(3)} County, {L(1.5)} (State)", body_style))
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

story.append(Paragraph("ADDITIONAL TERMS AND CONDITIONS", heading_style))
story.append(Paragraph("<b>Site Access and Scheduling:</b>", bold_style))
story.append(Paragraph(f"Subcontractor shall coordinate work schedule with Owner and other trades. Site access hours: {L(4)}", body_style))
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
story.append(Paragraph(f"This agreement shall be governed by the laws of the State of {L(4)}.", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("SIGNATURES", heading_style))
story.append(Paragraph("By signing below, parties acknowledge they have read, understood, and agree to all terms and conditions of this agreement.", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("<b>OWNER/GENERAL CONTRACTOR:</b>", bold_style))
story.append(Paragraph(f"Signature: {L(5)} Date: {L(2)}", body_style))
story.append(Paragraph(f"Print Name: {L(5)}", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("<b>SUBCONTRACTOR:</b>", bold_style))
story.append(Paragraph(f"Signature: {L(5)} Date: {L(2)}", body_style))
story.append(Paragraph(f"Print Name: {L(5)}", body_style))
story.append(Paragraph(f"Title: {L(5)}", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("<b>WITNESS (Optional):</b>", bold_style))
story.append(Paragraph(f"Signature: {L(5)} Date: {L(2)}", body_style))
story.append(Paragraph(f"Print Name: {L(5)}", body_style))

doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
files_created.append(filename)
print(f"✓ Created {filename} (6 pages)")
total_pages += 6

# 2.2 - Change Order Form (3 pages)
print("\n[2/8] Generating 2.2-change-order-form.pdf...")
filename = "2.2-change-order-form.pdf"
doc = SimpleDocTemplate(filename, pagesize=letter, leftMargin=LEFT_MARGIN, rightMargin=RIGHT_MARGIN, topMargin=TOP_MARGIN, bottomMargin=BOTTOM_MARGIN)
story = []

story.append(Paragraph("CHANGE ORDER FORM", title_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph(f"<b>Change Order Number:</b> {L(2.5)}", body_style))
story.append(Paragraph(f"<b>Date:</b> {L(3.5)}", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("PROJECT INFORMATION", heading_style))
story.append(Paragraph(f"<b>Project Address:</b> {L(8)}", body_style))
story.append(Paragraph(f"<b>Owner Name:</b> {L(8)}", body_style))
story.append(Paragraph(f"<b>Subcontractor/Trade:</b> {L(7.5)}", body_style))
story.append(Paragraph(f"<b>Original Contract Date:</b> {L(4)}", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("FINANCIAL SUMMARY", heading_style))
story.append(Paragraph(f"<b>Original Contract Amount:</b> $ {L(4)}", body_style))
story.append(Paragraph(f"<b>Previous Change Orders (Total):</b> $ {L(4)}", body_style))
story.append(Paragraph(f"<b>Revised Contract Amount (before this CO):</b> $ {L(4)}", body_style))
story.append(Paragraph(f"<b>This Change Order Amount:</b> $ {L(4)}", body_style))
story.append(Paragraph(f"    {CB} Addition (+)     {CB} Deduction (-)", body_style))
story.append(Paragraph(f"<b>New Contract Amount (including this CO):</b> $ {L(4)}", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("DESCRIPTION OF CHANGE", heading_style))
story.append(Paragraph("<b>Detailed description of work to be added, deleted, or modified:</b>", bold_style))
for i in range(10):
    story.append(Paragraph(L(12), body_style))
story.append(PageBreak())

story.append(Paragraph("REASON FOR CHANGE", heading_style))
story.append(Paragraph("Check all that apply:", body_style))
story.append(Paragraph(f"{CB} Owner-requested modification", body_style))
story.append(Paragraph(f"{CB} Design change", body_style))
story.append(Paragraph(f"{CB} Unforeseen site conditions", body_style))
story.append(Paragraph(f"{CB} Code requirement/inspector request", body_style))
story.append(Paragraph(f"{CB} Material substitution/unavailability", body_style))
story.append(Paragraph(f"{CB} Correction of error or omission", body_style))
story.append(Paragraph(f"{CB} Upgrade/enhancement", body_style))
story.append(Paragraph(f"{CB} Value engineering", body_style))
story.append(Paragraph(f"{CB} Other: {L(7)}", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>Detailed explanation:</b>", bold_style))
for i in range(5):
    story.append(Paragraph(L(12), body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("COST BREAKDOWN", heading_style))
cost_data = [
    ['Description', 'Quantity', 'Cost'],
    ['Labor:', '', ''],
    [L(6), L(2.5), f"$ {L(2)}"],
    [L(6), L(2.5), f"$ {L(2)}"],
    [L(6), L(2.5), f"$ {L(2)}"],
    ['Labor Subtotal:', '', f"$ {L(2)}"],
    ['Materials:', '', ''],
    [L(6), L(2.5), f"$ {L(2)}"],
    [L(6), L(2.5), f"$ {L(2)}"],
    [L(6), L(2.5), f"$ {L(2)}"],
    [L(6), L(2.5), f"$ {L(2)}"],
    ['Materials Subtotal:', '', f"$ {L(2)}"],
    ['Equipment/Other:', '', ''],
    [L(6), L(2.5), f"$ {L(2)}"],
    [L(6), L(2.5), f"$ {L(2)}"],
    ['Equipment Subtotal:', '', f"$ {L(2)}"],
    ['TOTAL COST IMPACT:', '', f"$ {L(2)}"],
]
story.append(create_standard_table(cost_data, [3*inch, 1.5*inch, 1.5*inch]))
story.append(PageBreak())

story.append(Paragraph("SCHEDULE IMPACT", heading_style))
story.append(Paragraph(f"<b>Original Completion Date:</b> {L(4)}", body_style))
story.append(Paragraph(f"<b>Schedule Impact:</b> {L(1.5)} days (+ or -)", body_style))
story.append(Paragraph(f"<b>New Completion Date:</b> {L(4)}", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("<b>Explanation of schedule impact:</b>", bold_style))
for i in range(3):
    story.append(Paragraph(L(12), body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("IMPACT ON OTHER TRADES", heading_style))
story.append(Paragraph(f"{CB} No impact on other trades", body_style))
story.append(Paragraph(f"{CB} Impacts other trades (explain below):", body_style))
for i in range(3):
    story.append(Paragraph(L(12), body_style))
story.append(Paragraph(f"Trades affected: {L(8)}", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("SUPPORTING DOCUMENTATION", heading_style))
story.append(Paragraph("Attached documents (check all that apply):", body_style))
story.append(Paragraph(f"{CB} Revised drawings/sketches", body_style))
story.append(Paragraph(f"{CB} Material quotes/invoices", body_style))
story.append(Paragraph(f"{CB} Photos of conditions requiring change", body_style))
story.append(Paragraph(f"{CB} Inspector notes/requirements", body_style))
story.append(Paragraph(f"{CB} Engineer specifications", body_style))
story.append(Paragraph(f"{CB} Other: {L(7)}", body_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("PAYMENT TERMS FOR THIS CHANGE ORDER", heading_style))
story.append(Paragraph(f"{CB} Payment due with next regular draw", body_style))
story.append(Paragraph(f"{CB} Payment upon completion of change order work", body_style))
story.append(Paragraph(f"{CB} Payment in installments: {L(6)}", body_style))
story.append(Paragraph(f"{CB} Other: {L(8)}", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("APPROVALS AND SIGNATURES", heading_style))
story.append(Paragraph("By signing below, both parties agree to the changes described in this Change Order and acknowledge that this Change Order modifies the original contract accordingly.", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("<b>OWNER APPROVAL:</b>", bold_style))
story.append(Paragraph(f"Signature: {L(5)} Date: {L(2)}", body_style))
story.append(Paragraph(f"Print Name: {L(5)}", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("<b>SUBCONTRACTOR APPROVAL:</b>", bold_style))
story.append(Paragraph(f"Signature: {L(5)} Date: {L(2)}", body_style))
story.append(Paragraph(f"Print Name: {L(5)}", body_style))
story.append(Paragraph(f"Company: {L(5)}", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("<b>NOTES:</b>", bold_style))
for i in range(3):
    story.append(Paragraph(L(12), body_style))

doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
files_created.append(filename)
print(f"✓ Created {filename} (3 pages)")
total_pages += 3

print("\n" + "=" * 60)
print(f"BATCH 1 COMPLETE: 2 of 8 documents generated")
print(f"Total pages so far: {total_pages}")
print(f"Files created: {len(files_created)}")
print("=" * 60)
print("\nContinuing with remaining documents...")
