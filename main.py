# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor = (0, 0, 0, 0)

kv='''
BoxLayout:
    orientation: "vertical"
    BoxLayout:
        Label:
            id: "durum"
            text: "Makine Durumu:"
            size_hint_x: 1
        Button:
            id: "durumbuton"
            color: (0, 1, 0, 1)
            size_hint_x: 2
            text: "Çalışıyor"


    BoxLayout:
        Label:
            id: "yapilantext"
            text: "Yaılan İş:"
            size_hint_x: 1
        TextInput:
            input_type: number
            id: "yapilan"
            size_hint_x: 2
            color: (0, 0, 0, 1)


    BoxLayout:
        Label:
            id: "cevrimsuresitext"
            text: "Çevrim Süresi:"
            size_hint_x: 1
        Button:
            id: "cevrimsuresi"
            size_hint_x: 2
    BoxLayout:
        Label:
            id: "isinaditext"
            text: "İşin Adı:"
            size_hint_x: 1
        TextInput:
            id: "isinadi"
            size_hint_x: 2

'''

class girisFormu(App):

    def build(self):
        self.root=Builder.load_string(kv)
        return self.root


girisFormu().run()
