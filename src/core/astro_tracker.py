"""
🔮 AstroInvest Tracker - Celestial Market Wisdom
Where planetary movements meet portfolio movements
"""

import ephem
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
from dataclasses import dataclass
import random

@dataclass
class PlanetaryInfluence:
    """Cosmic energy affecting the markets"""
    planet: str
    sign: str
    influence: str  # bullish, bearish, volatile, stable
    message: str
    strength: float  # 0-1 scale

@dataclass
class AstroForecast:
    """Daily astrological market forecast"""
    date: str
    overall_energy: str
    planetary_influences: List[PlanetaryInfluence]
    lunar_phase: str
    market_prediction: str
    cosmic_advice: str

class AstroInvestTracker:
    """
    🌟 Celestial guide for market movements
    Reading the cosmic patterns in financial flows
    """
    
    def __init__(self):
        self.observer = ephem.Observer()
        self.observer.date = datetime.now()
        
        # Define planets and their market associations
        self.planets = {
            'sun': {'name': '☀️ Sun', 'influence': 'leadership, gold, big moves'},
            'moon': {'name': '🌙 Moon', 'influence': 'emotions, silver, daily fluctuations'},
            'mercury': {'name': '☿ Mercury', 'influence': 'communication, tech stocks, quick trades'},
            'venus': {'name': '♀ Venus', 'influence': 'beauty, luxury goods, consumer stocks'},
            'mars': {'name': '♂ Mars', 'influence': 'energy, defense, aggressive trading'},
            'jupiter': {'name': '♃ Jupiter', 'influence': 'expansion, growth stocks, optimism'},
            'saturn': {'name': '♄ Saturn', 'influence': 'structure, blue chips, long-term stability'},
            'uranus': {'name': '♅ Uranus', 'influence': 'innovation, tech disruption, volatility'},
            'neptune': {'name': '♆ Neptune', 'influence': 'illusion, oil/gas, confusion'},
            'pluto': {'name': '♇ Pluto', 'influence': 'transformation, mining, major shifts'}
        }
        
        self.zodiac_signs = {
            'aries': {'element': 'fire', 'energy': 'aggressive', 'market_mood': 'bullish'},
            'taurus': {'element': 'earth', 'energy': 'stable', 'market_mood': 'steady growth'},
            'gemini': {'element': 'air', 'energy': 'versatile', 'market_mood': 'volatile'},
            'cancer': {'element': 'water', 'energy': 'protective', 'market_mood': 'defensive'},
            'leo': {'element': 'fire', 'energy': 'confident', 'market_mood': 'strong gains'},
            'virgo': {'element': 'earth', 'energy': 'analytical', 'market_mood': 'careful analysis'},
            'libra': {'element': 'air', 'energy': 'balanced', 'market_mood': 'sideways movement'},
            'scorpio': {'element': 'water', 'energy': 'intense', 'market_mood': 'dramatic swings'},
            'sagittarius': {'element': 'fire', 'energy': 'optimistic', 'market_mood': 'international expansion'},
            'capricorn': {'element': 'earth', 'energy': 'disciplined', 'market_mood': 'conservative growth'},
            'aquarius': {'element': 'air', 'energy': 'innovative', 'market_mood': 'tech revolution'},
            'pisces': {'element': 'water', 'energy': 'intuitive', 'market_mood': 'emotional trading'}
        }
        
        self.lunar_phases = {
            'new_moon': '🌑 New Moon - New beginnings, fresh investments',
            'waxing_crescent': '🌒 Waxing Crescent - Growing momentum, accumulation phase',
            'first_quarter': '🌓 First Quarter - Decisions and action, mid-cycle energy',
            'waxing_gibbous': '🌔 Waxing Gibbous - Building toward peak, strong growth',
            'full_moon': '🌕 Full Moon - Peak energy, maximum volatility',
            'waning_gibbous': '🌖 Waning Gibbous - Reflection and analysis, profit-taking',
            'last_quarter': '🌗 Last Quarter - Release and restructuring, corrections',
            'waning_crescent': '🌘 Waning Crescent - Clearing space, preparing for new cycle'
        }
    
    def get_planet_sign(self, planet_name: str) -> str:
        """Get the current zodiac sign of a planet"""
        try:
            planet = getattr(ephem, planet_name.capitalize())()
            planet.compute(self.observer)
            
            # Convert ecliptic longitude to zodiac sign
            longitude = float(planet.hlong) * 180.0 / ephem.pi
            sign_index = int(longitude / 30)
            signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo',
                    'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
            return signs[sign_index]
        except:
            return 'unknown'
    
    def get_lunar_phase(self) -> str:
        """Calculate current lunar phase"""
        moon = ephem.Moon()
        moon.compute(self.observer)
        
        # Get moon phase (0 = new, 0.5 = full, 1 = new again)
        phase = moon.phase / 100.0
        
        if phase < 0.03:
            return 'new_moon'
        elif phase < 0.22:
            return 'waxing_crescent'
        elif phase < 0.28:
            return 'first_quarter'
        elif phase < 0.47:
            return 'waxing_gibbous'
        elif phase < 0.53:
            return 'full_moon'
        elif phase < 0.72:
            return 'waning_gibbous'
        elif phase < 0.78:
            return 'last_quarter'
        else:
            return 'waning_crescent'
    
    def analyze_planetary_influence(self, planet: str) -> PlanetaryInfluence:
        """Analyze a planet's current market influence"""
        sign = self.get_planet_sign(planet)
        planet_info = self.planets.get(planet, {})
        sign_info = self.zodiac_signs.get(sign, {})
        
        # Generate influence based on planet-sign combination
        influences = ['bullish', 'bearish', 'volatile', 'stable']
        
        # Some logic for determining influence
        if sign_info.get('market_mood') == 'bullish' or 'growth' in sign_info.get('market_mood', ''):
            influence = 'bullish'
        elif 'defensive' in sign_info.get('market_mood', '') or 'conservative' in sign_info.get('market_mood', ''):
            influence = 'stable'
        elif 'volatile' in sign_info.get('market_mood', '') or 'dramatic' in sign_info.get('market_mood', ''):
            influence = 'volatile'
        else:
            influence = random.choice(influences)
        
        # Generate mystical message
        messages = {
            'bullish': f"🚀 {planet_info.get('name', planet)} in {sign.title()} brings expansive energy to {planet_info.get('influence', 'the markets')}",
            'bearish': f"📉 {planet_info.get('name', planet)} in {sign.title()} suggests caution around {planet_info.get('influence', 'investments')}",
            'volatile': f"⚡ {planet_info.get('name', planet)} in {sign.title()} creates turbulent energy in {planet_info.get('influence', 'trading')}",
            'stable': f"🧘 {planet_info.get('name', planet)} in {sign.title()} offers steady wisdom for {planet_info.get('influence', 'long-term planning')}"
        }
        
        return PlanetaryInfluence(
            planet=planet_info.get('name', planet),
            sign=sign.title(),
            influence=influence,
            message=messages[influence],
            strength=random.uniform(0.3, 0.9)
        )
    
    def generate_daily_forecast(self) -> AstroForecast:
        """
        🔮 Generate today's astrological market forecast
        Reading the celestial signs for trading wisdom
        """
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Analyze key planets
        key_planets = ['mercury', 'venus', 'mars', 'jupiter', 'saturn']
        planetary_influences = [self.analyze_planetary_influence(planet) for planet in key_planets]
        
        # Determine overall energy
        bullish_count = sum(1 for p in planetary_influences if p.influence == 'bullish')
        bearish_count = sum(1 for p in planetary_influences if p.influence == 'bearish')
        
        if bullish_count > bearish_count:
            overall_energy = "positive cosmic flow 🌟"
        elif bearish_count > bullish_count:
            overall_energy = "contemplative celestial energy 🌙"
        else:
            overall_energy = "balanced universal harmony ⚖️"
        
        # Get lunar phase
        lunar_phase = self.get_lunar_phase()
        
        # Generate market prediction
        predictions = [
            "The stars suggest gentle growth like morning dew 🌱",
            "Celestial patterns indicate a day of mindful trading 🧘",
            "Planetary alignment favors patient investors 🌟",
            "The cosmos whispers of hidden opportunities 🔮",
            "Universal energy supports conscious wealth building ✨",
            "Galactic wisdom guides toward abundant thinking 🌌"
        ]
        
        cosmic_advice = [
            "Trust your intuition more than market noise 🔮",
            "Align your investments with your highest values 💫",
            "Practice gratitude for all financial abundance 🙏",
            "Stay centered in times of market turbulence 🧘",
            "Remember that true wealth includes inner peace 🌸",
            "Let love, not fear, guide your money decisions ❤️"
        ]
        
        return AstroForecast(
            date=today,
            overall_energy=overall_energy,
            planetary_influences=planetary_influences,
            lunar_phase=self.lunar_phases[lunar_phase],
            market_prediction=random.choice(predictions),
            cosmic_advice=random.choice(cosmic_advice)
        )
    
    def get_best_trading_days(self, days_ahead: int = 7) -> List[Dict[str, str]]:
        """
        📅 Find the most auspicious trading days in the coming week
        When cosmic energy aligns with market success
        """
        best_days = []
        
        for i in range(days_ahead):
            date = datetime.now() + timedelta(days=i)
            self.observer.date = date
            
            # Simple scoring based on lunar phase and random "cosmic energy"
            lunar_phase = self.get_lunar_phase()
            cosmic_score = random.uniform(0.3, 0.9)
            
            # Boost score for certain lunar phases
            if lunar_phase in ['waxing_crescent', 'first_quarter', 'waxing_gibbous']:
                cosmic_score += 0.1
            
            best_days.append({
                'date': date.strftime("%Y-%m-%d"),
                'weekday': date.strftime("%A"),
                'lunar_phase': self.lunar_phases[lunar_phase],
                'cosmic_energy': f"{cosmic_score:.1f}/1.0",
                'recommendation': "Favorable for growth investments 📈" if cosmic_score > 0.7 else "Good for reflection and analysis 🤔"
            })
        
        # Reset observer to current time
        self.observer.date = datetime.now()
        
        return sorted(best_days, key=lambda x: float(x['cosmic_energy'].split('/')[0]), reverse=True) 