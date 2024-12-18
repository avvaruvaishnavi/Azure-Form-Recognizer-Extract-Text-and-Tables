Azure-Form-Recognizer-Extract-Text-and-Tables
This Python script demonstrates how to use the Azure Form Recognizer SDK to extract text and tables from images. It includes examples of analyzing forms and receipts using Azure Cognitive Services.

Description
The script utilizes the Azure Form Recognizer service to extract structured data from various documents, including forms and receipts. It connects to Azure Cognitive Services and processes the image URLs to retrieve text, tables, and other relevant data.

Setup Instructions
1. Install Dependencies
Install the required Python libraries by running:

bash
Copy code
pip install azure-ai-formrecognizer azure-core
2. Create cred.py File
In your project directory, create a file called cred.py and store your Azure API key and Endpoint URL there:

python
Copy code
# cred.py
url = "your-azure-endpoint-url"
key = "your-azure-api-key"
3. Modify the Image URLs
Change the furl and rurl variables in the script to the URLs of the images you want to analyze. The URLs can point to publicly accessible images or hosted image files:

python
Copy code
furl = "https://example.com/your-form-image.jpg"  # Replace with your form image URL
rurl = "https://example.com/your-receipt-image.png"  # Replace with your receipt image URL
4. Run the Script
After setting up cred.py and modifying the image URLs, run the Python script:

bash
Copy code
python main.py
Example Outputs
The script will extract data such as:

Form Data: Extracted tables from forms.
Receipt Data: Itemized list from receipts, including names, quantities, and prices.
For example, the script will print the extracted table cells and receipt items in the terminal, along with their respective confidence levels.

Notes
Ensure that your image URLs point to publicly accessible resources or use the appropriate authentication to access private URLs.
The script currently supports extracting tables and receipt data from form and receipt images.
If no brands or relevant fields are found, the script will print "No data found" accordingly.
