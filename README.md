# Invoice Automation Platform

## About the Project
This is an automation platform designed to process invoice images and extract meaningful text from them. It automates the entire workflow of detecting new files in a folder, processing the image, extracting key information such as invoice number, seller and client details, and saving the results to a CSV file.

## Process Flow
1. **File Detection**: The platform continuously monitors the `images` folder for new image files.
2. **Image Processing**: When a new image is detected, it preprocesses the image using OpenCV techniques.
3. **Text Extraction**: It extracts the text from the image using EasyOCR.
4. **Data Extraction**: Relevant data is extracted using regular expressions (regex) and Named Entity Recognition (NER).
5. **Data Storage**: The extracted information is structured and saved to a CSV file for future analysis.
   
This flow runs automatically once the system detects a new file in the `images` folder.

## Libraries Used

1. **Create a Conda Environment**
   ```bash
   conda create --name invoice_automation python=3.10
   conda activate invoice_automation
   ```
2. **Install Required Libraries**
    ```bash
    conda install watchdog pillow opencv
    pip install easyocr torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
    ```
3. **Optional for CUDA 12.4 Support (for GPU acceleration)**
    ```bash
    Make sure CUDA 12.4 and cuDNN are set up properly on your system.
    ```

## Made By
[Ramanuj Darvekar]