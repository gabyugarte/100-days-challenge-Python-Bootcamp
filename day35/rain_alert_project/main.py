import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key= "cc5a1d62fd55d167357c88a8dc585001"
# This data is from TWILIO Page: https://console.twilio.com/
account_sid = "ACe4fb998f5c07299ac7504bcd23f757d4"
auth_token = "a11def1780a2ef5689982d06b5d5dfde"
#I got my API KEY from this page, login in : https://home.openweathermap.org/users/sign_in
weather_params = {
    "lat":41.387920,
    "lon":2.169920,
    "appid": api_key,
    "cnt": 4,
}
# We get LAT and LON from this page: https://www.latlong.net/
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        # print("Bring an unbrella")
        will_rain = True
        
if will_rain:
    # print("Bring an unbrella")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="Gabicita, It`s going to rain today. Remember to bring an ☔",
    from_="+13345090685",
    to="+34640102075"
    )
    print(message.status)
    

