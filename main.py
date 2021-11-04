import requests
from bs4 import BeautifulSoup


# Function for fetching all urls and corresponding status codes


def geturls():
    urls = 'https://gamanza.com/'
    batch = requests.get(urls)
    magic = BeautifulSoup(batch.text, 'html.parser')

    # Open a file to save urls and status codes for later use.
    # "With open" would be a better use here.

    f = open("urls.txt", "w")

    for url in magic.find_all("a"):
        data = url.get('href')
        status_code = batch.status_code
        f.write(data + " ")
        f.write(str(status_code))
        f.write("\n")
    f.close()
    print("URLs gathered in urls.txt")


# Function for fetching urls from file and check their
# statuses. If status is not 200, statement will printed with status code and url.
# TODO add check if file already exists, only add non-existent url to file.


def checkstatus():
    status200 = " 200"
    f = open("urls.txt", "r")

    for line in f:
        if line.startswith("https://") or line.startswith("http://"):
            if status200 in line:
                continue
            else:
                print(line + "\n")
                print("URL status not ok, check status")
    print("All statuses checked")


geturls()
checkstatus()
