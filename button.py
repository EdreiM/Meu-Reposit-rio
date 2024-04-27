from time import sleep
import pyautogui

def botao(nome):
    entrada = nome
    if entrada in 'criarnovo':
        pyautogui.click(x=210, y=253)
        sleep(0.5)

    if entrada in 'itemvenda':
        pyautogui.click(x=921, y=554)
        sleep(0.5)

    if entrada in 'adicionarfotos':
        pyautogui.click(x=177, y=385)
        sleep(0.5)

    if entrada in 'barrapesquisa':
        pyautogui.click(x=940, y=50)
        sleep(0.5)

    if entrada in 'titulo':
        pyautogui.click(x=122, y=729)
        sleep(0.5)

    if entrada in 'preco':
        pyautogui.click(x=209, y=794)
        sleep(0.5)

    if entrada in 'categoria':
        pyautogui.click(x=186, y=406)
        sleep(0.5)

    if entrada in 'condicao':
        pyautogui.click(x=184, y=492)
        sleep(0.5)
        #novo
        pyautogui.click(x=152, y=541)

    if entrada in 'descricao':
        pyautogui.click(x=172, y=863)
        sleep(0.5)

    if entrada in 'tags':
        pyautogui.click(x=149, y=600)
        sleep(0.5)

    if entrada in 'avancar':
        pyautogui.click(x=165, y=996)
        sleep(0.5)

    if entrada in 'grupos':
        pyautogui.click(x=151, y=436)
        pyautogui.click(x=146, y=526)
        pyautogui.click(x=149, y=596)
        pyautogui.click(x=186, y=683)
        pyautogui.click(x=189, y=744)
        pyautogui.click(x=166, y=807)
        pyautogui.click(x=171, y=881)
        pyautogui.scroll(-800)
        sleep(0.5)

        pyautogui.click(x=277, y=281)
        pyautogui.click(x=170, y=360)
        pyautogui.click(x=183, y=432)
        pyautogui.click(x=183, y=492)
        pyautogui.click(x=180, y=544)
        pyautogui.click(x=206, y=633)
        pyautogui.click(x=203, y=707)
        pyautogui.click(x=185, y=787)
        pyautogui.click(x=206, y=852)
        pyautogui.scroll(-800)
        sleep(0.5)

        pyautogui.click(x=197, y=271)
        pyautogui.click(x=194, y=340)
        pyautogui.click(x=186, y=405)
        pyautogui.click(x=168, y=465)

    if entrada in 'publicar':
        pyautogui.click(x=264, y=999)


