import os
import unidecode as uni
from tkinter import *
from pathlib import Path as Ph


class Interface:

    def __init__(self, tk):

        self.caixa1 = self.caixa2 = self.caixa3 = None
        self.etiqueta1 = self.etiqueta2 = self.etiqueta3 = self.etiqueta4 = None
        self.checkbox2 = self.checkbox1 = None
        self.fonte = self.cor_letras = self.cor_fundo = self.roxo = None
        self.cores()
        self.tela(tk)
        self.fundo(tk)
        tk.mainloop()

    def cores(self) -> None:
        self.roxo = '#9400D3'
        self.cor_fundo = '#000000'
        self.cor_letras = '#FFFFFF'
        self.fonte = 15

    def tela(self, tk) -> None:
        wid = 600
        hei = 150
        tk.title('Ordem')
        tk.geometry(f'{wid}x150')
        tk.configure(bg=self.roxo)
        tk.minsize(width=wid, height=hei)
        tk.maxsize(width=wid, height=hei)

    def fundo(self, tk) -> None:
        fundo1 = Frame(tk, bg=self.cor_fundo)
        fundo1.pack(fill=BOTH, expand=1, padx=4, pady=4)

        frame1 = Frame(fundo1, bg=self.cor_fundo)
        frame1.pack(fill=BOTH, expand=True)
        frame2 = Frame(fundo1, bg=self.cor_fundo)
        frame2.pack(fill=BOTH, expand=True)
        frame3 = Frame(fundo1, bg=self.cor_fundo)
        frame3.pack(fill=BOTH, expand=True)
        self.botoes(frame1, frame2, frame3)

    def normal(self) -> None:
        self.etiqueta1["fg"] = "WHITE"

    def normal2(self) -> None:
        self.etiqueta2["fg"] = "WHITE"
        self.etiqueta3["fg"] = "WHITE"

    def erro(self) -> None:
        self.etiqueta1["fg"] = "RED"

    def erro2(self) -> None:
        self.etiqueta2["fg"] = "RED"
        self.etiqueta3["fg"] = "RED"

    def botoes(self, frame1, frame2, frame3) -> None:
        # Etiqueta
        self.etiqueta1 = Label(frame1, text="C://", bg=self.cor_fundo, fg=self.cor_letras, font=self.fonte)
        self.etiqueta1.place(relx=0, relheight=1, relwidth=0.1)
        self.etiqueta2 = Label(frame2, text="Doc", bg=self.cor_fundo, fg=self.cor_letras, font=self.fonte)
        self.etiqueta2.place(relx=0, relheight=1, relwidth=0.1)
        self.etiqueta3 = Label(frame2, text="Pasta", bg=self.cor_fundo, fg=self.cor_letras, font=self.fonte)
        self.etiqueta3.place(relx=0.44, relheight=1, relwidth=0.1)
        # Caixa de texto
        self.caixa1 = Entry(frame1, width=32, bd=2, font=15)
        self.caixa1.place(relx=0.09, rely=0.25, relwidth=0.8)
        self.caixa2 = Entry(frame2, width=32, bd=2, font=15)
        self.caixa2.place(relx=0.09, rely=0.25, relwidth=0.34)
        self.caixa3 = Entry(frame2, width=32, bd=2, font=15)
        self.caixa3.place(relx=0.55, rely=0.25, relwidth=0.34)
        # Etiquetas 2
        self.etiqueta4 = Label(frame3, text="---", bg=self.cor_fundo, fg=self.cor_letras, font=self.fonte)
        self.etiqueta4.place(relx=0.44, relheight=1, relwidth=0.1)
        etiqueta5 = Label(frame1, text='(+)', bg=self.cor_fundo, fg=self.cor_letras)
        etiqueta5.place(relx=0.91, relheight=1, relwidth=0.1)
        etiqueta6 = Label(frame2, text='(★)', bg=self.cor_fundo, fg=self.cor_letras)
        etiqueta6.place(relx=0.91, relheight=1, relwidth=0.1)

        # Checkbox
        self.checkbox1 = IntVar()
        box1 = Checkbutton(frame1, variable=self.checkbox1, onvalue=1, offvalue=0, bg=self.cor_fundo)
        box1.place(relx=0.91, rely=0.32, height=15, width=15)
        self.checkbox2 = IntVar()
        box2 = Checkbutton(frame2, variable=self.checkbox2, onvalue=1, offvalue=0, bg=self.cor_fundo)
        box2.place(relx=0.91, rely=0.32, height=15, width=15)

        # Botões
        boton1 = Button(frame3, text="Organizar", command=self.inicio, bg='#9932CC')
        boton1.place(relx=0.09, rely=0.15, relheight=0.63, relwidth=0.34)
        boton2 = Button(frame3, text="Parametro", command=self.adicionar, bg='#9932CC')
        boton2.place(relx=0.55, rely=0.15, relheight=0.63, relwidth=0.34)

    def inicio(self):
        if self.caixa2.get() != '':
            self.adicionar()
        self.normal2()
        sistema.inicio(self.caixa1, self.normal, self.erro, self.checkbox1.get(), self.checkbox2.get(),
                       self.inicio, self.etiqueta4)

    def adicionar(self):
        var = ''
        for folder in os.environ["APPDATA"]:
            if folder in r'\/':
                break
            var += folder
        rota = f'{var}{os.environ["HOMEPATH"]}'
        if os.path.isdir(f'{rota}/{self.caixa1.get().strip()}') and self.caixa1.get().strip() != '':
            var2 = self.caixa1.get().strip()
            self.caixa1.delete(0, 'end')
            self.caixa1.insert(0, fr'{rota}\{var2}')
        self.etiqueta4['text'] = '---'
        documentos = self.caixa2.get().split(', ')
        arquivo = self.caixa3.get()
        for doc in documentos:
            if doc != '' and arquivo != '':
                self.normal2()
                if self.checkbox1.get() == 1:
                    pasta.adicionar(doc, arquivo, self.caixa1.get().strip())
                else:
                    pasta.adicionar(doc, arquivo)
            elif doc != '' and arquivo == '':
                arquivo = doc
                self.normal2()
                if self.checkbox1.get() == 1:
                    pasta.adicionar(doc, arquivo, self.caixa1.get().strip())
                else:
                    pasta.adicionar(doc, arquivo)
                arquivo = ''
            else:
                self.erro2()
            self.caixa2.delete(0, 'end')
            self.caixa3.delete(0, 'end')


