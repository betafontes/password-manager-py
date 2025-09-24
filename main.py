import json
import os
import streamlit as st
import random
import string
from datetime import datetime

# ---- Arquivo local para armazenamento das senhas ----
arquivo_armazenamento = "senhas.json"


# ---- Função para carregar senhas ----
def carregar_senhas():
  if os.path.exists(arquivo_armazenamento):
    with open(arquivo_armazenamento, "r") as f:
      return json.load(f)
  return []

# ---- Função para salvar senhas ----
def salvar_senhas(data):
  with open(arquivo_armazenamento, "w") as f:
    json.dump(data, f, indent=4)

# ---- Função para gerar senha ----
def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_digitos=True, usar_simbolos=True):
  caracteres = ""
  if usar_maiusculas:
    caracteres += string.ascii_uppercase
  if usar_minusculas:
    caracteres += string.ascii_lowercase
  if usar_digitos:
    caracteres += string.digits
  if usar_simbolos:
    caracteres += string.punctuation

  if not caracteres:
    raise ValueError("Selecione pelo menos um tipo de caractere.")

  return ''.join(random.choice(caracteres) for _ in range(tamanho))

# ---- Interface ----
st.set_page_config(page_title="Gerador de Senhas", page_icon="🔑", layout="centered")

st.title("🔑 Gerenciador de Acesso - Gerador de Senhas")

menu = st.sidebar.radio("Menu", ["Gerar Senha", "Histórico"])

# ---- Gerar Senha ----
if menu == "Gerar Senha":

  # Centralizar os elementos
  st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

  tamanho = st.number_input("Tamanho da senha:", min_value=4, max_value=50, value=12, step=1)

  usar_maiusculas = st.checkbox("Incluir letras maiúsculas (A-Z)", value=True)
  usar_minusculas = st.checkbox("Incluir letras minúsculas (a-z)", value=True)
  usar_digitos = st.checkbox("Incluir dígitos (0-9)", value=True)
  usar_simbolos = st.checkbox("Incluir símbolos (!@#$...)", value=True)

  if st.button("🔑 Gerar Senha"):
    
    try:
      senha_gerada = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_digitos, usar_simbolos)
      st.success("Senha gerada com sucesso!")
      st.code(senha_gerada, language="text")

      st.text_input("Copiar senha:", senha_gerada)

      # ---- Guardar no histórico da sessão ----
      if "historico" not in st.session_state:
        st.session_state.historico = []
      st.session_state.historico.append(senha_gerada)

      # ---- Guardar no arquivo (com timestamp) ----
      dados = carregar_senhas()
      dados.append({"senha": senha_gerada, "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
      salvar_senhas(dados)

    except ValueError as e:
      st.error(str(e))

  st.markdown("</div>", unsafe_allow_html=True)

# ---- Histórico ----
elif menu == "Histórico":
  
  dados = carregar_senhas()

  if len(dados) == 0:
    st.info("Nenhuma senha gerada ainda.")
  else:
    for item in dados[::-1]:  # Última primeiro
      st.code(item["senha"], language="text")
      st.caption(f"⏰ Gerada em: {item['data']}")

    # ---- Opção de limpar histórico -----
    if st.button("🗑 Limpar Histórico"):
      salvar_senhas([])
      st.session_state.historico = []
      st.warning("Histórico limpo com sucesso!")
      st.rerun()
