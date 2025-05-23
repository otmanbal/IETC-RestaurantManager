from fpdf import FPDF
from models.finance_manager import load_finances
from datetime import datetime

def export_financial_report_pdf(filename="financial_report.pdf"):
    finances = load_finances()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Financial Report", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Date: {datetime.now().strftime('%Y-%m-%d')}", ln=True, align='C')
    pdf.ln(10)

    for entry in finances:
        line = f"{entry['date']} - {entry['type'].capitalize()} - {entry['description']} - ${entry['amount']:.2f}"
        pdf.cell(200, 10, txt=line, ln=True)

    pdf.output(filename)
