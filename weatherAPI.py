import requests

# Define your API key
api_key = '3af3a486-a9ad-4f33-9714-3cece9681aba'

# Latitude and longitude of the location you're interested in
latitude = '50.7179'  # Example latitude (London)
longitude = '-3.5327'  # Example longitude (London)

#print(f"this is the api key:{api_key}")
#print(f"this is the lat:{latitude}")
#print(f"this is the long:{longitude}")

# Construct the API request URL with latitude, longitude, and format specified as XML
#url = f'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/xml?res=daily&key={api_key}&lat={latitude}&lon={longitude}'

# Construct the API request URL with format specified as XML
url = f'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/xml/sitelist?&key={api_key}&output=xml'

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the XML response
    xml_data = response.text
    
    # Output the XML response to a file
    with open('sitelist.xml', 'w') as f:
        f.write(xml_data)

    print("Data written to sitelist.xml successfully.")
else:
    print("Error:", response.status_code)
