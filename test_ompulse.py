#!/usr/bin/env python3
"""
🧘 OmPulse Test Suite
Verifying the spiritual flow of our conscious investing app
"""

import asyncio
import requests
import time
import sys
from datetime import datetime

# Test configuration
BASE_URL = "http://localhost:8000"
TEST_SYMBOLS = ["AAPL", "GOOGL", "MSFT"]

def print_test_header(test_name):
    """Print a beautiful test header"""
    print(f"\n🌸 {'='*50}")
    print(f"   Testing: {test_name}")
    print(f"🌸 {'='*50}")

def test_health_check():
    """Test if the app is running"""
    print_test_header("Health Check")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ App is running: {data.get('status', 'Unknown')}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to app: {e}")
        print("💫 Make sure to run: python main.py")
        return False

def test_stock_pulse():
    """Test individual stock pulse endpoint"""
    print_test_header("Stock Pulse Energy")
    
    for symbol in TEST_SYMBOLS[:2]:  # Test first 2 symbols
        try:
            response = requests.get(f"{BASE_URL}/api/stocks/pulse/{symbol}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                pulse = data['pulse']
                print(f"✅ {symbol}:")
                print(f"   💰 Price: ${pulse['current_price']:.2f}")
                print(f"   📈 Change: {pulse['change_percent']:.2f}%")
                print(f"   🧘 Energy: {pulse['energy_level']}")
                print(f"   🌸 Message: {pulse['spiritual_message']}")
            else:
                print(f"❌ Failed to get {symbol} pulse: {response.status_code}")
        except Exception as e:
            print(f"❌ Error testing {symbol}: {e}")

def test_daily_meditation():
    """Test daily meditation endpoint"""
    print_test_header("Daily Market Meditation")
    
    try:
        response = requests.get(f"{BASE_URL}/api/meditation/daily", timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                meditation = data['meditation']
                print("✅ Daily meditation received:")
                print(f"   🙏 Affirmation: {meditation['market_affirmation']}")
                print(f"   🧘 Mantra: {meditation['mantra']}")
                print(f"   💎 Wisdom: {meditation['financial_wisdom']}")
            else:
                print(f"❌ Meditation failed: {data.get('error', 'Unknown')}")
        else:
            print(f"❌ Meditation request failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing meditation: {e}")

def test_astro_forecast():
    """Test astrology forecast endpoint"""
    print_test_header("Cosmic Market Forecast")
    
    try:
        response = requests.get(f"{BASE_URL}/api/astro/daily-forecast", timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                forecast = data['forecast']
                print("✅ Cosmic forecast received:")
                print(f"   🌟 Energy: {forecast['overall_energy']}")
                print(f"   🌙 Lunar: {forecast['lunar_phase']}")
                print(f"   🔮 Prediction: {forecast['market_prediction']}")
                print(f"   💫 Advice: {forecast['cosmic_advice']}")
            else:
                print(f"❌ Forecast failed: {data.get('error', 'Unknown')}")
        else:
            print(f"❌ Forecast request failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing astrology: {e}")

def test_market_sentiment():
    """Test market sentiment analysis"""
    print_test_header("Market Consciousness")
    
    try:
        symbols_str = ",".join(TEST_SYMBOLS)
        response = requests.get(f"{BASE_URL}/api/stocks/market/sentiment?symbols={symbols_str}", timeout=15)
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                sentiment = data['sentiment']
                print("✅ Market sentiment analyzed:")
                print(f"   🧘 Sentiment: {sentiment['sentiment']}")
                print(f"   📊 Avg Change: {sentiment['average_change']:.2f}%")
                print(f"   💭 Message: {sentiment['message']}")
            else:
                print(f"❌ Sentiment analysis failed")
        else:
            print(f"❌ Sentiment request failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing sentiment: {e}")

def test_portfolio_karma():
    """Test portfolio karmic analysis"""
    print_test_header("Portfolio Karma Assessment")
    
    # Mock portfolio data
    portfolio = [
        {"symbol": "AAPL", "shares": 10, "sector": "Technology"},
        {"symbol": "GOOGL", "shares": 5, "sector": "Technology"},
        {"symbol": "JNJ", "shares": 8, "sector": "Healthcare"}
    ]
    
    try:
        response = requests.post(f"{BASE_URL}/api/portfolio/karmic-analysis", json=portfolio, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                karma = data['karmic_analysis']
                print("✅ Karmic analysis complete:")
                print(f"   🔮 Level: {karma['karma_level']}")
                print(f"   📊 Score: {karma['karma_score']}")
                print(f"   💫 Message: {karma['karma_message']}")
            else:
                print(f"❌ Karma analysis failed")
        else:
            print(f"❌ Karma request failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing karma: {e}")

def test_all_affirmations():
    """Test all affirmation categories"""
    print_test_header("Spiritual Affirmations")
    
    categories = ["abundance", "patience", "wisdom", "gratitude"]
    
    for category in categories:
        try:
            response = requests.get(f"{BASE_URL}/api/meditation/affirmations/{category}", timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data['success']:
                    affirmations = data['affirmations']
                    print(f"✅ {category.title()}: {len(affirmations)} affirmations loaded")
                    print(f"   💫 Sample: {affirmations[0] if affirmations else 'None'}")
                else:
                    print(f"❌ {category} affirmations failed")
            else:
                print(f"❌ {category} request failed: {response.status_code}")
        except Exception as e:
            print(f"❌ Error testing {category}: {e}")

def run_all_tests():
    """Run the complete test suite"""
    print("🧘 Starting OmPulse Test Suite")
    print("🌸 Testing the spiritual flow of conscious investing...")
    
    # First check if app is running
    if not test_health_check():
        print("\n❌ App is not running. Please start it first:")
        print("   python main.py")
        print("   or")
        print("   python start.py")
        return False
    
    # Run all tests
    test_stock_pulse()
    test_daily_meditation()
    test_astro_forecast()
    test_market_sentiment()
    test_portfolio_karma()
    test_all_affirmations()
    
    # Final message
    print("\n🌟 Test Suite Complete!")
    print("🧘 If you see mostly ✅ marks, your OmPulse app is flowing beautifully!")
    print("🌸 If you see ❌ marks, the cosmic energies may need adjustment.")
    print("\n💫 Remember: Every test is a step toward conscious investing enlightenment")
    print("🙏 Namaste, and may your code be bug-free! 🙏")
    
    return True

if __name__ == "__main__":
    # Check if user wants to run specific test
    if len(sys.argv) > 1:
        test_name = sys.argv[1].lower()
        if test_name == "health":
            test_health_check()
        elif test_name == "pulse":
            test_stock_pulse()
        elif test_name == "meditation":
            test_daily_meditation()
        elif test_name == "astro":
            test_astro_forecast()
        elif test_name == "sentiment":
            test_market_sentiment()
        elif test_name == "karma":
            test_portfolio_karma()
        elif test_name == "affirmations":
            test_all_affirmations()
        else:
            print(f"🌫️ Unknown test: {test_name}")
            print("Available tests: health, pulse, meditation, astro, sentiment, karma, affirmations")
    else:
        run_all_tests() 