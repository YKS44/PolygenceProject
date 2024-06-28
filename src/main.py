from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (360, 640)

class CustomTextInput(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.bottom_layout = BoxLayout(
            size_hint=(1, None),
            height='50dp'
        )
        
        self.text_input = TextInput(
            hint_text='Enter some text here',
            size_hint=(0.8, 1)
        )
        
        self.button = Button(
            text='Submit',
            size_hint=(0.2, 1)
        )
        self.button.bind(on_press=self.on_button_press)
        
        self.bottom_layout.add_widget(self.text_input)
        self.bottom_layout.add_widget(self.button)
        
        self.add_widget(BoxLayout())
        self.add_widget(self.bottom_layout)

    def on_button_press(self, instance):
        self.user_text = self.text_input.text
        print(f'Stored text: {self.user_text}')  
        self.text_input.text = ''

class MyApp(App):
    def build(self):
        return CustomTextInput()

if __name__ == '__main__':
    MyApp().run()
