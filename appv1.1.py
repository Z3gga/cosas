import requests
import json
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import random as rd
import pandas as pd
logo = Image.open("icon.png")
st.set_page_config(page_title="Comparador de equipos Pokémon", page_icon=logo, layout="wide")

class pokemon():
    def __init__(self,name,sprite,type1,type2,Hp,Atq,Def,SpA,SpD,Spe):
        self.name = name
        self.sprite = sprite
        self.type1 = type1
        self.type2= type2
        self.Hp= Hp
        self.Atq= Atq
        self.Def= Def
        self.SpA= SpA
        self.SpD= SpD
        self.Spe= Spe       

types= {
    "normal":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/1.png",
    "fighting":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/2.png",
    "flying":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/3.png",
    "poison":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/4.png",
    "ground":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/5.png",
    "rock":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/6.png",
    "bug":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/7.png",
    "ghost":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/8.png",
    "steel":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/9.png",
    "fire":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/10.png",
    "water":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/11.png",
    "grass":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/12.png",
    "electric":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/13.png",
    "psychic":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/14.png",
    "ice":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/15.png",
    "dragon":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/16.png",
    "dark":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/17.png",
    "fairy":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/18.png",
    "None":False}
pok = []
team=[]
# Función para seleccionar Pokémon
def seleccionador(index):
    # Usa `session_state` para manejar el valor del input
    Specie = st.text_input(f"Selecciona un Pokémon {index + 1}", key=f"pokemon_name_{index}")
    
    return Specie



for x in range(6):
    pokemon_name = seleccionador(x)
    if pokemon_name:  # Solo agrega si `pokemon_name` no está vacío
        pok.append(pokemon_name)
print(pok)


for x in range (len(pok)):
        vname=pok[x]
        url="https://pokeapi.co/api/v2/pokemon/"+vname
        cosa = requests.get(url)
        data = cosa.json()
        
        vsprite = data.get("sprites").get("front_default")

        vtype1 = data.get("types", [{}])[0].get("type", {}).get("name") if len(data.get("types", [])) > 0 else "None"

        # Acceder al segundo tipo de forma segura
        vtype2 = data.get("types", [{}])[1].get("type", {}).get("name") if len(data.get("types", [])) > 1 else "None"

        vhp = data.get("stats", [{}])[0].get("base_stat")

        vatq= data.get("stats", [{}])[1].get("base_stat")
        vdef = data.get("stats", [{}])[2].get("base_stat")
        vspa= data.get("stats", [{}])[3].get("base_stat")
        vspd = data.get("stats", [{}])[4].get("base_stat")
        vspe = data.get("stats", [{}])[5].get("base_stat")
    

        x = pokemon(vname, vsprite, types[vtype1],types[vtype2],vhp,vatq,vdef,vspa,vspd,vspe)
        team.append(x)

st.title("Comparador de equipos Pokémon")



    # Mostrar imágenes solo si hay suficientes elementos en `img`

def Look(p):
    st.subheader(team[p].name.capitalize()) 
    st.image(team[p].sprite, use_column_width=True)
    st.image(team[p].type1, width=107)
    if team[p].type2:
        st.image(team[p].type2, width=107)

    df=pd.DataFrame({"index":["Hp","Atq","Def","SpA","SpD","Spe"],"a":[team[p].Hp,team[p].Atq,team[p].Def,team[p].SpA,team[p].SpD,team[p].Spe]})
    dfnew=df.rename(columns=df.iloc[0]).drop(df.index[0]).to_string(index=False)

    st.table(dfnew)

espacio1 = st.empty()

with espacio1:
            col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
        # Mostrar imágenes solo si están disponibles
if len(pok) >= 1:
            with col1:
                Look(0)

if len(pok) >= 2:
            with col2:
                Look(1)
if len(pok) >= 3:
            with col3:
                Look(2)
if len(pok) >= 4:
            with col4:
                Look(3)
if len(pok) >= 5:
            with col5:
                Look(4)
if len(pok) >= 6:
            with col6:
                Look(5)






