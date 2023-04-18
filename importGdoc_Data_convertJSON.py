import json
import openai_secret_manager

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Use openai_secret_manager to get the credentials for the Google Sheets API
secrets = openai_secret_manager.get_secrets("google")

# Use the credentials to authenticate with the Google Sheets API
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(secrets, scope)
client = gspread.authorize(creds)

# Open the Google Sheet by its title
sheet = client.open("Sheet1").sheet1

# Get all the data from the sheet as a list of lists
data = sheet.get_all_values()

# Convert the data into a JSON object
json_data = json.dumps(data)

# Print the JSON object
print(json_data)



#This script uses the gspread library to interact with the Google Sheets API and the openai_secret_manager library to securely retrieve the API credentials. It also uses json library to convert the data into json object.

#You'll need to replace "Sheet1" with the actual name of your sheet.

#You'll also need to install the gspread, oauth2client, openai_secret_manager library by running !pip install gspread oauth2client openai_secret_manager and also need to create a project and credentials in google cloud platform to get the credentials and add the credentials in openai secret manager.