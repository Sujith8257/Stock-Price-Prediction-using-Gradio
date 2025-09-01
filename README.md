# 📊 Stock Price Prediction with Insights

A comprehensive stock analysis application built with Gradio that provides real-time stock data, price predictions, outlier detection, and currency conversion capabilities.

## 🚀 Features

### 📈 Stock Analysis
- **Real-time Stock Data**: Fetch live stock prices using Yahoo Finance API
- **Multi-Exchange Support**: Support for NSE (National Stock Exchange) and BSE (Bombay Stock Exchange)
- **Interactive Charts**: Candlestick charts with Plotly for visual analysis
- **Outlier Detection**: Identify unusual price movements using statistical analysis
- **Trend Analysis**: Automated buy/sell/hold recommendations based on price trends

### 💱 Currency Conversion
- **Multi-Currency Support**: USD, INR, EUR, GBP, JPY
- **Real-time Exchange Rates**: Powered by Alpha Vantage API
- **Integrated Conversion**: View stock prices in your preferred currency

### 🎯 Smart Recommendations
- **Trend Analysis**: Analyzes last 3 price points for trend direction
- **Price Insights**: Shows day's highest, lowest, and current prices
- **Actionable Advice**: Provides buy/sell/hold recommendations with reasoning

## 🛠️ Technology Stack

- **Frontend**: Gradio (Python web framework)
- **Data Source**: Yahoo Finance API (yfinance)
- **Currency API**: Alpha Vantage Foreign Exchange
- **Charts**: Plotly Graph Objects
- **Data Processing**: Pandas, NumPy
- **GPU Acceleration**: PyTorch (CUDA support)

## 🔧 Tools & Frameworks

### 🤖 Machine Learning & Deep Learning
- **PyTorch**: Primary deep learning framework for GPU acceleration and tensor operations
- **TensorFlow**: Alternative ML framework (can be integrated for additional models)
- **NumPy**: Numerical computing and array operations
- **Pandas**: Data manipulation and analysis

### 📊 Data Visualization & Analysis
- **Plotly**: Interactive charts and graphs (candlestick charts, outlier detection)
- **Matplotlib**: Additional plotting capabilities (if needed)
- **Seaborn**: Statistical data visualization

### 🌐 Web Development & APIs
- **Gradio**: Web interface framework for ML applications
- **Requests**: HTTP library for API calls
- **yfinance**: Yahoo Finance API wrapper
- **Alpha Vantage**: Financial data API

### 🚀 Performance & Optimization
- **CUDA**: GPU acceleration for PyTorch operations
- **JIT Compilation**: PyTorch's just-in-time compilation for optimized performance
- **Memory Management**: Efficient tensor operations and GPU memory handling

### 📦 Additional Libraries
- **os**: Operating system interface
- **datetime**: Date and time handling
- **json**: JSON data processing

## 📋 Prerequisites

Before running this application, ensure you have:

- Python 3.7 or higher
- CUDA-compatible GPU (optional, for enhanced performance)
- Internet connection for API calls
- Alpha Vantage API key (free tier available)

## 🔧 Installation

1. **Clone or download the project files**

2. **Install required dependencies**:
   ```bash
   pip install gradio pandas plotly yfinance numpy alpha-vantage requests torch
   ```

3. **API Key Setup**:
   - Get a free API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
   - The application includes a default API key for testing purposes
   - For production use, replace the API key in the code with your own

## 🚀 Usage

### Running the Application

1. **Start the application**:
   ```bash
   python stock.py
   ```

2. **Access the web interface**:
   - The application will launch locally (usually at `http://localhost:7860`)
   - A public shareable link will also be generated

### How to Use

#### 📊 Stock Analysis
1. **Enter Stock Symbol**: Type the stock symbol or company name
   - Examples: `AAPL`, `MSFT`, `Reliance`, `Infosys`
2. **Select Exchange** (Optional):
   - `None`: Default (US stocks)
   - `NSE`: National Stock Exchange (India)
   - `BSE`: Bombay Stock Exchange (India)
3. **Choose Currency**: USD or INR
4. **Click "Analyze"**: Get comprehensive analysis

#### 💱 Currency Converter
1. **Select Source Currency**: Choose the currency you're converting from
2. **Select Target Currency**: Choose the currency you're converting to
3. **Enter Amount**: Input the amount to convert
4. **Click "Convert"**: Get real-time conversion rate and result

## 📊 Understanding the Output

### Stock Analysis Results
- **Company Name**: Full company name from Yahoo Finance
- **Latest Price**: Current stock price in selected currency
- **Day's Range**: Highest and lowest prices for the day
- **Recommendation**: Buy/Sell/Hold with reasoning
- **Trend Analysis**: Based on last 3 price points

### Charts
- **Candlestick Chart**: Shows open, high, low, and close prices
- **Outlier Detection**: Highlights unusual price movements (red dots)

### Currency Information
- **Exchange Rate**: Current USD to INR conversion rate
- **Conversion Details**: Amount and rate used for calculations

## 🔍 API Endpoints Used

### Yahoo Finance (yfinance)
- **Purpose**: Stock data retrieval
- **Data**: 5-minute interval data for the last day
- **Rate Limit**: No strict limits for basic usage

### Alpha Vantage
- **Purpose**: Currency exchange rates
- **Rate Limit**: 5 API calls per minute (free tier)
- **Endpoints**: Foreign Exchange API

## ⚙️ Configuration

### GPU Acceleration
The application automatically detects and uses CUDA if available:
```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
```

### API Keys
- **Alpha Vantage**: Replace `API_KEY` variable with your key
- **RapidAPI**: Additional Alpha Vantage endpoint available

## 📈 Features in Detail

### Outlier Detection
- Uses Z-score method (standard deviations from mean)
- Identifies prices beyond 2 standard deviations
- Visualized as red dots on the price chart

### Trend Analysis
- **Rising Trend**: Last 3 prices increasing → "Buy" recommendation
- **Falling Trend**: Last 3 prices decreasing → "Sell" recommendation
- **Sideways Trend**: Fluctuating prices → "Hold" recommendation

### Multi-Currency Support
- Automatic conversion for INR display
- Real-time exchange rates
- Support for major world currencies

## 🚨 Error Handling

The application includes comprehensive error handling for:
- Invalid stock symbols
- Network connectivity issues
- API rate limits
- Missing data
- Currency conversion failures

## 🔒 Security Notes

- API keys are included in the code for demonstration
- For production use, use environment variables
- Consider implementing rate limiting for public deployments

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Bug fixes
- New features
- Documentation improvements
- Performance optimizations

## 📞 Support

For issues or questions:
1. Check the error messages in the application
2. Verify your internet connection
3. Ensure API keys are valid
4. Check if the stock symbol exists

## 🔮 Future Enhancements

Potential improvements:
- Historical data analysis
- Technical indicators (RSI, MACD, etc.)
- Portfolio tracking
- Alert systems
- Machine learning predictions
- More exchanges and markets
- Advanced charting options

---

**Note**: This application is for educational and informational purposes only. Stock market investments carry risks, and this tool should not be the sole basis for investment decisions.
