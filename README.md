# 🔑 Gerador de Senhas com Streamlit

Este é um projeto simples e funcional de **gerador de senhas seguras**, construído com StreamLit. O objetivo é permitir que usuários gerem senhas com diferentes critérios, e tenham acesso a um pequeno histórico das senhas criadas durante a sessão.


## 🚀 Funcionalidades

- Geração de senhas aleatórias com base em critérios personalizados:

  - Letras maiúsculas (A-Z)
  - Letras minúsculas (a-z)
  - Dígitos (0-9)
  - Símbolos (!@#$...)
- Histórico das senhas geradas durante a sessão.
- Opção de limpar o histórico.
- Armazenamento temporário das senhas em arquivo JSON.

 O histórico é **resetado automaticamente ao iniciar o app**, evitando acúmulo de dados.


## 📦 Tecnologias Utilizadas

- Python 3
- Streamlit
- JSON
- Bibliotecas (`random`, `string`, `datetime`, `os`)
