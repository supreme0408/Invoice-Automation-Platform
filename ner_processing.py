import re

def extract_ner(segmented_text):
    # Dictionary to store extracted entities
    extracted_entities = {}

    # Invoice Section extraction
    invoice_section = segmented_text.get('Invoice Section', '')
    invoice_no_match = re.search(r'Invoice no: (\d+)', invoice_section)
    date_issue_match = re.search(r'Date of issue: (\d{2}/\d{2}/\d{4})', invoice_section)
    
    if invoice_no_match:
        extracted_entities['Invoice Number'] = invoice_no_match.group(1)
    
    if date_issue_match:
        extracted_entities['Date of Issue'] = date_issue_match.group(1)

    # Seller Section extraction
    seller_section = segmented_text.get('Seller Section', '')
    seller_address_match = re.search(r'([\w\s-]+ \d+ \w+ [\w\s]+ \w+,\s\w+\s\d+)', seller_section)
    seller_tax_id_match = re.search(r'Tax Id: (\d{3}-\d{2}-\d{4})', seller_section)
    
    if seller_address_match:
        extracted_entities['Seller Address'] = seller_address_match.group(1)
    
    if seller_tax_id_match:
        extracted_entities['Seller Tax ID'] = seller_tax_id_match.group(1)

    # Client Section extraction
    client_section = segmented_text.get('Client Section', '')
    client_address_match = re.search(r'([\w\s-]+ \d+ [\w\s]+ \w+,\s\w+\s\d+)', client_section)
    client_tax_id_match = re.search(r'Tax Id: (\d{3}-\d{2}-\d{4})', client_section)
    
    if client_address_match:
        extracted_entities['Client Address'] = client_address_match.group(1)
    
    if client_tax_id_match:
        extracted_entities['Client Tax ID'] = client_tax_id_match.group(1)

    # Summary Section extraction
    summary_section = segmented_text.get('Summary Section', '')
    gross_worth_match = re.search(r'Total\s+\$\s?([\d,]+\.\d{2})', summary_section)
    
    # if gross_worth_match:
    #     extracted_entities['Gross Worth'] = gross_worth_match.group(1)

    return extracted_entities

# Example usage for testing
if __name__ == "__main__":
    test_text = """
    Invoice no: 40378170
    Date of issue: 10/15/2012

    Seller: Patel, Thompson and Montgomery
    Client: Jackson, Odonnell and Jackson
    356 Kyle Vista 267 John Track Suite 841
    New James, MA 46228 Jenniferville, PA 98601

    ITEMS
    No. Description Qty UM Net price Net worth VAT [%] Gross worth
    1. Leed's Wine Companion Bottle 1,00 each 7,50 7,50 10% 8,25

    SUMMARY
    VAT [%] Net worth VAT Gross worth
    10% 7,50 0,75 8,25

    Total $ 7,50 $ 0,75 $ 8,25
    """
    
    extracted_data = extract_ner(test_text)
    print("Extracted Data:")
    print(extracted_data)
