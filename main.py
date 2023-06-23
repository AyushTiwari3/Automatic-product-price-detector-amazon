import requests
from bs4 import BeautifulSoup
import smtplib
import lxml
URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
USER_AGENT="Find through http tracker"
ACCEPT_LANG="en-US,en;q=0.9"
MY_EMAIL = "your mail"
MY_PASSWORD = "your pass"
parmas={
    "encode":"UTF-8"
}

headers={
    "User-Agent": USER_AGENT  ,
    "Accept-Language":ACCEPT_LANG
}

response=requests.get(url=URL,headers=headers)
html_info=response.text

soup=BeautifulSoup(html_info,"lxml")
price=soup.find(name="span",class_="a-price-whole")
final_price=float(price.text)

if final_price<100:
    with smtplib.SMTP_SSL("smtp.googlemail.com") as connection:
        # connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD,)
        connection.sendmail(
            
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            
            msg=f"Subject: Amazon Price Alert\n\nInstant Pot Duo Plus 9 in 1 Electric Pressure Cooker,Slow Cooker,Rice Cooker,Steamer,Saute, Yogurt Maker, Warmer & Sterilizer, Includes Free App with over 1900 Recipes, Stainless Steel, 3 Quart {URL}"
            
        )
