import streamlit as st
import json
import os

FILE = "progress.json"

if os.path.exists(FILE):
    with open(FILE, "r") as f:
        progress = json.load(f)
else:
    progress = {}

def checkbox(label):
    checked = st.checkbox(label, value=progress.get(label, False))
    progress[label] = checked
    with open(FILE, "w") as f:
        json.dump(progress, f)

        
st.title("QA learning roadmap tracking")

st.header("python")

st.checkbox("variable")
st.checkbox("data types")
st.checkbox("if/else")
st.checkbox("while loops")
st.checkbox("for loops")
st.checkbox("functions")
st.checkbox("lists")
st.checkbox("calculator project")
st.checkbox("file handling")
st.checkbox("modules")
st.checkbox("try/except")

st.header("SQL")

st.checkbox("create database")
st.checkbox("create table")
st.checkbox("insert")
st.checkbox("select")
st.checkbox("where")
st.checkbox("order by")
st.checkbox("update")
st.checkbox("delete")
st.checkbox("count")
st.checkbox("sum")
st.checkbox("AVG")
st.checkbox("join")

st.header("Manual testing ")

st.checkbox("Test case")
st.checkbox("bug reporting ")
st.checkbox("severity vs priority")
st.checkbox("bug life cycle")
st.checkbox("jira basics")

st.header("automation Testing")

st.checkbox("selenium")
st.checkbox("playwright")
st.checkbox("locators ")
st.checkbox("automation project")

st.header("API testing and other tools ")

st.checkbox("GitHub basics")
st.checkbox("Streamlit basics")
st.checkbox("API testing basics")
st.checkbox("Postman")
st.checkbox("test scenarios")
st.checkbox("reproduction steps")


st.success("keep learning daily")




