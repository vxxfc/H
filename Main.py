from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.display = TextInput(multiline=False, readonly=True, halign="right", font_size=32)
        self.add_widget(self.display)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                btn = Button(text=label, font_size=24)
                btn.bind(on_press=self.on_button_press)
                h_layout.add_widget(btn)
            self.add_widget(h_layout)

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.display.text = ""
        elif text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except Exception:
                self.display.text = "Error"
        else:
            self.display.text += text

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == "__main__":
    CalculatorApp().run()
