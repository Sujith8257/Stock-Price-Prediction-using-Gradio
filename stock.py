import gradio as gr
import pandas as pd
import plotly.graph_objects as go
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
import yfinance as yf
import numpy as np

# Alpha Vantage API Key
API_KEY = "MBN5XNLN7PKDNLRZ"

def get_stock_symbol(company_name):
    try:
        search = yf.Ticker(company_name)
        return search.info.get("symbol", company_name), search.info.get("longName", company_name)
    except Exception:
        return company_name, company_name

def get_stock_data(ticker, exchange):
    try:
        ticker, company_name = get_stock_symbol(ticker)
        if exchange == "NSE":
            ticker = f"{ticker}.NS"
        elif exchange == "BSE":
            ticker = f"{ticker}.BO"
        ts = TimeSeries(key=API_KEY, output_format='pandas')
        data, _ = ts.get_intraday(symbol=ticker, interval='5min', outputsize='compact')
        data.rename(columns={
            '1. open': 'Open',
            '2. high': 'High',
            '3. low': 'Low',
            '4. close': 'Close',
            '5. volume': 'Volume'
        }, inplace=True)
        data.index = pd.to_datetime(data.index)
        data.sort_index(inplace=True)
        return data, ticker, company_name
    except Exception:
        return None, None, None

def get_exchange_rate(currency):
    if currency == "INR":
        try:
            fx = ForeignExchange(key=API_KEY)
            data, _ = fx.get_currency_exchange_rate(from_currency="USD", to_currency="INR")
            return float(data["5. Exchange Rate"])
        except Exception:
            return None
    return 1

def generate_chart(data, currency, exchange_rate):
    if currency == "INR":
        data[['Open', 'High', 'Low', 'Close']] *= exchange_rate
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name=f'Candlestick ({currency})'
    ))
    fig.update_layout(title="Stock Price Chart", xaxis_title="Date", yaxis_title=f"Price ({currency})")
    return fig

def detect_outliers(data):
    close_prices = data["Close"]
    z_scores = (close_prices - close_prices.mean()) / close_prices.std()
    outliers = data[np.abs(z_scores) > 2]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=close_prices, mode="lines", name="Close Price"))
    fig.add_trace(go.Scatter(x=outliers.index, y=outliers["Close"], mode="markers",
                             name="Outliers", marker=dict(color="red", size=8)))
    fig.update_layout(title="Outlier Detection in Stock Prices", xaxis_title="Date", yaxis_title="Close Price")
    return fig

def stock_prediction(ticker, exchange, currency):
    data, resolved_ticker, company_name = get_stock_data(ticker, exchange)
    if data is None or data.empty:
        return None, None, "⚠ Failed to fetch data. Check the stock symbol or company name.", ""
    exchange_rate = get_exchange_rate(currency)
    if exchange_rate is None:
        return None, None, "⚠ Failed to fetch exchange rate. Try again later.", ""
    chart = generate_chart(data.copy(), currency, exchange_rate)
    outlier_chart = detect_outliers(data.copy())
    latest_price = data['Close'].iloc[-1] * exchange_rate
    lowest_price = data['Low'].min() * exchange_rate
    highest_price = data['High'].max() * exchange_rate
    last_3_prices = data['Close'].iloc[-3:] * exchange_rate
    if last_3_prices.is_monotonic_increasing:
        trend = "📈 Buy"
        reason = "The stock price has been rising steadily, indicating a bullish trend."
    elif last_3_prices.is_monotonic_decreasing:
        trend = "📉 Sell"
        reason = "The stock price is falling consistently, indicating a bearish trend."
    else:
        trend = "⏳ Hold"
        reason = "The stock price is fluctuating without a clear trend, suggesting stability."
    currency_symbol = "₹" if currency == "INR" else "$"
    result_text = (
        f"🏷 *Company Name:* {company_name}\n"
        f"📌 *Latest Price for {resolved_ticker}:* {currency_symbol}{latest_price:.2f}\n"
        f"📉 *Day's Lowest Price:* {currency_symbol}{lowest_price:.2f}\n"
        f"📈 *Day's Highest Price:* {currency_symbol}{highest_price:.2f}\n"
        f"🔍 *Recommendation:* {trend}\n"
        f"💡 *Reason:* {reason}"
    )
    rate_info = f"🔄 1 USD = ₹{exchange_rate:.2f}" if currency == "INR" else "No conversion applied (Currency in USD)"
    return chart, outlier_chart, result_text, rate_info

def currency_conversion_general(from_currency, to_currency, amount):
    try:
        fx = ForeignExchange(key=API_KEY)
        data, _ = fx.get_currency_exchange_rate(from_currency=from_currency, to_currency=to_currency)
        rate = float(data["5. Exchange Rate"])
        converted = rate * amount
        return f"💱 {amount:.2f} {from_currency} = {converted:.2f} {to_currency} (Rate: {rate:.4f})"
    except Exception:
        return "⚠ Unable to fetch currency conversion rate."

with gr.Blocks() as app:
    gr.Markdown("""# 📊 Stock Price Prediction with Insights
Enter a stock/company name, optionally choose an exchange (NSE/BSE) and currency (INR/USD) to get charts, outliers, price insights, and recommendations.
""")
    with gr.Row():
        ticker_input = gr.Textbox(label="Enter Stock Symbol or Company Name (e.g., AAPL, Reliance, Infosys)")
        exchange_input = gr.Radio(["None", "NSE", "BSE"], label="Select Exchange (Optional)", value="None")
        currency_input = gr.Radio(["USD", "INR"], label="Select Currency", value="USD")
    submit_btn = gr.Button("🔍 Analyze", variant="primary")
    chart_output = gr.Plot(label="📈 Stock Candlestick Chart")
    outlier_output = gr.Plot(label="🔍 Outlier Detection Graph")
    analysis_output = gr.Textbox(label="📊 Stock Analysis and Recommendation")
    conversion_output = gr.Textbox(label="💱 Currency Conversion Info")

    submit_btn.click(fn=stock_prediction,
                     inputs=[ticker_input, exchange_input, currency_input],
                     outputs=[chart_output, outlier_output, analysis_output, conversion_output])

    gr.Markdown("""---""")
    gr.Markdown("""### 💱 Currency Converter""")
    with gr.Row():
        from_curr = gr.Dropdown(["USD", "INR", "EUR", "GBP", "JPY"], label="From Currency", value="USD")
        to_curr = gr.Dropdown(["USD", "INR", "EUR", "GBP", "JPY"], label="To Currency", value="INR")
        amount = gr.Number(label="Amount", value=1.0)
    convert_btn = gr.Button("Convert", variant="secondary")
    conversion_text = gr.Textbox(label="Conversion Result")
    convert_btn.click(fn=currency_conversion_general, inputs=[from_curr, to_curr, amount], outputs=conversion_text)

app.launch(share=True)