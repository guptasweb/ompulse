"""
🧘 Meditation Routes - Sacred Endpoints for Financial Mindfulness
Where inner peace meets outer abundance
"""

from fastapi import APIRouter, HTTPException
from typing import Optional
from datetime import datetime

from ..core.meditation_engine import MarketMeditationEngine
from ..core.stock_fetcher import ZenStockFetcher

router = APIRouter()

# Initialize engines
meditation_engine = MarketMeditationEngine()
stock_fetcher = ZenStockFetcher()

@router.get("/daily")
async def get_daily_meditation(market_sentiment: Optional[str] = None):
    """
    🌅 Receive today's personalized market meditation
    Starting your financial day with mindful intention
    """
    try:
        # If no sentiment provided, get current market sentiment
        if not market_sentiment:
            # Get sentiment from major market indices
            major_symbols = ["SPY", "QQQ", "DIA"]
            pulses = await stock_fetcher.get_multiple_pulses(major_symbols)
            sentiment_data = stock_fetcher.get_market_sentiment(pulses)
            market_sentiment = sentiment_data.get("sentiment", "balanced")
        
        # Generate meditation
        meditation = meditation_engine.generate_daily_meditation(market_sentiment)
        
        return {
            "success": True,
            "meditation": {
                "date": meditation.date,
                "market_affirmation": meditation.market_affirmation,
                "breathing_exercise": meditation.breathing_exercise,
                "financial_wisdom": meditation.financial_wisdom,
                "chakra_focus": meditation.chakra_focus,
                "mantra": meditation.mantra,
                "based_on_sentiment": market_sentiment
            },
            "invitation": "🌸 Take a moment to breathe deeply and center yourself before engaging with the markets",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ The meditation channel is temporarily clouded",
            "backup_wisdom": "🧘 In all uncertainty, return to your breath and trust your inner wisdom"
        }

@router.get("/mood-meditation")
async def get_market_mood_meditation(sentiment: str = "calm", avg_change: float = 0.0):
    """
    🎭 Get meditation guidance based on current market mood
    Responding wisely to market emotional energy
    """
    try:
        mood_meditation = meditation_engine.get_market_mood_meditation(sentiment, avg_change)
        
        return {
            "success": True,
            "mood_meditation": mood_meditation,
            "current_sentiment": sentiment,
            "average_change": avg_change,
            "gentle_reminder": "🌊 You are not your portfolio - you are the peaceful observer of its movements",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ Unable to channel mood meditation at this time",
            "universal_truth": "🕉️ Peace exists within you regardless of market conditions"
        }

@router.get("/weekly-reading")
async def get_weekly_financial_reading():
    """
    🔮 Receive mystical guidance for the trading week ahead
    Weekly financial energy forecast
    """
    try:
        reading = meditation_engine.get_weekly_financial_reading()
        
        return {
            "success": True,
            "weekly_reading": reading,
            "week_start": datetime.now().strftime("%Y-%m-%d"),
            "cosmic_note": "🌌 The universe conspires to support your highest financial good",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ The cosmic signals are unclear this week",
            "eternal_wisdom": "💫 Trust in the process and stay aligned with your values"
        }

@router.get("/affirmations/{category}")
async def get_affirmations_by_category(category: str):
    """
    ✨ Get affirmations for specific financial energies
    Categories: abundance, patience, wisdom, gratitude
    """
    try:
        valid_categories = ["abundance", "patience", "wisdom", "gratitude"]
        
        if category.lower() not in valid_categories:
            raise HTTPException(
                status_code=400,
                detail=f"🌸 Please choose from: {', '.join(valid_categories)}"
            )
        
        affirmations = meditation_engine.affirmations.get(category.lower(), [])
        
        return {
            "success": True,
            "category": category.lower(),
            "affirmations": affirmations,
            "usage_tip": "🧘 Repeat these affirmations during market volatility to stay centered",
            "frequency": "💫 Use these 3 times daily: morning intention, midday reset, evening gratitude",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ Unable to access affirmations at this time",
            "universal_affirmation": "🙏 I am worthy of abundance and financial peace"
        }

@router.get("/breathing-exercises")
async def get_breathing_exercises():
    """
    🌬️ Access sacred breathing practices for financial stress
    Pranayama for prosperity consciousness
    """
    try:
        exercises = meditation_engine.breathing_exercises
        
        return {
            "success": True,
            "breathing_exercises": exercises,
            "when_to_use": [
                "📉 When experiencing losses or market downturns",
                "📈 During high gains to stay grounded", 
                "🤔 Before making important investment decisions",
                "😰 When feeling financial anxiety or fear",
                "🧘 As part of daily financial meditation practice"
            ],
            "scientific_note": "🧠 Deep breathing activates the parasympathetic nervous system, promoting clearer financial decision-making",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ Breathing guidance temporarily unavailable",
            "simple_practice": "🌬️ Breathe in peace, breathe out fear. Repeat 3 times."
        }

@router.get("/financial-mantras")
async def get_financial_mantras():
    """
    🕉️ Sacred sounds for financial transformation
    Mantras to align money energy with highest good
    """
    try:
        mantras = meditation_engine.mantras
        
        return {
            "success": True,
            "mantras": mantras,
            "how_to_use": [
                "🌅 Repeat during morning meditation before market open",
                "💭 Use as mental background during trading decisions",
                "🌙 Chant before sleep to program subconscious abundance",
                "🚶 Repeat while walking to integrate energy",
                "📱 Set as phone reminders throughout trading day"
            ],
            "power_note": "🔮 Mantras work by rewiring neural pathways toward abundance consciousness",
            "timing": "⏰ Most powerful when repeated 108 times with intention",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ Mantra transmission interrupted",
            "eternal_mantra": "🕉️ Om Gam Ganapataye Namaha - Removing obstacles to prosperity"
        }

@router.post("/custom-meditation")
async def create_custom_meditation(portfolio_mood: str, personal_intention: str):
    """
    🎨 Create personalized meditation based on your portfolio and intentions
    Bespoke spiritual guidance for your unique financial journey
    """
    try:
        # Generate custom elements based on inputs
        custom_elements = {
            "opening": f"🌸 Today I align my {portfolio_mood} energy with my intention: {personal_intention}",
            "affirmation": f"💫 My portfolio reflects my commitment to {personal_intention}",
            "breathing": "🌬️ I breathe in clarity for my financial decisions, I breathe out all doubt and fear",
            "visualization": f"🔮 I see my {personal_intention} manifesting through wise and conscious investments",
            "closing": "🙏 I trust the universe to guide my financial journey toward my highest good"
        }
        
        return {
            "success": True,
            "custom_meditation": custom_elements,
            "portfolio_mood": portfolio_mood,
            "personal_intention": personal_intention,
            "practice_tip": "🧘 Spend 5-10 minutes with this custom meditation before trading",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ Custom meditation creation temporarily unavailable",
            "universal_practice": "🕉️ I am one with abundance. My investments serve the highest good."
        } 