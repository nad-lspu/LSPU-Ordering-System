from kivymd.uix.screen import MDScreen
from firebase.firebase_config import db
from kivy.properties import ListProperty

class UserHomeScreen(MDScreen):
    menu_items = ListProperty([])

    def on_enter(self):
        self.load_menu()

    def load_menu(self):
        menu_data = db.child("menu").get().val()
        if menu_data:
            self.menu_items = list(menu_data.values())
            self.ids.menu_list.clear_widgets()
            for item in self.menu_items:
                self.ids.menu_list.add_widget(
                    OneLineListItem(text=f"{item['name']} - ₱{item['price']}",
                                    on_release=lambda x=item: self.add_to_cart(x))
                )

    def add_to_cart(self, item):
        from firebase.firebase_config import auth
        user = auth.current_user
        if user:
            db.child("cart").child(user['localId']).push(item)
