import streamlit as st
import time
import random

st.set_page_config(page_title='Cosa facciamo stasera?', page_icon='icona.png')
st.title('Decisore ufficiale di serate!')
st.write('Siete indecisi? Nessun problema. Cliccate e lasciate scegliere al destino.')

if 'pausa_fatta' not in st.session_state:
    with st.spinner('Prima di tutto...'):
        time.sleep(3)
    st.session_state['pausa_fatta']=True

x = st.slider('Quanto mi ami?', 0, 100)
if 0<=x<=50:
    st.write('Così poco? :(')
elif 50<x<=80:
    st.write('Mi accontento :)')
elif 80<x<=100:
    st.write('YAAAAAAAY :D')

st.divider()
st.write("Come stai oggi?")
voto = st.feedback('stars')
if voto is not None:
    if voto<=1:
        st.write("mi spiace amore, ti meriti un bacione ;)")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCnmWCrJ7MXBQfnmS7qvhQAwqnHoWGsUFKSd-jyUWA7w&s=10")
    elif 2<=voto<=3:
        st.write("potrebbe andare meglio, ti do subito un bacione!")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCQwt0CznCtARjwOF8R1cijCdKjs__iQ1dSyJQQK-dkg&s=10")
    elif voto==4:
        st.write("che belloooo, MWAAAAH!")
        st.image("https://i.pinimg.com/736x/b3/46/a2/b346a2d7498ba7351c906718948dfbf5.jpg")


st.divider()
activated = st.toggle('Ti amo <3')
if activated:
    st.write('Anche io ti amo <3333')

st.divider()
#Casa o fuori?
scelta_luogo = st.selectbox('Dove passiamo la serata?', ['Nel chill a casa', 'Usciamo fuori'])

st.divider() #separatore

if scelta_luogo == 'Nel chill a casa':
    attivita_casa = st.radio('Cosa vi va di fare?', ['Guardare un film o qualcosa su youtube', 'Mangiare qualcosa insieme'])
    if attivita_casa == 'Guardare un film o qualcosa su youtube':
        film = ['Film della marvel (vedi lista)', 'Film dello studio ghibli', 'ASMR di Cozygiulz', 'Film o serie di Universum']
        st.info('Siamo entrambi troppo indecisi, continua a cliccare finchè non esce quello giusto!')
        if st.button('Scegli un film a caso'):
            st.session_state['film_scelto'] = random.choice(film)
        if 'film_scelto' in st.session_state:
            st.write(f"Proposta: {st.session_state['film_scelto']}")
            if st.button('Va bene questo film!'):
                st.success(f"Stasera si guarda: **{st.session_state['film_scelto']}**")
    elif attivita_casa == 'Mangiare qualcosa insieme':
        cibo_casa = ["Ordiniamo una pizza", "Cuciniamo l'omu rice", "Ordiniamo cinese e pan coniglio!", "Cuciniamo qualcosa che ci ispira"]
        st.info('Non ti convince? Continua a cliccare')
        if st.button('Scegli cosa mangiare'):
            st.session_state['cibo_scelto'] = random.choice(cibo_casa)
        if 'cibo_scelto' in st.session_state:
            st.write(f"Proposta: {st.session_state['cibo_scelto']}")
            if st.button('Va bene questo cibo!'):
                st.success(f'Stasera si mangia: **{st.session_state['cibo_scelto']}**')

elif scelta_luogo== 'Usciamo fuori':
    attivita_fuori = st.radio('Qual è il piano?', ['Andiamo a mangiare qualcosa', 'Facciamo un giro in centro'])
    if attivita_fuori == 'Andiamo a mangiare qualcosa':
        ristoranti = ['Aperitivo con vista sassi', 'Pizzaaaa', 'Smash burger']
        st.info('Non ti va? Scegli altro')
        if st.button('Cosa vuoi mangiare?'):
            st.session_state['risto_scelto'] = random.choice(ristoranti)
        if 'risto_scelto' in st.session_state:
            st.write(f"Proposta: {st.session_state['risto_scelto']}")
            if st.button('Va bene questo!'):
                st.success(f"Il destino dice: **{st.session_state['risto_scelto']}**")
    elif attivita_fuori == 'Facciamo un giro in centro':
        posti = ['pic-nic al castello', 'chilling al castello', 'giretto in centro o nei sassi', 'drink casuale']
        st.info('Non sei nel mood? Scegli altro')
        if st.button('Dove andiamo?'):
            st.session_state['posto_scelto'] = random.choice(posti)
        
        if 'posto_scelto' in st.session_state:
            st.write(f"Proposta: {st.session_state['posto_scelto']}")
            if st.button("Siamo d'accordo?"):
                st.success(f"Perfetto! Allora {st.session_state['posto_scelto']}")
