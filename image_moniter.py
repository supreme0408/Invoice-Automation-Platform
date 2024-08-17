import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import easyocr

import threading
import queue

import ocr_processing
import ner_processing
import data_saving

import os
os.environ['USE_TORCH'] = '1'
# os.environ['USE_TF'] = '1'

# Define the folder to watch
IMAGE_FOLDER = 'images/'

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

# Queue to manage files
file_queue = queue.Queue()

# Handler for detecting new files
class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Wait for 1 second to make sure the file is fully copied
        time.sleep(1)
        if event.is_directory:
            return
        if event.src_path.endswith((".png", ".jpg", ".jpeg")):
            # Add new images to the queue
            print(f"New image detected {event.src_path}")
            file_queue.put(event.src_path)

def process_images():
    while True:
        if not file_queue.empty():
            image_path = file_queue.get()
            print(f"Processing image: {image_path}")
            # Call your OCR and processing functions here
            process_image(image_path)
        time.sleep(1)

# Function to process image (stub for now, will fill later)
def process_image(image_path):
    # print(f"Processing image: {image_path}")
    # Placeholder for OCR and NER functions
    extracted_text = ocr_processing.extract_text_segment_easyocr(image_path,reader)
    # print(f"Extracted Text from Image\n")
    extracted_data = ner_processing.extract_ner(extracted_text)
    # print(f"Extracted Data\n")
    data_saving.save_data(extracted_data,image_id=image_path)

if __name__ == "__main__":
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, path=IMAGE_FOLDER, recursive=False)
    
    # Start a background thread to process images
    processing_thread = threading.Thread(target=process_images)
    processing_thread.start()
    
    # Start monitoring
    print(f"Monitoring folder: {IMAGE_FOLDER}")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
