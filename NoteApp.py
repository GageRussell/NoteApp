import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
#adding extra line to commit 
import speech_recognition as sr

class MyGrid(GridLayout):
    #**kwargs is setting up class to take any number of params
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        # set up button
        self.submit = Button(text="Start Listening", font_size=30)
        #bind click event
        self.submit.bind(on_press = self.startListen)
        # add button widget
        self.add_widget(self.submit)
        #self.add_widget(Label(text="Note Text"))
        self.note = TextInput(multiline=False)
        #add text widget
        self.add_widget(self.note)

    def startListen(self, instance):
        print("Clicked")
        #clearing note
        self.note.text = ''
        #intialize speech recog
        r=sr.Recognizer()
        # start listening
        with sr.Microphone() as source:
            print('Listening')
            audio= r.listen(source)
            text = r.recognize_google(audio)
        #send speech to text field
        try:
            self.note.text = text
            print('Capture Complete')
        except:
            pass


class NoteApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    #run method inherited from App, has graphics, constructors, init, etc
    NoteApp().run()