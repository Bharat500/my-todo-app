import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("Made with Streamlit")
st.subheader("This is my todo app.")
st.write("\n")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox is True:
        todos.pop(index)
        print(todos)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

    #st.checkbox(todo, key=f"todo_{index}")

st.text_input(label="Enter a new todo",
              placeholder= "Enter a new todo.... ",
              on_change=add_todo, key="new_todo")

print("hello")

st.session_state
