from cbrf.models import DailyCurrenciesRates


# Function to get the dollar rate from the CBRF
def get_course() -> float:
    daily = DailyCurrenciesRates()
    currency = 'R01235'  # The currency code of the US dollar by https://www.cbr.ru/scripts/XML_val.asp?d=0
    return daily.get_by_id(currency).value
