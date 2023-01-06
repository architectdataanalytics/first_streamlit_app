import streamlit
import pandas
#🥣 🥗 🐔 🥑🍞
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avacado Toast')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#Picklist to pick a fruit.
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado,Strawberries'])
streamlit.dataframe(my_fruit_list)
