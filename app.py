import pyshorteners

API_Key='829afb0b11e8f67893815a8b8535a985f4768a67'
print("\nURL Shortener")

long_URL=input("\nEnter Long URL: ")

try:
    url_Shortener=pyshorteners.Shortener(api_key=API_Key)

    short_URL = url_Shortener.bitly.short(long_URL)

    print("\nShort URL:"+short_URL)

except:
    print("\nSomething Went Worng! Try Again")    