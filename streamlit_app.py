import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header ('Breakfast Favorites') 
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header ('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇') 

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)

fruites_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

fruits_to_show = my_fruit_list.loc[fruits_selected]
