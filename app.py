import streamlit as st
st.title("Calculator with History")
if 'history' not in st.session_state:
    st.session_state.history = []
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)
operation = st.selectbox("Choose an operation", ["Addition", "Subtraction", "Multiplication", "Division"])
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        expression = f"{num1} + {num2} = {result}"
    elif operation == "Subtraction":
        result = num1 - num2
        expression = f"{num1} - {num2} = {result}"
    elif operation == "Multiplication":
        result = num1 * num2
        expression = f"{num1} * {num2} = {result}"
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            expression = f"{num1} / {num2} = {result}"
        else:
            result = "Error! Division by zero."
            expression = f"{num1} / {num2} = {result}"
    st.success(f"The result is: {result}")
    st.session_state.history.append(expression)
st.subheader("History")
if st.session_state.history:
    for exp in st.session_state.history:
        st.write(exp)
else:
    st.write("No history yet.")
if st.button("Reset History"):
    st.session_state.history.clear()
    st.success("History reset.")

st.sidebar.info("Calculator By Ali")
