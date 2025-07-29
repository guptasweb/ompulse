#!/usr/bin/env python3
"""
🧘 OmPulse - Spiritual Stock Market Tracker
Where Finance Meets Mindfulness
"""

import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

# Import our modules
from src.api import stock_routes, meditation_routes, astro_routes, portfolio_routes
from src.core.websocket_manager import ZenWebSocketManager

# Create the FastAPI app
app = FastAPI(
    title="🧘 OmPulse",
    description="Spiritual Stock Market Tracker - Where Finance Meets Mindfulness",
    version="1.0.0"
)

# Set up static files and templates
if not os.path.exists("static"):
    os.makedirs("static")
if not os.path.exists("templates"):
    os.makedirs("templates")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize WebSocket manager for real-time data
websocket_manager = ZenWebSocketManager()

# Include API routes
app.include_router(stock_routes.router, prefix="/api/stocks", tags=["stocks"])
app.include_router(meditation_routes.router, prefix="/api/meditation", tags=["meditation"])
app.include_router(astro_routes.router, prefix="/api/astro", tags=["astrology"])
app.include_router(portfolio_routes.router, prefix="/api/portfolio", tags=["portfolio"])

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Sacred home - the lotus center of our financial consciousness"""
    # Detect mobile user agent
    user_agent = request.headers.get("user-agent", "").lower()
    is_mobile = any(mobile in user_agent for mobile in ["mobile", "android", "iphone", "ipad"])
    
    if is_mobile:
        return templates.TemplateResponse("mobile.html", {"request": request})
    else:
        return templates.TemplateResponse("index.html", {"request": request})

@app.get("/mobile", response_class=HTMLResponse)
async def mobile_app(request: Request):
    """Direct mobile app access"""
    return templates.TemplateResponse("mobile.html", {"request": request})

@app.get("/health")
async def health_check():
    """Check if our financial chakras are aligned"""
    return {"status": "✨ All energy centers flowing harmoniously ✨"}

# PWA offline page
@app.get("/offline.html", response_class=HTMLResponse)
async def offline_page():
    """Offline spiritual guidance page"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🧘 OmPulse - Offline</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { 
                font-family: Arial, sans-serif; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white; 
                text-align: center; 
                padding: 50px 20px;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            .offline-content {
                max-width: 400px;
                background: rgba(255,255,255,0.1);
                padding: 40px 30px;
                border-radius: 20px;
                backdrop-filter: blur(10px);
            }
            .zen-icon { font-size: 4em; margin-bottom: 20px; }
            .offline-message { font-size: 1.2em; line-height: 1.6; margin-bottom: 30px; }
            .wisdom { font-style: italic; opacity: 0.8; }
        </style>
    </head>
    <body>
        <div class="offline-content">
            <div class="zen-icon">🧘</div>
            <h1>OmPulse</h1>
            <div class="offline-message">
                Connection to the market stream is temporarily clouded.
            </div>
            <div class="wisdom">
                "In the silence between breaths, infinite wisdom resides."
            </div>
            <br>
            <div style="font-size: 0.9em;">
                🌸 Your inner guidance remains strong, even offline
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    print("🧘 Starting OmPulse - Your spiritual journey to financial enlightenment begins...")
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True,
        log_level="info"
    ) 