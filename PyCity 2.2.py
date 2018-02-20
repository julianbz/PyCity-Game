#-*- coding:utf-8 -*-
from wx  import *
import datetime

class Miapp(App):

    def OnInit(self):
        style =  wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX ^ wx.MINIMIZE_BOX
        self.vent2=Frame(None,-1,"",pos=(100,25),size=(1000 ,700 ),style=style )
        self.vent2.Maximize(True)
        self.vent2.Show()

        image_file = 'fondo.png'
        bmp18 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.vent10 = wx.StaticBitmap(self.vent2, -1, bmp18,pos=(0,0),size=(1366,768))
        self.vent10.Show()

#-----Cierra juego----------------------------
        self.bc=Button(self.vent10,-1,label="",pos=(1183,36),size=(73,42 ))
        self.bc.SetBitmap(BitmapFromImage(Image("bsal.png")))
        self.bc.Bind(EVT_BUTTON,self.bcj)
        self.bc.Show()
#----------------------INICIO---------------------------------------------
        image_file = 'ppant2.png'
        bmp12 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        style2 = wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX ^ wx.MINIMIZE_BOX ^ wx.CLOSE_BOX
        self.vent3=Frame(None,-1,"",pos=(100,25),size=(1366 ,768 ),style=style2 )
        self.vent3.Maximize(True)
        self.vent3.Show()

        self.fondoinicio = wx.StaticBitmap(self.vent3, -1, bmp12,pos=(0,0),size=(1366,768))
        self.bcierra=Button(self.fondoinicio,-1,label="",pos=(536,539),size=(295 ,61 ))
        self.bcierra.SetBitmap(BitmapFromImage(Image("bpant.png")))
        self.bcierra.Bind(EVT_BUTTON,self.iniciajuego)
        self.bcierra.Show()

        self.salir=Button(self.fondoinicio,-1,label="",pos=(856,549),size=(73,42 ))
        self.salir.SetBitmap(BitmapFromImage(Image("bsal.png")))
        self.salir.Bind(EVT_BUTTON,self.Cierratodo)
        self.salir.Show()

        self.fondoinicio.Show()



