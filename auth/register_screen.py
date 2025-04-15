from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import toast
from firebase.firebase_config import auth, db
from kivy.lang import Builder

class RegisterScreen(MDScreen):
    def on_kv_post(self, base_widget):
        self.menu = MDDropdownMenu(
            caller=self.ids.role_dropdown,
            items=[
                {"text": "user", "on_release": lambda x='user': self.set_role(x)},
                {"text": "admin", "on_release": lambda x='admin': self.set_role(x)},
            ],
            width_mult=4,
        )

    def set_role(self, role):
        self.ids.role_dropdown.set_item(role)
        self.menu.dismiss()

    def register(self, email, password, role):
        try:
            user = auth.create_user_with_email_and_password(email, password)
            uid = user['localId']
            db.child("users").child(uid).set({"email": email, "role": role})
            toast("Registered successfully!")
            self.manager.current = "login"
        except:
            toast("Registration failed!")
