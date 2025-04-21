from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, SwapTransition
from screens.login_screen import LoginScreen
from screens.register_screen import RegisterScreen
from screens.user_dashboard import UserDashboard
from screens.admin_dashboard import AdminDashboard

class GrabPiyudApp(MDApp):
    def build(self):
        self.title = "Grab Piyu-d"
        self.theme_cls.primary_palette = "Green"

        Builder.load_file("kv/login.kv")
        Builder.load_file("kv/register.kv")
        Builder.load_file("kv/user_dashboard.kv")
        Builder.load_file("kv/admin_dashboard.kv")

        sm = ScreenManager(transition=SwapTransition())
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(UserDashboard(name="user_dashboard"))
        sm.add_widget(AdminDashboard(name="admin_dashboard"))
        return sm

    def logout(self):
        self.root.current = "login"


GrabPiyudApp().run()
