import requests

def currency_converter(from_code, to_code, amount):  
    url = f"https://api.exchangerate-api.com/v4/latest/{from_code}"

    try:
        response = requests.get(url)
        data = response.json()
    except requests.exceptions.ConnectionError:
        print("Check internet connection.") 
        return

    if "error" in data:
        print("Invalid base currency code:", from_code)
        return

    rates = data.get("rates", {})

    if to_code not in rates:
        print("Invalid target currency code:", to_code)
        return

    result = amount * rates[to_code]
    print(f"\n{amount} {from_code} = {result:.2f} {to_code}")


def display_menu():
    print("\nWELCOME TO CURRENCY CONVERTER")
    print("-------------------------------------------------------------")


def main():
    while True:
        display_menu()

        amount_str = input("Enter amount to convert: ")
        try:
            amount = float(amount_str)
        except ValueError:
            print("Please enter a valid number.")
            continue

        from_code = input("Convert FROM (e.g., USD, INR, AED): ").strip().upper()
        to_code = input("Convert TO (e.g., USD, INR, EUR): ").strip().upper()

        currency_converter(from_code, to_code, amount)

        choice = input("\nType STOP to exit, or press Enter to continue: ").upper().strip()
        if choice == "STOP":
            print("\nThank You For Using Currency Converter :)\n")
            break

main()
