"""
🧘 Meditation Engine - Daily Market Wisdom
Blending financial awareness with spiritual growth
"""

import random
from datetime import datetime
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class DailyMeditation:
    """A moment of financial mindfulness"""
    date: str
    market_affirmation: str
    breathing_exercise: str
    financial_wisdom: str
    chakra_focus: str
    mantra: str

class MarketMeditationEngine:
    """
    🌸 Sacred space for financial mindfulness
    Where market awareness meets inner peace
    """
    
    def __init__(self):
        self.affirmations = {
            "abundance": [
                "💰 Money flows to me like water to the ocean - naturally and abundantly",
                "🌟 I am a magnet for financial opportunities and prosperity",
                "🌱 My wealth grows like a garden tended with love and patience",
                "✨ I trust the universe to provide exactly what I need, when I need it"
            ],
            "patience": [
                "🧘 I remain centered and calm as markets fluctuate around me",
                "🌊 Like the ocean, I am vast and unmoved by temporary waves",
                "🌙 Patience is my superpower in the world of investing",
                "🍃 I breathe deeply and let fear transform into wisdom"
            ],
            "wisdom": [
                "🦉 I make financial decisions from a place of inner knowing",
                "📚 Every market movement teaches me something valuable",
                "🔮 I trust my intuition to guide my investment choices",
                "💡 Clarity comes when I quiet my mind and listen within"
            ],
            "gratitude": [
                "🙏 I am grateful for every dollar that flows through my life",
                "🌸 Gratitude multiplies my blessings and attracts more abundance",
                "❤️ I appreciate both gains and losses as teachers on my journey",
                "🌈 My heart overflows with appreciation for financial opportunities"
            ]
        }
        
        self.breathing_exercises = [
            "🌬️ **4-7-8 Prosperity Breath**: Inhale for 4 counts (I receive), hold for 7 (I trust), exhale for 8 (I release fear)",
            "💨 **Abundance Square**: Breathe in wealth (4), hold gratitude (4), breathe out doubt (4), pause in trust (4)",
            "🌊 **Ocean Breath**: Deep, rhythmic breathing like gentle waves - each inhale brings abundance, each exhale releases limitation",
            "🌺 **Lotus Breath**: Breathe into your heart center, imagining a golden lotus opening with each breath, revealing your abundant nature"
        ]
        
        self.financial_wisdom = [
            "🌱 True wealth grows slowly, like an ancient tree with deep roots",
            "⚖️ Balance in your portfolio reflects balance in your life",
            "🎯 Invest in alignment with your values, not just your profits",
            "🌊 Ride the waves of volatility without losing your center",
            "🔮 The best investment you can make is in your own consciousness",
            "🧘 Peaceful mind, profitable decisions",
            "💎 Pressure creates diamonds - both in markets and in life",
            "🌸 What you resist persists - accept market fluctuations with grace"
        ]
        
        self.chakra_focuses = [
            "🔴 **Root Chakra** - Grounding your financial security in trust and stability",
            "🧡 **Sacral Chakra** - Creative approaches to building wealth and abundance", 
            "💛 **Solar Plexus** - Personal power and confidence in financial decisions",
            "💚 **Heart Chakra** - Making money decisions from love, not fear",
            "💙 **Throat Chakra** - Speaking your financial truth and communicating about money",
            "💜 **Third Eye** - Intuitive insight into market trends and opportunities",
            "🤍 **Crown Chakra** - Connecting to universal abundance and higher wisdom"
        ]
        
        self.mantras = [
            "I am one with abundance 💰",
            "Money flows to me effortlessly 🌊", 
            "I invest with wisdom and trust 🧘",
            "Prosperity is my natural state 🌟",
            "I am grateful for all wealth in my life 🙏",
            "My financial decisions are guided by love ❤️",
            "I attract opportunities that align with my highest good ✨"
        ]
    
    def generate_daily_meditation(self, market_sentiment: str = "balanced") -> DailyMeditation:
        """
        🌅 Create today's personalized market meditation
        Combining current market energy with spiritual wisdom
        """
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Choose affirmation category based on market sentiment
        if market_sentiment in ["turbulent", "descending"]:
            affirmation_category = "patience"
        elif market_sentiment in ["soaring", "rising"]:
            affirmation_category = "gratitude"
        elif market_sentiment == "calm":
            affirmation_category = "wisdom"
        else:
            affirmation_category = "abundance"
        
        return DailyMeditation(
            date=today,
            market_affirmation=random.choice(self.affirmations[affirmation_category]),
            breathing_exercise=random.choice(self.breathing_exercises),
            financial_wisdom=random.choice(self.financial_wisdom),
            chakra_focus=random.choice(self.chakra_focuses),
            mantra=random.choice(self.mantras)
        )
    
    def get_market_mood_meditation(self, sentiment: str, avg_change: float) -> Dict[str, str]:
        """
        🎭 Generate meditation based on current market mood
        Responding to the market's emotional energy
        """
        meditations = {
            "soaring": {
                "title": "🦅 Riding the Winds of Abundance",
                "message": "As the market soars, remember that true wealth comes from inner abundance. Let gratitude be your anchor in times of prosperity.",
                "practice": "Take 3 deep breaths and say: 'I receive this abundance with humility and share it with love.'"
            },
            "rising": {
                "title": "🌱 Growing with Grace", 
                "message": "Your investments bloom like flowers in spring. Stay present and water them with patience and wisdom.",
                "practice": "Visualize your money as seeds growing into a beautiful garden that nourishes many."
            },
            "calm": {
                "title": "🧘 Sacred Stillness",
                "message": "In market calm, find your center. This peaceful energy reflects your own inner balance.",
                "practice": "Sit quietly for 5 minutes and appreciate the stability in your financial journey."
            },
            "descending": {
                "title": "🍂 Lessons in Letting Go",
                "message": "As autumn teaches trees to release their leaves, markets teach us about cycles and renewal.",
                "practice": "Breathe out any fear about losses. Breathe in trust that new growth always follows."
            },
            "turbulent": {
                "title": "🌊 Staying Centered in the Storm",
                "message": "Even in market turbulence, you are the calm eye of the hurricane. Your peace is unshakeable.",
                "practice": "Ground yourself: Feel your feet on the earth and remember that this too shall pass."
            }
        }
        
        return meditations.get(sentiment, meditations["calm"])
    
    def get_weekly_financial_reading(self) -> Dict[str, str]:
        """
        🔮 Weekly financial energy reading
        Mystical guidance for the trading week ahead
        """
        readings = [
            {
                "theme": "🌙 New Moon Manifestation",
                "guidance": "This week carries potent creative energy. Plant seeds for long-term financial growth.",
                "action": "Set clear intentions for your investment goals and write them down."
            },
            {
                "theme": "🌕 Full Moon Release", 
                "guidance": "Time to release what no longer serves your financial journey. Clear space for abundance.",
                "action": "Review your portfolio and release investments that don't align with your values."
            },
            {
                "theme": "⚡ Mercury Energy",
                "guidance": "Communication and quick thinking favor your financial decisions this week.",
                "action": "Research new opportunities and have important money conversations."
            },
            {
                "theme": "♀️ Venus Blessing",
                "guidance": "Attraction and beauty principles guide your wealth building. What you love grows.",
                "action": "Invest in companies and causes that you're passionate about."
            },
            {
                "theme": "♂️ Mars Action",
                "guidance": "Bold action and courage are your financial allies. Take calculated risks.",
                "action": "Make that investment decision you've been contemplating with confidence."
            }
        ]
        
        return random.choice(readings) 