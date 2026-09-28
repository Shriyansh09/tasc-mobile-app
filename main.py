# TASC Mobile Network Core Runtime
import os
import sys
import time
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# --- APNI FIREBASE URL YAHAN UPDATE KAREIN ---
SERVER_URL = "https://my-tasc-terminal-default-rtdb.firebaseio.com"

class TascMobileEngine(App):
    def build(self):
        self.title = "TASC OVERLORD PORTAL"
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.lbl = Label(text="ENTER HARDWARE ACCESS TOKEN ID", font_size=18)
        self.layout.add_widget(self.lbl)
        
        self.txt_user = TextInput(hint_text="Username", multiline=False, size_hint_y=None, height=40)
        self.layout.add_widget(self.txt_user)
        
        self.txt_pass = TextInput(hint_text="Password", password=True, multiline=False, size_hint_y=None, height=40)
        self.layout.add_widget(self.txt_pass)
        
        self.btn_login = Button(text="VALIDATE DYNAMIC AUTH", size_hint_y=None, height=50)
        self.btn_login.bind(on_press=self.verify_owner)
        self.layout.add_widget(self.btn_login)
        
        return self.layout

    def verify_owner(self, instance):
        if self.txt_user.text == "admin" and self.txt_pass.text == "TASC123":
            self.load_terminal_console()
        else:
            self.lbl.text = "[AUTH FAILED] SECURITY BREACH ALERT"

    def load_terminal_console(self):
        self.layout.clear_widgets()
        self.lbl.text = "TASC_MOBILE:~# (Active Core Connection)"
        self.layout.add_widget(self.lbl)
        
        btn_lock = Button(text="RUN PC TERMINAL RESET ACTION", background_color=(1, 0, 0, 1), size_hint_y=None, height=60)
        btn_lock.bind(on_press=self.fire_sync_signal)
        self.layout.add_widget(btn_lock)
        
    def fire_sync_signal(self, instance):
        try:
            res = requests.put(f"{SERVER_URL}/node_status.json", json={"lock_signal": "LOCKED"})
            if res.status_code == 200:
                self.lbl.text = "[SUCCESS] STATE RESET BROADCAST COMPLETED."
            else:
                self.lbl.text = "[FAILED] ENDPOINT CONSOLE TIMEOUT."
        except Exception:
            self.lbl.text = "[ERROR] CONNECTION CARRIER FAILED."

if __name__ == "__main__":
    TascMobileEngine().run()
