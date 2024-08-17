import pandas as pd
import os

# Function to structure and save extracted data to CSV in append mode
def save_data(extracted_entities, image_id, output_dir="output", output_file="invoice_data.csv"):
    # Create a directory for output if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize a list to store the structured invoice data
    invoice_details = []

    # Structure the extracted data into a dictionary
    invoice_details.append({
        "Invoice Number": extracted_entities.get("Invoice Number", ""),
        "Date of Issue": extracted_entities.get("Date of Issue", ""),
        "Seller Address": extracted_entities.get("Seller Address", ""),
        "Seller Tax ID": extracted_entities.get("Seller Tax ID", ""),
        "Client Address": extracted_entities.get("Client Address", ""),
        "Client Tax ID": extracted_entities.get("Client Tax ID", "")
        # "Gross Worth": extracted_entities.get("Gross Worth", "")
    })
    
    # Convert the extracted data into a DataFrame
    invoice_df = pd.DataFrame(invoice_details)
    
    # Define the full path for CSV file
    output_path = os.path.join(output_dir, output_file)
    
    # Save the DataFrame to a CSV file in append mode
    invoice_df.to_csv(output_path, mode='a', header=not os.path.exists(output_path), index=False)
    
    print(f"Data appended successfully to {output_path} for {image_id}")

# Example usage (assuming extracted_entities is available from NER step)
if __name__ == "__main__":
    extracted_entities = {
        "Invoice Number": "49565075",
        "Date of Issue": "10/28/2019",
        "Seller Address": "Kane-Morgan 968 Carr Mission Apt: 320 Bernardville, VA 28211",
        "Seller Tax ID": "964-95-3813",
        "Client Address": "Garcia Inc 445 Haas Viaduct Suite 454 Michaelhaven, LA 32852",
        "Client Tax ID": "909-75-5482",
        "Gross Worth": "96.73"
    }
    
    save_data(extracted_entities)
