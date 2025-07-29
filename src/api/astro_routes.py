"""
🔮 Astrology Routes - Celestial Guidance for Market Wisdom
Where cosmic consciousness meets financial intelligence
"""

from fastapi import APIRouter, HTTPException
from typing import Optional
from datetime import datetime

from ..core.astro_tracker import AstroInvestTracker

router = APIRouter()

# Initialize astro tracker
astro_tracker = AstroInvestTracker()

@router.get("/daily-forecast")
async def get_daily_astro_forecast():
    """
    🌟 Receive today's astrological market forecast
    Reading celestial patterns for trading wisdom
    """
    try:
        forecast = astro_tracker.generate_daily_forecast()
        
        return {
            "success": True,
            "forecast": {
                "date": forecast.date,
                "overall_energy": forecast.overall_energy,
                "planetary_influences": [
                    {
                        "planet": influence.planet,
                        "sign": influence.sign,
                        "influence": influence.influence,
                        "message": influence.message,
                        "strength": round(influence.strength, 2)
                    }
                    for influence in forecast.planetary_influences
                ],
                "lunar_phase": forecast.lunar_phase,
                "market_prediction": forecast.market_prediction,
                "cosmic_advice": forecast.cosmic_advice
            },
            "mystical_note": "🌌 The stars whisper secrets to those who listen with their hearts",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ The cosmic signals are unclear today",
            "backup_guidance": "✨ Trust your inner knowing above all external signs"
        }

@router.get("/lunar-phase")
async def get_current_lunar_phase():
    """
    🌙 Discover the current lunar energy and its market influence
    How the moon's cycle affects trading rhythms
    """
    try:
        phase = astro_tracker.get_lunar_phase()
        phase_info = astro_tracker.lunar_phases.get(phase, "Unknown phase")
        
        lunar_trading_advice = {
            "new_moon": "🌑 Perfect time for setting new investment intentions and starting fresh financial plans",
            "waxing_crescent": "🌒 Energy builds for accumulating positions and gradual growth strategies",
            "first_quarter": "🌓 Decision time - take action on investment plans you've been considering",
            "waxing_gibbous": "🌔 Strong momentum phase - good for adding to winning positions",
            "full_moon": "🌕 Peak energy - expect maximum volatility and emotional trading",
            "waning_gibbous": "🌖 Time for reflection and profit-taking on successful trades",
            "last_quarter": "🌗 Release what's not working - good for portfolio cleanup",
            "waning_crescent": "🌘 Clearing phase - prepare for new opportunities by simplifying"
        }
        
        return {
            "success": True,
            "lunar_phase": {
                "phase": phase,
                "description": phase_info,
                "trading_advice": lunar_trading_advice.get(phase, "Trust the natural cycles"),
                "energy_level": "High" if "full" in phase else "Medium" if "quarter" in phase else "Gentle"
            },
            "moon_wisdom": "🌙 The moon reminds us that all things have cycles - including markets",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ Unable to read lunar energies at this time",
            "universal_truth": "🌙 In all phases, the moon teaches us about timing and patience"
        }

@router.get("/best-trading-days")
async def get_best_trading_days(days_ahead: int = 7):
    """
    📅 Find the most auspicious trading days in the coming period
    When cosmic energy aligns with market success
    """
    try:
        if days_ahead > 30:
            days_ahead = 30  # Limit to 30 days
        
        best_days = astro_tracker.get_best_trading_days(days_ahead)
        
        return {
            "success": True,
            "forecast_period": f"Next {days_ahead} days",
            "best_trading_days": best_days,
            "cosmic_strategy": "🌟 Align your most important trades with high-energy cosmic days",
            "gentle_reminder": "🧘 Even on challenging cosmic days, mindful trading always prevails",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ Cosmic calendar temporarily clouded",
            "eternal_wisdom": "⏰ Every day holds potential when approached with presence and wisdom"
        }

