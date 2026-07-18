# this task is to create a stock portfolio management system that allows users to track their investments, view stock prices, and analyze their portfolio performance. The system will include features such as adding and removing stocks, viewing current stock prices, calculating portfolio value, and generating performance reports.

stock_prices ={
    "AAPL": 150.00,
    "GOOGL": 2800.00,
    "MSFT": 300.00,
    "TSLA": 700.00,
    "AMZN": 3500.00,
    "FB": 350.00
}
stock = input("Enter stock name: ")
quantity = int(input("Enter quantity: "))

print("Welcome to the Stock Portfolio Management System!")

price = stock_prices[stock]

Total_investment = price * quantity

print("Your total investment is: $", Total_investment)


      