import requests
import openpyxl
# Open the Excel file
workbook = openpyxl.load_workbook('Copy of GreenlandGlacierNames_GGNv01.xlsx')
sheet = workbook.active
# Iterate through the rows in the Excel sheet
for row in sheet.iter_rows(min_row=2, values_only=True):
    latitude = row[3]
    longitude = row[4]
    # Perform reverse geocoding using OpenCage Geocoder API
    api_key = '0142f29790574c8bafe57c17de8b2620'
    url = f'https://api.opencagedata.com/geocode/v1/json?key={api_key}&q={latitude}+{longitude}&pretty=1'
    response = requests.get(url)
    data = response.json()
    if len(data['results']) > 0:
        result = data['results'][0]
        formatted_address = result['formatted']
        # Update the Excel sheet with the geographical name
        #row[5] = formatted_address
# Save the updated Excel file
workbook.save('updated_file.xlsx')










