"""
🌊 WebSocket Manager - Real-time Market Flow
Streaming market consciousness in real-time
"""

import asyncio
import json
from typing import Set, Dict, List
from fastapi import WebSocket, WebSocketDisconnect
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class ZenWebSocketManager:
    """
    🕉️ Sacred channel for real-time market energy
    Broadcasting the pulse of financial consciousness
    """
    
    def __init__(self):
        self.active_connections: Set[WebSocket] = set()
        self.user_watchlists: Dict[WebSocket, List[str]] = {}
        self.last_prices: Dict[str, float] = {}
        self.is_streaming = False
        
    async def connect(self, websocket: WebSocket, symbols: List[str] = None):
        """
        🔗 Welcome a new soul to the market stream
        Establishing sacred connection to live data
        """
        await websocket.accept()
        self.active_connections.add(websocket)
        
        if symbols:
            self.user_watchlists[websocket] = symbols
        
        # Send welcome message
        welcome_msg = {
            "type": "connection",
            "message": "🧘 Welcome to the OmPulse stream - where market energy flows in real-time",
            "timestamp": datetime.now().isoformat(),
            "zen_wisdom": "Like a river, money flows best when not resisted 🌊"
        }
        await websocket.send_text(json.dumps(welcome_msg))
        
        logger.info(f"New connection established. Total connections: {len(self.active_connections)}")
    
    def disconnect(self, websocket: WebSocket):
        """
        🙏 Gracefully release a connection
        Honoring the completion of this market journey
        """
        self.active_connections.discard(websocket)
        if websocket in self.user_watchlists:
            del self.user_watchlists[websocket]
        
        logger.info(f"Connection closed. Total connections: {len(self.active_connections)}")
    
    async def send_personal_message(self, message: dict, websocket: WebSocket):
        """
        💌 Send a personal message to individual soul
        Direct communication channel
        """
        try:
            await websocket.send_text(json.dumps(message))
        except Exception as e:
            logger.error(f"Error sending personal message: {e}")
            self.disconnect(websocket)
    
    async def broadcast_to_all(self, message: dict):
        """
        📢 Share wisdom with all connected souls
        Universal broadcast of market consciousness
        """
        if not self.active_connections:
            return
        
        disconnected = set()
        
        for connection in self.active_connections:
            try:
                await connection.send_text(json.dumps(message))
            except WebSocketDisconnect:
                disconnected.add(connection)
            except Exception as e:
                logger.error(f"Error broadcasting message: {e}")
                disconnected.add(connection)
        
        # Clean up disconnected clients
        for connection in disconnected:
            self.disconnect(connection)
    
    async def broadcast_stock_update(self, symbol: str, price: float, change: float, change_percent: float, energy: str, message: str):
        """
        📈 Share stock energy updates with all connected souls
        Broadcasting the pulse of individual stocks
        """
        # Check if price actually changed to avoid spam
        if symbol in self.last_prices and abs(self.last_prices[symbol] - price) < 0.01:
            return
        
        self.last_prices[symbol] = price
        
        update = {
            "type": "stock_update",
            "symbol": symbol,
            "price": round(price, 2),
            "change": round(change, 2),
            "change_percent": round(change_percent, 2),
            "energy_level": energy,
            "spiritual_message": message,
            "timestamp": datetime.now().isoformat(),
            "pulse_emoji": self._get_pulse_emoji(energy)
        }
        
        await self.broadcast_to_all(update)
    
    async def broadcast_market_sentiment(self, sentiment_data: dict):
        """
        🌍 Share overall market consciousness
        Broadcasting the collective energy of the market
        """
        message = {
            "type": "market_sentiment",
            "sentiment": sentiment_data.get("sentiment"),
            "message": sentiment_data.get("message"),
            "average_change": round(sentiment_data.get("average_change", 0), 2),
            "energy_distribution": sentiment_data.get("energy_distribution", {}),
            "timestamp": datetime.now().isoformat(),
            "meditation_moment": self._get_sentiment_meditation(sentiment_data.get("sentiment"))
        }
        
        await self.broadcast_to_all(message)
    
    async def send_meditation_reminder(self):
        """
        🧘 Send mindful market reminders
        Gentle nudges for conscious trading
        """
        reminders = [
            "🌱 Take a deep breath and check in with your investment intentions",
            "🧘 Remember: Peace in the mind leads to profit in the portfolio", 
            "💫 Your inner abundance attracts outer abundance",
            "🌊 Let your investments flow like water - finding their natural level",
            "🌸 Gratitude for what you have opens doors to more abundance"
        ]
        
        import random
        reminder = {
            "type": "meditation_reminder",
            "message": random.choice(reminders),
            "timestamp": datetime.now().isoformat()
        }
        
        await self.broadcast_to_all(reminder)
    
    def _get_pulse_emoji(self, energy: str) -> str:
        """Get emoji representation of stock energy"""
        emoji_map = {
            "calm": "🧘",
            "rising": "🌱",
            "soaring": "🦅", 
            "descending": "🍃",
            "turbulent": "🌊",
            "disconnected": "🌫️"
        }
        return emoji_map.get(energy, "✨")
    
    def _get_sentiment_meditation(self, sentiment: str) -> str:
        """Get meditation moment for market sentiment"""
        meditations = {
            "calm": "In stillness, we find clarity. Breathe and appreciate this peaceful moment.",
            "rising": "Feel the energy of growth. Like a plant reaching for the sun, your wealth expands.",
            "soaring": "Celebrate abundance while staying grounded. What goes up teaches us about gratitude.",
            "descending": "In release, we find renewal. Trust the natural cycles of the market.",
            "turbulent": "You are the calm in the center of the storm. Your peace is unshakeable."
        }
        return meditations.get(sentiment, "Every moment is an opportunity to choose peace over panic.")
    
    async def start_live_stream(self, stock_fetcher, symbols: List[str], interval_seconds: int = 30):
        """
        🌊 Begin the sacred stream of live market data
        Continuous flow of financial consciousness
        """
        self.is_streaming = True
        logger.info(f"Starting live stream for symbols: {symbols}")
        
        while self.is_streaming and self.active_connections:
            try:
                # Fetch current stock data
                pulses = await stock_fetcher.get_multiple_pulses(symbols)
                
                # Broadcast individual stock updates
                for pulse in pulses:
                    await self.broadcast_stock_update(
                        pulse.symbol,
                        pulse.current_price,
                        pulse.change,
                        pulse.change_percent,
                        pulse.energy_level,
                        pulse.spiritual_message
                    )
                
                # Broadcast market sentiment
                sentiment = stock_fetcher.get_market_sentiment(pulses)
                await self.broadcast_market_sentiment(sentiment)
                
                # Wait before next update
                await asyncio.sleep(interval_seconds)
                
            except Exception as e:
                logger.error(f"Error in live stream: {e}")
                await asyncio.sleep(10)  # Wait before retrying
        
        logger.info("Live stream ended")
    
    def stop_live_stream(self):
        """
        🛑 Mindfully end the market stream
        Closing the channel with gratitude
        """
        self.is_streaming = False
        logger.info("Live stream stopped")

# Global instance
websocket_manager = ZenWebSocketManager() 