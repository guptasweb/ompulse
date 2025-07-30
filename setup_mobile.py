#!/usr/bin/env python3
"""
📱 OmPulse Mobile Setup
Quick configuration for your spiritual mobile app
"""

import os
import sys
import subprocess
import socket
from pathlib import Path

def print_banner():
    """Display the mobile setup banner"""
    banner = """
    📱 ═══════════════════════════════════════════════════════════ 📱
                           
                        🌸 OmPulse Mobile Setup 🌸
                    Converting Spiritual Wisdom to Mobile
                    
    📱 ═══════════════════════════════════════════════════════════ 📱
    """
    print(banner)

def get_local_ip():
    """Get the local IP address for mobile access"""
    try:
        # Connect to a remote address to find local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "localhost"

def check_mobile_files():
    """Check if mobile files exist"""
    required_files = [
        "templates/mobile.html",
        "static/manifest.json", 
        "static/sw.js"
    ]
    
    missing = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing.append(file_path)
    
    return missing

def create_static_directories():
    """Create required static directories"""
    directories = [
        "static/icons",
        "static/screenshots"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {directory}")

def create_simple_icons():
    """Create simple placeholder icons for PWA"""
    icon_content = """
    # This is where you would place your app icons
    # For now, you can:
    # 1. Use online tools like https://favicon.io to generate icons
    # 2. Create PNG icons in these sizes: 72x72, 96x96, 128x128, 144x144, 152x152, 192x192, 384x384, 512x512
    # 3. Place them in the static/icons/ directory
    # 4. Name them as: icon-{size}.png (e.g., icon-192x192.png)
    
    For a quick start, you can use emoji-based icons:
    🧘 - Main app icon (meditation/spiritual theme)
    🪷 - Home/dashboard icon  
    🔮 - Astrology section icon
    💫 - Meditation/wisdom icon
    """
    
    with open("static/icons/README.txt", "w") as f:
        f.write(icon_content)
    
    print("📝 Created icon guidance in static/icons/README.txt")

def setup_pwa():
    """Set up Progressive Web App configuration"""
    print("\n🌐 Setting up Progressive Web App (PWA)...")
    
    # Check if files exist
    missing = check_mobile_files()
    if missing:
        print("❌ Missing mobile files:")
        for file_path in missing:
            print(f"   - {file_path}")
        print("\n💫 These files should have been created automatically.")
        print("   If they're missing, please run the main setup again.")
        return False
    
    # Create directories
    create_static_directories()
    create_simple_icons()
    
    print("✅ PWA setup complete!")
    return True

def setup_kivy():
    """Set up Kivy mobile app"""
    print("\n📲 Setting up Native Kivy App...")
    
    # Check if Kivy files exist
    if not Path("mobile_kivy_app.py").exists():
        print("❌ mobile_kivy_app.py not found")
        return False
    
    # Check if buildozer spec exists
    if not Path("buildozer.spec").exists():
        print("❌ buildozer.spec not found")
        return False
    
    # Check if Kivy is installed
    try:
        import kivy
        print("✅ Kivy is already installed")
    except ImportError:
        print("📦 Installing Kivy...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "kivy[base]", "requests", "plyer"])
            print("✅ Kivy installed successfully")
        except Exception as e:
            print(f"❌ Failed to install Kivy: {e}")
            return False
    
    print("✅ Kivy setup complete!")
    print("💫 To build APK, you'll need Linux/WSL and run: buildozer android debug")
    return True

def show_usage_instructions(local_ip):
    """Show how to use the mobile app"""
    print(f"\n🌸 Mobile App Ready! Here's how to use it:")
    
    print(f"\n📱 PWA (Recommended):")
    print(f"   1. Start OmPulse: python start.py")
    print(f"   2. On your Android phone, open Chrome and visit:")
    print(f"      http://{local_ip}:8000")
    print(f"      or")
    print(f"      http://{local_ip}:8000/mobile")
    print(f"   3. Tap 'Add to Home Screen' when prompted")
    print(f"   4. Enjoy your spiritual stock tracker! 🧘")
    
    print(f"\n📲 Kivy Native App:")
    print(f"   1. Test locally: python mobile_kivy_app.py")
    print(f"   2. Build APK: buildozer android debug (Linux/WSL only)")
    print(f"   3. Install APK on your Android device")
    
    print(f"\n💫 Pro Tips:")
    print(f"   - Make sure your phone and computer are on the same WiFi")
    print(f"   - If {local_ip} doesn't work, try your computer's IP address")
    print(f"   - For PWA, Chrome will handle updates automatically")
    print(f"   - For best experience, add OmPulse to your home screen")

def main():
    """Main setup function"""
    print_banner()
    
    print("🌱 Preparing your spiritual stock tracker for mobile consciousness...")
    
    # Get local IP for mobile access
    local_ip = get_local_ip()
    print(f"🔍 Detected local IP: {local_ip}")
    
    # Ask user which approach they want
    print("\n🌟 Choose your mobile approach:")
    print("   1. 🌐 Progressive Web App (PWA) - Quick & Easy")
    print("   2. 📲 Native Kivy App - Advanced Users")
    print("   3. 🎯 Both approaches")
    
    choice = input("\n💫 Enter your choice (1/2/3): ").strip()
    
    success = True
    
    if choice in ["1", "3"]:
        success &= setup_pwa()
    
    if choice in ["2", "3"]:
        success &= setup_kivy()
    
    if choice not in ["1", "2", "3"]:
        print("❌ Invalid choice. Please run the script again.")
        return
    
    if success:
        show_usage_instructions(local_ip)
        print(f"\n🙏 Your OmPulse mobile app is ready!")
        print(f"🌸 May your mobile investing journey be filled with wisdom and abundance!")
        print(f"🧘 Namaste! 🧘")
    else:
        print(f"\n🌫️ Some issues occurred during setup.")
        print(f"💫 Please check the errors above and try again.")
        print(f"🙏 The universe sometimes requires patience with technology.")

if __name__ == "__main__":
    main() 