class Pasta:
    def __init__(self):
        self.local_keys = Ph(os.environ['HOMEPATH'] + '/.Ordem')
        self.keys = '_Keyes.txt'
        self.verificar()

    def verificar(self) -> None:
        if not Ph(self.local_keys).is_dir():
            Ph(self.local_keys).mkdir()
        if not Ph(self.local_keys/self.keys).is_file():
            self.limpar_criar()

    def limpar_criar(self, local=None) -> None:
        if local is not None:
            if local != '' and Ph(local).is_dir():
                local_keys = {local}
            else:
                return
        else:
            local_keys = self.local_keys
        with open(f'{Ph(local_keys)/self.keys}', '+w') as txt:
            txt.write('')

    def adicionar(self, novas_keys: str, novas_values: str, local=None) -> None:
        if local is not None:
            if local != '' and Ph(local).is_dir():
                local_keys = local
            else:
                return
        else:
            local_keys = self.local_keys
        with open(f'{Ph(local_keys)/self.keys}', 'a', encoding='utf-8') as txt:
            txt.write(fr'{novas_keys} {novas_values} ')

    def ler(self, local=None) -> None | dict[str, str]:
        if local is not None:
            if local != '' and Ph(local).is_dir():
                local_keys = local
            else:
                return
        else:
            local_keys = self.local_keys
        with open(f'{Ph(local_keys)/self.keys}', 'rt', encoding='utf-8') as txt:
            lista_keys = txt.readline().split()
        keys_values = {}
        for palavra in range(1, len(lista_keys), 2):
            keys_values[lista_keys[palavra-1]] = lista_keys[palavra]
        return keys_values


