"""
🧿 Portfolio Routes - Karmic Analysis of Your Investment Energy
Where your money meets your soul's purpose
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Optional, Any
from datetime import datetime
import random

router = APIRouter()

@router.post("/karmic-analysis")
async def analyze_portfolio_karma(portfolio: List[Dict[str, Any]]):
    """
    🔮 Analyze the karmic energy of your portfolio
    Understanding the spiritual signature of your investments
    
    Expected format: [{"symbol": "AAPL", "shares": 10, "sector": "Technology"}]
    """
    try:
        if not portfolio:
            raise HTTPException(status_code=400, detail="🌸 Please provide your portfolio for karmic analysis")
        
        # Analyze sector distribution
        sector_energy = {}
        total_positions = len(portfolio)
        
        for holding in portfolio:
            sector = holding.get("sector", "Unknown")
            if sector not in sector_energy:
                sector_energy[sector] = 0
            sector_energy[sector] += 1
        
        # Calculate sector percentages
        sector_percentages = {sector: (count/total_positions)*100 for sector, count in sector_energy.items()}
        
        # Assign karmic meanings to sectors
        sector_karma = {
            "Technology": "🔮 Innovation and future consciousness - you're investing in human evolution",
            "Healthcare": "💚 Healing and compassion energy - your money serves the wellness of humanity", 
            "Energy": "⚡ Power and transformation - you're channeling fundamental forces",
            "Financial": "💰 Abundance and flow - you understand money as energy exchange",
            "Consumer": "🛍️ Human needs and desires - you're connected to daily life rhythms",
            "Industrial": "🏭 Building and creating - your investments support material manifestation",
            "Real Estate": "🏠 Foundation and security - you value stability and shelter",
            "Utilities": "💡 Essential services - you're investing in life's basic needs",
            "Materials": "🌍 Earth's gifts - you honor the physical foundation of prosperity",
            "Communication": "📡 Connection and information - you support human communication"
        }
        
        # Calculate overall karma score
        positive_sectors = ["Healthcare", "Technology", "Renewable Energy", "Education"]
        karma_score = 0
        
        for sector, percentage in sector_percentages.items():
            if sector in positive_sectors:
                karma_score += percentage * 1.5
            else:
                karma_score += percentage * 1.0
        
        karma_score = min(karma_score, 100)  # Cap at 100
        
        # Determine karma level
        if karma_score >= 80:
            karma_level = "🌟 Enlightened Investor"
            karma_message = "Your portfolio radiates high vibrational energy and serves the greater good"
        elif karma_score >= 60:
            karma_level = "🌱 Conscious Investor"
            karma_message = "Your investments show awareness of their impact on the world"
        elif karma_score >= 40:
            karma_level = "⚖️ Balanced Investor"
            karma_message = "Your portfolio balances personal gain with some conscious choices"
        else:
            karma_level = "🌫️ Unconscious Investor"
            karma_message = "Consider aligning your investments more closely with your values"
        
        # Generate sector analysis
        sector_analysis = []
        for sector, percentage in sector_percentages.items():
            sector_analysis.append({
                "sector": sector,
                "percentage": round(percentage, 1),
                "karmic_meaning": sector_karma.get(sector, "✨ Every investment carries energy - choose consciously"),
                "energy_level": "High" if percentage > 25 else "Medium" if percentage > 10 else "Low"
            })
        
        return {
            "success": True,
            "karmic_analysis": {
                "karma_level": karma_level,
                "karma_score": round(karma_score, 1),
                "karma_message": karma_message,
                "total_positions": total_positions,
                "sector_distribution": sector_analysis,
                "spiritual_insights": [
                    "🧘 Your portfolio is a reflection of your consciousness",
                    "🌱 Money invested with intention creates positive ripples in the universe", 
                    "💫 Consider the energy behind each company you support",
                    "🙏 Gratitude for your investments multiplies their blessings"
                ]
            },
            "recommendations": {
                "high_vibe_sectors": ["Clean Energy", "Healthcare Innovation", "Education Technology", "Sustainable Agriculture"],
                "alignment_tip": "🌸 Choose companies whose missions resonate with your heart",
                "rebalancing_guidance": "⚖️ Consider reducing positions that don't align with your values"
            },
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ Unable to read your portfolio's karmic signature",
            "universal_truth": "💫 All wealth is energy - invest with love and wisdom"
        }

@router.get("/energy-assessment/{symbol}")
async def assess_stock_energy(symbol: str):
    """
    🔮 Assess the spiritual energy of a specific stock
    Understanding a company's vibrational frequency
    """
    try:
        # Mock energy assessment - in production you'd use ESG data, company mission, etc.
        symbol = symbol.upper()
        
        # Simplified energy categories based on common symbols
        energy_profiles = {
            "AAPL": {"energy": "Innovation", "vibration": "High", "purpose": "Creative expression through technology"},
            "GOOGL": {"energy": "Knowledge", "vibration": "High", "purpose": "Organizing world's information for all"},
            "TSLA": {"energy": "Transformation", "vibration": "Revolutionary", "purpose": "Sustainable transportation revolution"},
            "AMZN": {"energy": "Service", "vibration": "Expansive", "purpose": "Connecting people with what they need"},
            "MSFT": {"energy": "Empowerment", "vibration": "Stable", "purpose": "Empowering every person and organization"},
            "JNJ": {"energy": "Healing", "vibration": "Compassionate", "purpose": "Caring for human health and wellness"},
            "XOM": {"energy": "Extraction", "vibration": "Dense", "purpose": "Traditional energy resource management"},
            "WMT": {"energy": "Provision", "vibration": "Practical", "purpose": "Everyday low prices for all people"},
            "BRK.B": {"energy": "Wisdom", "vibration": "Grounded", "purpose": "Long-term value creation philosophy"}
        }
        
        profile = energy_profiles.get(symbol, {
            "energy": "Unknown", 
            "vibration": "Neutral", 
            "purpose": "Company purpose requires individual research"
        })
        
        # Generate random but realistic metrics
        metrics = {
            "esg_alignment": random.uniform(0.3, 0.9),
            "innovation_factor": random.uniform(0.2, 0.95),
            "social_impact": random.uniform(0.1, 0.8),
            "environmental_consciousness": random.uniform(0.2, 0.85),
            "employee_wellbeing": random.uniform(0.4, 0.9)
        }
        
        # Calculate overall energy score
        energy_score = sum(metrics.values()) / len(metrics) * 100
        
        # Energy level interpretation
        if energy_score >= 75:
            energy_level = "🌟 High Vibrational"
            energy_advice = "This stock aligns with conscious investing principles"
        elif energy_score >= 50:
            energy_level = "🌱 Growing Consciousness"
            energy_advice = "This company shows promise for positive impact"
        elif energy_score >= 25:
            energy_level = "⚖️ Mixed Energy"
            energy_advice = "Research this company's values and practices carefully"
        else:
            energy_level = "🌫️ Dense Energy"
            energy_advice = "Consider if this investment aligns with your highest values"
        
        return {
            "success": True,
            "symbol": symbol,
            "energy_assessment": {
                "energy_type": profile["energy"],
                "vibrational_frequency": profile["vibration"],
                "company_purpose": profile["purpose"],
                "energy_level": energy_level,
                "energy_score": round(energy_score, 1),
                "spiritual_advice": energy_advice
            },
            "detailed_metrics": {
                "esg_alignment": round(metrics["esg_alignment"], 2),
                "innovation_factor": round(metrics["innovation_factor"], 2),
                "social_impact": round(metrics["social_impact"], 2),
                "environmental_consciousness": round(metrics["environmental_consciousness"], 2),
                "employee_wellbeing": round(metrics["employee_wellbeing"], 2)
            },
            "investment_meditation": f"🧘 Before investing in {symbol}, ask: Does this company's mission align with my values?",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"🌫️ Unable to assess {symbol}'s energy signature",
            "universal_guidance": "💫 Trust your intuition about investments - your inner wisdom knows best"
        }

@router.get("/esg-harmony-score")
async def calculate_esg_harmony_score(symbols: str):
    """
    🌍 Calculate the Environmental, Social, Governance harmony of your watchlist
    Understanding how your investments serve the planet and humanity
    """
    try:
        symbol_list = [s.strip().upper() for s in symbols.split(",") if s.strip()]
        
        if len(symbol_list) > 15:
            symbol_list = symbol_list[:15]  # Limit for performance
        
        # Mock ESG scores - in production use real ESG data
        esg_scores = {}
        total_environmental = 0
        total_social = 0
        total_governance = 0
        
        for symbol in symbol_list:
            # Generate realistic but random ESG scores
            env_score = random.uniform(0.2, 0.9)
            social_score = random.uniform(0.3, 0.85)
            gov_score = random.uniform(0.4, 0.95)
            
            esg_scores[symbol] = {
                "environmental": env_score,
                "social": social_score,
                "governance": gov_score,
                "overall": (env_score + social_score + gov_score) / 3
            }
            
            total_environmental += env_score
            total_social += social_score
            total_governance += gov_score
        
        # Calculate averages
        num_stocks = len(symbol_list)
        avg_environmental = total_environmental / num_stocks
        avg_social = total_social / num_stocks
        avg_governance = total_governance / num_stocks
        overall_harmony = (avg_environmental + avg_social + avg_governance) / 3
        
        # Harmony level interpretation
        if overall_harmony >= 0.8:
            harmony_level = "🌟 Enlightened Portfolio"
            harmony_message = "Your investments radiate positive energy for planet and people"
        elif overall_harmony >= 0.6:
            harmony_level = "🌱 Conscious Portfolio"
            harmony_message = "Your portfolio shows strong awareness of ESG principles"
        elif overall_harmony >= 0.4:
            harmony_level = "⚖️ Balanced Portfolio"
            harmony_message = "Some good ESG choices with room for improvement"
        else:
            harmony_level = "🌫️ Unconscious Portfolio"
            harmony_message = "Consider aligning your investments with sustainability values"
        
        return {
            "success": True,
            "esg_harmony": {
                "harmony_level": harmony_level,
                "harmony_score": round(overall_harmony * 100, 1),
                "harmony_message": harmony_message,
                "environmental_score": round(avg_environmental * 100, 1),
                "social_score": round(avg_social * 100, 1),
                "governance_score": round(avg_governance * 100, 1)
            },
            "individual_scores": {symbol: {
                "environmental": round(scores["environmental"] * 100, 1),
                "social": round(scores["social"] * 100, 1),
                "governance": round(scores["governance"] * 100, 1),
                "overall": round(scores["overall"] * 100, 1)
            } for symbol, scores in esg_scores.items()},
            "improvement_suggestions": [
                "🌱 Consider adding more renewable energy companies",
                "🤝 Look for companies with strong labor practices",
                "🏛️ Prioritize companies with transparent governance",
                "🌍 Research each company's environmental commitments"
            ],
            "cosmic_truth": "🌌 Your investment choices ripple through the universe - choose wisely",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ ESG harmony calculation temporarily unavailable",
            "eternal_wisdom": "💫 The universe rewards conscious choices in all areas of life"
        }

@router.get("/portfolio-chakra-alignment")
async def analyze_portfolio_chakra_alignment(symbols: str):
    """
    🌈 Analyze how your portfolio aligns with the seven chakras
    Understanding the energetic balance of your investments
    """
    try:
        symbol_list = [s.strip().upper() for s in symbols.split(",") if s.strip()]
        
        # Chakra associations with investment types
        chakra_sectors = {
            "root": ["REITs", "Utilities", "Banks", "Insurance", "Basic Materials"],
            "sacral": ["Consumer Discretionary", "Entertainment", "Food & Beverage", "Hospitality"],
            "solar_plexus": ["Energy", "Industrials", "Defense", "Automotive"],
            "heart": ["Healthcare", "Social Impact", "ESG Funds", "Education"],
            "throat": ["Communications", "Media", "Telecommunications", "Software"],
            "third_eye": ["Technology", "AI", "Research", "Innovation"],
            "crown": ["Spiritual Companies", "Meditation Apps", "Wellness", "Consciousness"]
        }
        
        # Mock chakra alignment scoring
        chakra_scores = {
            "root": random.uniform(0.3, 0.8),
            "sacral": random.uniform(0.2, 0.7),
            "solar_plexus": random.uniform(0.4, 0.9),
            "heart": random.uniform(0.5, 0.95),
            "throat": random.uniform(0.3, 0.85),
            "third_eye": random.uniform(0.6, 0.95),
            "crown": random.uniform(0.1, 0.6)
        }
        
        chakra_meanings = {
            "root": "🔴 Root Chakra - Security, stability, basic needs fulfillment",
            "sacral": "🧡 Sacral Chakra - Creativity, pleasure, emotional flow", 
            "solar_plexus": "💛 Solar Plexus - Personal power, confidence, action",
            "heart": "💚 Heart Chakra - Love, compassion, healing, connection",
            "throat": "💙 Throat Chakra - Communication, truth, expression",
            "third_eye": "💜 Third Eye - Intuition, wisdom, innovation, vision",
            "crown": "🤍 Crown Chakra - Spiritual connection, higher purpose"
        }
        
        # Find strongest and weakest chakras
        strongest_chakra = max(chakra_scores, key=chakra_scores.get)
        weakest_chakra = min(chakra_scores, key=chakra_scores.get)
        
        # Calculate overall balance
        balance_score = 1 - (max(chakra_scores.values()) - min(chakra_scores.values()))
        
        return {
            "success": True,
            "chakra_analysis": {
                "overall_balance": round(balance_score * 100, 1),
                "strongest_chakra": {
                    "chakra": strongest_chakra,
                    "score": round(chakra_scores[strongest_chakra] * 100, 1),
                    "meaning": chakra_meanings[strongest_chakra]
                },
                "weakest_chakra": {
                    "chakra": weakest_chakra,
                    "score": round(chakra_scores[weakest_chakra] * 100, 1),
                    "meaning": chakra_meanings[weakest_chakra]
                },
                "individual_chakras": {
                    chakra: {
                        "score": round(score * 100, 1),
                        "meaning": chakra_meanings[chakra],
                        "strength": "Strong" if score > 0.7 else "Moderate" if score > 0.4 else "Weak"
                    }
                    for chakra, score in chakra_scores.items()
                }
            },
            "rebalancing_suggestions": [
                f"🔴 Strengthen Root: Add utility or REIT stocks for stability",
                f"💚 Open Heart: Include more healthcare and social impact investments",
                f"💜 Awaken Third Eye: Increase technology and innovation positions",
                f"🤍 Connect Crown: Consider companies with spiritual or wellness missions"
            ],
            "meditation": f"🧘 Your portfolio currently channels strongest energy through your {strongest_chakra} chakra",
            "cosmic_balance": "🌈 A balanced portfolio nourishes all chakras and creates harmonious abundance",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "🌫️ Chakra alignment reading temporarily clouded",
            "universal_truth": "🌈 True wealth flows when all energy centers are balanced and open"
        } 