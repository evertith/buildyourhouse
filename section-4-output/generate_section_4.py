#!/usr/bin/env python3
"""
Generate Section 4: Systems Installation PDFs
Owner-Builder Job Site Binder
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfgen import canvas
import os

# Page settings
LEFT_MARGIN = 1.5 * inch
RIGHT_MARGIN = 1.0 * inch
TOP_MARGIN = 1.0 * inch
BOTTOM_MARGIN = 1.0 * inch
PAGE_WIDTH = letter[0]
PAGE_HEIGHT = letter[1]

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        self.section_name = kwargs.pop('section_name', 'Section 4: Systems Installation')
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_decorations(self, count):
        self.setFont('Helvetica', 9)

        # Header
        header_text = f"Owner-Builder Job Site Binder | {self.section_name} | Page {self._pageNumber}"
        self.drawString(LEFT_MARGIN, PAGE_HEIGHT - 0.5 * inch, header_text)
        self.line(LEFT_MARGIN, PAGE_HEIGHT - 0.6 * inch,
                 PAGE_WIDTH - RIGHT_MARGIN, PAGE_HEIGHT - 0.6 * inch)

        # Footer
        self.drawCentredString(PAGE_WIDTH / 2, 0.5 * inch, str(self._pageNumber))
        self.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, 0.5 * inch, "© 2024 Build Your House")

def create_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name='CustomTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        textColor=colors.black,
        spaceAfter=12,
        alignment=TA_LEFT
    ))

    styles.add(ParagraphStyle(
        name='CustomHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        textColor=colors.black,
        spaceAfter=10,
        spaceBefore=10,
        alignment=TA_LEFT
    ))

    styles.add(ParagraphStyle(
        name='CustomSubHeading',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=12,
        textColor=colors.black,
        spaceAfter=8,
        spaceBefore=8,
        alignment=TA_LEFT
    ))

    styles.add(ParagraphStyle(
        name='CustomBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='CheckboxItem',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        textColor=colors.black,
        leftIndent=20,
        spaceAfter=8
    ))

    return styles

def create_checkbox_table(items, col_widths=None):
    """Create a table with checkboxes"""
    if col_widths is None:
        col_widths = [0.3*inch, 5.5*inch]

    data = []
    for item in items:
        data.append(['☐', item])

    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))

    return table

def create_field_table(fields, col_widths=None):
    """Create a table with labeled fields"""
    if col_widths is None:
        col_widths = [2.0*inch, 4.0*inch]

    data = []
    for label, field_type in fields:
        if field_type == 'line':
            data.append([f"{label}:", "_" * 50])
        elif field_type == 'multiline':
            data.append([f"{label}:", "\n\n"])
        else:
            data.append([f"{label}:", field_type])

    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))

    return table

def create_data_table(data, col_widths, header_row=True):
    """Create a data table with borders"""
    table = Table(data, colWidths=col_widths, repeatRows=1 if header_row else 0)

    style_commands = [
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]

    if header_row:
        style_commands.extend([
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ])

    table.setStyle(TableStyle(style_commands))
    return table

# ============================================================================
# 4.1 ELECTRICAL SYSTEM COMPLETION LOG
# ============================================================================

def create_electrical_system_log():
    filename = "4.1-electrical-system-completion-log.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN
    )

    story = []
    styles = create_styles()

    # Title Page
    story.append(Paragraph("ELECTRICAL SYSTEM", styles['CustomTitle']))
    story.append(Paragraph("COMPLETION LOG", styles['CustomTitle']))
    story.append(Spacer(1, 0.3*inch))

    project_info = [
        ('Project Address', 'line'),
        ('Project Name', 'line'),
        ('Permit Number', 'line'),
        ('Electrician/Company', 'line'),
        ('License Number', 'line'),
        ('Contact Phone', 'line'),
    ]
    story.append(create_field_table(project_info))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>PURPOSE:</b> This log documents the completion and testing of all electrical systems from rough-in through final inspection. Use this to verify every outlet, switch, fixture, and circuit is properly installed and functioning before final inspection.", styles['CustomBody']))
    story.append(PageBreak())

    # ROUGH-IN TO FINISH VERIFICATION
    story.append(Paragraph("ROUGH-IN TO FINISH VERIFICATION", styles['CustomHeading']))
    story.append(Paragraph("Review rough-in work and verify proper completion:", styles['CustomBody']))
    story.append(Spacer(1, 0.1*inch))

    roughin_checks = [
        "All electrical boxes properly located per plan",
        "All boxes properly secured to framing",
        "Box depth appropriate for wall finish thickness",
        "All boxes filled out flush with finished wall surface",
        "Vapor barrier properly sealed around boxes (if applicable)",
        "All required backing/blocking installed for fixtures",
        "All cables properly secured within 8\" of boxes",
        "Cable stapling meets code (every 4.5 feet, 12\" from boxes)",
        "Proper cable protection through studs (1-1/4\" from edge or nail plates)",
        "No damaged cable jackets or conductors",
        "All wire splices made in accessible boxes only",
        "All boxes have required cubic inch capacity for number of conductors",
    ]
    story.append(create_checkbox_table(roughin_checks))
    story.append(PageBreak())

    # DEVICE INSTALLATION VERIFICATION
    story.append(Paragraph("DEVICE INSTALLATION VERIFICATION", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    device_checks = [
        "All receptacles installed with correct orientation (ground down or up per preference)",
        "All receptacles same color throughout (white or ivory - consistent choice)",
        "All receptacles properly secured to boxes (no gaps)",
        "All receptacles 15A or 20A as required by circuit",
        "Tamper-resistant receptacles installed per code (if required)",
        "GFCI receptacles installed in all required locations (bathrooms, kitchen, garage, exterior)",
        "AFCI breakers or receptacles installed per code requirements",
        "All switch devices properly installed and secured",
        "Switch heights consistent throughout (typically 48\" to center)",
        "Dimmer switches compatible with light fixtures/bulbs",
        "3-way and 4-way switches wired correctly",
        "All device cover plates installed (correct size and color)",
        "Weatherproof covers installed on all exterior receptacles",
        "Weatherproof covers installed on all exterior switches",
        "In-use covers provided for exterior GFCI receptacles",
    ]
    story.append(create_checkbox_table(device_checks))
    story.append(PageBreak())

    # OUTLET TESTING LOG
    story.append(Paragraph("OUTLET TESTING LOG", styles['CustomHeading']))
    story.append(Paragraph("Test and document each outlet/receptacle:", styles['CustomBody']))
    story.append(Spacer(1, 0.1*inch))

    outlet_data = [['Room/Location', 'Outlet ID', 'Polarity OK', 'GFCI Test', 'Notes']]
    for i in range(30):
        outlet_data.append(['', '', '☐', '☐', ''])

    story.append(create_data_table(outlet_data, [1.5*inch, 1.0*inch, 0.9*inch, 0.9*inch, 1.7*inch]))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Testing Notes:</b> Use outlet tester for polarity. Press TEST button on all GFCI outlets - should trip. Press RESET to restore power.", styles['CustomBody']))
    story.append(PageBreak())

    # LIGHTING FIXTURES INSTALLATION
    story.append(Paragraph("LIGHTING FIXTURES INSTALLATION", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    fixture_data = [['Room/Location', 'Fixture Type', 'Installed', 'Bulb Type', 'Dimmer Compatible', 'Tested OK', 'Notes']]
    for i in range(25):
        fixture_data.append(['', '', '☐', '', '☐ Y  ☐ N', '☐', ''])

    story.append(create_data_table(fixture_data, [1.2*inch, 1.0*inch, 0.5*inch, 0.9*inch, 0.9*inch, 0.5*inch, 1.0*inch]))
    story.append(PageBreak())

    # CEILING FAN INSTALLATION & TESTING
    story.append(Paragraph("CEILING FAN INSTALLATION & TESTING", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    fan_data = [['Room/Location', 'Fan Model', 'Box Rated for Fan', 'Light Kit', 'Remote/Wall Control', 'All Speeds Work', 'No Wobble', 'Notes']]
    for i in range(8):
        fan_data.append(['', '', '☐', '☐', '', '☐', '☐', ''])

    story.append(create_data_table(fan_data, [1.2*inch, 1.0*inch, 0.8*inch, 0.5*inch, 0.9*inch, 0.7*inch, 0.6*inch, 0.8*inch]))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Fan Installation Checks:</b>", styles['CustomSubHeading']))
    fan_checks = [
        "Ceiling box rated for fan weight (must be fan-rated box)",
        "Fan properly secured to fan-rated box or brace",
        "Downrod length appropriate for ceiling height",
        "All fan blades balanced and secure",
        "Light kit properly installed (if applicable)",
        "Wall control or remote functioning properly",
        "All fan speeds operate smoothly",
        "No wobble or unusual noise at any speed",
        "Reverse function works (summer/winter direction)",
    ]
    story.append(create_checkbox_table(fan_checks))
    story.append(PageBreak())

    # SWITCH OPERATION TESTING
    story.append(Paragraph("SWITCH OPERATION TESTING", styles['CustomHeading']))
    story.append(Paragraph("Test every switch and verify correct fixture control:", styles['CustomBody']))
    story.append(Spacer(1, 0.1*inch))

    switch_data = [['Room/Location', 'Switch Location', 'Controls Which Fixture', 'Type', 'Works OK', 'Notes']]
    for i in range(35):
        switch_data.append(['', '', '', '', '☐', ''])

    story.append(create_data_table(switch_data, [1.3*inch, 1.3*inch, 1.5*inch, 0.9*inch, 0.6*inch, 1.0*inch]))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Type Codes:</b> S=Single-pole, 3=3-way, 4=4-way, D=Dimmer, P=Pilot light, T=Timer", styles['CustomBody']))
    story.append(PageBreak())

    # ELECTRICAL PANEL COMPLETION
    story.append(Paragraph("ELECTRICAL PANEL COMPLETION", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    panel_info = [
        ('Panel Make/Model', 'line'),
        ('Main Breaker Size', 'line'),
        ('Panel Location', 'line'),
        ('Number of Circuits', 'line'),
    ]
    story.append(create_field_table(panel_info))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Panel Completion Checklist:</b>", styles['CustomSubHeading']))
    panel_checks = [
        "All circuit breakers properly installed and seated",
        "All breaker connections tight (proper torque per manufacturer)",
        "Main breaker correct size for service (typically 100A, 150A, or 200A)",
        "All circuits properly labeled on breaker",
        "Panel directory card completely filled out and legible",
        "All GFCI breakers installed and functioning (test button works)",
        "All AFCI breakers installed per code requirements",
        "Combination AFCI/GFCI breakers where required",
        "No double-tapped breakers (unless breaker is rated for 2 wires)",
        "All unused breaker spaces filled with blank plates",
        "All knockouts sealed (no open holes in panel)",
        "Panel cover/dead front properly installed",
        "Panel cover screws all installed and tight",
        "Proper working clearance maintained (30\" wide x 36\" deep x 6'6\" high)",
        "Panel properly grounded (ground wire to ground bar)",
        "Neutral and ground bars properly separated (if required)",
        "Service entrance cable properly secured",
        "Panel labeled \"MAIN ELECTRICAL PANEL\" or \"MAIN DISCONNECT\"",
    ]
    story.append(create_checkbox_table(panel_checks))
    story.append(PageBreak())

    # CIRCUIT DIRECTORY
    story.append(Paragraph("CIRCUIT DIRECTORY", styles['CustomHeading']))
    story.append(Paragraph("Document all circuits for panel directory:", styles['CustomBody']))
    story.append(Spacer(1, 0.1*inch))

    circuit_data = [['Breaker #', 'Amperage', 'Type', 'Circuit Description/Serves', 'GFCI', 'AFCI']]
    for i in range(1, 43):
        circuit_data.append([str(i), '', '', '', '☐', '☐'])

    story.append(create_data_table(circuit_data, [0.6*inch, 0.7*inch, 0.7*inch, 2.5*inch, 0.5*inch, 0.5*inch]))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Type Codes:</b> SP=Single-pole, DP=Double-pole (240V)", styles['CustomBody']))
    story.append(PageBreak())

    # SMOKE & CO DETECTOR INSTALLATION
    story.append(Paragraph("SMOKE & CO DETECTOR INSTALLATION", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    detector_data = [['Location', 'Type', 'Make/Model', 'Interconnected', 'Battery Backup', 'Tested OK', 'Install Date']]
    for i in range(12):
        detector_data.append(['', '', '', '☐', '☐', '☐', ''])

    story.append(create_data_table(detector_data, [1.3*inch, 0.8*inch, 1.0*inch, 0.9*inch, 0.8*inch, 0.7*inch, 0.8*inch]))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Detector Requirements & Testing:</b>", styles['CustomSubHeading']))
    detector_checks = [
        "Smoke detector in every bedroom",
        "Smoke detector outside each sleeping area",
        "Smoke detector on every level including basement",
        "All smoke detectors hard-wired with battery backup",
        "All smoke detectors interconnected (test one, all sound)",
        "Carbon monoxide detector on every level",
        "Carbon monoxide detector near sleeping areas",
        "CO detectors hard-wired with battery backup (or plug-in with battery)",
        "All detectors tested with test button - alarm sounds",
        "Interconnection tested - trigger one, all alarm",
        "Date of installation written on detector",
        "Manufacturer instructions left with homeowner",
    ]
    story.append(create_checkbox_table(detector_checks))
    story.append(PageBreak())

    # SPECIAL SYSTEMS & EQUIPMENT
    story.append(Paragraph("SPECIAL SYSTEMS & EQUIPMENT", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Kitchen Appliances:</b>", styles['CustomSubHeading']))
    kitchen_checks = [
        "Range/Cooktop circuit - proper voltage (240V or 120V)",
        "Range receptacle matches appliance plug or direct wire connection made",
        "Dishwasher circuit - dedicated 20A circuit",
        "Dishwasher receptacle or direct wire as required",
        "Disposal circuit - GFCI protected or on dedicated circuit",
        "Microwave circuit - dedicated 20A circuit (if built-in)",
        "Refrigerator circuit - dedicated 20A circuit",
        "All appliances tested and functioning",
    ]
    story.append(create_checkbox_table(kitchen_checks))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>HVAC Equipment:</b>", styles['CustomSubHeading']))
    hvac_elec_checks = [
        "Furnace/air handler circuit - correct amperage",
        "Disconnect switch installed within sight of equipment",
        "Condensing unit circuit - correct amperage (typically 30-60A)",
        "Condensing unit disconnect installed and accessible",
        "Thermostat wiring complete and functioning",
        "All HVAC equipment properly grounded",
    ]
    story.append(create_checkbox_table(hvac_elec_checks))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Water Heater:</b>", styles['CustomSubHeading']))
    wh_elec_checks = [
        "Water heater circuit - correct amperage (check data plate)",
        "Water heater properly wired (240V for electric)",
        "Disconnect or breaker lockout as required by code",
        "Water heater properly grounded",
    ]
    story.append(create_checkbox_table(wh_elec_checks))
    story.append(PageBreak())

    # EXTERIOR ELECTRICAL
    story.append(Paragraph("<b>Laundry:</b>", styles['CustomSubHeading']))
    laundry_checks = [
        "Washer circuit - dedicated 20A circuit",
        "Dryer circuit - 240V 30A circuit (electric dryer)",
        "Dryer receptacle - NEMA 10-30R or 14-30R",
        "All laundry area outlets GFCI protected",
    ]
    story.append(create_checkbox_table(laundry_checks))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Garage & Exterior:</b>", styles['CustomSubHeading']))
    garage_checks = [
        "All garage receptacles GFCI protected",
        "Garage door opener circuit and receptacle",
        "Garage door opener functioning properly",
        "All exterior receptacles GFCI protected",
        "All exterior receptacles have weatherproof covers",
        "All exterior lighting installed and functioning",
        "Exterior lighting on photocell or timer (if specified)",
        "Landscape lighting transformer installed (if applicable)",
        "Service entrance lighting installed and functioning",
    ]
    story.append(create_checkbox_table(garage_checks))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Other Systems:</b>", styles['CustomSubHeading']))
    other_fields = [
        ('Doorbell/Chime - Working:', '☐ Yes  ☐ No'),
        ('Security System - Installed:', '☐ Yes  ☐ No  ☐ N/A'),
        ('Generator Transfer Switch:', '☐ Yes  ☐ No  ☐ N/A'),
        ('Sump Pump Circuit:', '☐ Yes  ☐ No  ☐ N/A'),
        ('Well Pump Circuit:', '☐ Yes  ☐ No  ☐ N/A'),
        ('Septic Pump Circuit:', '☐ Yes  ☐ No  ☐ N/A'),
        ('Attic/Crawl Space Lights:', '☐ Yes  ☐ No  ☐ N/A'),
    ]
    story.append(create_field_table(other_fields, [2.5*inch, 3.5*inch]))
    story.append(PageBreak())

    # FINAL ELECTRICAL TESTING
    story.append(Paragraph("FINAL ELECTRICAL TESTING", styles['CustomHeading']))
    story.append(Paragraph("Complete testing before requesting final inspection:", styles['CustomBody']))
    story.append(Spacer(1, 0.1*inch))

    final_test_checks = [
        "ALL outlets tested with circuit tester - correct polarity, no open grounds",
        "ALL GFCI outlets tested - trip function works, reset function works",
        "ALL switches tested - operate correct fixtures",
        "ALL 3-way and 4-way switches tested from all locations",
        "ALL light fixtures tested - all bulbs working",
        "ALL dimmer switches tested - smooth dimming operation",
        "ALL ceiling fans tested - all speeds, reverse function, light kits",
        "ALL smoke detectors tested - alarm sounds",
        "ALL smoke detectors interconnection tested - all alarm together",
        "ALL carbon monoxide detectors tested - alarm sounds",
        "ALL appliance circuits tested with appliances operating",
        "ALL exterior outlets and lights tested",
        "Garage door opener tested",
        "Doorbell tested",
        "Panel directory verified - all circuits correctly labeled",
        "Main disconnect operation tested",
        "No flickering lights when major loads turn on",
        "No warm or hot outlets, switches, or breakers under load",
        "No buzzing or humming from outlets, switches, or panel",
    ]
    story.append(create_checkbox_table(final_test_checks))
    story.append(PageBreak())

    # FINAL INSPECTION & SIGN-OFF
    story.append(Paragraph("FINAL ELECTRICAL INSPECTION", styles['CustomHeading']))
    story.append(Spacer(1, 0.2*inch))

    inspection_info = [
        ('Inspection Requested Date', 'line'),
        ('Inspection Scheduled Date', 'line'),
        ('Inspector Name', 'line'),
        ('Inspection Date', 'line'),
        ('Inspection Time', 'line'),
    ]
    story.append(create_field_table(inspection_info))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Inspection Result:</b>", styles['CustomSubHeading']))
    story.append(Paragraph("☐ PASSED - Certificate Issued", styles['CheckboxItem']))
    story.append(Paragraph("☐ FAILED - Corrections Required (see below)", styles['CheckboxItem']))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Required Corrections:</b>", styles['CustomSubHeading']))
    story.append(Spacer(1, 0.1*inch))
    for i in range(10):
        story.append(Paragraph("_" * 90, styles['CustomBody']))

    story.append(Spacer(1, 0.2*inch))
    reinspection_info = [
        ('Corrections Completed Date', 'line'),
        ('Re-Inspection Date', 'line'),
        ('Re-Inspection Result', '☐ PASSED  ☐ FAILED'),
    ]
    story.append(create_field_table(reinspection_info))
    story.append(Spacer(1, 0.3*inch))

    story.append(Paragraph("<b>Certificate of Occupancy / Electrical Certificate:</b>", styles['CustomSubHeading']))
    cert_info = [
        ('Certificate Number', 'line'),
        ('Date Issued', 'line'),
        ('Issued By', 'line'),
    ]
    story.append(create_field_table(cert_info))

    story.append(Spacer(1, 0.3*inch))
    signature_fields = [
        ('Electrician Signature', 'line'),
        ('Date', 'line'),
        ('Owner/Builder Signature', 'line'),
        ('Date', 'line'),
    ]
    story.append(create_field_table(signature_fields))

    # Build PDF
    doc.build(story, canvasmaker=lambda *args, **kwargs: NumberedCanvas(*args, section_name='Section 4.1: Electrical System Completion Log', **kwargs))
    print(f"Created {filename}")
    return filename

# ============================================================================
# 4.2 PLUMBING SYSTEM COMPLETION LOG
# ============================================================================

def create_plumbing_system_log():
    filename = "4.2-plumbing-system-completion-log.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN
    )

    story = []
    styles = create_styles()

    # Title Page
    story.append(Paragraph("PLUMBING SYSTEM", styles['CustomTitle']))
    story.append(Paragraph("COMPLETION LOG", styles['CustomTitle']))
    story.append(Spacer(1, 0.3*inch))

    project_info = [
        ('Project Address', 'line'),
        ('Project Name', 'line'),
        ('Permit Number', 'line'),
        ('Plumber/Company', 'line'),
        ('License Number', 'line'),
        ('Contact Phone', 'line'),
    ]
    story.append(create_field_table(project_info))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>PURPOSE:</b> This log documents the installation and testing of all plumbing fixtures and systems. Use this to verify every fixture is properly installed, leak-free, and functioning correctly before final inspection.", styles['CustomBody']))
    story.append(PageBreak())

    # FIXTURE INSTALLATION STANDARDS
    story.append(Paragraph("FIXTURE INSTALLATION STANDARDS", styles['CustomHeading']))
    story.append(Paragraph("Each fixture must meet these installation requirements:", styles['CustomBody']))
    story.append(Spacer(1, 0.1*inch))

    install_standards = [
        "Fixture installed level and plumb (check with level)",
        "All supply line connections tight - no leaks under pressure",
        "All drain connections sealed - no leaks during drain test",
        "Fixture operates correctly - no drips, proper flow",
        "Shut-off valves installed and operational",
        "Shut-off valves accessible (not behind permanently fixed items)",
        "Aerators installed and clean (no debris from construction)",
        "P-traps properly installed and vented",
        "All fixtures properly secured to backing/blocking",
        "All mounting hardware tight and secure",
        "Caulking/sealing complete where fixture meets wall/floor",
        "Manufacturer's installation instructions followed",
    ]
    story.append(create_checkbox_table(install_standards))
    story.append(PageBreak())

    # KITCHEN PLUMBING
    story.append(Paragraph("KITCHEN PLUMBING", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Kitchen Sink:</b>", styles['CustomSubHeading']))
    kitchen_sink_fields = [
        ('Sink Make/Model', 'line'),
        ('Faucet Make/Model', 'line'),
        ('Installation Date', 'line'),
    ]
    story.append(create_field_table(kitchen_sink_fields))
    story.append(Spacer(1, 0.1*inch))

    kitchen_sink_checks = [
        "☐ Sink properly supported (clips or undermount hardware secure)",
        "☐ Sink level and properly sealed to countertop",
        "☐ Hot supply line to left side (standard)",
        "☐ Cold supply line to right side (standard)",
        "☐ Supply lines connected and tight - no leaks",
        "☐ Shut-off valves installed (hot and cold)",
        "☐ Shut-off valves operate properly",
        "☐ Faucet installed per manufacturer instructions",
        "☐ Faucet operates smoothly - both hot and cold",
        "☐ Spray hose operates properly (if equipped)",
        "☐ Aerator installed and clean",
        "☐ P-trap properly installed",
        "☐ Drain connections tight - no leaks",
        "☐ Drain stopper operates properly",
        "☐ Water pressure adequate",
        "☐ Hot water delivery time acceptable",
    ]
    for check in kitchen_sink_checks:
        story.append(Paragraph(check, styles['CheckboxItem']))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Dishwasher:</b>", styles['CustomSubHeading']))
    dishwasher_checks = [
        "☐ Dishwasher make/model: _________________________________",
        "☐ Water supply line connected (typically 3/8\" or 1/2\")",
        "☐ Supply line shut-off valve installed and accessible",
        "☐ Drain line connected to disposal or drain",
        "☐ High loop installed on drain line (or air gap)",
        "☐ Dishwasher secured to countertop/cabinets",
        "☐ Dishwasher level front-to-back and side-to-side",
        "☐ Door opens and closes properly",
        "☐ Test cycle run - fills properly",
        "☐ Test cycle run - drains completely",
        "☐ No leaks during test cycle",
        "☐ Spray arms rotate freely",
    ]
    for check in dishwasher_checks:
        story.append(Paragraph(check, styles['CheckboxItem']))

    story.append(PageBreak())

    story.append(Paragraph("<b>Garbage Disposal:</b>", styles['CustomSubHeading']))
    disposal_checks = [
        "☐ Disposal make/model: _________________________________",
        "☐ Disposal properly mounted to sink",
        "☐ Discharge drain connected and sealed",
        "☐ Dishwasher connection made (if applicable)",
        "☐ Disposal operates properly",
        "☐ No leaks at mounting flange",
        "☐ No leaks at discharge connection",
        "☐ Reset button accessible",
        "☐ Allen wrench for jam clearing included",
    ]
    for check in disposal_checks:
        story.append(Paragraph(check, styles['CheckboxItem']))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Ice Maker Line:</b>", styles['CustomSubHeading']))
    icemaker_checks = [
        "☐ Ice maker supply line installed: ☐ Yes  ☐ No  ☐ N/A",
        "☐ Supply line material: ☐ Copper  ☐ PEX  ☐ Braided stainless",
        "☐ Shut-off valve installed and accessible",
        "☐ Supply line properly secured",
        "☐ Connection to refrigerator made",
        "☐ No leaks at connections",
        "☐ Ice maker produces ice (if refrigerator installed)",
    ]
    for check in icemaker_checks:
        story.append(Paragraph(check, styles['CheckboxItem']))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Other Kitchen:</b>", styles['CustomSubHeading']))
    other_kitchen_fields = [
        ('Pot Filler Faucet', '☐ Installed  ☐ N/A  Notes: _______________'),
        ('Water Filtration System', '☐ Installed  ☐ N/A  Notes: _______________'),
        ('Instant Hot Water Dispenser', '☐ Installed  ☐ N/A  Notes: _______________'),
        ('Bar Sink', '☐ Installed  ☐ N/A  Notes: _______________'),
    ]
    story.append(create_field_table(other_kitchen_fields, [2.5*inch, 3.5*inch]))
    story.append(PageBreak())

    # BATHROOM PLUMBING - FIXTURE BY FIXTURE
    story.append(Paragraph("BATHROOM PLUMBING - FIXTURE LOG", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    # Bathroom 1
    story.append(Paragraph("<b>BATHROOM #1:</b>", styles['CustomSubHeading']))
    bath1_info = [
        ('Location/Name', 'line'),
        ('Type', '☐ Full  ☐ 3/4  ☐ Half  ☐ Master'),
    ]
    story.append(create_field_table(bath1_info, [2.0*inch, 4.0*inch]))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<i>Sink/Vanity:</i>", styles['CustomBody']))
    bath1_sink_checks = [
        "☐ Sink/vanity installed and level",
        "☐ Faucet make/model: _________________________________",
        "☐ Hot/cold supply connected - no leaks",
        "☐ Shut-off valves installed and working",
        "☐ Faucet operates properly",
        "☐ Drain connected - no leaks",
        "☐ Pop-up drain operates smoothly",
        "☐ P-trap properly installed",
        "☐ Adequate water pressure",
        "☐ Hot water delivery time acceptable",
    ]
    for check in bath1_sink_checks:
        story.append(Paragraph(check, styles['CheckboxItem']))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<i>Toilet:</i>", styles['CustomBody']))
    bath1_toilet_checks = [
        "☐ Toilet make/model: _________________________________",
        "☐ Toilet properly set on flange",
        "☐ Toilet level and secure",
        "☐ Wax ring seal - no leaks at base",
        "☐ Water supply connected - no leaks",
        "☐ Shut-off valve installed and working",
        "☐ Toilet flushes properly - complete flush",
        "☐ Tank fills properly - stops at correct level",
        "☐ No continuous running",
        "☐ No leaks at tank-to-bowl connection",
        "☐ Seat installed properly",
    ]
    for check in bath1_toilet_checks:
        story.append(Paragraph(check, styles['CheckboxItem']))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<i>Shower/Tub:</i>", styles['CustomBody']))
    bath1_shower_checks = [
        "☐ Type: ☐ Shower only  ☐ Tub only  ☐ Tub/shower combo  ☐ N/A",
        "☐ Fixture make/model: _________________________________",
        "☐ Valve installed properly - no leaks behind wall",
        "☐ Shower head/tub spout installed",
        "☐ Hot/cold operation correct (left hot, right cold)",
        "☐ Water temperature appropriate (120°F max)",
        "☐ Water pressure adequate",
        "☐ Diverter operates properly (tub/shower)",
        "☐ No leaks at shower head connection",
        "☐ No leaks at tub spout",
        "☐ Drain operates properly",
        "☐ Tub stopper/trip lever works (if applicable)",
        "☐ Shower door installed and seals properly (if applicable)",
        "☐ No leaks during operation",
    ]
    for check in bath1_shower_checks:
        story.append(Paragraph(check, styles['CheckboxItem']))

    story.append(PageBreak())

    # Bathroom 2
    story.append(Paragraph("<b>BATHROOM #2:</b>", styles['CustomSubHeading']))
    bath2_info = [
        ('Location/Name', 'line'),
        ('Type', '☐ Full  ☐ 3/4  ☐ Half  ☐ Master'),
    ]
    story.append(create_field_table(bath2_info, [2.0*inch, 4.0*inch]))
    story.append(Spacer(1, 0.1*inch))

    # Repeat similar structure for bathroom 2
    story.append(Paragraph("<i>Sink/Vanity:</i>", styles['CustomBody']))
    story.append(Paragraph("☐ Faucet make/model: _________________________________", styles['CheckboxItem']))
    story.append(Paragraph("☐ All installation checks complete (see Bathroom #1 checklist)", styles['CheckboxItem']))
    story.append(Paragraph("☐ No leaks - supply or drain", styles['CheckboxItem']))
    story.append(Paragraph("☐ Operates properly", styles['CheckboxItem']))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<i>Toilet:</i>", styles['CustomBody']))
    story.append(Paragraph("☐ Toilet make/model: _________________________________", styles['CheckboxItem']))
    story.append(Paragraph("☐ All installation checks complete (see Bathroom #1 checklist)", styles['CheckboxItem']))
    story.append(Paragraph("☐ No leaks", styles['CheckboxItem']))
    story.append(Paragraph("☐ Flushes properly", styles['CheckboxItem']))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<i>Shower/Tub:</i>", styles['CustomBody']))
    story.append(Paragraph("☐ Type: ☐ Shower only  ☐ Tub only  ☐ Tub/shower combo  ☐ N/A", styles['CheckboxItem']))
    story.append(Paragraph("☐ Fixture make/model: _________________________________", styles['CheckboxItem']))
    story.append(Paragraph("☐ All installation checks complete (see Bathroom #1 checklist)", styles['CheckboxItem']))
    story.append(Paragraph("☐ No leaks", styles['CheckboxItem']))
    story.append(Paragraph("☐ Operates properly", styles['CheckboxItem']))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>BATHROOM #3:</b>", styles['CustomSubHeading']))
    story.append(Paragraph("Location/Name: _________________________________ Type: ☐ Full  ☐ 3/4  ☐ Half  ☐ N/A", styles['CheckboxItem']))
    story.append(Paragraph("☐ All fixtures installed per checklists above", styles['CheckboxItem']))
    story.append(Paragraph("☐ All fixtures tested - no leaks, proper operation", styles['CheckboxItem']))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>BATHROOM #4:</b>", styles['CustomSubHeading']))
    story.append(Paragraph("Location/Name: _________________________________ Type: ☐ Full  ☐ 3/4  ☐ Half  ☐ N/A", styles['CheckboxItem']))
    story.append(Paragraph("☐ All fixtures installed per checklists above", styles['CheckboxItem']))
    story.append(Paragraph("☐ All fixtures tested - no leaks, proper operation", styles['CheckboxItem']))

    story.append(PageBreak())

    # LAUNDRY PLUMBING
    story.append(Paragraph("LAUNDRY PLUMBING", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    laundry_checks = [
        "☐ Washer box/outlet installed at proper height (typically 42-48\")",
        "☐ Hot and cold supply valves installed",
        "☐ Supply valves operate properly (quarter-turn or multi-turn)",
        "☐ Supply valves accessible",
        "☐ Drain standpipe installed (18-30\" high typical)",
        "☐ P-trap installed on standpipe",
        "☐ Washer hoses connected (if washer installed)",
        "☐ No leaks at valve connections",
        "☐ Washer test cycle run (if washer installed)",
        "☐ Drain handles washer discharge without overflow",
        "☐ Laundry sink installed (if applicable)",
        "☐ Laundry sink faucet operates properly (if applicable)",
        "☐ Gas line for dryer (if applicable): ☐ Installed  ☐ N/A",
    ]
    story.append(create_checkbox_table(laundry_checks))
    story.append(PageBreak())

    # WATER HEATER
    story.append(Paragraph("WATER HEATER INSTALLATION", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    wh_info = [
        ('Make/Model', 'line'),
        ('Type', '☐ Electric  ☐ Gas  ☐ Tankless  ☐ Heat Pump'),
        ('Capacity', 'line'),
        ('Location', 'line'),
        ('Installation Date', 'line'),
    ]
    story.append(create_field_table(wh_info))
    story.append(Spacer(1, 0.1*inch))

    wh_checks = [
        "☐ Water heater properly supported/secured",
        "☐ Water heater level (tank type)",
        "☐ Cold water inlet connected properly",
        "☐ Hot water outlet connected properly",
        "☐ Shut-off valve on cold water inlet",
        "☐ TPR (temperature/pressure relief) valve installed",
        "☐ TPR discharge pipe installed - terminates 6\" above floor or outside",
        "☐ TPR discharge pipe proper material (copper or CPVC)",
        "☐ Drain valve accessible",
        "☐ Gas line connected properly (if gas) - no leaks",
        "☐ Gas shut-off valve within 6 feet (if gas)",
        "☐ Vent pipe properly installed (if gas)",
        "☐ Vent pipe terminates properly outside",
        "☐ Electrical connection made (if electric)",
        "☐ Electrical disconnect accessible (if electric)",
        "☐ Pan installed under heater (if in living space or attic)",
        "☐ Pan drain line runs to exterior or floor drain",
        "☐ Earthquake straps installed (if required by code)",
        "☐ Expansion tank installed (if required)",
        "☐ Water heater producing hot water",
        "☐ Temperature set to 120°F or lower",
        "☐ No leaks at any connections",
        "☐ Manufacturer's instructions left with homeowner",
        "☐ Warranty information recorded",
    ]
    story.append(create_checkbox_table(wh_checks))
    story.append(PageBreak())

    # EXTERIOR PLUMBING
    story.append(Paragraph("EXTERIOR PLUMBING", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Hose Bibs (Exterior Faucets):</b>", styles['CustomSubHeading']))
    hosebib_data = [['Location', 'Type', 'Frost-Free', 'Operates OK', 'No Leaks', 'Shut-off Valve', 'Notes']]
    for i in range(6):
        hosebib_data.append(['', '', '☐', '☐', '☐', '☐', ''])

    story.append(create_data_table(hosebib_data, [1.3*inch, 1.0*inch, 0.7*inch, 0.8*inch, 0.7*inch, 0.8*inch, 0.9*inch]))
    story.append(Spacer(1, 0.2*inch))

    exterior_checks = [
        "☐ All hose bibs freeze-proof type (if required by climate)",
        "☐ All hose bibs properly secured to structure",
        "☐ All hose bibs slope down when off (for drainage)",
        "☐ Interior shut-off valves accessible for winter shutdown",
        "☐ Exterior shower (if applicable): ☐ Installed  ☐ Tested  ☐ N/A",
    ]
    story.append(create_checkbox_table(exterior_checks))
    story.append(PageBreak())

    # SYSTEM TESTING
    story.append(Paragraph("COMPLETE SYSTEM TESTING", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Pressure Test:</b>", styles['CustomSubHeading']))
    pressure_info = [
        ('Test Date', 'line'),
        ('Static Pressure (PSI)', 'line'),
        ('Test Duration', 'line'),
        ('Pressure Loss', 'line'),
    ]
    story.append(create_field_table(pressure_info))
    story.append(Spacer(1, 0.1*inch))

    pressure_checks = [
        "☐ All fixtures and supply lines pressurized",
        "☐ System pressure 40-60 PSI (typical residential)",
        "☐ Pressure held steady for minimum 15 minutes",
        "☐ No visible leaks at any connection",
        "☐ No drop in pressure during test",
        "☐ Pressure regulator functioning (if installed)",
    ]
    story.append(create_checkbox_table(pressure_checks))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Drain Flow Test:</b>", styles['CustomSubHeading']))
    drain_checks = [
        "☐ All drains flow freely - no slow drainage",
        "☐ No gurgling sounds from drains",
        "☐ All P-traps holding water (no dry traps)",
        "☐ No sewer gas odors",
        "☐ All vents functioning properly",
        "☐ Multiple fixtures run simultaneously - drains handle load",
        "☐ No leaks at drain connections under use",
    ]
    story.append(create_checkbox_table(drain_checks))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Hot Water Performance:</b>", styles['CustomSubHeading']))
    hw_fields = [
        ('Furthest Fixture from Water Heater', 'line'),
        ('Hot Water Delivery Time (minutes)', 'line'),
        ('Hot Water Temperature at Tap (°F)', 'line'),
    ]
    story.append(create_field_table(hw_fields))
    story.append(Spacer(1, 0.1*inch))

    hw_checks = [
        "☐ Hot water delivery time acceptable (typically under 2 minutes)",
        "☐ Water temperature 120°F or lower (scalding prevention)",
        "☐ Consistent temperature at all fixtures",
        "☐ Adequate hot water volume for household needs",
    ]
    story.append(create_checkbox_table(hw_checks))

    story.append(PageBreak())

    # SPECIAL SYSTEMS
    story.append(Paragraph("SPECIAL SYSTEMS (if applicable)", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Well System:</b>", styles['CustomSubHeading']))
    well_fields = [
        ('Well Installed', '☐ Yes  ☐ No  ☐ N/A'),
        ('Well Depth (feet)', 'line'),
        ('Pump Type', '☐ Submersible  ☐ Jet  ☐ Other: _______'),
        ('Pump HP', 'line'),
        ('Pressure Tank Size (gallons)', 'line'),
        ('Cut-in Pressure (PSI)', 'line'),
        ('Cut-out Pressure (PSI)', 'line'),
    ]
    story.append(create_field_table(well_fields, [2.5*inch, 3.5*inch]))
    story.append(Spacer(1, 0.1*inch))

    well_checks = [
        "☐ Pump operates properly",
        "☐ Pressure tank properly charged",
        "☐ Pressure switch functioning correctly",
        "☐ Well cap sealed properly",
        "☐ Water quality test completed",
        "☐ Adequate flow rate for household needs",
    ]
    story.append(create_checkbox_table(well_checks))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Septic System:</b>", styles['CustomSubHeading']))
    septic_fields = [
        ('Septic System Installed', '☐ Yes  ☐ No  ☐ N/A'),
        ('Tank Size (gallons)', 'line'),
        ('Tank Type', '☐ Concrete  ☐ Plastic  ☐ Fiberglass'),
        ('Drain Field Type', 'line'),
        ('Installation Date', 'line'),
        ('Inspection Date', 'line'),
        ('Inspection Result', '☐ Passed  ☐ Failed'),
    ]
    story.append(create_field_table(septic_fields, [2.5*inch, 3.5*inch]))

    story.append(PageBreak())

    # FINAL INSPECTION
    story.append(Paragraph("FINAL PLUMBING INSPECTION", styles['CustomHeading']))
    story.append(Spacer(1, 0.2*inch))

    inspection_info = [
        ('Inspection Requested Date', 'line'),
        ('Inspection Scheduled Date', 'line'),
        ('Inspector Name', 'line'),
        ('Inspection Date', 'line'),
        ('Inspection Time', 'line'),
    ]
    story.append(create_field_table(inspection_info))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Pre-Inspection Checklist:</b>", styles['CustomSubHeading']))
    preinspect_checks = [
        "☐ All fixtures installed and tested",
        "☐ No leaks anywhere in system",
        "☐ All drains flowing properly",
        "☐ Water pressure adequate throughout",
        "☐ Hot water system functioning",
        "☐ All shut-off valves accessible",
        "☐ Access panels installed where required",
        "☐ Clean-outs accessible",
        "☐ All work completed per approved plans",
    ]
    story.append(create_checkbox_table(preinspect_checks))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Inspection Result:</b>", styles['CustomSubHeading']))
    story.append(Paragraph("☐ PASSED - Certificate Issued", styles['CheckboxItem']))
    story.append(Paragraph("☐ FAILED - Corrections Required (see below)", styles['CheckboxItem']))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Required Corrections:</b>", styles['CustomSubHeading']))
    story.append(Spacer(1, 0.1*inch))
    for i in range(10):
        story.append(Paragraph("_" * 90, styles['CustomBody']))

    story.append(Spacer(1, 0.2*inch))
    reinspection_info = [
        ('Corrections Completed Date', 'line'),
        ('Re-Inspection Date', 'line'),
        ('Re-Inspection Result', '☐ PASSED  ☐ FAILED'),
    ]
    story.append(create_field_table(reinspection_info))

    story.append(Spacer(1, 0.3*inch))
    signature_fields = [
        ('Plumber Signature', 'line'),
        ('Date', 'line'),
        ('Owner/Builder Signature', 'line'),
        ('Date', 'line'),
    ]
    story.append(create_field_table(signature_fields))

    # Build PDF
    doc.build(story, canvasmaker=lambda *args, **kwargs: NumberedCanvas(*args, section_name='Section 4.2: Plumbing System Completion Log', **kwargs))
    print(f"Created {filename}")
    return filename

# ============================================================================
# 4.3 HVAC SYSTEM COMPLETION
# ============================================================================

def create_hvac_system_completion():
    filename = "4.3-hvac-system-completion.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN
    )

    story = []
    styles = create_styles()

    # Title Page
    story.append(Paragraph("HVAC SYSTEM", styles['CustomTitle']))
    story.append(Paragraph("COMPLETION & COMMISSIONING", styles['CustomTitle']))
    story.append(Spacer(1, 0.3*inch))

    project_info = [
        ('Project Address', 'line'),
        ('Project Name', 'line'),
        ('Permit Number', 'line'),
        ('HVAC Contractor', 'line'),
        ('License Number', 'line'),
        ('Contact Phone', 'line'),
    ]
    story.append(create_field_table(project_info))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>PURPOSE:</b> This document verifies proper installation, startup, and commissioning of the complete HVAC system. Proper commissioning ensures the system operates efficiently, safely, and as designed.", styles['CustomBody']))
    story.append(PageBreak())

    # EQUIPMENT INSTALLATION
    story.append(Paragraph("EQUIPMENT INSTALLATION", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Indoor Unit (Furnace/Air Handler):</b>", styles['CustomSubHeading']))
    indoor_info = [
        ('Make/Model', 'line'),
        ('Serial Number', 'line'),
        ('BTU Input/Output', 'line'),
        ('Fuel Type', '☐ Natural Gas  ☐ Propane  ☐ Electric  ☐ Oil'),
        ('AFUE Rating', 'line'),
        ('Location', 'line'),
        ('Installation Date', 'line'),
    ]
    story.append(create_field_table(indoor_info))
    story.append(Spacer(1, 0.1*inch))

    indoor_checks = [
        "☐ Unit installed level and properly supported",
        "☐ Proper clearances maintained (front, sides, top per manufacturer)",
        "☐ Unit properly secured to platform or hung from joists",
        "☐ Gas line connected properly (if gas) - no leaks",
        "☐ Gas shut-off valve within 6 feet (if gas)",
        "☐ Gas line pressure tested (if gas)",
        "☐ Electrical connection made - proper voltage and amperage",
        "☐ Electrical disconnect within sight of unit",
        "☐ Condensate drain line installed with proper slope",
        "☐ Condensate drain terminates appropriately",
        "☐ Condensate trap installed (if required)",
        "☐ Secondary drain pan installed (if in attic/living space)",
        "☐ Secondary drain pan alarm/sensor installed",
        "☐ Combustion air intake adequate (if gas)",
        "☐ Vent pipe properly installed (if gas)",
        "☐ Vent pipe properly supported and sloped",
        "☐ Vent termination proper distance from windows/openings",
        "☐ Filter access accessible",
        "☐ Blower door/access panels properly secured",
    ]
    story.append(create_checkbox_table(indoor_checks))
    story.append(PageBreak())

    story.append(Paragraph("<b>Outdoor Unit (Condensing Unit/Heat Pump):</b>", styles['CustomSubHeading']))
    outdoor_info = [
        ('Make/Model', 'line'),
        ('Serial Number', 'line'),
        ('Tonnage', 'line'),
        ('SEER Rating', 'line'),
        ('Type', '☐ Air Conditioner  ☐ Heat Pump'),
        ('Refrigerant Type', 'line'),
        ('Location', 'line'),
    ]
    story.append(create_field_table(outdoor_info))
    story.append(Spacer(1, 0.1*inch))

    outdoor_checks = [
        "☐ Unit installed on level pad (concrete or composite)",
        "☐ Pad stable and properly sized",
        "☐ Unit level side-to-side and front-to-back (within 1/4\")",
        "☐ Proper clearances maintained (12\" sides, 24\" service side, 60\" top)",
        "☐ No vegetation or obstructions blocking airflow",
        "☐ Refrigerant lines connected and insulated",
        "☐ Line set insulation complete - no exposed copper",
        "☐ Line set properly secured to structure",
        "☐ Electrical disconnect installed within sight of unit",
        "☐ Electrical disconnect proper rating (check data plate)",
        "☐ Whip (flexible conduit) to unit installed properly",
        "☐ Electrical connections tight at contactor and terminals",
        "☐ Condenser fan rotates freely by hand (power off)",
        "☐ Coil fins undamaged and clean",
        "☐ Service valves accessible",
    ]
    story.append(create_checkbox_table(outdoor_checks))
    story.append(PageBreak())

    # DUCTWORK COMPLETION
    story.append(Paragraph("DUCTWORK COMPLETION", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    duct_checks = [
        "☐ All supply registers installed",
        "☐ All supply registers properly secured",
        "☐ Register boot connections sealed with mastic",
        "☐ All return grilles installed",
        "☐ Return grille connections sealed",
        "☐ Main trunk line connections sealed",
        "☐ All branch take-offs sealed",
        "☐ Flexible duct properly supported (every 4-5 feet)",
        "☐ Flexible duct not kinked or crushed",
        "☐ Ductwork insulation complete (if required)",
        "☐ No disconnected ductwork",
        "☐ Filter installed - correct size noted: _____________",
        "☐ Filter access accessible",
        "☐ Return air pathways adequate (no blocked returns)",
        "☐ Access panels installed for dampers and controls",
    ]
    story.append(create_checkbox_table(duct_checks))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Register/Grille Schedule:</b>", styles['CustomSubHeading']))
    register_data = [['Room', 'Supply Register Size', 'Qty', 'Return Grille Size', 'Qty', 'Notes']]
    for i in range(15):
        register_data.append(['', '', '', '', '', ''])

    story.append(create_data_table(register_data, [1.3*inch, 1.2*inch, 0.4*inch, 1.1*inch, 0.4*inch, 1.6*inch]))
    story.append(PageBreak())

    # THERMOSTAT
    story.append(Paragraph("THERMOSTAT INSTALLATION", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    tstat_info = [
        ('Make/Model', 'line'),
        ('Type', '☐ Programmable  ☐ Non-Programmable  ☐ Smart/WiFi'),
        ('Location', 'line'),
        ('Number of Zones', 'line'),
    ]
    story.append(create_field_table(tstat_info))
    story.append(Spacer(1, 0.1*inch))

    tstat_checks = [
        "☐ Thermostat located on interior wall (not exterior)",
        "☐ Location away from direct sunlight",
        "☐ Location away from heat sources (lamps, appliances)",
        "☐ Location away from drafts (doors, windows)",
        "☐ Thermostat mounted level at 52-60\" height",
        "☐ All wires properly labeled",
        "☐ All wire connections tight",
        "☐ Thermostat wired correctly - tested with system",
        "☐ Programmable thermostat programmed (if applicable)",
        "☐ Smart thermostat connected to WiFi (if applicable)",
        "☐ Homeowner trained on thermostat operation",
        "☐ Manual/instructions left with homeowner",
    ]
    story.append(create_checkbox_table(tstat_checks))
    story.append(PageBreak())

    # SYSTEM COMMISSIONING
    story.append(Paragraph("SYSTEM COMMISSIONING", styles['CustomHeading']))
    story.append(Paragraph("Professional commissioning must be performed by qualified HVAC technician:", styles['CustomBody']))
    story.append(Spacer(1, 0.2*inch))

    commissioning_info = [
        ('Commissioning Technician', 'line'),
        ('Company', 'line'),
        ('License Number', 'line'),
        ('Commissioning Date', 'line'),
    ]
    story.append(create_field_table(commissioning_info))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Refrigerant Charging (Air Conditioner/Heat Pump):</b>", styles['CustomSubHeading']))
    refrigerant_fields = [
        ('Refrigerant Type', 'line'),
        ('Charge Weight (lbs)', 'line'),
        ('Charging Method', '☐ Subcooling  ☐ Superheat  ☐ Weigh-In'),
        ('Outdoor Temperature (°F)', 'line'),
        ('Indoor Temperature (°F)', 'line'),
        ('Indoor Relative Humidity (%)', 'line'),
    ]
    story.append(create_field_table(refrigerant_fields))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Subcooling Method (preferred for TXV systems):</b>", styles['CustomBody']))
    subcool_fields = [
        ('High Side Pressure (PSI)', 'line'),
        ('Saturation Temperature (°F)', 'line'),
        ('Liquid Line Temperature (°F)', 'line'),
        ('Subcooling (°F)', 'line'),
        ('Target Subcooling per Manufacturer', 'line'),
        ('Subcooling Within Spec', '☐ Yes  ☐ No'),
    ]
    story.append(create_field_table(subcool_fields, [3.0*inch, 3.0*inch]))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Superheat Method (for fixed orifice/piston systems):</b>", styles['CustomBody']))
    superheat_fields = [
        ('Low Side Pressure (PSI)', 'line'),
        ('Saturation Temperature (°F)', 'line'),
        ('Suction Line Temperature (°F)', 'line'),
        ('Superheat (°F)', 'line'),
        ('Target Superheat per Manufacturer', 'line'),
        ('Superheat Within Spec', '☐ Yes  ☐ No'),
    ]
    story.append(create_field_table(superheat_fields, [3.0*inch, 3.0*inch]))
    story.append(PageBreak())

    story.append(Paragraph("<b>Airflow Verification:</b>", styles['CustomSubHeading']))
    airflow_fields = [
        ('Blower Speed Setting', 'line'),
        ('Supply Air Temperature (°F)', 'line'),
        ('Return Air Temperature (°F)', 'line'),
        ('Temperature Split (°F)', 'line'),
        ('Target Split (cooling: 15-20°F)', 'line'),
        ('Airflow CFM (if measured)', 'line'),
        ('Target Airflow (400 CFM/ton)', 'line'),
        ('Airflow Adequate', '☐ Yes  ☐ No'),
    ]
    story.append(create_field_table(airflow_fields, [3.0*inch, 3.0*inch]))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Gas Furnace Checks (if applicable):</b>", styles['CustomSubHeading']))
    gas_fields = [
        ('Gas Type', '☐ Natural Gas  ☐ Propane'),
        ('Manifold Pressure (in. w.c.)', 'line'),
        ('Target Manifold Pressure', 'line'),
        ('Temperature Rise (°F)', 'line'),
        ('Target Temperature Rise Range', 'line'),
        ('Flame Appearance', '☐ Blue/Stable  ☐ Other: _______'),
        ('Carbon Monoxide Test (PPM)', 'line'),
        ('CO Level Acceptable (<10 PPM)', '☐ Yes  ☐ No'),
        ('Vent Draft Adequate', '☐ Yes  ☐ No  ☐ N/A'),
    ]
    story.append(create_field_table(gas_fields, [3.0*inch, 3.0*inch]))
    story.append(PageBreak())

    # OPERATIONAL TESTING
    story.append(Paragraph("OPERATIONAL TESTING", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Heating Mode Test:</b>", styles['CustomSubHeading']))
    heat_checks = [
        "☐ Thermostat set to HEAT mode",
        "☐ Temperature set above room temperature",
        "☐ Furnace/heat pump starts within 1-2 minutes",
        "☐ Ignition sequence normal (if gas)",
        "☐ Burner flames stable and blue (if gas)",
        "☐ Blower starts after heat-up delay",
        "☐ Warm air from all supply registers",
        "☐ Airflow adequate at all registers",
        "☐ System runs continuously without cycling",
        "☐ No unusual noises during operation",
        "☐ System reaches temperature setpoint and cycles off",
        "☐ Blower continues for cool-down period",
        "☐ No error codes or warning lights",
    ]
    story.append(create_checkbox_table(heat_checks))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Cooling Mode Test:</b>", styles['CustomSubHeading']))
    cool_checks = [
        "☐ Thermostat set to COOL mode",
        "☐ Temperature set below room temperature",
        "☐ Outdoor unit starts (compressor and fan)",
        "☐ Indoor blower starts",
        "☐ Cool air from all supply registers",
        "☐ Temperature drop 15-20°F (supply vs. return)",
        "☐ Condensate draining properly",
        "☐ No water leaks from indoor unit",
        "☐ Outdoor unit running smoothly - no unusual noises",
        "☐ System runs continuously without short-cycling",
        "☐ System reaches temperature setpoint and cycles off",
        "☐ No error codes or warning lights",
    ]
    story.append(create_checkbox_table(cool_checks))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>General System Operation:</b>", styles['CustomSubHeading']))
    operation_checks = [
        "☐ Thermostat controls system properly",
        "☐ Fan mode AUTO and ON both work",
        "☐ System cycles properly - not short-cycling",
        "☐ No vibration in ductwork during operation",
        "☐ No whistling or whooshing sounds from registers",
        "☐ All rooms receiving adequate airflow",
        "☐ Return air adequate - no negative pressure issues",
        "☐ Emergency heat operates (if heat pump) - ☐ N/A",
        "☐ Reversing valve operates (if heat pump) - ☐ N/A",
        "☐ Outdoor unit clean and free of debris",
    ]
    story.append(create_checkbox_table(operation_checks))
    story.append(PageBreak())

    # AIRFLOW BALANCING
    story.append(Paragraph("AIRFLOW BALANCING", styles['CustomHeading']))
    story.append(Paragraph("Verify adequate airflow to all rooms:", styles['CustomBody']))
    story.append(Spacer(1, 0.1*inch))

    balance_data = [['Room', 'Supply Register', 'Airflow', 'Temperature', 'Damper Adjustment', 'Notes']]
    for i in range(18):
        balance_data.append(['', '', '☐ Good  ☐ Low', '', '', ''])

    story.append(create_data_table(balance_data, [1.2*inch, 1.0*inch, 1.0*inch, 0.8*inch, 1.2*inch, 1.0*inch]))
    story.append(Spacer(1, 0.1*inch))

    balance_checks = [
        "☐ All rooms receiving airflow",
        "☐ Hot/cold spots identified and addressed",
        "☐ Dampers adjusted for balanced airflow",
        "☐ Temperature variation between rooms minimal (within 3-4°F)",
    ]
    story.append(create_checkbox_table(balance_checks))
    story.append(PageBreak())

    # FINAL INSPECTION
    story.append(Paragraph("FINAL HVAC INSPECTION", styles['CustomHeading']))
    story.append(Spacer(1, 0.2*inch))

    inspection_info = [
        ('Inspection Requested Date', 'line'),
        ('Inspection Scheduled Date', 'line'),
        ('Inspector Name', 'line'),
        ('Inspection Date', 'line'),
        ('Inspection Time', 'line'),
    ]
    story.append(create_field_table(inspection_info))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Pre-Inspection Checklist:</b>", styles['CustomSubHeading']))
    preinspect_checks = [
        "☐ All equipment properly installed",
        "☐ All ductwork complete and sealed",
        "☐ System commissioned by qualified technician",
        "☐ Refrigerant charge verified",
        "☐ Heating and cooling both tested",
        "☐ Thermostat functioning properly",
        "☐ All required disconnects installed",
        "☐ Proper clearances maintained",
        "☐ Condensate drains functioning",
        "☐ Work completed per approved plans",
    ]
    story.append(create_checkbox_table(preinspect_checks))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Inspection Result:</b>", styles['CustomSubHeading']))
    story.append(Paragraph("☐ PASSED - Certificate Issued", styles['CheckboxItem']))
    story.append(Paragraph("☐ FAILED - Corrections Required (see below)", styles['CheckboxItem']))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Required Corrections:</b>", styles['CustomSubHeading']))
    story.append(Spacer(1, 0.1*inch))
    for i in range(8):
        story.append(Paragraph("_" * 90, styles['CustomBody']))

    story.append(Spacer(1, 0.2*inch))
    reinspection_info = [
        ('Corrections Completed Date', 'line'),
        ('Re-Inspection Date', 'line'),
        ('Re-Inspection Result', '☐ PASSED  ☐ FAILED'),
    ]
    story.append(create_field_table(reinspection_info))
    story.append(PageBreak())

    # WARRANTY & DOCUMENTATION
    story.append(Paragraph("WARRANTY & DOCUMENTATION", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    warranty_info = [
        ('Equipment Warranty Period', 'line'),
        ('Parts Warranty Period', 'line'),
        ('Labor Warranty Period', 'line'),
        ('Compressor Warranty Period', 'line'),
        ('Registration Required', '☐ Yes  ☐ No'),
        ('Registration Completed', '☐ Yes  ☐ No  ☐ N/A'),
        ('Registration Date', 'line'),
    ]
    story.append(create_field_table(warranty_info))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Documentation Provided to Homeowner:</b>", styles['CustomSubHeading']))
    docs_checks = [
        "☐ Equipment owner's manuals (indoor and outdoor units)",
        "☐ Thermostat manual and programming guide",
        "☐ Warranty information and registration",
        "☐ Filter size and replacement schedule",
        "☐ Maintenance schedule and recommendations",
        "☐ Contractor contact information for service",
        "☐ As-built duct layout (if available)",
        "☐ Commissioning report with all measurements",
    ]
    story.append(create_checkbox_table(docs_checks))

    story.append(Spacer(1, 0.3*inch))
    signature_fields = [
        ('HVAC Technician Signature', 'line'),
        ('Date', 'line'),
        ('Owner/Builder Signature', 'line'),
        ('Date', 'line'),
    ]
    story.append(create_field_table(signature_fields))

    # Build PDF
    doc.build(story, canvasmaker=lambda *args, **kwargs: NumberedCanvas(*args, section_name='Section 4.3: HVAC System Completion', **kwargs))
    print(f"Created {filename}")
    return filename

# ============================================================================
# 4.4 FINAL SYSTEMS WALKTHROUGH
# ============================================================================

def create_final_systems_walkthrough():
    filename = "4.4-final-systems-walkthrough.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN
    )

    story = []
    styles = create_styles()

    # Title Page
    story.append(Paragraph("FINAL SYSTEMS", styles['CustomTitle']))
    story.append(Paragraph("WALKTHROUGH CHECKLIST", styles['CustomTitle']))
    story.append(Spacer(1, 0.3*inch))

    project_info = [
        ('Project Address', 'line'),
        ('Project Name', 'line'),
        ('Walkthrough Date', 'line'),
        ('Conducted By', 'line'),
    ]
    story.append(create_field_table(project_info))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>PURPOSE:</b> This comprehensive walkthrough verifies that ALL systems are functioning properly before final inspection and move-in. Test every fixture, outlet, switch, and system. This is your final quality check.", styles['CustomBody']))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>INSTRUCTIONS:</b> Go through every room systematically. Check every box as you test. Mark any issues in the Notes column for immediate correction. Do not skip anything - test everything!", styles['CustomBody']))
    story.append(PageBreak())

    # ELECTRICAL SYSTEMS WALKTHROUGH
    story.append(Paragraph("ELECTRICAL SYSTEMS WALKTHROUGH", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Complete Lighting Test:</b>", styles['CustomSubHeading']))
    story.append(Paragraph("Turn on EVERY light switch in the house and verify operation:", styles['CustomBody']))
    story.append(Spacer(1, 0.1*inch))

    light_data = [['Room/Location', 'Switch Tested', 'Light Works', 'Bulbs OK', '3-Way Works', 'Dimmer OK', 'Notes']]
    for i in range(30):
        light_data.append(['', '☐', '☐', '☐', '☐ N/A', '☐ N/A', ''])

    story.append(create_data_table(light_data, [1.3*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.7*inch, 0.6*inch, 1.2*inch]))
    story.append(PageBreak())

    story.append(Paragraph("<b>Complete Outlet Test:</b>", styles['CustomSubHeading']))
    story.append(Paragraph("Test EVERY outlet with circuit tester:", styles['CustomBody']))
    story.append(Spacer(1, 0.1*inch))

    outlet_data = [['Room/Location', 'Outlet Tested', 'Polarity OK', 'GFCI Trips', 'GFCI Resets', 'Notes']]
    for i in range(35):
        outlet_data.append(['', '☐', '☐', '☐ N/A', '☐ N/A', ''])

    story.append(create_data_table(outlet_data, [1.8*inch, 0.8*inch, 0.8*inch, 0.7*inch, 0.8*inch, 1.3*inch]))
    story.append(PageBreak())

    story.append(Paragraph("<b>Safety Device Testing:</b>", styles['CustomSubHeading']))
    smoke_co_checks = [
        "☐ All smoke detectors tested - alarm sounds",
        "☐ All smoke detectors interconnected - test one, all alarm",
        "☐ All carbon monoxide detectors tested - alarm sounds",
        "☐ All GFCI outlets tested - trip function works",
        "☐ All GFCI outlets reset properly",
        "☐ AFCI breakers tested - function properly",
    ]
    story.append(create_checkbox_table(smoke_co_checks))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Exterior Electrical:</b>", styles['CustomSubHeading']))
    exterior_elec_checks = [
        "☐ All exterior lights tested and working",
        "☐ All exterior outlets tested - GFCI protected",
        "☐ Garage door opener operates properly",
        "☐ Garage lights work",
        "☐ Doorbell works (front and back if applicable)",
        "☐ Landscape lighting tested (if installed)",
    ]
    story.append(create_checkbox_table(exterior_elec_checks))
    story.append(PageBreak())

    # PLUMBING SYSTEMS WALKTHROUGH
    story.append(Paragraph("PLUMBING SYSTEMS WALKTHROUGH", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Run Every Faucet:</b>", styles['CustomSubHeading']))
    story.append(Paragraph("Test hot AND cold water at every fixture:", styles['CustomBody']))
    story.append(Spacer(1, 0.1*inch))

    faucet_data = [['Location/Fixture', 'Cold Runs', 'Hot Runs', 'Pressure OK', 'No Leaks', 'Drains OK', 'Notes']]
    fixtures = [
        'Kitchen Sink',
        'Kitchen Sink Spray',
        'Master Bath Sink 1',
        'Master Bath Sink 2',
        'Master Shower',
        'Master Tub',
        'Bath 2 Sink',
        'Bath 2 Shower/Tub',
        'Bath 3 Sink',
        'Bath 3 Shower/Tub',
        'Bath 4 Sink',
        'Powder Room Sink',
        'Laundry Sink',
        'Utility Sink',
        'Hose Bib - Front',
        'Hose Bib - Back',
        'Hose Bib - Side',
    ]

    for fixture in fixtures:
        faucet_data.append([fixture, '☐', '☐', '☐', '☐', '☐', ''])

    # Add blank rows for additional fixtures
    for i in range(5):
        faucet_data.append(['', '☐', '☐', '☐', '☐', '☐', ''])

    story.append(create_data_table(faucet_data, [1.4*inch, 0.6*inch, 0.6*inch, 0.7*inch, 0.6*inch, 0.6*inch, 1.1*inch]))
    story.append(PageBreak())

    story.append(Paragraph("<b>Flush Every Toilet:</b>", styles['CustomSubHeading']))
    toilet_data = [['Location', 'Flushes Properly', 'Fills Properly', 'Stops Filling', 'No Leaks', 'No Running', 'Notes']]
    for i in range(6):
        toilet_data.append(['', '☐', '☐', '☐', '☐', '☐', ''])

    story.append(create_data_table(toilet_data, [1.5*inch, 0.9*inch, 0.8*inch, 0.8*inch, 0.6*inch, 0.7*inch, 0.9*inch]))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Appliance Testing:</b>", styles['CustomSubHeading']))
    appliance_checks = [
        "☐ Dishwasher - run complete cycle, fills properly",
        "☐ Dishwasher - drains completely, no leaks",
        "☐ Garbage disposal - operates properly, no leaks",
        "☐ Washing machine - fills properly (if installed)",
        "☐ Washing machine - drains properly (if installed)",
        "☐ Ice maker - produces ice (if installed)",
        "☐ Water heater - producing hot water consistently",
    ]
    story.append(create_checkbox_table(appliance_checks))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Leak Check:</b>", styles['CustomSubHeading']))
    leak_checks = [
        "☐ Check under all sinks - no leaks",
        "☐ Check around all toilets - no water at base",
        "☐ Check all shut-off valve connections - no drips",
        "☐ Check water heater connections - no leaks",
        "☐ Check around tub/shower surrounds - no water damage",
        "☐ Check ceilings below bathrooms - no water stains",
        "☐ Check basement/crawl space - no pipe leaks",
    ]
    story.append(create_checkbox_table(leak_checks))
    story.append(PageBreak())

    # HVAC SYSTEMS WALKTHROUGH
    story.append(Paragraph("HVAC SYSTEMS WALKTHROUGH", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Extended Heating Test (30 minutes minimum):</b>", styles['CustomSubHeading']))
    heat_test_fields = [
        ('Test Start Time', 'line'),
        ('Start Temperature', 'line'),
        ('Target Temperature', 'line'),
        ('Test End Time', 'line'),
        ('End Temperature', 'line'),
    ]
    story.append(create_field_table(heat_test_fields))
    story.append(Spacer(1, 0.1*inch))

    heat_test_checks = [
        "☐ System starts when thermostat calls for heat",
        "☐ Warm air from all registers within 5 minutes",
        "☐ System runs continuously without cycling off",
        "☐ Temperature rises steadily",
        "☐ All rooms getting warm air",
        "☐ No cold spots in house",
        "☐ System reaches setpoint and cycles off properly",
        "☐ No unusual noises during operation",
        "☐ No burning smell",
        "☐ Blower operates smoothly",
    ]
    story.append(create_checkbox_table(heat_test_checks))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Extended Cooling Test (30 minutes minimum):</b>", styles['CustomSubHeading']))
    cool_test_fields = [
        ('Test Start Time', 'line'),
        ('Start Temperature', 'line'),
        ('Target Temperature', 'line'),
        ('Test End Time', 'line'),
        ('End Temperature', 'line'),
    ]
    story.append(create_field_table(cool_test_fields))
    story.append(Spacer(1, 0.1*inch))

    cool_test_checks = [
        "☐ System starts when thermostat calls for cooling",
        "☐ Outdoor unit running (compressor and fan)",
        "☐ Cool air from all registers within 5 minutes",
        "☐ System runs continuously without short-cycling",
        "☐ Temperature drops steadily",
        "☐ All rooms getting cool air",
        "☐ No warm spots in house",
        "☐ Condensate draining properly (check drain)",
        "☐ System reaches setpoint and cycles off properly",
        "☐ No unusual noises from indoor or outdoor unit",
    ]
    story.append(create_checkbox_table(cool_test_checks))
    story.append(PageBreak())

    story.append(Paragraph("<b>Airflow Check - Every Register:</b>", styles['CustomSubHeading']))
    register_check_data = [['Room', 'Airflow Adequate', 'Register Secure', 'Notes']]
    for i in range(20):
        register_check_data.append(['', '☐', '☐', ''])

    story.append(create_data_table(register_check_data, [2.0*inch, 1.2*inch, 1.2*inch, 1.8*inch]))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Thermostat Function:</b>", styles['CustomSubHeading']))
    tstat_checks = [
        "☐ Thermostat displays correctly",
        "☐ Heat mode functions",
        "☐ Cool mode functions",
        "☐ Fan AUTO mode works",
        "☐ Fan ON mode works",
        "☐ Temperature displayed accurately",
        "☐ Program operates correctly (if programmable)",
        "☐ WiFi connected (if smart thermostat)",
    ]
    story.append(create_checkbox_table(tstat_checks))
    story.append(PageBreak())

    # DOORS AND WINDOWS
    story.append(Paragraph("DOORS AND WINDOWS WALKTHROUGH", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Test Every Door:</b>", styles['CustomSubHeading']))
    door_data = [['Door Location', 'Opens/Closes', 'Latches', 'Lock Works', 'No Sticking', 'Weatherstrip OK', 'Notes']]
    for i in range(20):
        door_data.append(['', '☐', '☐', '☐', '☐', '☐', ''])

    story.append(create_data_table(door_data, [1.4*inch, 0.8*inch, 0.6*inch, 0.7*inch, 0.7*inch, 0.9*inch, 0.9*inch]))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Test Every Window:</b>", styles['CustomSubHeading']))
    window_data = [['Window Location', 'Opens/Closes', 'Locks', 'Screen OK', 'No Damage', 'Weatherstrip OK', 'Notes']]
    for i in range(20):
        window_data.append(['', '☐', '☐', '☐', '☐', '☐', ''])

    story.append(create_data_table(window_data, [1.4*inch, 0.8*inch, 0.6*inch, 0.7*inch, 0.7*inch, 0.9*inch, 0.9*inch]))
    story.append(PageBreak())

    # FINAL CHECKS
    story.append(Paragraph("FINAL SYSTEM CHECKS", styles['CustomHeading']))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("<b>Safety Systems:</b>", styles['CustomSubHeading']))
    safety_checks = [
        "☐ All smoke detectors working and interconnected",
        "☐ All CO detectors working",
        "☐ All GFCI outlets working",
        "☐ Fire extinguisher locations identified",
        "☐ Main electrical panel labeled completely",
        "☐ Main water shut-off accessible and labeled",
        "☐ Main gas shut-off accessible and labeled (if gas)",
        "☐ Emergency phone numbers posted",
    ]
    story.append(create_checkbox_table(safety_checks))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Garage:</b>", styles['CustomSubHeading']))
    garage_checks = [
        "☐ Garage door opener works - remote and wall button",
        "☐ Garage door safety sensors working (obstruction test)",
        "☐ Garage door opens and closes smoothly",
        "☐ Garage door emergency release works",
        "☐ Garage lights work",
        "☐ Garage outlets work (GFCI protected)",
        "☐ Garage service door works and locks",
    ]
    story.append(create_checkbox_table(garage_checks))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Miscellaneous:</b>", styles['CustomSubHeading']))
    misc_checks = [
        "☐ Doorbell works (all locations)",
        "☐ Attic access operable",
        "☐ Crawl space access operable (if applicable)",
        "☐ Sump pump operates (if applicable)",
        "☐ Well pump operates (if applicable)",
        "☐ Septic alarm tested (if applicable)",
        "☐ Security system tested (if applicable)",
        "☐ Intercom system tested (if applicable)",
    ]
    story.append(create_checkbox_table(misc_checks))
    story.append(PageBreak())

    # ISSUES LOG
    story.append(Paragraph("ISSUES IDENTIFIED", styles['CustomHeading']))
    story.append(Paragraph("List all issues found during walkthrough for immediate correction:", styles['CustomBody']))
    story.append(Spacer(1, 0.2*inch))

    issues_data = [['#', 'System', 'Location', 'Issue Description', 'Corrected', 'Date Fixed']]
    for i in range(1, 26):
        issues_data.append([str(i), '', '', '', '☐', ''])

    story.append(create_data_table(issues_data, [0.3*inch, 0.9*inch, 1.2*inch, 2.5*inch, 0.6*inch, 0.7*inch]))
    story.append(PageBreak())

    # SIGN-OFF
    story.append(Paragraph("WALKTHROUGH COMPLETION", styles['CustomHeading']))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Walkthrough Summary:</b>", styles['CustomSubHeading']))
    summary_fields = [
        ('Total Items Checked', 'line'),
        ('Issues Found', 'line'),
        ('Issues Corrected', 'line'),
        ('Outstanding Issues', 'line'),
    ]
    story.append(create_field_table(summary_fields))

    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("☐ All systems tested and functioning properly", styles['CheckboxItem']))
    story.append(Paragraph("☐ All identified issues corrected", styles['CheckboxItem']))
    story.append(Paragraph("☐ House ready for final inspection", styles['CheckboxItem']))
    story.append(Paragraph("☐ House ready for occupancy", styles['CheckboxItem']))

    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("<b>Notes/Comments:</b>", styles['CustomSubHeading']))
    for i in range(8):
        story.append(Paragraph("_" * 90, styles['CustomBody']))

    story.append(Spacer(1, 0.3*inch))
    signature_fields = [
        ('Conducted By (Print Name)', 'line'),
        ('Signature', 'line'),
        ('Date', 'line'),
        ('', ''),
        ('Owner/Builder (Print Name)', 'line'),
        ('Signature', 'line'),
        ('Date', 'line'),
    ]
    story.append(create_field_table(signature_fields))

    # Build PDF
    doc.build(story, canvasmaker=lambda *args, **kwargs: NumberedCanvas(*args, section_name='Section 4.4: Final Systems Walkthrough', **kwargs))
    print(f"Created {filename}")
    return filename

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    import os

    # Change to output directory
    output_dir = "/Users/evertith/Repositories/2025/nexarune/buildyourhouse/build-your-house/section-4-output"
    os.chdir(output_dir)

    print("=" * 70)
    print("GENERATING SECTION 4: SYSTEMS INSTALLATION")
    print("=" * 70)
    print()

    files_created = []

    # Create each PDF
    print("Creating 4.1 - Electrical System Completion Log...")
    files_created.append(create_electrical_system_log())
    print()

    print("Creating 4.2 - Plumbing System Completion Log...")
    files_created.append(create_plumbing_system_log())
    print()

    print("Creating 4.3 - HVAC System Completion...")
    files_created.append(create_hvac_system_completion())
    print()

    print("Creating 4.4 - Final Systems Walkthrough...")
    files_created.append(create_final_systems_walkthrough())
    print()

    print("=" * 70)
    print("SECTION 4 GENERATION COMPLETE")
    print("=" * 70)
    print(f"Total files created: {len(files_created)}")
    print(f"Output directory: {output_dir}")
    print()
    print("Files created:")
    for f in files_created:
        filepath = os.path.join(output_dir, f)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f"  - {f} ({size:,} bytes)")
    print()
    print("All PDFs ready for review!")
