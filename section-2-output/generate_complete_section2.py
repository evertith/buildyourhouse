#!/usr/bin/env python3
"""Complete Section 2 PDF Generator - All 8 Documents"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
import os

# Constants
LEFT_MARGIN = 1.5 * inch
RIGHT_MARGIN = 1.0 * inch
TOP_MARGIN = 1.0 * inch
BOTTOM_MARGIN = 1.0 * inch
CB = "☐"

def add_header_footer(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setFont('Helvetica', 9)
    header_text = f"Owner-Builder Job Site Binder | Section 2: Contracts & Legal Documents | Page {doc.page}"
    canvas_obj.drawString(LEFT_MARGIN, letter[1] - 0.5*inch, header_text)
    canvas_obj.line(LEFT_MARGIN, letter[1] - 0.6*inch, letter[0] - RIGHT_MARGIN, letter[1] - 0.6*inch)
    canvas_obj.drawCentredString(letter[0]/2, 0.5*inch, str(doc.page))
    canvas_obj.drawRightString(letter[0] - RIGHT_MARGIN, 0.5*inch, "© 2024 Build Your House")
    canvas_obj.line(LEFT_MARGIN, 0.7*inch, letter[0] - RIGHT_MARGIN, 0.7*inch)
    canvas_obj.restoreState()

def L(inches):
    return "_" * int(inches * 10)

styles = getSampleStyleSheet()
title_style = ParagraphStyle('T', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=16, spaceAfter=12, alignment=TA_CENTER)
heading_style = ParagraphStyle('H', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=6, spaceBefore=12)
body_style = ParagraphStyle('B', parent=styles['Normal'], fontName='Helvetica', fontSize=11, spaceAfter=6, leading=14)
bold_style = ParagraphStyle('Bo', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11, spaceAfter=6)

def create_table(data, widths=None):
    t = Table(data, colWidths=widths)
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t

os.chdir("/Users/evertith/Repositories/2025/nexarune/buildyourhouse/build-your-house/section-2-output")
total = 0
files = []

# Documents 2.1 and 2.2 already created above, now create 2.3-2.8

# 2.3 - Lien Waiver Templates (4 pages)
print("\n[3/8] Generating 2.3-lien-waiver-templates.pdf...")
fn = "2.3-lien-waiver-templates.pdf"
doc = SimpleDocTemplate(fn, pagesize=letter, leftMargin=LEFT_MARGIN, rightMargin=RIGHT_MARGIN, topMargin=TOP_MARGIN, bottomMargin=BOTTOM_MARGIN)
s = []

s.append(Paragraph("CONDITIONAL LIEN WAIVER<br/>(Partial Payment)", title_style))
s.append(Spacer(1, 0.2*inch))
s.append(Paragraph(f"<b>Project Name:</b> {L(7.5)}", body_style))
s.append(Paragraph(f"<b>Project Address:</b> {L(7.5)}", body_style))
s.append(Paragraph(f"<b>Owner Name:</b> {L(7.5)}", body_style))
s.append(Paragraph(f"<b>Date:</b> {L(3.5)}", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph(f"Upon receipt of payment in the amount of $ {L(3.5)}, the undersigned hereby waives and releases any and all lien rights, stop payment notice rights, and bond rights the undersigned has or may have against the above-referenced property for labor, services, equipment, or materials furnished to the property through {L(3.5)} (through-date).", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>This waiver is CONDITIONAL upon payment.</b> This waiver and release is void and of no effect unless and until the undersigned actually receives payment in the amount stated above.", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>Payment Information:</b>", bold_style))
s.append(Paragraph(f"Payment Amount: $ {L(4)}", body_style))
s.append(Paragraph(f"Check Number: {L(3.5)}", body_style))
s.append(Paragraph(f"Date of Check: {L(3.5)}", body_style))
s.append(Paragraph(f"Payment Period: From {L(2.5)} To {L(2.5)}", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>Exceptions:</b>", bold_style))
s.append(Paragraph("This waiver does not cover:", body_style))
s.append(Paragraph("• Any work, materials, or services provided after the through-date listed above", body_style))
s.append(Paragraph("• Any retention amounts held", body_style))
s.append(Paragraph(f"• Disputed claims for extra work in the amount of $ {L(2.5)}", body_style))
s.append(Paragraph(f"• Other exceptions: {L(6)}", body_style))
s.append(Spacer(1, 0.2*inch))
s.append(Paragraph("<b>Company/Individual Information:</b>", bold_style))
s.append(Paragraph(f"Name of Claimant: {L(7)}", body_style))
s.append(Paragraph(f"Company Name: {L(7)}", body_style))
s.append(Paragraph(f"License Number: {L(4.5)}", body_style))
s.append(Paragraph(f"Address: {L(8.5)}", body_style))
s.append(Paragraph(f"Phone: {L(3.5)}", body_style))
s.append(Spacer(1, 0.2*inch))
s.append(Paragraph(f"<b>Signature:</b> {L(5)} <b>Date:</b> {L(2.5)}", body_style))
s.append(Paragraph(f"<b>Print Name:</b> {L(5)}", body_style))
s.append(Paragraph(f"<b>Title:</b> {L(5)}", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<i><b>WARNING:</b> This document waives rights unconditionally and states that you have been paid for giving up those rights. This document is enforceable against you if you sign it, even if you have not been paid. If you have not been paid, use a conditional waiver and release form.</i>", body_style))
s.append(PageBreak())

s.append(Paragraph("UNCONDITIONAL LIEN WAIVER<br/>(Partial Payment)", title_style))
s.append(Spacer(1, 0.2*inch))
s.append(Paragraph(f"<b>Project Name:</b> {L(7.5)}", body_style))
s.append(Paragraph(f"<b>Project Address:</b> {L(7.5)}", body_style))
s.append(Paragraph(f"<b>Owner Name:</b> {L(7.5)}", body_style))
s.append(Paragraph(f"<b>Date:</b> {L(3.5)}", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph(f"The undersigned has been paid and has received progress payment in the amount of $ {L(3.5)}, and hereby waives and releases any and all lien rights, stop payment notice rights, and bond rights the undersigned has or may have against the above-referenced property for labor, services, equipment, or materials furnished to the property through {L(3.5)} (through-date).", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>This waiver is UNCONDITIONAL.</b> This waiver and release is effective immediately upon signing and is not dependent upon receipt of payment.", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>Payment Information:</b>", bold_style))
s.append(Paragraph(f"Payment Amount Received: $ {L(4)}", body_style))
s.append(Paragraph(f"Check Number: {L(3.5)}", body_style))
s.append(Paragraph(f"Date Payment Received: {L(3.5)}", body_style))
s.append(Paragraph(f"Payment Period: From {L(2.5)} To {L(2.5)}", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>Amount Summary:</b>", bold_style))
s.append(Paragraph(f"Total contract amount to date: $ {L(4)}", body_style))
s.append(Paragraph(f"Previous payments received: $ {L(4)}", body_style))
s.append(Paragraph(f"This payment amount: $ {L(4)}", body_style))
s.append(Paragraph(f"Balance remaining: $ {L(4)}", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>Exceptions:</b>", bold_style))
s.append(Paragraph("This waiver does not cover:", body_style))
s.append(Paragraph("• Any work, materials, or services provided after the through-date listed above", body_style))
s.append(Paragraph(f"• Any retention amounts held in the amount of $ {L(2.5)}", body_style))
s.append(Paragraph(f"• Disputed claims for extra work in the amount of $ {L(2.5)}", body_style))
s.append(Paragraph(f"• Other exceptions: {L(6)}", body_style))
s.append(Spacer(1, 0.2*inch))
s.append(Paragraph("<b>Company/Individual Information:</b>", bold_style))
s.append(Paragraph(f"Name of Claimant: {L(7)}", body_style))
s.append(Paragraph(f"Company Name: {L(7)}", body_style))
s.append(Paragraph(f"License Number: {L(4.5)}", body_style))
s.append(Paragraph(f"Address: {L(8.5)}", body_style))
s.append(Paragraph(f"Phone: {L(3.5)}", body_style))
s.append(Spacer(1, 0.2*inch))
s.append(Paragraph(f"<b>Signature:</b> {L(5)} <b>Date:</b> {L(2.5)}", body_style))
s.append(Paragraph(f"<b>Print Name:</b> {L(5)}", body_style))
s.append(Paragraph(f"<b>Title:</b> {L(5)}", body_style))
s.append(PageBreak())

s.append(Paragraph("CONDITIONAL LIEN WAIVER<br/>(Final Payment)", title_style))
s.append(Spacer(1, 0.2*inch))
s.append(Paragraph(f"<b>Project Name:</b> {L(7.5)}", body_style))
s.append(Paragraph(f"<b>Project Address:</b> {L(7.5)}", body_style))
s.append(Paragraph(f"<b>Owner Name:</b> {L(7.5)}", body_style))
s.append(Paragraph(f"<b>Date:</b> {L(3.5)}", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph(f"Upon receipt of FINAL payment in the amount of $ {L(3.5)}, the undersigned hereby waives and releases any and all lien rights, stop payment notice rights, and bond rights the undersigned has or may have against the above-referenced property for all labor, services, equipment, or materials furnished to the property.", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>This waiver is CONDITIONAL upon receipt of final payment.</b> This waiver and release is void and of no effect unless and until the undersigned actually receives final payment in the amount stated above.", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>Final Payment Information:</b>", bold_style))
s.append(Paragraph(f"Total Contract Amount: $ {L(4)}", body_style))
s.append(Paragraph(f"Previous Payments Received: $ {L(4)}", body_style))
s.append(Paragraph(f"Final Payment Amount: $ {L(4)}", body_style))
s.append(Paragraph(f"Check Number: {L(3.5)}", body_style))
s.append(Paragraph(f"Date of Check: {L(3.5)}", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph(f"<b>Retention Release:</b> Retention amount being released: $ {L(4)}", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>Certification:</b>", bold_style))
s.append(Paragraph("The undersigned certifies that:", body_style))
s.append(Paragraph(f"{CB} All work has been completed per contract specifications", body_style))
s.append(Paragraph(f"{CB} All materials have been paid for", body_style))
s.append(Paragraph(f"{CB} All subcontractors and suppliers have been paid in full", body_style))
s.append(Paragraph(f"{CB} All required warranties have been provided to owner", body_style))
s.append(Paragraph(f"{CB} All punch list items have been completed", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>Exceptions:</b>", bold_style))
s.append(Paragraph("This waiver does not cover (if none, write \"NONE\"):", body_style))
s.append(Paragraph(L(12), body_style))
s.append(Paragraph(L(12), body_style))
s.append(Spacer(1, 0.2*inch))
s.append(Paragraph("<b>Company/Individual Information:</b>", bold_style))
s.append(Paragraph(f"Name of Claimant: {L(7)}", body_style))
s.append(Paragraph(f"Company Name: {L(7)}", body_style))
s.append(Paragraph(f"License Number: {L(4.5)}", body_style))
s.append(Paragraph(f"Address: {L(8.5)}", body_style))
s.append(Paragraph(f"Phone: {L(3.5)}", body_style))
s.append(Spacer(1, 0.2*inch))
s.append(Paragraph(f"<b>Signature:</b> {L(5)} <b>Date:</b> {L(2.5)}", body_style))
s.append(Paragraph(f"<b>Print Name:</b> {L(5)}", body_style))
s.append(Paragraph(f"<b>Title:</b> {L(5)}", body_style))
s.append(PageBreak())

s.append(Paragraph("UNCONDITIONAL LIEN WAIVER<br/>(Final Payment)", title_style))
s.append(Spacer(1, 0.2*inch))
s.append(Paragraph(f"<b>Project Name:</b> {L(7.5)}", body_style))
s.append(Paragraph(f"<b>Project Address:</b> {L(7.5)}", body_style))
s.append(Paragraph(f"<b>Owner Name:</b> {L(7.5)}", body_style))
s.append(Paragraph(f"<b>Date:</b> {L(3.5)}", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph(f"The undersigned has been paid in full and has received FINAL payment in the amount of $ {L(3.5)}, and hereby waives and releases any and all lien rights, stop payment notice rights, and bond rights the undersigned has or may have against the above-referenced property for all labor, services, equipment, or materials furnished to the property.", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>This waiver is UNCONDITIONAL and FINAL.</b> This waiver and release is effective immediately upon signing and releases all rights to file liens or claims against the property.", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>Final Payment Information:</b>", bold_style))
s.append(Paragraph(f"Total Contract Amount: $ {L(4)}", body_style))
s.append(Paragraph(f"Total Change Orders: $ {L(4)}", body_style))
s.append(Paragraph(f"Final Contract Amount: $ {L(4)}", body_style))
s.append(Paragraph(f"Previous Payments Received: $ {L(4)}", body_style))
s.append(Paragraph(f"Retention Released: $ {L(4)}", body_style))
s.append(Paragraph(f"Final Payment Amount: $ {L(4)}", body_style))
s.append(Paragraph(f"Check Number: {L(3.5)}", body_style))
s.append(Paragraph(f"Date Payment Received: {L(3.5)}", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>Final Certification:</b>", bold_style))
s.append(Paragraph("The undersigned certifies that:", body_style))
s.append(Paragraph(f"{CB} All work has been completed per contract specifications", body_style))
s.append(Paragraph(f"{CB} All materials have been paid for in full", body_style))
s.append(Paragraph(f"{CB} All subcontractors and suppliers have been paid in full", body_style))
s.append(Paragraph(f"{CB} All required warranties have been provided to owner", body_style))
s.append(Paragraph(f"{CB} All punch list items have been completed", body_style))
s.append(Paragraph(f"{CB} Final inspection has been passed", body_style))
s.append(Paragraph(f"{CB} No outstanding claims or disputes exist", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<b>Exceptions:</b>", bold_style))
s.append(Paragraph("This is a FINAL waiver with NO exceptions. If any claims remain, do NOT sign this form.", body_style))
s.append(Spacer(1, 0.2*inch))
s.append(Paragraph("<b>Company/Individual Information:</b>", bold_style))
s.append(Paragraph(f"Name of Claimant: {L(7)}", body_style))
s.append(Paragraph(f"Company Name: {L(7)}", body_style))
s.append(Paragraph(f"License Number: {L(4.5)}", body_style))
s.append(Paragraph(f"Address: {L(8.5)}", body_style))
s.append(Paragraph(f"Phone: {L(3.5)}", body_style))
s.append(Spacer(1, 0.2*inch))
s.append(Paragraph(f"<b>Signature:</b> {L(5)} <b>Date:</b> {L(2.5)}", body_style))
s.append(Paragraph(f"<b>Print Name:</b> {L(5)}", body_style))
s.append(Paragraph(f"<b>Title:</b> {L(5)}", body_style))
s.append(Spacer(1, 0.1*inch))
s.append(Paragraph("<i><b>WARNING:</b> This document waives ALL rights unconditionally and states that you have been paid IN FULL for giving up those rights. This document is enforceable against you if you sign it, even if you have not been paid in full. If you have not been paid in full, use a conditional waiver and release form.</i>", body_style))

doc.build(s, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
files.append(fn)
print(f"✓ Created {fn} (4 pages)")
total += 4

print(f"\nProgress: 3/8 documents complete, {total} pages total")
