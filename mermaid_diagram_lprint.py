import streamlit as st
from pathlib import Path

st.set_page_config(page_title="LPrint Function Diagram", layout="wide")

st.title("Mermaid Diagram Generator")
st.markdown("Enter a function name to generate its Mermaid diagram.")

# Simulated static mapping of a few function relationships
function_call_map = {
    "lprintAddPrinter": ["lprintIsPrinterInUse", "lprintLog", "lprintSavePrinters"],
    "lprintDeletePrinter": ["lprintLog", "lprintSavePrinters"],
    "lprintGetPrinter": [],
}

# Input from user
func_name = st.text_input("Enter function name (e.g., lprintAddPrinter)")

if func_name:
    called_funcs = function_call_map.get(func_name)

    if called_funcs is None:
        st.warning(f"Function '{func_name}' not found.")
    elif not called_funcs:
        st.info(f"Function '{func_name}' does not call any other functions.")
    else:
        st.subheader("Mermaid Diagram")

        # Mermaid diagram
        diagram = f"graph TD\n    {func_name}"
        for callee in called_funcs:
            diagram += f" --> {callee}"

        st.code(diagram, language="mermaid")
