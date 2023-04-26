from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file("design.kv")


class LoginScreen(Screen):
    def sing_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, username, password):
        with open("users.json") as f:
            users = json.load(f)

        print(username, password)
        if username in users and users[username]["password"] == password:
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text =" username or password are wrong!"
        


class LoginSuccessScreen(Screen):
    def log_out(self):
        self.manager.current = "login_screen"


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as f:
            users = json.load(f)
        users[uname] = {
            "username": uname,
            "password": pword,
            "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        }

        with open("users.json", "w") as f:
            json.dump(users, f)

        self.manager.current = "sign_up_screen_success"


class SignUpSuccessScreen(Screen):
    def go_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
