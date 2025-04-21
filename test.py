from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
Screen:
    MDLabel:
        text: "Hello, KivyMD!"
        halign: "center"
'''

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

TestApp().run()
