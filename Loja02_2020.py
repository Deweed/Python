
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
menu = 0
while menu != 5:
      print ("""\n          ITENS ESCOLHIDOS\n\n
          escolha a opção:  
        (1) Memorias Ram ddr4 8gb 2666Mhz 
        (2) Headphones 
        (3) Camisetas Geek 
        (4) Pilhas 
        (5) Finalizar do Programa \n""")
      menu = int(input("Qual a opção escolhida? "))
#-----------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------#


      if( menu ==1):
              print ("""Memória HyperX Fury, 8GB, 2666MHz, DDR4, CL16, Preto - HX426C16FB3/8 (unidade)
R$ 341,06
R$ 43,91
https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=103547
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------

MEMORIA CORSAIR VENGEANCE LPX 8GB (1X8) DDR4 2666MHZ VERMELHO, CMK8GX4M1A2666C16R
R$317,06
R$47,21
https://www.pichau.com.br/hardware/memorias/memoria-corsair-vengeance-lpx-8gb-2666mhz-ddr4-red-cmk8gx4m1a2666c16r
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------

Memória Desktop Team Group 8GB DDR4 2666 Mhz TED48G2666C1901
R$ 292,90
R$ 24,91
https://www.americanas.com.br/produto/1498866054/memoria-desktop-team-group-8gb-ddr4-2666-mhz-ted48g2666c1901?pfm_carac=memoria%20ddr4%202666&pfm_index=2&pfm_page=search&pfm_pos=grid&pfm_type=search_page
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------

Memória Desktop Kingston 8GB DDR4 2666 Mhz KVR26N19S8/8-US
R$ 351,40
R$ 9,99
https://www.submarino.com.br/produto/619867556/memoria-desktop-kingston-8gb-ddr4-2666-mhz-kvr26n19s8-8-us?pfm_carac=memoria%20ddr4%202666&pfm_page=search&pfm_pos=grid&pfm_type=search_pag
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
""")

      elif (menu == 2):
                  print ("""Headphone Bluetooth JBL T500BT com Microfone - Preto
 R$229,00
*Frete grátis
https://www.magazineluiza.com.br/headphone-bluetooth-jbl-t500bt-com-microfone-preto/p/030910800/ea/frdf/
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------



Headphone Bluetooth com Microfone JBL Tune 500BT
R$ 229,90
R$ 38,97
https://www.zoom.com.br/lead?oid=232568875&sortorder=7&index=7&searchterm=&pagesize=60&channel=1
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------



Fone de Ouvido Bluetooth JBL T500BT Preto - JBLT500BTBLK
R$ 299,00
R$ 19,20
https://www.americanas.com.br/produto/54327736/fone-de-ouvido-bluetooth-jbl-t500bt-preto-jblt500btblk?pfm_carac=Headphone%20%20JBL%20T500BT%20&pfm_page=search&pfm_pos=grid&pfm_type=search_page
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------



Headphone Bluetooth preto T500BT Jbl CX 1 UN
R$ 299,00
FRETE GRÁTIS
https://www.kalunga.com.br/prod/headphone-bluetooth-preto-t500bt-jbl/229468?menuID=54
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
""")

      elif (menu == 3): 
                      print ("""Camiseta Flash - Vermelho
R$ 39,90
R$ 5,08
https://www.riachuelo.com.br/camiseta-flash-13375121_sku
--------------------------------------------------------------------
--------------------------------------------------------------------



Camiseta Vikings Ragnar Skull
R$ 59,90
R$ 47,31
https://www.studiogeek.com.br/camiseta-vikings-ragnar-skull/preto
-------------------------------------------------------------------
-------------------------------------------------------------------



CAMISETA PRATICAMENTE INOFENSIVA
R$ 44,90
Promo! 31% OFF
R$ 21,90
https://chicorei.com/camiseta/praticamente-inofensiva-1165.html
-------------------------------------------------------------------
-------------------------------------------------------------------




Camiseta Woltruverino
R$45,00
R$19,37
https://nerdstore.com.br/produto/camiseta-woltruverino/
--------------------------------------------------------------------
--------------------------------------------------------------------""")

      elif(menu == 4):
                          print ("""Pilha 4AA Panasonic Pacote 4 unidades
R$5,90
R$ 24,90
https://www.magazineluiza.com.br/pilha-4aa-panasonic-pacote-4-unidades/p/ec8f6ja023/cj/ilha/
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------


Pilha Alcalina AAA Elgin pacote com 4 pilhas
R$19,98
R$ 44,74
https://www.extra.com.br/cameras-filmadoras-drones/acessorios/pilhasebaterias/pilha-alcalina-aaa-elgin-pacote-com-4-pilhas-6746927.html
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------



Pilha Alcalina Palito AAA com 4, Panasonic, LR03XAB/4B192, Pacote de 4
R$19,99
Frete GRÁTIS: receba até Segunda-feira
https://www.amazon.com.br/Alcalina-Palito-Panasonic-LR03XAB-4B192/dp/B076X7BZVN
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------



Pilha Alcalina AAA Elgin pacote com 4 pilhas
R$ 19,98
R$ 44,74
https://www.pontofrio.com.br/pilha-alcalina-aaa-elgin-pacote-com-4-pilhas/p/6746927
------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------""")
      elif (menu == 5):
                                 print ("Programa Finalizado. Volte Sempre!!!")
                                 
      else:
            print("Opção Inválida, tente novamente")
