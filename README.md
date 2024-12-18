# Azure-Form-Recognizer-Extract-Text-and-Tables

## Description

This Python script uses the **Azure Cognitive Services Computer Vision API** to use the Azure Form Recognizer SDK to extract text and tables from images. It includes examples of analyzing forms and receipts using Azure Cognitive Services.
## Setup Instructions

1. **Install Dependencies**:
   Install the required Python libraries by running:
   ```bash
   pip install azure-ai-formrecognizer azure-core
   ```

2. **Create `cred.py` File**:
   In your project directory, create a file called `cred.py` and store your Azure **API key** and **Endpoint URL** there.
   ```python
   # cred.py
   url = "your-azure-endpoint-url"
   key = "your-azure-api-key"
   ```

3. **Modify the Image URL**:
   Change the furl and rurl variables in the script to the URLs of the images you want to analyze. The URLs can point to publicly accessible images or hosted image files:
   ```python
  furl = "https://example.com/your-form-image.jpg"  # Replace with your form image URL
  rurl = "https://example.com/your-receipt-image.png"  # Replace with your receipt image URL
   ```

5. **Run the Script**:
   After setting up `cred.py` and modifying the image URL, run the Python script:
   ```bash
   python main.py
   ```

## Notes

- Ensure that your image URLs point to publicly accessible resources or use the appropriate authentication to access private URLs.
-The script currently supports extracting tables and receipt data from form and receipt images.
