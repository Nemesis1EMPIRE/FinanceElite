from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty
import json
import os

# Configuration
CONFIG = {
    'TVA_RATE': 18,
    'CSS_RATE': 1,
    'CURRENCY': 'FCFA'
}

class DashboardScreen(Screen):
    total_ca = StringProperty('0 FCFA')
    total_clients = StringProperty('0')
    
    def update_stats(self):
        # Logique similaire à votre JavaScript
        pass

class FacturesScreen(Screen):
    def load_invoices(self):
        # Charger les factures
        pass

class DepensesScreen(Screen):
    def load_expenses(self):
        # Charger les dépenses
        pass

class FinanciaApp(MDApp):
    data_file = 'financia_data.json'
    
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        
        # Créer le ScreenManager
        sm = ScreenManager()
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(FacturesScreen(name='factures'))
        sm.add_widget(DepensesScreen(name='depenses'))
        
        return sm
    
    def on_start(self):
        # Charger les données
        self.load_data()
        
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_data(self, data):
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def format_currency(self, amount):
        return f"{amount:,.0f} FCFA"

if __name__ == '__main__':
    Window.size = (360, 640)  # Taille mobile
    FinanciaApp().run()
