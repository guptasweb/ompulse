#!/usr/bin/env python3
"""
🧘 OmPulse Mobile - Native Android App with Kivy
Spiritual Stock Market Tracker for Android devices
"""

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.utils import get_color_from_hex
import requests
import json
import asyncio
import threading

kivy.require('2.0.0')

class ZenBackground(BoxLayout):
    """Spiritual background widget with gradient"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.4, 0.49, 0.91, 1)  # Purple-blue gradient simulation
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
        self.bind(size=self._update_rect, pos=self._update_rect)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MeditationPopup(Popup):
    """Spiritual meditation popup"""
    def __init__(self, message, **kwargs):
        super().__init__(**kwargs)
        self.title = "🧘 Meditation Moment"
        self.size_hint = (0.8, 0.6)
        
        content = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Meditation message
        message_label = Label(
            text=message,
            text_size=(None, None),
            halign='center',
            valign='middle',
            font_size='18sp',
            markup=True
        )
        content.add_widget(message_label)
        
        # Close button
        close_btn = Button(
            text="Thank You 🙏",
            size_hint=(0.6, 0.3),
            pos_hint={'center_x': 0.5},
            background_color=get_color_from_hex('#667eea')
        )
        close_btn.bind(on_press=self.dismiss)
        content.add_widget(close_btn)
        
        self.content = content

class StockCard(BoxLayout):
    """Individual stock display card"""
    def __init__(self, symbol, price, change, change_percent, message, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = '100dp'
        self.padding = 10
        self.spacing = 5
        
        # Background
        with self.canvas.before:
            Color(1, 1, 1, 0.1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        # Header with symbol and price
        header = BoxLayout(orientation='horizontal', size_hint_y=0.4)
        
        symbol_label = Label(
            text=f"{symbol}",
            font_size='20sp',
            bold=True,
            size_hint_x=0.4,
            halign='left'
        )
        symbol_label.bind(size=symbol_label.setter('text_size'))
        
        price_label = Label(
            text=f"${price:.2f}",
            font_size='18sp',
            size_hint_x=0.6,
            halign='right'
        )
        price_label.bind(size=price_label.setter('text_size'))
        
        header.add_widget(symbol_label)
        header.add_widget(price_label)
        
        # Change info
        change_color = [0.3, 0.7, 0.3, 1] if change >= 0 else [0.9, 0.3, 0.3, 1]
        change_text = f"+{change:.2f} ({change_percent:.1f}%)" if change >= 0 else f"{change:.2f} ({change_percent:.1f}%)"
        
        change_label = Label(
            text=change_text,
            font_size='14sp',
            color=change_color,
            size_hint_y=0.3,
            halign='right'
        )
        change_label.bind(size=change_label.setter('text_size'))
        
        # Spiritual message
        message_label = Label(
            text=message,
            font_size='12sp',
            color=[1, 1, 1, 0.8],
            size_hint_y=0.3,
            halign='center',
            text_size=(None, None)
        )
        message_label.bind(size=message_label.setter('text_size'))
        
        self.add_widget(header)
        self.add_widget(change_label)
        self.add_widget(message_label)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class HomeTab(TabbedPanelItem):
    """Home tab with live stock data"""
    def __init__(self, app_instance, **kwargs):
        super().__init__(**kwargs)
        self.text = "🪷 Home"
        self.app_instance = app_instance
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Input for symbols
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='50dp', spacing=10)
        
        self.symbol_input = TextInput(
            text="AAPL,GOOGL,MSFT,TSLA",
            multiline=False,
            size_hint_x=0.7,
            hint_text="Enter symbols..."
        )
        
        update_btn = Button(
            text="Update",
            size_hint_x=0.3,
            background_color=get_color_from_hex('#667eea')
        )
        update_btn.bind(on_press=self.update_symbols)
        
        input_layout.add_widget(self.symbol_input)
        input_layout.add_widget(update_btn)
        
        # Stock list
        self.stock_scroll = ScrollView()
        self.stock_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        self.stock_layout.bind(minimum_height=self.stock_layout.setter('height'))
        
        self.stock_scroll.add_widget(self.stock_layout)
        
        layout.add_widget(input_layout)
        layout.add_widget(Label(text="🌊 Live Market Stream", font_size='18sp', size_hint_y=None, height='30dp'))
        layout.add_widget(self.stock_scroll)
        
        self.content = layout
        
        # Load initial data
        Clock.schedule_once(self.load_initial_data, 1)
    
    def update_symbols(self, instance):
        """Update watchlist symbols"""
        symbols = self.symbol_input.text.split(',')
        symbols = [s.strip().upper() for s in symbols if s.strip()]
        self.load_stock_data(symbols)
    
    def load_initial_data(self, dt):
        """Load initial stock data"""
        initial_symbols = ["AAPL", "GOOGL", "MSFT", "TSLA"]
        threading.Thread(target=self.load_stock_data, args=(initial_symbols,)).start()
    
    def load_stock_data(self, symbols):
        """Load stock data from API"""
        try:
            # Clear existing data
            Clock.schedule_once(lambda dt: self.stock_layout.clear_widgets(), 0)
            
            for symbol in symbols:
                try:
                    response = requests.get(f"http://localhost:8000/api/stocks/pulse/{symbol}", timeout=10)
                    if response.status_code == 200:
                        data = response.json()
                        pulse = data['pulse']
                        
                        # Create stock card on main thread
                        Clock.schedule_once(
                            lambda dt, p=pulse: self.add_stock_card(p), 0
                        )
                except Exception as e:
                    print(f"Error loading {symbol}: {e}")
                    
        except Exception as e:
            print(f"Error loading stock data: {e}")
    
    def add_stock_card(self, pulse_data):
        """Add stock card to layout"""
        card = StockCard(
            symbol=pulse_data['symbol'],
            price=pulse_data['current_price'],
            change=pulse_data['change'],
            change_percent=pulse_data['change_percent'],
            message=pulse_data['spiritual_message']
        )
        self.stock_layout.add_widget(card)

class MeditationTab(TabbedPanelItem):
    """Meditation tab with daily wisdom"""
    def __init__(self, app_instance, **kwargs):
        super().__init__(**kwargs)
        self.text = "🧘 Meditation"
        self.app_instance = app_instance
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title
        title = Label(
            text="🌅 Daily Market Meditation",
            font_size='20sp',
            size_hint_y=None,
            height='40dp',
            bold=True
        )
        
        # Meditation content
        self.meditation_label = Label(
            text="Loading today's spiritual guidance...",
            text_size=(None, None),
            halign='center',
            valign='middle',
            font_size='16sp'
        )
        
        # Meditation button
        meditation_btn = Button(
            text="💫 Quick Meditation",
            size_hint=(0.8, None),
            height='50dp',
            pos_hint={'center_x': 0.5},
            background_color=get_color_from_hex('#667eea')
        )
        meditation_btn.bind(on_press=self.show_meditation)
        
        layout.add_widget(title)
        layout.add_widget(self.meditation_label)
        layout.add_widget(meditation_btn)
        
        self.content = layout
        
        # Load meditation data
        Clock.schedule_once(self.load_meditation, 1)
    
    def load_meditation(self, dt):
        """Load daily meditation from API"""
        threading.Thread(target=self._fetch_meditation).start()
    
    def _fetch_meditation(self):
        """Fetch meditation data"""
        try:
            response = requests.get("http://localhost:8000/api/meditation/daily", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data['success']:
                    meditation = data['meditation']
                    text = f"""[b]{meditation['market_affirmation']}[/b]