@router.get("/planetary-influence/{planet}")
async def get_planetary_influence(planet: str):
    """
    🪐 Analyze a specific planet's current market influence
    Deep dive into individual celestial energies
    """
    try:
        valid_planets = ['mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
        
        if planet.lower() not in valid_planets:
            raise HTTPException(
                status_code=400,
                detail=f"🌟 Please choose from: {', '.join(valid_planets)}"
            )
        
        influence = astro_tracker.analyze_planetary_influence(planet.lower())
        
        # Get sign information
        sign = astro_tracker.get_planet_sign(planet.lower())
        sign_info = astro_tracker.zodiac_signs.get(sign, {})
        
        return {
            "success": True,
            "planetary_analysis": {
                "planet": influence.planet,
                "current_sign": influence.sign,
                "market_influence": influence.influence,
                "cosmic_message": influence.message,
                "strength": round(influence.strength, 2),
                "sign_energy": sign_info.get("energy", "unknown"),
                "element": sign_info.get("element", "unknown"),
                "market_mood": sign_info.get("market_mood", "neutral")
            },
            "interpretation": f"🔮 {influence.planet} in {influence.sign} brings {influence.influence} energy to the markets",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"🌫️ Unable to read {planet}'s cosmic signature",
            "cosmic_truth": "🌌 All planets work together in the grand symphony of the universe"
        }

@router.get("/mercury-retrograde")
async def check_mercury_retrograde():
    """
    ☿ Check if Mercury is in retrograde and get trading guidance
    Special wisdom for communication planet's backward dance
    """
    try:
        # Simplified check - in production you'd use more sophisticated astronomical calculations
        import random
        
        # Mock retrograde check (in real implementation, calculate actual Mercury retrograde periods)
        is_retrograde = random.choice([True, False])
        
        if is_retrograde:
            guidance = {
                "status": "🔄 Mercury is in Retrograde",
                "trading_advice": [
                    "📝 Double-check all trade details before executing",
                    "💬 Avoid major communication-dependent deals",
                    "🔍 Review and revise existing positions rather than starting new ones",
                    "🧘 Practice extra patience with technology and platforms",
                    "📚 Great time for research and education, not action"
                ],
                "opportunities": [
                    "🔮 Re-examine old investment ideas with fresh perspective",
                    "📊 Revisit and rebalance existing portfolio allocations",
                    "💡 Reconnect with financial advisors and mentors"
                ],
                "mantra": "🕉️ In retrograde, I retreat, reflect, and prepare for forward motion"
            }
        else:
            guidance = {
                "status": "➡️ Mercury is Direct",
                "trading_advice": [
                    "💨 Communications flow smoothly - good for negotiations",
                    "📱 Technology works in your favor for trading",
                    "🚀 Forward momentum supports new investment initiatives",
                    "📞 Network and share ideas with other investors",
                    "⚡ Quick decisions are supported by clear thinking"
                ],
                "opportunities": [
                    "🌟 Launch new investment strategies",
                    "📈 Execute plans you've been developing",
                    "🤝 Make important financial agreements"
                ],
                "mantra": "🕉️ I move forward with clarity and confident communication"
            }
        
        return {
            "success": True,
            "mercury_status": guidance,
            "cosmic_note": "☿ Mercury governs communication, technology, and quick thinking in markets",
            "duration": "Retrograde periods typically last 3-4 weeks, occurring 3-4 times per year",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ Mercury's message is unclear",
            "universal_wisdom": "💫 Whether direct or retrograde, mindful communication always serves"
        }

@router.get("/cosmic-market-cycles")
async def get_cosmic_market_cycles():
    """
    🌌 Understand major cosmic cycles affecting long-term market trends
    Big picture astrological influences on financial cycles
    """
    try:
        cycles_info = {
            "jupiter_cycle": {
                "duration": "12 years",
                "influence": "Growth and expansion cycles",
                "description": "🪐 Jupiter's orbit creates major economic expansion and contraction cycles",
                "trading_insight": "Major bull markets often align with Jupiter's beneficial aspects"
            },
            "saturn_cycle": {
                "duration": "29.5 years", 
                "influence": "Structure and discipline cycles",
                "description": "🪐 Saturn brings lessons in financial responsibility and long-term thinking",
                "trading_insight": "Bear markets and corrections often coincide with challenging Saturn aspects"
            },
            "saturn_jupiter_conjunction": {
                "duration": "20 years",
                "influence": "Major societal and economic shifts",
                "description": "🌟 The 'Great Conjunction' marks new eras in economic thinking",
                "trading_insight": "These conjunctions often coincide with technological and financial innovations"
            },
            "uranus_cycle": {
                "duration": "84 years",
                "influence": "Innovation and disruption cycles", 
                "description": "⚡ Uranus brings sudden changes and technological revolutions",
                "trading_insight": "Disruptive technologies often emerge during key Uranus transits"
            }
        }
        
        return {
            "success": True,
            "cosmic_cycles": cycles_info,
            "current_phase": "🌟 We're in an era of technological transformation guided by Uranus energy",
            "investment_wisdom": "🧘 Understanding these cycles helps with long-term portfolio planning",
            "mystic_note": "🔮 As above, so below - cosmic patterns reflect in earthly markets",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ Cosmic cycle information temporarily unavailable", 
            "eternal_truth": "🌌 The universe operates in perfect cycles, and so do markets"
        } 