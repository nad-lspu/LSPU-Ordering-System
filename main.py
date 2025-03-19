from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar

# Set window size for mobile compatibility
Window.size = (360, 640)

# Define the KV language string for the UI
KV = '''
ScreenManager:
    LoginScreen:

<LoginScreen>:
    name: 'login'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        md_bg_color: [1, 1, 1, 1]  # White background

        # Top App Bar
        MDTopAppBar:
            title: 'Grab Piyu-d'
            elevation: 0
            md_bg_color: [1, 0, 0, 1]  # Red color for the app bar
            specific_text_color: [1, 1, 1, 1]  # White text

        # Logo and Welcome Text
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(60)
            padding: dp(20)

            MDLabel:
                text: 'Welcome Back!'
                font_style: 'H4'
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: [0, 0, 0, 1]  # Black text

            MDLabel:
                text: 'Login to continue'
                font_style: 'Subtitle1'
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: [0.5, 0.5, 0.5, 1]  # Gray text

        # Input Fields
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(15)
            padding: dp(20)

            MDTextField:
                id: username
                hint_text: 'Username'
                icon_left: 'account'
                size_hint_x: 0.9
                pos_hint: {'center_x': 0.5}
                mode: 'round'
                color_active: [0, 0.5, 1, 1]  # Blue for active state

            MDTextField:
                id: password
                hint_text: 'Password'
                icon_left: 'lock'
                size_hint_x: 0.9
                pos_hint: {'center_x': 0.5}
                password: True
                mode: 'round'
                color_active: [0, 0.5, 1, 1]  # Blue for active state

        # Login Button
        MDFillRoundFlatButton:
            text: 'Login'
            size_hint_x: 0.8
            pos_hint: {'center_x': 0.5}
            on_release: root.login()
            md_bg_color: [0, 0.8, 0, 1]  # Green background for the button
            text_color: [1, 1, 1, 1]  # White text

        # Forgot Password Link
        MDLabel:
            text: 'Forgot Password?'
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: [0, 0.5, 1, 1]  # Blue color for the link
            on_touch_down: root.forgot_password() if self.collide_point(*args[1].pos) else None

        # Sign Up Section
        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)
            spacing: dp(10)
            padding: dp(20)
            pos_hint: {'center_x': 0.5}

            MDLabel:
                text: "Don't have an account?"
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: [0.5, 0.5, 0.5, 1]  # Gray text

            MDLabel:
                text: 'Sign Up'
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: [0, 0.5, 1, 1]  # Blue text
                on_touch_down: root.sign_up() if self.collide_point(*args[1].pos) else None
'''

# Define the LoginScreen class
class LoginScreen(Screen):
    def login(self):
        username = self.ids.username.text
        password = self.ids.password.text

        # Simple validation
        if username == 'user' and password == 'password':
            print("Login successful!")
        else:
            self.show_error_dialog("Invalid username or password")

    def forgot_password(self):
        self.show_error_dialog("Forgot password feature coming soon!")

    def sign_up(self):
        self.show_error_dialog("Sign up feature coming soon!")

    def show_error_dialog(self, message):
        dialog = MDDialog(
            title="Error",
            text=message,
            size_hint=(0.8, 0.3),
            buttons=[
                MDFillRoundFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

# Define the main app class
class GrabPiyuDApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"  # Set primary color to red
        self.theme_cls.accent_palette = "Green"  # Set accent color to green
        return Builder.load_string(KV)

# Run the app
if __name__ == '__main__':
    GrabPiyuDApp().run()