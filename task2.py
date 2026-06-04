# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 150
}

total_investment = 0

print("Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

n = int(input("Enter the number of stocks you own: "))

portfolio_details = []

for i in range(n):
    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        portfolio_details.append(
            f"{stock} - Quantity: {quantity}, Value: ${investment}"
        )

    else:
        print("Stock not found!")

print("\nPortfolio Summary")
for item in portfolio_details:
    print(item)

print(f"\nTotal Investment Value: ${total_investment}")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")

    for item in portfolio_details:
        file.write(item + "\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio saved to 'portfolio.txt'")
