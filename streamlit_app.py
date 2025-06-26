# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col, when_matched

 
# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
  """Choose the fruits for your custom smoothie
  """
)

title = st.text_input("Name of smoothie:", "")
st.write("The name on your smoothie will be ", title)

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect("choose up to five ingredients:"
                                  ,my_dataframe
                                 , max_selections=5)

if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)

    ingredients_string=''
     
    for fruit_chosen in ingredients_list:
        ingredients_string +=fruit_chosen+' '
     
    st.write(ingredients_string)
    
    name_on_order=''
    for name_chosen in title:
        name_on_order =title
    st.write(name_on_order)
    
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','"""+name_on_order+"""')"""

    st.write(my_insert_stmt)
   
    
    time_to_insert=st.button("submit order")
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!'+" "+name_on_order, icon="✅")
    st.stop()

    #if ingredients_string:
        #session.sql(my_insert_stmt).collect()
      #  st.success('Your Smoothie is ordered!', icon="✅")







