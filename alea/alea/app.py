
from random import randint, random
import toga
from toga.style import Pack
from toga.style.pack import CENTER, COLUMN, ROW


class Alea(toga.App):

    #async def doRoll(self, widget, **kwargs):
    def doRoll(self, widget):
        n = int(widget.label.split(' D')[-1])
        self.results.text = 'Rolling'
        #yield random() * 3
        #await asyncio.sleep(random() * 3)
        self.results.text = randint(1, n)


    def startup(self):
        faces = [4, 6, 8, 12, 20]
    
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)
        
        # Create a box and add some buttons for the buttons
        rolls = []
        for face in faces:
            button = toga.Button(f'Roll D{face}',
                                 on_press=self.doRoll,
                                 style=Pack(width=100, padding=5)            
            )
            rolls.append(button)

        self.buttons = toga.Box(
            children = rolls,
            style = Pack(direction=ROW, padding=5)
        )
            
        # Create a text area for the results
        self.results = toga.Label(
            'Iacta Alea Esto',
            style = Pack(alignment=CENTER, padding=5)
        )

        # Add the content on the main window
        self.main_window.content = toga.Box(
            children = [self.buttons, self.results],
            style = Pack(direction=COLUMN, padding=5)
        )

        # Show the main window
        self.main_window.show()


def main():
    return Alea('Alea', 'com.bobmarchese.alea')

