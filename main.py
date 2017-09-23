from bs4 import BeautifulSoup
import requests
import pandas as pd
# Downloading page 'http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.WcXQzFuCz3h'
page = requests.get('http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.WcXQzFuCz3h')
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

seven_day = soup.find(id="seven-day-forecast")

forecast_item = seven_day.find_all(class_="tombstone-container")
tonight = forecast_item[0]

# print(tonight.prettify())

# display particular weather condition
# period = tonight.find(class_="period-name").get_text()
# short_desc = tonight.find(class_="short-desc").get_text()
# temp = tonight.find(class_="temp").get_text()
#
# print(period)
# print(short_desc)
# print(temp)
# img = tonight.find("img")
# Extracting title from img tag
# desc = img['title']
#
# print(desc)

# extracting period from p tag 
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
# print(periods)

# extracting title from img tag
forecast_icon_tags = seven_day.select(".tombstone-container img")
desc = [s['title'] for s in forecast_icon_tags]
# print(desc)

# extracting short description
short_desc_tags = seven_day.select(".tombstone-container .short-desc")
short_desc = [sd.get_text() for sd in short_desc_tags]
# print(short_desc)

# extracting temperature
temp_tags = seven_day.select(".tombstone-container .temp")
temps = [t.get_text() for t in temp_tags]
# print(temps)

# storing extracted data in DataFrame
weather = pd.DataFrame({
    "Period": periods,
    "Description": desc,
    "Short_desc": short_desc,
    "Temperature": temps
})


print(weather)
