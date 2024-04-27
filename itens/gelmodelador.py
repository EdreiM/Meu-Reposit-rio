def ativar(valor):
    if valor == 1:
        import button
        from time import sleep
        import pyautogui
        import pyperclip
        import procura

        pasta = 'gel modelador' #de acordo com as pastas

        # entrando no marketplace
        button.botao('criarnovo')
        button.botao('itemvenda')
        sleep(2)

        # adiciona fotos
        button.botao('adicionarfotos')
        procura.fotos(f'E:\Marketplaceauto\{pasta}\photos')


        # abrir arquivo com o título e colar, parametros (caminho, nome botao para localizar)
        sleep(0.5)
        procura.arquivotxt(f'E:\Marketplaceauto\{pasta}\itulo.txt', 'titulo')



        procura.arquivotxt(f'E:\Marketplaceauto\{pasta}\preco.txt', 'preco')

        pyautogui.click(x=874, y=534)

        #rolar scroll para baixo
        pyautogui.click(x=270, y=705)
        sleep(0.5)
        pyautogui.scroll(-550)
        sleep(0.5)

        #clicar no botão categoria
        button.botao('categoria')
        #rolar scroll
        pyautogui.click(x=332, y=577)
        sleep(0.8)
        pyautogui.click(x=332, y=577)
        sleep(0.8)
        #click saude/beleza
        pyautogui.click(x=154, y=642)
        sleep(0.5)

        #clicar no botão condição
        button.botao('condicao')

        #clicar na descrição
        procura.arquivotxt(f'E:\Marketplaceauto\{pasta}\descricao.txt', 'descricao')
        pyautogui.scroll(-550)
        sleep(0.5)

        #Tags
        procura.tags(f'E:\Marketplaceauto\{pasta}\dags.txt', 'tags')

        #clicar em avançar
        button.botao('avancar')

        #selecionar grupos
        button.botao('grupos')

        #publicar
        button.botao('publicar')
        sleep(15)


