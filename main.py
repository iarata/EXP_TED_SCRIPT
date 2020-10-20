import requests
from bs4 import BeautifulSoup as soup


client = requests.get("https://www.ted.com/talks/greg_gage_how_to_control_someone_else_s_arm_with_your_brain/transcript?language=en").content 
psClient = soup(client, "html.parser")

transcript = psClient.findAll("p")


cleanedData = ""
for item in transcript:
    cleanedData += item.text.replace('\t','')

print(cleanedData)
