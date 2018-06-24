
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class DemoApplication(toga.App):
    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name, 
                                           size=(360, 280))

        # Create a main content box
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Add something to the main box
        main_box.add(toga.Label('Hello World!',
                                style=Pack(padding=5)))

        # Create another box and add it to main_box
        grid_box = toga.Box(style=Pack(direction=COLUMN,
                                       padding=5))
        main_box.add(grid_box)

        # Add 4 x 5 array of Buttons to the grid box
        count = 1
        for row in range(5):
            row_box = toga.Box(style=Pack(padding=5))
            for col in range(4):
                row_box.add(toga.Button(f'{count}',
                                        style=Pack(padding=5)))
                count += 1
            grid_box.add(row_box)

        # Add the content on the main window
        self.main_window.content = main_box

        # Show the main window
        self.main_window.show()


def main():
    return DemoApplication('Demo Application', 'com.bobmarchese.demo.demo')

