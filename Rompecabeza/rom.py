
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc
from random import sample

mapache = misc.face()
rompecabezas = []
juego = []



def split_image(imagen):
    global rompecabezas

    arr1, arr2, arr3 = np.split(mapache,3)
    p1, p2, p3, p4 = np.hsplit(arr1,4)
    a1, a2, a3, a4 = np.hsplit(arr2,4)
    c1, c2, c3, c4 = np.hsplit(arr3,4)

    rompecabezas.append(p1)
    rompecabezas.append(p2)
    rompecabezas.append(p3)
    rompecabezas.append(p4)
    rompecabezas.append(a1)
    rompecabezas.append(a2)
    rompecabezas.append(a3)
    rompecabezas.append(a4)
    rompecabezas.append(c1)
    rompecabezas.append(c2)
    rompecabezas.append(c3)
    rompecabezas.append(c4)

    draw_image(rompecabezas)
    mix()

def draw_image(lista_rompecabezas):
    fig, axs = plt.subplots(3, 4, sharex='col', sharey='row',
                        gridspec_kw={'hspace': 0, 'wspace': 0})
    (ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8), (ax9, ax10, ax11, ax12) = axs

    axs[0, 0].imshow(lista_rompecabezas[0])
    axs[0, 1].imshow(lista_rompecabezas[1])
    axs[0, 2].imshow(lista_rompecabezas[2])
    axs[0, 3].imshow(lista_rompecabezas[3])
    axs[1, 0].imshow(lista_rompecabezas[4])
    axs[1, 1].imshow(lista_rompecabezas[5])
    axs[1, 2].imshow(lista_rompecabezas[6])
    axs[1, 3].imshow(lista_rompecabezas[7])
    axs[2, 0].imshow(lista_rompecabezas[8])
    axs[2, 1].imshow(lista_rompecabezas[9])
    axs[2, 2].imshow(lista_rompecabezas[10])
    axs[2, 3].imshow(lista_rompecabezas[11])

    for ax in fig.get_axes():
        ax.label_outer()
    plt.show


def mix():
    global rompecabezas
    global juego
    lista_random = (sample(rompecabezas,12))
    longitud = len(rompecabezas)
    for i in range(longitud):
        juego.append(lista_random[i])


def mov_puzzle():
    global juego
    aux_juego = juego[:]
    print("Las piezas son:\n0 1 2 3\n4 5 6 7\n8 9 10 11")
    opcion_1 = (int(input("INGRESE LA POSICION QUE DESEA CAMBIAR: ")))
    opcion_2 = (int(input("¿POR QUE POSICION DESEA CAMBIAR?: ")))
    juego[opcion_2] = juego[opcion_1]
    juego[opcion_1] = aux_juego[opcion_2]
    draw_image(juego)



split_image(mapache)

draw_image(juego)

mov_puzzle()
