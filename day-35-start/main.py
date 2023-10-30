import requests
import smtplib

my_email = "muawan541@gmail.com"
password = "yrpd eawr mydz enqd"

api_key= "2177a6835743011426b079980e04ba27"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "lat": 33.241505,
    "lon": -25.221245,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
condition_code = weather_data["weather"][0]["id"]
print(condition_code)
if condition_code < 700:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs= "heyyymuhammad@gmail.com",
            msg=f"Subject: Bring an Umbrella\nThis email is sent by Muhammad to notify you that it is raining. Please bring an Umbrella with you.\nThank you."
        )


