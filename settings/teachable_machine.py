import requests
from bs4 import BeautifulSoup

def run_teachable_machine_prediction(image_url):
    # Make a POST request to the Teachable Machine model's URL
    response = requests.post("https://teachablemachine.withgoogle.com/models/EKNQW_21J/", data={"url": image_url})
    
    # Parse the response and extract the prediction result
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.select_one(".output div").text
    
    return result