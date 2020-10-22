import requests
from bs4 import BeautifulSoup as soup

def main() -> str:
    userInput = str(input("👉 Enter the url of TED Talks (available at: https://www.ted.com/talks): ")).replace(" ", "").replace("\n", "")

    if "/transcript" not in userInput:
        userInput = userInput + "/transcript"
    
    request = requests.get(userInput).content
    soup_element = soup(request, "html.parser")

    transcript = soup_element.findAll("p")

    results = ""
    for texts in transcript:
        results += texts.text.replace("\t", "")

    return results


if __name__ == "__main__":
    print(main())
