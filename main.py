from kivymd.app import MDApp
from kivy.lang import Builder
from auth.login_screen import LoginScreen
from auth.register_screen import RegisterScreen

class GrabPiyudApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file("kivy/main.kv")

if __name__ == "__main__":
    GrabPiyudApp().run()