#---------------------------------------------------------------------------
        image_file = 'fondo.png'
        bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.vent = wx.StaticBitmap(self.vent10, -1, bmp1,pos=(183,34),size=(1000,700))
        self.vent.Show()

        self.menu=Button(self.vent,-1,label="",pos=(659,600),size=(265,63))
        self.menu.SetBitmap(BitmapFromImage(Image("b_men2.png")))
        self.menu.Show()
        self.menu.Bind(EVT_BUTTON,self.AbrirMenu)

        bmp1 = wx.Image('f_men2.png',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1=wx.StaticBitmap(self.vent,-1,bmp1,pos=(659,720),size=(339,607))
        self.button3=wx.Button(self.bitmap1,id=-1,label='',size=(64,64),pos=(200,0))
        self.button3.SetBitmap(BitmapFromImage(Image("b2_men.png")))
        self.button3.Show()
        self.bitmap1.Show()
        self.vent.Show()#AGREGAR BOTONES EN BITMAP1

        self.chat=Button(self.vent,-1,label="",pos=(909,93),size=(75,75))
        self.chat.SetBitmap(BitmapFromImage(Image("b_chat.png")))
        self.chat.Show()
        self.chat.Bind(EVT_BUTTON,self.AbrirChat)

        bmp2=wx.Image('f_chat.png',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap2=wx.StaticBitmap(self.vent,-1,bmp2,pos=(659,720),size=(339,607))
        self.button4=wx.Button(self.bitmap2,id=-1,label='',size=(64,64),pos=(0,0))
        self.button4.SetBitmap(BitmapFromImage(Image("f_chat.png")))
        self.button4.Show()
        self.bitmap1.Show()

#------------------ JUGABILIDAD------------------------------------------------
#------------Level-------------------------
        self.lvl=0
#------------Poblacion---------------------
        self.pp=0
#------------Dinero------------------------
        self.dine=120
#------------Listas compra terreno---------
        self.ct=[0,0,0,0,0,0,0,0,0,0,0,0,0]
#------------Lista de personas por casa----
        self.per=[4,8,2,2,10,10,2,2,2,10,2,0]
#------------Lista cuanto cuesta cada casa-
        self.dn=[15,20,20,25,15,70,25,25,50,115,60,0]
#-------------Experiencia de cada casa-----
        self.exp=[15,15,20,20,15,55,25,20,35,90,60,0]
#-------------Imagenes de las casas--------
        self.image=["casa.jpeg","hospital.png","escuela.png","edificio.png","policia.png","iglesia.png","bomberos.png","banco.png","universidad.png","estadio.png","plaza.png","green.jpg"]
        self.image2=["b_casa.png","b_hospital.png","b_escuela.png","b_edificio.png","b_policia.png","b_iglesia.png","b_bomberos.png","b_banco.png","b_universidad.png","b_estadio.png","b_plaza.png","green.jpg"]
        self.image2mo=["info_casa.png","info_hospital.png","info_escuela.png","info_edificio.png","info_policia.png","info_iglesia.png","info_bomberos.png","info_banco.png","info_universidad.png","info_estadio.png","info_plaza.png","green.jpg"]
#-------------Lista contadores-------------
#-------------Lista contadores-------------
        self.cont=[0,0,0,0,0,0,0,0,0,0,0,0]
#-------------Lista de cuanto dinero pagara-
        self.dinepaga=[10,15,5,10,5,25,5,10,30,10,20,0]
#-------------Lista de Botones terreno-
        botonList = self.botonList = []
#-------------Lista de Botones compra-
        botonList2 = self.botonList2 = []

        for x in range (100):
            self.botonList.insert(0,0)

        for z in range (15):
            self.botonList2.insert(0,0)

#----------------LISTA de TERRENOS-----------------------
        self.terr=[]
        for x in range (100):
            self.terr.insert(0,0)
#-----------------------MENSAJES DE CHAT--------------------------------------
        self.chatimage=['chat_casa.png','chat_hospital.png','chat_escuela.png','chat_edificio.png','chat_policia.png','chat_iglesia.png','chat_bomberos.png','chat_banco.png','chat_universidad.png','chat_estadio.png','chat_plaza.png']
        self.posi=[0,0,0,0,0,0,0,0,0,0,0]
        self.stop=0
#-----------block time-------------
        self.final=0
        self.block1=0
        self.block2=0
        self.block3=0
        self.termino=0
#------------CONTADOR DE DINERO 30SEC-----------------------
        self.contador=0

#--------------------SONIDO---------------------------------
        sound = Sound("sonidoprincipal.wav")
        sound.Play(SOUND_ASYNC)

#-------------------Disparo atomatico de button-----------------------
        self.Bind(wx.EVT_CLOSE, self.cierra)
        self.Bind(wx.EVT_TIMER, self.tiempo)

        self.hora = wx.Timer(self, -1)
        self.hora.Start(400)# 1 minuto aproximadamente

#------------------Cartel de informacion--------------------------------------
        self.salida1=""
        self.salida2=""
        self.salida3=""
        self.bdine2 = wx.Font(12, wx.DECORATIVE, wx.ITALIC, wx.BOLD)
        otrotext = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)

        self.bdine=StaticText(self.vent,-1,label=self.salida1,pos=(419,13),size=(40 ,30 ))

        self.bdine.SetFont(self.bdine2)
        self.bdine.SetBackgroundColour("#1c2c2b")
        self.bdine.SetForegroundColour((255,255,255))

        self.bexp=StaticText(self.vent,-1,label=self.salida2,pos=(547,13),size=(40 ,30 ))
        self.bexp.SetFont(self.bdine2)
        self.bexp.SetBackgroundColour("#1c2c2b")
        self.bexp.SetForegroundColour((255,255,255))

        self.salida1=str (self.dine)
        self.bdine.SetLabel("$"+self.salida1)

        self.salida2=str(self.lvl)
        self.bexp.SetLabel(self.salida2)

        self.bpanel=StaticText(self.vent,-1,label=self.salida3,pos=(684,13),size=(309 ,30 ),style=wx.ALIGN_LEFT)
        self.bpanel.SetFont(otrotext)
        self.bpanel.SetForegroundColour((255,255,255))
        self.bpanel.SetBackgroundColour("#202020")

#--------------Terrenos----------------

        self.posix=[488,543,378,433,488,543,323,378,433,488,543,323,378,433,488,543,378,433,488,543,433,488,543,488,543]
        self.posiy=[198,198,253,253,253,253,308,308,308,308,308,363,363,363,363,363,418,418,418,418,473,473,473,528,528]
#----------------NIVEL 1-------------
#--------------------------Terreno n°1----------------------------
        for x in range (len(self.posix)):
            self.b = wx.Button(self.vent,x+1000,label="",pos=(self.posix[x],self.posiy[x]),size=(55,55))
            self.b.SetBitmap(BitmapFromImage(Image("green.jpg")))
            self.b.Bind(wx.EVT_BUTTON,self.onClick)
            self.botonList[x]=self.b
            self.botonList[x].Bind(EVT_BUTTON, self.onClick)
            self.b.Show()

#--------- COMPRAR TERRENOS---------------------------------

        self.terreno1=Button(self.vent,-1,label="",pos=(33,22),size=(55 ,55 ))
        self.terreno1.Bind(EVT_BUTTON,self.pnt1)
        self.terreno1.Show(False)

        self.terreno2=Button(self.vent,-1,label="",pos=(22,22),size=(55 ,55 ))
        self.terreno2.Bind(EVT_BUTTON,self.pnt2)
        self.terreno2.Show(False)

        self.terreno3=Button(self.vent,-1,label="",pos=(67,22),size=(55 ,55 ))
        self.terreno3.Bind(EVT_BUTTON,self.pnt3)
        self.terreno3.Show(False)

        self.impu=Button(self.vent,-1,label="",pos=(67,22),size=(55 ,55 ))
        self.impu.Bind(EVT_BUTTON,self.paga)
        self.impu.Show(False)

        self.pbn1a=Button(self.vent,-1,label="",pos=(33,22),size=(55 ,55 ))
        self.pbn1a.Bind(EVT_BUTTON,self.pbn1)
        self.pbn1a.Show(False)

        self.pbn2a=Button(self.vent,-1,label="",pos=(22,22),size=(55 ,55 ))
        self.pbn2a.Bind(EVT_BUTTON,self.pbn2)
        self.pbn2a.Show(False)

        self.pbn3a=Button(self.vent,-1,label="",pos=(67,22),size=(55 ,55 ))
        self.pbn3a.Bind(EVT_BUTTON,self.pbn3)
        self.pbn3a.Show(False)

        self.men=Button(self.vent,-1,label="",pos=(67,22),size=(55 ,55 ))
        self.men.Bind(EVT_BUTTON,self.mensaje)
        self.men.Show(False)



        return True

    def pnt1 (self,event):
        self.posixa=[213,268,323,378,433,213,268,323,378,433,213,268,323,213,268,213,268,213,268,323,268,323,378,378,433]
        self.posiya=[143,143,143,143,143,198,198,198,198,198,253,253,253,308,308,363,363,418,418,418,473,473,473,528,528]

        if self.lvl>= 230:
            for x in range (len(self.posixa)):
                self.b = wx.Button(self.vent,x+1000+25,label="",pos=(self.posixa[x],self.posiya[x]),size=(55,55))
                self.b.SetBitmap(BitmapFromImage(Image("green.jpg")))
                self.b.Bind(wx.EVT_BUTTON,self.onClick)
                self.botonList[x+25]=self.b
                self.botonList[x+25].Bind(EVT_BUTTON, self.onClick)
                self.b.Show()


#--------------------------Terreno n°2----------------------------

    def pnt2 (self,event):
        self.posixb=[48,103,158,213,268,323,378,433,488,543,488,543,48,103,158,48,103,158,48,103,158,48,103,158,158]
        self.posiyb=[88,88,88,88,88,88,88,88,88,88,143,143,143,143,143,198,198,198,253,253,253,308,308,308,363]
        if self.lvl>= 520:
            for x in range (len(self.posixb)):
                self.b = wx.Button(self.vent,x+1000+50,label="",pos=(self.posixb[x],self.posiyb[x]),size=(55,55))
                self.b.SetBitmap(BitmapFromImage(Image("green.jpg")))
                self.b.Bind(wx.EVT_BUTTON,self.onClick)
                self.botonList[x+50]=self.b
                self.botonList[x+50].Bind(EVT_BUTTON, self.onClick)
                self.b.Show()

#--------------------------Terreno n°3----------------------------

    def pnt3 (self,event):

        self.posixc=[48,103,48,103,158,48,103,158,213,48,103,158,213,268,323,48,103,158,213,268,323,378,433,488,543]
        self.posiyc=[363,363,418,418,418,473,473,473,473,528,528,528,528,528,528,583,583,583,583,583,583,583,583,583,583]
        if self.lvl>= 970:
            for x in range (len(self.posixc)):
                self.b = wx.Button(self.vent,x+1000+75,label="",pos=(self.posixc[x],self.posiyc[x]),size=(55,55))
                self.b.SetBitmap(BitmapFromImage(Image("green.jpg")))
                self.b.Bind(wx.EVT_BUTTON,self.onClick)
                self.botonList[x+75]=self.b
                self.botonList[x+75].Bind(EVT_BUTTON, self.onClick)
                self.b.Show()


#------------TIEMPO ---------------------------------------
    def cierra (self,event):
        self.hora.Stop()
        self.Destroy()

    def tiempo(self,event):
        datetime.datetime.now()
        self.contador+=1

        if  self.lvl>= 230 and self.block1!=1:
            evt = CommandEvent(EVT_BUTTON.typeId)
            evt.SetEventObject(self.terreno1)
            evt.SetId(self.terreno1.GetId())
            self.terreno1.GetEventHandler().ProcessEvent(evt)

            evt = CommandEvent(EVT_BUTTON.typeId)
            evt.SetEventObject(self.pbn1a)
            evt.SetId(self.pbn1a.GetId())
            self.pbn1a.GetEventHandler().ProcessEvent(evt)
            self.block1=1
        elif self.lvl>=520 and self.block2 !=1:
            evt = CommandEvent(EVT_BUTTON.typeId)
            evt.SetEventObject(self.terreno2)
            evt.SetId(self.terreno2.GetId())
            self.terreno2.GetEventHandler().ProcessEvent(evt)

            evt = CommandEvent(EVT_BUTTON.typeId)
            evt.SetEventObject(self.pbn2a)
            evt.SetId(self.pbn2a.GetId())
            self.pbn2a.GetEventHandler().ProcessEvent(evt)
            self.block2=1
        elif self.lvl>=970 and self.block3!=1:
            evt = CommandEvent(EVT_BUTTON.typeId)
            evt.SetEventObject(self.terreno3)
            evt.SetId(self.terreno3.GetId())
            self.terreno3.GetEventHandler().ProcessEvent(evt)

            evt = CommandEvent(EVT_BUTTON.typeId)
            evt.SetEventObject(self.pbn3a)
            evt.SetId(self.pbn3a.GetId())
            self.pbn3a.GetEventHandler().ProcessEvent(evt)
            self.block3=1
        else:
            evt = CommandEvent(EVT_BUTTON.typeId)
            evt.SetEventObject(self.impu)
            evt.SetId(self.impu.GetId())
            self.impu.GetEventHandler().ProcessEvent(evt)

            evt = CommandEvent(EVT_BUTTON.typeId)
            evt.SetEventObject(self.men)
            evt.SetId(self.men.GetId())
            self.men.GetEventHandler().ProcessEvent(evt)

#--------------CONTROL DE TIEMPO Y SALIDA-------------------------------

    def paga(self, event):
        if self.contador==60:
            for x in range (len(self.cont)):
                tot=self.cont[x]*self.dinepaga[x]
                self.dine=self.dine+tot
                self.salida1=str (self.dine)
                self.bdine.SetLabel("$"+self.salida1)
                sound = Sound("paga.wav")
                sound.Play(SOUND_ASYNC)
                self.contador=0


        if self.termino!=1:
            self.final=0
            for x in range(len(self.terr)):
                if self.terr[x]!=0:
                    self.final+=1
                    if self.final==100:
                        self.termino=1
                        image_file = 'pfinal.png'
                        bmp13 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
                        style3 =  wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX ^ wx.MINIMIZE_BOX^ wx.CLOSE_BOX
                        self.vent4=Frame(None,-1,"",pos=(100,25),size=(1366 ,768 ),style=style3 )
                        self.vent4.Maximize(True)
                        self.vent4.Show()

                        self.fondofinal = wx.StaticBitmap(self.vent4, -1, bmp13,pos=(0,0),size=(1366,768))

                        self.bfinal=Button(self.fondofinal,-1,label="",pos=(921,539),size=(73 ,42 ))
                        self.bfinal.SetBitmap(BitmapFromImage(Image("bsal.png")))
                        self.bfinal.Bind(EVT_BUTTON,self.terminajuego)
                        self.bfinal.Show()
                        self.fondofinal.Show()

#--------------------------Terreno n°2----------------------------

    def mensaje(self,event):
        if self.lvl>=0 and self.lvl<10 and self.stop==0:
            self.chat.SetBitmap(BitmapFromImage(Image("b_chat2.png")))
            self.posi[0]=1
            self.stop+=1
            n2="TIENES UN MENSAJE"
            self.bpanel.SetLabel(n2)
            sound = Sound("sonidoprincipal.wav")
            sound.Play(SOUND_ASYNC)
        elif self.lvl>=10 and self.lvl<30 and self.stop==1:
            self.chat.SetBitmap(BitmapFromImage(Image("b_chat2.png")))
            self.posi[1]=1
            self.stop+=1
            sound = Sound("sonidodemensaje.wav")
            sound.Play(SOUND_ASYNC)
            n2="TIENES UN MENSAJE"
            self.bpanel.SetLabel(n2)
        elif self.lvl>=30 and self.lvl<240  and self.stop==2:
            self.chat.SetBitmap(BitmapFromImage(Image("b_chat2.png")))
            self.posi[2]=1
            self.stop+=1
            sound = Sound("sonidodemensaje.wav")
            sound.Play(SOUND_ASYNC)
            n2="TIENES UN MENSAJE"
            self.bpanel.SetLabel(n2)
        elif self.lvl>=230 and self.lvl<250 and self.stop==3:
            self.chat.SetBitmap(BitmapFromImage(Image("b_chat2.png")))
            self.posi[3]=1
            self.stop+=1
            sound = Sound("sonidodemensaje.wav")
            sound.Play(SOUND_ASYNC)
            n2="TIENES UN MENSAJE"
            self.bpanel.SetLabel(n2)
        elif self.lvl>=250 and self.lvl<270 and self.stop==4:
            self.chat.SetBitmap(BitmapFromImage(Image("b_chat2.png")))
            self.posi[4]=1
            self.stop+=1
            sound = Sound("sonidodemensaje.wav")
            sound.Play(SOUND_ASYNC)
        elif self.lvl>=270 and self.lvl<525 and self.stop==5:# ANDA
            self.chat.SetBitmap(BitmapFromImage(Image("b_chat2.png")))
            self.posi[5]=1
            self.stop+=1
            sound = Sound("sonidodemensaje.wav")
            sound.Play(SOUND_ASYNC)
            n2="TIENES UN MENSAJE"
            self.bpanel.SetLabel(n2)
        elif self.lvl>=525 and self.lvl<545  and self.stop==6:
            self.chat.SetBitmap(BitmapFromImage(Image("b_chat2.png")))
            self.posi[6]=1
            self.stop+=1
            sound = Sound("sonidodemensaje.wav")
            sound.Play(SOUND_ASYNC)
            n2="TIENES UN MENSAJE"
            self.bpanel.SetLabel(n2)
        elif self.lvl>=545 and self.lvl<580 and self.stop==7:
            self.chat.SetBitmap(BitmapFromImage(Image("b_chat2.png")))
            self.posi[7]=1
            self.stop+=1
            sound = Sound("sonidodemensaje.wav")
            sound.Play(SOUND_ASYNC)
            n2="TIENES UN MENSAJE"
            self.bpanel.SetLabel(n2)
        elif self.lvl>=580 and self.lvl<1030 and self.stop==8:
            self.chat.SetBitmap(BitmapFromImage(Image("b_chat2.png")))
            self.posi[8]=1
            self.stop+=1
            sound = Sound("sonidodemensaje.wav")
            sound.Play(SOUND_ASYNC)
            n2="TIENES UN MENSAJE"
            self.bpanel.SetLabel(n2)
        elif self.lvl>=1030 and self.lvl<1085 and self.stop==9:
            self.chat.SetBitmap(BitmapFromImage(Image("b_chat2.png")))
            self.posi[9]=1
            self.stop+=1
            sound = Sound("sonidodemensaje.wav")
            sound.Play(SOUND_ASYNC)
            n2="TIENES UN MENSAJE"
            self.bpanel.SetLabel(n2)
        elif self.lvl>=1085 and self.lvl<2000 and self.stop==10:
            self.chat.SetBitmap(BitmapFromImage(Image("b_chat2.png")))
            self.posi[10]=1
            self.stop+=1
            sound = Sound("sonidodemensaje.wav")
            sound.Play(SOUND_ASYNC)
            n2="TIENES UN MENSAJE"
            self.bpanel.SetLabel(n2)


#--------------------------PARTE DEL MENU---------------------
    def AbrirMenu(self,event):
        self.menu.Show(False)
        self.chat.Show(False)
        bmp1=wx.Image('f_men2.png',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1=wx.StaticBitmap(self.vent,-1,bmp1,pos=(659,93),size=(339,607))
        self.button3 = wx.Button(self.bitmap1, id=-1, label='', size=(64,64), pos=(175,0))
        self.button3.SetBitmap(BitmapFromImage(Image("b2_men.png")))
        self.button3.Bind(EVT_BUTTON,self.CerrarMenu)

        evt = CommandEvent(EVT_BUTTON.typeId)
        evt.SetEventObject(self.pbn1a)
        evt.SetId(self.pbn1a.GetId())
        self.pbn1a.GetEventHandler().ProcessEvent(evt)

        evt = CommandEvent(EVT_BUTTON.typeId)
        evt.SetEventObject(self.pbn2a)
        evt.SetId(self.pbn2a.GetId())
        self.pbn2a.GetEventHandler().ProcessEvent(evt)

        evt = CommandEvent(EVT_BUTTON.typeId)
        evt.SetEventObject(self.pbn3a)
        evt.SetId(self.pbn3a.GetId())
        self.pbn3a.GetEventHandler().ProcessEvent(evt)


        #BOTONES DE CONSTRUIR

        for y in range (3):
            n=self.image2[y]
            self.c = wx.Button(self.bitmap1,id=y+1000,label="",pos=(y*100+30,78),size=(80,80))
            self.c.Bind(wx.EVT_BUTTON,self.onClick2)
            self.c.SetBitmap(BitmapFromImage(Image(n)))
            self.botonList2[y]=self.c
            self.c.Bind(EVT_ENTER_WINDOW,self.MO)
            self.c.Bind(EVT_LEAVE_WINDOW,self.ML)
            self.c.Show()

        comprabomba=wx.Button(self.bitmap1,id=-1,label='',size=(80,80),pos=(229,376))
        comprabomba.SetBitmap(BitmapFromImage(Image("b_bomba.png")))
        comprabomba.Show()
        comprabomba.Bind(EVT_BUTTON,self.comprabomba)

        self.bitmap1.Show()

    def pbn1 (self,event):
        if self.lvl>=230:
            for y in range (3):
                n=self.image2[y+3]
                self.c = wx.Button(self.bitmap1,id=y+1003,label="",pos=(y*100+30,178),size=(80,80))
                self.c.Bind(wx.EVT_BUTTON,self.onClick2)
                self.c.SetBitmap(BitmapFromImage(Image(n)))
                self.botonList2[y+3]=self.c
                self.c.Bind(EVT_ENTER_WINDOW,self.MO)
                self.c.Bind(EVT_LEAVE_WINDOW,self.ML)

                self.c.Show()
            self.bitmap1.Show()
    def pbn2(self,event):
        if self.lvl>=520:
            for y in range (3):
                n=self.image2[y+6]
                self.c = wx.Button(self.bitmap1,id=y+1006,label="",pos=(y*100+30,278),size=(80,80))
                self.c.Bind(wx.EVT_BUTTON,self.onClick2)
                self.c.SetBitmap(BitmapFromImage(Image(n)))
                self.botonList2[y+6]=self.c
                self.c.Bind(EVT_ENTER_WINDOW,self.MO)
                self.c.Bind(EVT_LEAVE_WINDOW,self.ML)

                self.c.Show()
            self.bitmap1.Show()
    def pbn3(self,event):
        if self.lvl>=970:
            for y in range (2):
                n=self.image2[y+9]
                self.c = wx.Button(self.bitmap1,id=y+1009,label="",pos=(y*100+30,378),size=(80,80))
                self.c.Bind(wx.EVT_BUTTON,self.onClick2)
                self.c.SetBitmap(BitmapFromImage(Image(n)))
                self.botonList2[y+9]=self.c
                self.c.Bind(EVT_ENTER_WINDOW,self.MO)
                self.c.Bind(EVT_LEAVE_WINDOW,self.ML)
                self.c.Show()
            self.bitmap1.Show()

    def CerrarMenu(self,event):
        self.menu.Show()
        self.bitmap1.Show(False)
        self.button3.Show(False)
        self.chat.Show()

    def AbrirChat(self,event):
        self.chat.Show(False)
        self.bitmap1.Show(False)
        self.menu.Show(False)
        bmp1=wx.Image('f_chat.png',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap2=wx.StaticBitmap(self.vent,-1,bmp1,pos=(645,59),size=(339,607))
        self.button4 = wx.Button(self.bitmap2, id=-1, label='', size=(37,60), pos=(300,39))
        self.button4.SetBitmap(BitmapFromImage(Image("ce_chat.png")))
        self.button4.Bind(EVT_BUTTON,self.CerrarChat)

#ACA SE AGREGAN LOS MJES DE INFO DE CASAS, EDIFICIOS, ETC
#CREAR UN STATICBITMAP PARA CADA MENSAJE
        for x in range (len(self.chatimage)):
            self.chat.SetBitmap(BitmapFromImage(Image("b_chat.png")))
            if self.posi[x]==1:
                bmp2=wx.Image(self.chatimage[x],wx.BITMAP_TYPE_ANY).ConvertToBitmap()
                self.bitmap3=wx.StaticBitmap(self.bitmap2,-1,bmp2,pos=(0,105),size=(341,448))
                self.bitmap3.SetBitmap(BitmapFromImage(Image(self.chatimage[x])))
                self.bitmap3.Show()
                self.vent.Show()
                self.posi[x]=0

        self.vent.Show()

    def CerrarChat(self,event):
        self.chat.Show()
        self.bitmap2.Show(False)
        self.button4.Show(False)
        self.menu.Show()

#-------------------SISTEMA DE COMPRAS--------------------------

    def onClick2(self,e):
        ident = e.GetId() - 1000
        for y in range (len(self.ct)):
            self.ct[y]=0
        if self.dine>=self.dn[ident]:
            self.ct[ident]=1
            sound = Sound("click.wav")
            sound.Play(SOUND_ASYNC)
            n2="Felicidades por su compra"
            self.bpanel.SetLabel(n2)
        else:
            n2=("No tiene dinero suficiente")
            self.bpanel.SetLabel(n2)

    def MO(self,e):
        ident = e.GetId() - 1000
        n=self.image2mo[ident]
        bmp2=wx.Image(n,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.bitmap2=wx.StaticBitmap(self.bitmap1,-1,bmp2,pos=(30,479),size=(280,129))
        self.bitmap2.Show()

    def ML(self,e):
        self.bitmap2.Show(False)


    def comprabomba(self,event):
        for y in range (len(self.ct)):
            self.ct[y]=0
        if self.dine>=0:
            self.ct[11]=1
            sound = Sound("click.wav")
            sound.Play(SOUND_ASYNC)
            n2="Puede destruir cualquier edificio"
            self.bpanel.SetLabel(n2)

#------------------------PONE TERRENOS----------------------
    def onClick(self,e):
        ident = e.GetId() - 1000
        if self.terr[ident]==0 or self.ct[11]==1:
            for x in range (len(self.ct)):
                if self.ct[x]==1:
                    self.botonList[ident].SetBitmap(BitmapFromImage(Image(self.image[x])))
                    self.ct[x]-=1
                    self.cont[x]=self.cont[x]+1
                    self.dine-=self.dn[x]
                    self.salida1=str (self.dine)
                    self.bdine.SetLabel("$"+self.salida1)
                    self.lvl=self.lvl+self.exp[x]
                    self.salida2=str (self.lvl)
                    self.bexp.SetLabel(self.salida2)
                    if x==11:
                        posi=self.terr[ident]-1
                        self.terr[ident]=0
                        self.cont[posi]-=1
                    else:
                        self.terr[ident]=(x+1)
                        sound = Sound("compra.wav")
                        sound.Play(SOUND_ASYNC)
                    if x==11:
                        sound = Sound("bomba.wav")
                        sound.Play(SOUND_ASYNC)

    def iniciajuego (self,event):
        self.vent3.Close(True)
        sound = Sound("sonidodemensaje.wav")
        sound.Play(SOUND_ASYNC)

    def terminajuego(self,event):
        self.vent2.Close(True)
        self.vent4.Close(True)

    def Cierratodo(self,event):
        self.vent3.Close(True)
        self.vent2.Close(True)

    def bcj (self,event):
        self.vent2.Close(True)
App=Miapp()
App.MainLoop()