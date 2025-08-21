import streamlit as st

st.title("Calculadora de CR")

# inicializa lista de disciplinas
if "disciplinas" not in st.session_state:
    st.session_state.disciplinas = []

# --- Inputs ---
col1, col2 = st.columns(2)

with col1:
    creditos = st.number_input("Créditos da disciplina", min_value=0, step=1)
with col2:
    conceito = st.text_input("Conceito (A-F)").lower()

# botão para adicionar disciplina
if st.button("Adicionar disciplina"):
    valor = {"a":4, "b":3, "c":2, "d":1, "f":0}.get(conceito, None)
    if valor is None:
        st.error("Conceito inválido!")
    else:
        st.session_state.disciplinas.append((creditos, valor, conceito.upper()))
        st.success(f"Disciplina adicionada! Total: {len(st.session_state.disciplinas)}")

# --- Mostra tabela ---
if st.session_state.disciplinas:
    st.subheader("Disciplinas adicionadas")
    tabela = []
    for i, (c, v, conc) in enumerate(st.session_state.disciplinas, start=1):
        tabela.append({"Nº": i, "Créditos": c, "Conceito": conc, "Valor": v})
    st.table(tabela)

# --- Calcula CR ---
if st.button("Calcular CR final"):
    if not st.session_state.disciplinas:
        st.warning("Nenhuma disciplina adicionada!")
    else:
        multiplicadores = [c * v for c, v, _ in st.session_state.disciplinas]
        total_creditos = sum([c for c, _, _ in st.session_state.disciplinas])
        media = sum(multiplicadores) / total_creditos

        st.subheader(f"CR final: {media:.2f}")

        # avaliação
        if media < 1.5:
            st.write("Seu CR está muito baixo.")
        elif 1.5 <= media < 2:
            st.write("Seu CR está baixo.")
        elif 2 <= media < 2.5:
            st.write("Seu CR está médio.")
        elif 2.5 <= media < 3:
            st.write("Seu CR está bom.")
        else:
            st.write("Seu CR está excelente.")
