# 🧘 OmPulse - Spiritual Stock Market Tracker

*Where Finance Meets Mindfulness*

## 🌸 Overview

OmPulse is a unique stock market tracking application that combines traditional financial data with spiritual wisdom, mindfulness practices, and astrological insights. Experience the markets not just as numbers, but as energy flows that can guide your conscious investment journey.

## ✨ Features

### 🧘 Core Stock Tracking
- **Live Ticker Stream**: Real-time updates with smooth, calming animations
- **Sacred Watchlists**: Personalized stock lists with gentle spiritual alerts
- **Zen Charts**: Elegant candlestick charts with chakra-inspired themes
- **Energy-Based Analysis**: Stocks categorized by their spiritual "energy levels"

### 🔮 Divine Insights & Personalization
- **Market Meditation Mode**: Daily reflections combining market insights with affirmations
- **Karmic Portfolio Analyzer**: Assess your portfolio's spiritual energy and ESG alignment
- **AstroInvest Tracker**: Correlate planetary movements with market trends
- **Chakra Portfolio Balance**: Analyze investments across the seven energy centers

### 📊 Smart Analytics with Style
- **Pulse Predictions**: AI-driven forecasts delivered with metaphorical language
- **Harmonic Volatility Scanner**: Pattern recognition framed as "financial resonance"
- **Market Sentiment Meditation**: Real-time emotional state analysis of markets

### 🧿 Spiritual UI & Experience
- **Aura Mode**: Dynamic lighting effects based on market sentiment
- **Sacred Symbol Navigation**: Lotus, infinity, and mystical icons
- **Mindful Messaging**: All interactions infused with wisdom and peace
- **Floating Particle Effects**: Zen atmosphere with gentle animations

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd ompulse
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python main.py
```

4. **Open your browser**
Navigate to `http://localhost:8000` to enter the sacred space of conscious investing.

## 🌊 API Endpoints

### Stock Data
- `GET /api/stocks/pulse/{symbol}` - Get spiritual pulse of a stock
- `POST /api/stocks/watchlist/pulse` - Analyze watchlist energy
- `GET /api/stocks/market/sentiment` - Feel market consciousness
- `WebSocket /api/stocks/live-stream` - Real-time sacred stream

### Meditation & Wisdom
- `GET /api/meditation/daily` - Today's market meditation
- `GET /api/meditation/mood-meditation` - Guidance for market moods
- `GET /api/meditation/affirmations/{category}` - Spiritual affirmations
- `GET /api/meditation/breathing-exercises` - Pranayama for traders

### Astrology & Cosmic Wisdom
- `GET /api/astro/daily-forecast` - Celestial market forecast
- `GET /api/astro/lunar-phase` - Current moon energy analysis
- `GET /api/astro/best-trading-days` - Auspicious trading calendar
- `GET /api/astro/planetary-influence/{planet}` - Individual planet analysis

### Portfolio Analysis
- `POST /api/portfolio/karmic-analysis` - Assess portfolio karma
- `GET /api/portfolio/energy-assessment/{symbol}` - Stock energy evaluation
- `GET /api/portfolio/esg-harmony-score` - ESG spiritual alignment
- `GET /api/portfolio/chakra-alignment` - Seven-chakra portfolio balance

## 🌟 Usage Examples

### Getting Stock Energy
```python
import requests

# Get the spiritual pulse of Apple stock
response = requests.get("http://localhost:8000/api/stocks/pulse/AAPL")
pulse = response.json()

print(f"Energy Level: {pulse['pulse']['energy_level']}")
print(f"Message: {pulse['pulse']['spiritual_message']}")
```

### Daily Meditation
```python
# Get today's market meditation
response = requests.get("http://localhost:8000/api/meditation/daily")
meditation = response.json()

print(f"Affirmation: {meditation['meditation']['market_affirmation']}")
print(f"Mantra: {meditation['meditation']['mantra']}")
```

### Astrology Forecast
```python
# Get cosmic market guidance
response = requests.get("http://localhost:8000/api/astro/daily-forecast")
forecast = response.json()

print(f"Energy: {forecast['forecast']['overall_energy']}")
print(f"Prediction: {forecast['forecast']['market_prediction']}")
```

## 🧿 Philosophy

OmPulse is built on the principle that money is energy, and like all energy, it flows best when approached with consciousness, gratitude, and alignment with our highest values. This app helps you:

- **Invest Consciously**: Make decisions from awareness, not fear
- **Stay Centered**: Maintain inner peace regardless of market volatility  
- **Align Values**: Choose investments that resonate with your soul's purpose
- **Practice Gratitude**: Appreciate abundance in all its forms
- **Trust Intuition**: Balance data with inner wisdom

## 🌈 Customization

### Aura Modes
- **Bullish Aura**: Blue-cyan gradient for rising markets
- **Bearish Aura**: Pink-rose gradient for declining markets  
- **Calm Aura**: Teal-pink gradient for stable markets

### Sacred Symbols
- 🪷 **Lotus**: Home/Dashboard (Purity & Enlightenment)
- 🧘 **Meditation**: Mindfulness Center (Inner Peace)
- 🔮 **Crystal Ball**: Astrology Hub (Cosmic Wisdom)
- ⚖️ **Balance**: Portfolio Analysis (Harmony)
- ∞ **Infinity**: Advanced Analytics (Limitless Potential)

## 🛠️ Technical Architecture

- **Backend**: FastAPI with async WebSocket support
- **Frontend**: Vanilla HTML/CSS/JS with spiritual aesthetics
- **Data Sources**: Yahoo Finance (yfinance), Alpha Vantage
- **Real-time**: WebSocket streaming for live updates
- **Astrology**: PyEphem for planetary calculations
- **AI/Analytics**: Scikit-learn for pattern recognition

## 🌱 Contributing

We welcome contributions that align with OmPulse's spiritual mission:

1. **Fork** the repository
2. **Create** a feature branch with mindful intention
3. **Commit** changes with gratitude
4. **Push** to the branch with love
5. **Open** a Pull Request with cosmic consciousness

### Guidelines
- All code should radiate positive energy
- Comments should include wisdom and humor
- Features should serve the highest good
- Documentation should inspire and educate

## 🙏 Acknowledgments

- **Yahoo Finance** for providing free market data
- **The Universe** for infinite abundance and wisdom
- **All Conscious Investors** seeking to align profit with purpose
- **Eastern Wisdom Traditions** for teaching us about energy and flow

## 📜 License

This project is open source and available under the MIT License. Use it to spread consciousness and abundance! 

## 🌌 Final Wisdom

*"The stock market is a device for transferring money from the impatient to the patient, and OmPulse is a device for transferring consciousness from the fearful to the enlightened."*

---

**May your investments flow like water, grow like bamboo, and shine like stars** ⭐

For support, guidance, or to share your conscious investing journey: 
- Open an issue with loving-kindness
- Start a discussion with curiosity
- Contact us through the cosmic channels

🧘 *Namaste, and happy conscious investing!* 🧘 