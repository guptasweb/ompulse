#!/usr/bin/env python3
"""
🧘 OmPulse Startup Script
Quick launcher for your spiritual stock market journey
"""

import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import yfinance
        import fastapi
        import uvicorn
        import ephem
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("🌱 Installing dependencies...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Dependencies installed successfully")
            return True
        except Exception as install_error:
            print(f"❌ Failed to install dependencies: {install_error}")
            return False

def print_banner():
    """Display the spiritual banner"""
    banner = """
    🧘 ═══════════════════════════════════════════════════════════ 🧘
                           
                           🌸 OmPulse 🌸
                   Spiritual Stock Market Tracker
                    Where Finance Meets Mindfulness
                           
    🧘 ═══════════════════════════════════════════════════════════ 🧘
    """
    print(banner)

def main():
    """Main startup function"""
    print_banner()
    
    print("🌱 Initializing your conscious investing journey...")
    
    # Check if we're in the right directory
    if not Path("main.py").exists():
        print("❌ Please run this script from the OmPulse root directory")
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Dependency check failed. Please install manually:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    
    print("🔮 Starting the sacred market stream...")
    
    try:
        # Start the FastAPI server
        import uvicorn
        
        print("🌊 OmPulse is now flowing at: http://localhost:8000")
        print("🌸 Opening your browser to the sacred space...")
        
        # Open browser after a short delay
        def open_browser():
            time.sleep(2)
            webbrowser.open("http://localhost:8000")
        
        import threading
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        print("\n💫 Spiritual Market Wisdom:")
        print("   • Press Ctrl+C to mindfully close the application")
        print("   • Your portfolio is a reflection of your consciousness")
        print("   • May your investments serve your highest good")
        print("   • Trust the process and stay centered 🧘\n")
        
        # Run the app
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
        
    except KeyboardInterrupt:
        print("\n\n🙏 Thank you for using OmPulse")
        print("🌸 May your financial journey be filled with wisdom and abundance")
        print("🧘 Namaste! 🧘")
        
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("🌫️ The cosmic energies seem disrupted. Please check your setup.")
        print("💫 Try running: python main.py")

if __name__ == "__main__":
    main() 