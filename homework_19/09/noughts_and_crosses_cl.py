from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')


class Game(App):
    def __init__(self):
        super().__init__()
        self.buttons = list()
        self.switch = True

    def noughts_and_crosses_toe(self, arg):
        arg.disabled = True
        arg.text = 'X' if self.switch else '0'
        self.switch = not self.switch

        coordinates_win = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                           (0, 3, 6), (1, 4, 7), (2, 5, 8),
                           (0, 4, 8), (2, 4, 6))

        vector = lambda item: [self.buttons[x].text for x in item]
        color = [0, 1, 0, 1]

        for thing in coordinates_win:
            if vector(thing).count('X') == 3 or vector(thing).count('0') == 3:
                for i in thing:
                    self.buttons[i].color = color
                for button in self.buttons:
                    button.disabled = True
                break

    def restart(self):
        self.switch = True

        for button in self.buttons:
            button.color = [0, 0, 0, 1]
            button.text = ''
            button.disabled = False

    def build(self):
        self.title = 'Noughts and crosses'
        root = BoxLayout(orientation='vertical', padding=5)
        grid = GridLayout(cols=3)

        for i in range(9):
            button = Button(
                color=[0, 0, 0, 1],
                font_size=24,
                disabled=False,
                on_press=self.noughts_and_crosses_toe
            )
            self.buttons.append(button)
            grid.add_widget(button)

            root.add_widget(Button(text='Restart', size_hint=[1, .1], on_press=self.restart))
        return root


if __name__ == "__main__":
    Game().run()
