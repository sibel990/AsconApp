from nicegui import app, ui
import ascon as asc

app.native.window_args['resizable'] = False

methodlar = {1: 'Ascon-128', 2: 'Ascon-128a'}


def sifirla():
    anahtarText.value = ""
    nonceText.value = ""
    tagText.value = ""
    sonucText.value = ""
    methodToggle.value = 1



def sifrele():
    
    if sifText.value != "" and bVeriText.value != "":
        data = sifText.value
        bData = bVeriText.value
        method = methodlar[methodToggle.value]
        print(method)
        deger = asc.sifrele_aead(data,bData,method)

        anahtar = deger[0]
        nonce = deger[1]
        sonuc = deger[2]
        tag = deger[3]

        anahtarText.value = anahtar
        nonceText.value = nonce
        tagText.value = tag
        sonucText.value = sonuc
    else:
        ui.notify("Alanları Boş Bırakmayın")



def desifrele():
    method = methodlar[methodToggle2.value]
    bdata = bVeriText2.value
    dkey = bytes.fromhex(anahtarText2.value) 
    dnonce = bytes.fromhex(nonceText2.value) 
    dshex = bytes.fromhex(sifText2.value) 

    sonuc = asc.desifrele_aead(bdata,dkey,dnonce,dshex,method)
    sonucText2.value = sonuc
        


with ui.tabs().classes('w-full') as tabs:
    sifreleTab = ui.tab('Şifrele')
    desifreleTab = ui.tab('Çöz')
with ui.tab_panels(tabs, value=sifreleTab).classes('w-full'):
    with ui.tab_panel(sifreleTab):
        with ui.card().classes('no-shadow border-[1px]'):
            with ui.column():
                ui.label('Şifreleme Methodu :')
                methodToggle = ui.toggle({1: 'Ascon-128', 2: 'Ascon-128a'}, value=1).props('no-caps')
                ui.label('Şifrelenecek Metin :')
                sifText = ui.textarea(label='Metin', placeholder='metin girin',).props('clearable').props('outlined').props('autogrow : false').style('width: 600px')
                ui.label('Bağıntılı Veri :')
                bVeriText = ui.textarea(label='Veri', placeholder='veri girin').props('clearable').props('outlined').props('autogrow : false').style('width: 600px')
                ui.label('Anahtar (random olarak atanır) :')
                anahtarText =ui.textarea(label='Anahtar', placeholder='anahtar girin').props('clearable').props('outlined').props('autogrow : false').props('readonly').style('width: 600px')                
                ui.label('Nonce (random olarak atanır) :')
                nonceText = ui.textarea(label='Nonce', placeholder='nonce girin').props('clearable').props('outlined').props('autogrow : false').props('readonly').style('width: 600px')
                
                button1 = ui.button('Şifrele!',on_click=sifrele).props('no-caps')
                ui.separator()

                ui.label('Çıktı :')
                tagText = ui.textarea(label='Tag', placeholder='Tag').props('clearable').props('outlined').props('autogrow : false').props('readonly').style('width: 600px')
                sonucText = ui.textarea(label='Şifrelenmiş Metin', placeholder='Şifrelenmiş Metin').props('outlined').style('width: 600px; ')
                ui.button('Sıfırla',on_click=sifirla).props('no-caps')

    with ui.tab_panel(desifreleTab):
        with ui.card().classes('no-shadow border-[1px]'):
            with ui.column():
                ui.label('Deşifreleme Methodu :')
                methodToggle2 = ui.toggle({1: 'Ascon-128', 2: 'Ascon-128a'}, value=1).props('no-caps')
                ui.label('Deşifrelenecek Metin :')
                sifText2 = ui.textarea(label='Metin', placeholder='metin girin',).props('clearable').props('outlined').props('autogrow : false').style('width: 600px')
                ui.label('Bağıntılı Veri :')
                bVeriText2 = ui.textarea(label='Veri', placeholder='veri girin').props('clearable').props('outlined').props('autogrow : false').style('width: 600px')
                ui.label('Anahtar (random olarak atanır) :')
                anahtarText2 =ui.textarea(label='Anahtar', placeholder='anahtar girin').props('clearable').props('outlined').props('autogrow : false').style('width: 600px')                
                ui.label('Nonce (random olarak atanır) :')
                nonceText2 = ui.textarea(label='Nonce', placeholder='nonce girin').props('clearable').props('outlined').props('autogrow : false').style('width: 600px')
                
                button2 = ui.button('Deşifrele!',on_click=desifrele).props('no-caps')
                ui.separator()

                ui.label('Çıktı :')
                
                sonucText2 = ui.textarea(label='Deşifrelenmiş Metin', placeholder='Deşifrelenmiş Metin').props('outlined').style('width: 600px; ')
                ui.button('Sıfırla',on_click=sifirla).props('no-caps')






ui.run(reload=False,native=True, window_size=(1000, 700), fullscreen=False, language='tr', title='SibAscon')
