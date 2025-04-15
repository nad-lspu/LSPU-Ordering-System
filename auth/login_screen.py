from kivymd.uix.screen import MDScreen
from firebase.firebase_config import auth, db
from kivymd.toast import toast

class LoginScreen(MDScreen):
    def login(self, email, password):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            uid = user['localId']
            role = db.child("users").child(uid).child("role").get().val()

            toast(f"Logged in as {role}")
            if role == "admin":
                self.manager.current = "login"  # for now, just stay here
            else:
                self.manager.current = "login"  # for now, just stay here
        except:
            toast("Login failed!")