class Sistema:
    def __init__(self) -> None:
        self.documento = self.caminho = self.folder = None

    def inicio(self, caminho, normal, erro, checkbox1, checkbox2, inicio, etiqueta4):

        if 'limpar' == caminho.get().lower().strip():
            etiqueta4['text'] = 'OK'
            etiqueta4['fg'] = 'GREEN'
            normal()
            if checkbox1 == 1:
                if not pasta.limpar_criar(caminho.get()):
                    erro()
            else:
                pasta.limpar_criar()
            caminho.delete(0, 'end')
        elif Ph(caminho.get().strip()).is_dir() and caminho.get().strip() != '':
            etiqueta4['text'] = '...'
            etiqueta4['fg'] = 'WHITE'
            normal()
            self.documentos(caminho, checkbox1, checkbox2, erro)
            etiqueta4['text'] = 'OK'
            etiqueta4['fg'] = 'GREEN'
        else:
            var = ''
            for folder in os.environ["APPDATA"]:
                if folder in r'\/':
                    break
                var += folder
            rota = f'{var}{os.environ["HOMEPATH"]}'
            if Ph(f'{rota}/{caminho.get().strip()}').is_dir() and caminho.get().strip() != '':
                var2 = caminho.get().strip()
                caminho.delete(0, 'end')
                caminho.insert(0, fr'{rota}\{var2}')
                inicio()
            else:
                etiqueta4['text'] = '---'
                erro()

    def documentos(self, caminho, checkbox1, checkbox2, erro) -> None:
        if checkbox1 == 1:
            if caminho.get() != '' and Ph(caminho.get()).is_dir():
                keys_values = pasta.ler(caminho.get().strip())
            else:
                erro()
                return
        else:
            keys_values = pasta.ler()
        self.documento = Ph(caminho.get().strip()).iterdir()
        self.caminho = Ph(caminho.get().strip())
        for self.folder in self.documento:
            self.documento = Ph(caminho.get().strip()).iterdir()
            caracter = None
            if Ph(self.folder).is_file():
                for folder2 in keys_values:
                    if uni.unidecode(folder2) in uni.unidecode(self.folder.name):
                        caracter = keys_values[folder2]
                if caracter is not None:
                    self.favoritos(caracter)
                elif checkbox2 == 0:
                    self.formato()

    def favoritos(self, caracter):
        for arquivo in self.documento:
            if arquivo.is_dir():
                if uni.unidecode(caracter.lower()) in uni.unidecode(arquivo.name.lower()):
                    self.move(arquivo)
                    return
        self.criar(caracter)

    def formato(self):
        arquivo = self.folder.suffix[1:].lower()
        for folder2 in self.documento:
            if Ph(folder2).is_dir() and arquivo in folder2.name.lower():
                self.move(arquivo)
                return
        self.criar(arquivo)

    def criar(self, arquivo):
        Ph(self.caminho/arquivo).mkdir()
        self.move(arquivo)

    def move(self, arquivo):
        for numero in range(0, 9):
            if f' ({numero}).' in self.folder.name:
                re = 4
                self.repetidos(arquivo, re)
                return
        re = 0
        if self.folder.name != '_Keyes.txt':
            if not Ph(self.caminho/arquivo/self.folder.name).is_file():
                os.rename(f'{Ph(self.caminho/self.folder.name)}', f'{Ph(self.caminho/arquivo/self.folder.name)}')
            else:

                self.repetidos(arquivo, re)

    def repetidos(self, arquivo, re):
        n = 1
        if not Ph(self.caminho/arquivo/'Repitidos').is_dir():
            Ph(self.caminho/arquivo/'Repitidos').mkdir(parents=True)
        while True:
            folder = f'{self.folder.stem[:-re]} ({n}){self.folder.suffix}'
            if not Ph(self.caminho/arquivo/'Repitidos'/folder).is_file():
                os.rename(f"{Ph(self.caminho/self.folder)}", f'{Ph(self.caminho/arquivo/"Repitidos"/folder)}')
                break
            else:
                n += 1


if __name__ == '__main__':
    pasta = Pasta()
    sistema = Sistema()
    interface = Interface(Tk())
