from alphasign import Sign, SignType, Text
import time
import yfinance as yf
import pprint

# Open sign
sign = Sign()
sign.open(port="/dev/ttyUSB0")

# Get stock data for select companies
companies = ["AMZN", "GOOGL", "TSLA", "MSFT", "AAPL", "NFLX", "META"]

while True:
    text = ""
    for company in companies:
        try:
            ticker = yf.Ticker(company).info
        except:
            print(f"ERROR FOR {company}")

        if not ticker:
            print(f"CANNOT FIND {company}")

        diff = round(ticker['previousClose'] - ticker['currentPrice'],2)
        price = ticker['currentPrice']
        color = "{{red}}" if diff < 0 else "{{green}}"

        text += f"{{amber}}{company.split('.')[0]} {color}{price} {diff} / "

    print(f"Updating")
    tosend = Text(text[:-2])
    sign.send(tosend.to_packet(label="A", mode=Text.Mode.rotate))
    time.sleep(60)
