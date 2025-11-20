# Live Currency Converter (Python)

This is a simple Python program that converts an amount from one currency to another using **live exchange rates**.  
It uses the ExchangeRate API to fetch real-time currency data and displays the converted value in the terminal.

This project is made for the VITyarthi flipped course requirement.

---

## Features

- Convert money from one currency to another (e.g., USD → INR, INR → EUR)
- Uses **live online exchange rates**
- Validates:
  - Numeric amount
  - Currency codes (e.g., INR, USD, EUR, JPY)
- Handles errors:
  - Wrong amount
  - Wrong currency code
  - No internet connection
- Simple and clean command-line interface

---

## Project Structure

Since this project is small, all logic is inside a **single Python file**:


No extra folders or modules are required.

---

## Requirements

Install the only required library:


pip install requests

python version-python 3.8+

## How to Run

Run the program in your terminal / command prompt:

python currency_converter.py


### You will be asked to enter:

Amount

Currency code to convert from

Currency code to convert to

Example:

Enter amount to convert: 100
Convert FROM (e.g., USD, INR, AED): INR
Convert TO (e.g., USD, INR, EUR): USD


And the output will be like:

100.0 INR = 1.20 USD

## How It Works (Simple Explanation)

You enter an amount and two currency codes.

The program sends a request to:

https://api.exchangerate-api.com/v4/latest/<base_currency>


It receives a list of exchange rates.

It calculates:

converted_amount = amount * rate


It prints the converted value.

   Error Handling

The program safely handles:

1.Non-numeric amounts

2.Currency codes that don’t exist

3.Internet not working

4.API not responding

So it never crashes unexpectedly.



## Author

Vedha
VIT Bhopal University
VITyarthi – Build Your Own Project