"""
🧘 Stock Data Fetcher - Channeling market energies
Connecting to the universal flow of financial information
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import asyncio
from dataclasses import dataclass

@dataclass
class StockPulse:
    """A single heartbeat in the market's rhythm"""
    symbol: str
    current_price: float
    change: float
    change_percent: float
    volume: int
    market_cap: Optional[float] = None
    energy_level: str = "balanced"  # calm, rising, turbulent
    spiritual_message: str = ""

class ZenStockFetcher:
    """
    🌸 The sacred conduit for market wisdom
    Fetches stock data with mindful awareness
    """
    
    def __init__(self):
        self.tickers_cache = {}
        self.last_fetch_time = {}
        
    def _get_energy_level(self, change_percent: float) -> str:
        """Interpret the stock's spiritual energy"""
        if abs(change_percent) < 1:
            return "calm"
        elif change_percent > 3:
            return "soaring"
        elif change_percent > 0:
            return "rising" 
        elif change_percent < -3:
            return "turbulent"
        else:
            return "descending"
    
    def _generate_spiritual_message(self, symbol: str, energy: str, change_percent: float) -> str:
        """Generate mindful market messages"""
        messages = {
            "calm": f"🧘 {symbol} flows like still water, finding its natural balance",
            "rising": f"🌱 {symbol} grows like bamboo, steady and strong toward the light",
            "soaring": f"🦅 {symbol} soars like an eagle, riding the winds of abundance",
            "descending": f"🍃 {symbol} moves like autumn leaves, teaching us about letting go",
            "turbulent": f"🌊 {symbol} churns like ocean waves, reminding us that storms pass"
        }
        return messages.get(energy, f"✨ {symbol} dances to the rhythm of the market")
    
    async def get_stock_pulse(self, symbol: str) -> StockPulse:
        """
        🔮 Retrieve a stock's current pulse
        Channeling real-time market energy
        """
        try:
            # Create ticker if not cached
            if symbol not in self.tickers_cache:
                self.tickers_cache[symbol] = yf.Ticker(symbol)
            
            ticker = self.tickers_cache[symbol]
            
            # Get current data
            info = ticker.info
            history = ticker.history(period="2d")
            
            if history.empty:
                raise ValueError(f"No data flowing for {symbol}")
            
            current_price = history['Close'].iloc[-1]
            prev_close = history['Close'].iloc[-2] if len(history) > 1 else current_price
            
            change = current_price - prev_close
            change_percent = (change / prev_close) * 100 if prev_close > 0 else 0
            
            energy = self._get_energy_level(change_percent)
            message = self._generate_spiritual_message(symbol, energy, change_percent)
            
            return StockPulse(
                symbol=symbol,
                current_price=current_price,
                change=change,
                change_percent=change_percent,
                volume=int(history['Volume'].iloc[-1]),
                market_cap=info.get('marketCap'),
                energy_level=energy,
                spiritual_message=message
            )
            
        except Exception as e:
            # Zen error handling
            return StockPulse(
                symbol=symbol,
                current_price=0.0,
                change=0.0,
                change_percent=0.0,
                volume=0,
                energy_level="disconnected",
                spiritual_message=f"🌫️ {symbol}'s energy is clouded. The universe asks for patience."
            )
    
    async def get_multiple_pulses(self, symbols: List[str]) -> List[StockPulse]:
        """
        🌈 Gather multiple stock energies simultaneously
        Like reading the aura of the entire market
        """
        tasks = [self.get_stock_pulse(symbol) for symbol in symbols]
        return await asyncio.gather(*tasks)
    
    def get_market_sentiment(self, pulses: List[StockPulse]) -> Dict[str, any]:
        """
        🧘 Analyze the collective market consciousness
        Reading the overall energy of your watchlist
        """
        if not pulses:
            return {"sentiment": "void", "message": "The market meditates in silence"}
        
        total_change = sum(p.change_percent for p in pulses)
        avg_change = total_change / len(pulses)
        
        energy_counts = {}
        for pulse in pulses:
            energy_counts[pulse.energy_level] = energy_counts.get(pulse.energy_level, 0) + 1
        
        dominant_energy = max(energy_counts, key=energy_counts.get)
        
        sentiment_messages = {
            "calm": "🧘 The market breathes deeply, centered in peaceful awareness",
            "rising": "🌱 Positive energy flows like spring water through the market",
            "soaring": "🦅 The market soars with abundant joy and prosperity",
            "descending": "🍂 The market teaches patience through gentle release",
            "turbulent": "🌊 Volatility reminds us to stay grounded in our center"
        }
        
        return {
            "sentiment": dominant_energy,
            "average_change": avg_change,
            "message": sentiment_messages.get(dominant_energy, "✨ The market dances its mysterious dance"),
            "energy_distribution": energy_counts,
            "total_symbols": len(pulses)
        } 