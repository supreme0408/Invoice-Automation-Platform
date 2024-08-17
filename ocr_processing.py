# import os
# os.environ['USE_TORCH'] = '1'
# os.environ['USE_TF'] = '1'
# import easyocr
import cv2

# Initialize the EasyOCR reader
# reader = easyocr.Reader(['en'])

# Preprocess the image for better OCR results
def preprocess_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Step 1: Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2: Apply a Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Step 3: Binarize the image (convert to black and white)
    _, binary_image = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)

    # Optional: Save the preprocessed image for debugging purposes
    preprocessed_image_path = image_path.replace('images/', 'output/').replace('.jpg', '_preprocessed.jpg')
    cv2.imwrite(preprocessed_image_path, binary_image)

    return preprocessed_image_path

# Function to extract text using EasyOCR
def extract_text_easyocr(image_path,reader):
    # preprocessed_image = preprocess_image(image_path)
    # Perform OCR using EasyOCR
    result = reader.readtext(image_path)

    # Extract the recognized text from the result
    extracted_text = ' '.join([text for (_, text, _) in result])
    return extracted_text

# OCR function to extract text from the preprocessed image
def extract_text_segment_easyocr(image_path,reader):
    preprocessed_image = preprocess_image(image_path)
    # Segment the invoice image
    invoice_section, seller_section, client_section, summary_section = segment_invoice(preprocessed_image)

    # Extract text from each segment
    invoice_text = extract_text_easyocr(invoice_section, reader)
    seller_text = extract_text_easyocr(seller_section, reader)
    client_text = extract_text_easyocr(client_section, reader)
    summary_text = extract_text_easyocr(summary_section, reader)

    segmented_text = {
    'Invoice Section': invoice_text,  # Text from the invoice section
    'Seller Section': seller_text,    # Text from the seller section
    'Client Section': client_text,    # Text from the client section
    'Summary Section': summary_text   # Text from the summary section
    }

    return segmented_text

# Segment the invoice into specific sections
def segment_invoice(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Top 20% for invoice number and date of issue
    invoice_section = image[:int(0.2 * height), :]

    # 20%-30% height for seller and client info
    seller_section = image[int(0.2 * height):int(0.3 * height), :int(0.5 * width)]
    client_section = image[int(0.2 * height):int(0.3 * height), int(0.5 * width):]

    # Last 60% for summary info
    summary_section = image[int(0.4 * height):, :]

    return invoice_section, seller_section, client_section, summary_section

# Example usage (can be integrated with the file monitoring script)
if __name__ == "__main__":
    image_path = "images/image3.jpg"  # Replace with an actual image
    preprocessed_image = preprocess_image(image_path)
    # extracted_text = extract_text_easyocr(preprocessed_image)
    extracted_text = extract_text_segment_easyocr(preprocessed_image,reader)
    
    print("Extracted Text:")
    print(extracted_text)