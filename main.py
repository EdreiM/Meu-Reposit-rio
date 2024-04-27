import PySimpleGUI as sg


from itens import geldental
from itens import strax
from itens import gelmodelador
from itens import luvasilicone
from itens import antiestrias
from itens import manteigajoli
from itens import hidratantejoli
from itens import acidoglicolico
from itens import gellimpeza
from itens import hidratantefacial
from itens import empire
from itens import stamina
from itens import inebriante
from itens import grand
from itens import peeloff
from itens import serumolhos
from itens import serumfacial
from itens import croche



#Criação da janela
layout = [
    [sg.Text('Selecione o que deseja publicar:')],
    [sg.Checkbox('Gel dental'), sg.Checkbox('Gel modelador'), sg.Checkbox('Strax Hidratante')],
    [sg.Checkbox('Luva de silicone'), sg.Checkbox('Antiestrias'), sg.Checkbox('Manteiga Joli')],
    [sg.Checkbox('Hidratante Joli'), sg.Checkbox('Ácido Glicólico'), sg.Checkbox('Gel de limpeaza')],
    [sg.Checkbox('Hidratante facial'), sg.Checkbox('Empire Perfume'), sg.Checkbox('Stamina Perfume')],
    [sg.Checkbox('Inebriante Perfume'), sg.Checkbox('Grand Perfume'), sg.Checkbox('Máscara Peel Off')],
    [sg.Checkbox('Olhos Serum'), sg.Checkbox('Facial Serum')],

    [sg.Checkbox('Crochê')],

    [sg.Button('Publicar')]
]

window = sg.Window('Marketplace Auto', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Publicar':
        if values[0] == True:
            geldental.ativar(1)

        if values[1] == True:
            gelmodelador.ativar(1)

        if values[2] == True:
            strax.ativar(1)

        if values[3] == True:
            luvasilicone.ativar(1)

        if values[4] == True:
            antiestrias.ativar(1)

        if values[5] == True:
            manteigajoli.ativar(1)

        if values[6] == True:
            hidratantejoli.ativar(1)

        if values[7] == True:
            acidoglicolico(1)

        if values[8] == True:
            gellimpeza.ativar(1)

        if values[9] == True:
            hidratantefacial.ativar(1)

        if values[10] == True:
            empire.ativar(1)

        if values[11] == True:
            stamina.ativar(1)

        if values[12] == True:
            inebriante.ativar(1)

        if values[13] == True:
            grand.ativar(1)

        if values[14] == True:
            peeloff.ativar(1)

        if values[15] == True:
            serumolhos.ativar(1)

        if values[16] == True:
            serumfacial.ativar(1)

        if values[17] == True:
            croche.ativar(1)



window.close()

print('------FINALIZADO------')
