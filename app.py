import requests
from djinni_parser import parser as dj_parser
from helpers import check_bot, getNotifiedId, getURLs, notify, setNotifiedId
from dotenv import load_dotenv

load_dotenv()

def app ():
    urls = getURLs()

    resp = requests.get(
        str(urls.get("DJINNI")) , 
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

    if (resp.status_code == 200) :
        djinni_jobs = dj_parser(resp.content.decode())
        
        for k, v in djinni_jobs.items():
            if (k not in getNotifiedId() and notify(v)):
                setNotifiedId(k)
    else :
        print("Request Error")


app()