🌬️ [i]{meditation['breathing_exercise']}[/i]

💎 {meditation['financial_wisdom']}

🕉️ [b]{meditation['mantra']}[/b]"""
                    
                    Clock.schedule_once(
                        lambda dt: setattr(self.meditation_label, 'text', text), 0
                    )
                    Clock.schedule_once(
                        lambda dt: setattr(self.meditation_label, 'markup', True), 0
                    )
        except Exception as e:
            Clock.schedule_once(
                lambda dt: setattr(self.meditation_label, 'text', 
                "🌫️ Meditation channel temporarily clouded\n\n🕉️ Trust your inner wisdom"), 0
            )
    
    def show_meditation(self, instance):
        """Show meditation popup"""
        meditation_messages = [
            "🌱 Take a deep breath and check in with your investment intentions",
            "🧘 Remember: Peace in the mind leads to profit in the portfolio",
            "💫 Your inner abundance attracts outer abundance",
            "🌊 Let your investments flow like water - finding their natural level",
            "🌸 Gratitude for what you have opens doors to more abundance"
        ]
        
        import random
        message = random.choice(meditation_messages)
        popup = MeditationPopup(message)
        popup.open()

class AstrologyTab(TabbedPanelItem):
    """Astrology tab with cosmic insights"""
    def __init__(self, app_instance, **kwargs):
        super().__init__(**kwargs)
        self.text = "🔮 Astrology"
        self.app_instance = app_instance
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title
        title = Label(
            text="🌟 Cosmic Market Forecast",
            font_size='20sp',
            size_hint_y=None,
            height='40dp',
            bold=True
        )
        
        # Astro content
        self.astro_label = Label(
            text="Reading celestial patterns...",
            text_size=(None, None),
            halign='center',
            valign='middle',
            font_size='16sp'
        )
        
        layout.add_widget(title)
        layout.add_widget(self.astro_label)
        
        self.content = layout
        
        # Load astro data
        Clock.schedule_once(self.load_astro, 1)
    
    def load_astro(self, dt):
        """Load astrology forecast from API"""
        threading.Thread(target=self._fetch_astro).start()
    
    def _fetch_astro(self):
        """Fetch astrology data"""
        try:
            response = requests.get("http://localhost:8000/api/astro/daily-forecast", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data['success']:
                    forecast = data['forecast']
                    text = f"""[size=24]{forecast['lunar_phase'].split(' ')[0]}[/size]

[b]{forecast['overall_energy']}[/b]

{forecast['market_prediction']}

[i]{forecast['cosmic_advice']}[/i]"""
                    
                    Clock.schedule_once(
                        lambda dt: setattr(self.astro_label, 'text', text), 0
                    )
                    Clock.schedule_once(
                        lambda dt: setattr(self.astro_label, 'markup', True), 0
                    )
        except Exception as e:
            Clock.schedule_once(
                lambda dt: setattr(self.astro_label, 'text', 
                "🌫️ Cosmic signals unclear\n\n✨ Trust your inner knowing"), 0
            )

class OmPulseMobileApp(App):
    """Main OmPulse mobile application"""
    
    def build(self):
        self.title = "🧘 OmPulse - Spiritual Stock Tracker"
        
        # Main tabbed interface
        tabs = TabbedPanel(do_default_tab=False)
        
        # Add tabs
        home_tab = HomeTab(self)
        meditation_tab = MeditationTab(self)
        astro_tab = AstrologyTab(self)
        
        tabs.add_widget(home_tab)
        tabs.add_widget(meditation_tab)
        tabs.add_widget(astro_tab)
        
        return tabs

if __name__ == "__main__":
    # Check if server is running
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        print("🌊 Connected to OmPulse server")
    except:
        print("⚠️ OmPulse server not running. Please start it first:")
        print("   python main.py")
        print("\nStarting mobile app anyway...")
    
    OmPulseMobileApp().run() 