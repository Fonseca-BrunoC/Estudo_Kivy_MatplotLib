from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 100)
x2 = x / 5
y = np.linspace(0, 200)

f1 = plt.figure()
ax1 = f1.add_subplot(111)
plt.rc('axes', titlesize=15)
plt.rc('axes', labelsize=10)
l1 = ax1.plot(x, y, marker ='o',color = 'red', label = 'Dados ajustados', linestyle = '')
l2 = ax1.plot(x2, y, color = 'blue', label = 'Modelo linearizado')
ax1.set_title("AJUSTE LINEAR DA EQUAÇÃO DE ARRHENIUS", weight ='bold')
ax1.set_xlabel('1 / T',weight='bold')
ax1.set_ylabel('ln (k)', weight='bold')
plt.rc('legend', fontsize=13)
ax1.legend()
ax1.grid(True)
f1.set_figheight(5)
f1.set_figwidth(8)


class Graph(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(f1))

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        Builder.load_file('tela.kv')
        return Graph()

if __name__ == '__main__':
    MainApp().run()