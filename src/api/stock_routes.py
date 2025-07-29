"""
📈 Stock Routes - Sacred Endpoints for Market Wisdom
Where API meets enlightenment
"""

from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect, Query
from typing import List, Optional
import asyncio
from datetime import datetime

from ..core.stock_fetcher import ZenStockFetcher, StockPulse
from ..core.websocket_manager import websocket_manager

router = APIRouter()

# Initialize our zen stock fetcher
stock_fetcher = ZenStockFetcher()

@router.get("/pulse/{symbol}")
async def get_stock_pulse(symbol: str):
    """
    🧘 Get the current spiritual pulse of a stock
    Channeling the energy of a single stock's journey
    """
    try:
        pulse = await stock_fetcher.get_stock_pulse(symbol.upper())
        return {
            "success": True,
            "pulse": {
                "symbol": pulse.symbol,
                "current_price": pulse.current_price,
                "change": pulse.change,
                "change_percent": pulse.change_percent,
                "volume": pulse.volume,
                "market_cap": pulse.market_cap,
                "energy_level": pulse.energy_level,
                "spiritual_message": pulse.spiritual_message
            },
            "zen_moment": "🌸 Every price movement is a teaching from the universe",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"🌫️ The market's energy is clouded for {symbol}. Please try again with patience."
        )

@router.post("/watchlist/pulse")
async def get_watchlist_pulse(symbols: List[str]):
    """
    🌈 Get the collective pulse of your sacred watchlist
    Reading the combined energy of multiple stocks
    """
    try:
        if len(symbols) > 20:
            raise HTTPException(
                status_code=400,
                detail="🧘 Please limit your watchlist to 20 symbols for optimal energy flow"
            )
        
        # Clean symbols
        clean_symbols = [s.upper().strip() for s in symbols if s.strip()]
        
        # Get all pulses
        pulses = await stock_fetcher.get_multiple_pulses(clean_symbols)
        
        # Get market sentiment
        sentiment = stock_fetcher.get_market_sentiment(pulses)
        
        # Format response
        pulse_data = []
        for pulse in pulses:
            pulse_data.append({
                "symbol": pulse.symbol,
                "current_price": pulse.current_price,
                "change": pulse.change,
                "change_percent": pulse.change_percent,
                "volume": pulse.volume,
                "energy_level": pulse.energy_level,
                "spiritual_message": pulse.spiritual_message
            })
        
        return {
            "success": True,
            "watchlist": pulse_data,
            "market_sentiment": sentiment,
            "collective_wisdom": "🌊 Your watchlist flows together like a river toward abundance",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="🌫️ The collective energy is unclear. Please breathe and try again."
        )

@router.get("/market/sentiment")
async def get_market_sentiment(symbols: str = Query("AAPL,GOOGL,MSFT,TSLA,AMZN")):
    """
    🌍 Feel the overall pulse of the market consciousness
    Reading the emotional state of the financial collective
    """
    try:
        symbol_list = [s.strip().upper() for s in symbols.split(",") if s.strip()]
        
        if len(symbol_list) > 10:
            symbol_list = symbol_list[:10]  # Limit for performance
        
        pulses = await stock_fetcher.get_multiple_pulses(symbol_list)
        sentiment = stock_fetcher.get_market_sentiment(pulses)
        
        return {
            "success": True,
            "sentiment": sentiment,
            "symbols_analyzed": len(symbol_list),
            "cosmic_message": "🔮 The market breathes with the rhythm of collective consciousness",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="🌫️ The market's emotional state is unclear at this moment"
        )

@router.websocket("/live-stream")
async def websocket_live_stream(websocket: WebSocket, symbols: str = "AAPL,GOOGL,MSFT"):
    """
    🌊 Sacred stream of real-time market consciousness
    Connect to the live flow of stock energies
    """
    symbol_list = [s.strip().upper() for s in symbols.split(",") if s.strip()]
    
    await websocket_manager.connect(websocket, symbol_list)
    
    try:
        # Start the live stream in background
        stream_task = asyncio.create_task(
            websocket_manager.start_live_stream(stock_fetcher, symbol_list, interval_seconds=30)
        )
        
        # Keep connection alive and listen for client messages
        while True:
            try:
                data = await websocket.receive_text()
                message = eval(data)  # Simple parsing - in production use json.loads with error handling
                
                if message.get("action") == "update_symbols":
                    new_symbols = message.get("symbols", [])
                    websocket_manager.user_watchlists[websocket] = new_symbols
                    
                    await websocket_manager.send_personal_message({
                        "type": "confirmation",
                        "message": f"🌸 Watchlist updated with {len(new_symbols)} symbols",
                        "symbols": new_symbols
                    }, websocket)
                
                elif message.get("action") == "meditation_request":
                    await websocket_manager.send_meditation_reminder()
                
            except WebSocketDisconnect:
                break
            except Exception as e:
                await websocket_manager.send_personal_message({
                    "type": "error",
                    "message": "🌫️ Energy disruption in the stream. Please stay centered."
                }, websocket)
                
    except WebSocketDisconnect:
        pass
    finally:
        websocket_manager.disconnect(websocket)
        if 'stream_task' in locals():
            stream_task.cancel()

@router.get("/popular-symbols")
async def get_popular_symbols():
    """
    ⭐ Discover popular stocks flowing with abundant energy
    Symbols that resonate with collective investment consciousness
    """
    popular_stocks = {
        "tech_giants": ["AAPL", "GOOGL", "MSFT", "AMZN", "META"],
        "growth_energy": ["TSLA", "NVDA", "NFLX", "CRM", "ZOOM"],
        "stable_flow": ["BRK.B", "JNJ", "PG", "KO", "WMT"],
        "innovation_spirit": ["PLTR", "RBLX", "COIN", "SQ", "SHOP"],
        "renewable_consciousness": ["ENPH", "SEDG", "PLUG", "ICLN", "QCLN"]
    }
    
    return {
        "success": True,
        "categories": popular_stocks,
        "spiritual_note": "🌱 Choose stocks that align with your values and resonate with your soul's purpose",
        "mindful_tip": "🧘 Diversification brings balance, just like a balanced life brings peace"
    }

@router.get("/symbol/search/{query}")
async def search_symbols(query: str):
    """
    🔍 Search for stocks with mindful intention
    Find symbols that call to your investment spirit
    """
    # This is a simplified version - in production you'd use a real symbol search API
    mock_results = [
        {"symbol": "AAPL", "name": "Apple Inc.", "energy": "innovative prosperity"},
        {"symbol": "GOOGL", "name": "Alphabet Inc.", "energy": "infinite knowledge"},
        {"symbol": "TSLA", "name": "Tesla Inc.", "energy": "revolutionary transformation"},
        {"symbol": "AMZN", "name": "Amazon.com Inc.", "energy": "abundant distribution"},
        {"symbol": "MSFT", "name": "Microsoft Corp.", "energy": "foundational strength"}
    ]
    
    # Filter based on query
    filtered = [stock for stock in mock_results if query.upper() in stock["symbol"] or query.lower() in stock["name"].lower()]
    
    return {
        "success": True,
        "query": query,
        "results": filtered[:10],  # Limit results
        "zen_guidance": "🔮 Let intuition guide you to the right investments for your journey"
    } 