import pyautogui
import pyperclip
import button
from time import sleep

def fotos(cami):
    # Procura fotos
    caminho = f'{cami}'
    pyperclip.copy(caminho)
    # acha a barra de pesquisa
    button.botao('barrapesquisa')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    # clica na pasta para selecionar tudo e enviar fotos
    pyautogui.click(x=874, y=534)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('enter')



def arquivotxt(cami, botao):
    # abrir arquivo com o título e colar
    with open(f'{cami}', 'r', encoding='utf-8') as titulo:
        palavra = titulo.read()
        pyperclip.copy(palavra)
        sleep(1)
        button.botao(f'{botao}')
        sleep(1)
        pyautogui.hotkey('ctrl', 'v', interval=0.15)



def tags(cami, botao):
    button.botao(f'{botao}')
    with open(f'{cami}', 'r', encoding='utf-8') as tags:
        linhas = tags.readlines()
        #escrever cada uma tag e dar enter
        for palavra in linhas:
            pyperclip.copy(palavra)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
