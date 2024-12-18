from azure.ai.formrecognizer import FormRecognizerClient 
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.credentials import AzureKeyCredential
import cred

url=cred.url
key=cred.key

frc=FormRecognizerClient(url,AzureKeyCredential(key))
ftc=FormTrainingClient(url,AzureKeyCredential(key))

furl="https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/forms/Form_1.jpg"

res=frc.begin_recognize_content_from_url(furl)
page=res.result()

table=page[0].tables[0]
for cell in table.cells:
    print(cell.text,"-------",cell.confidence)

rurl="https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/receipt/contoso-receipt.png"

res1=frc.begin_recognize_receipts_from_url(rurl)
result=res1.result()

for receipt in result:
    for name , field in receipt.fields.items():
        if name=="Items":
            print()
            print("receipt items:")
            for id,items in enumerate(field.value):
                print()
                print(format(id+1))
                for item_name, item in items.value.items():
                    print(item_name,item.value)