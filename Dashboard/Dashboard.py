import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style="dark")

def create_season_df(df):
    season_df = df.groupby(by="season").agg({
    "cnt": "sum"
    })
    season_df.rename(columns={
        "cnt": "bike_rentals"
    },inplace=True)
    season_df["season_name"] = ["spring", "summer", "fall", "winter"]
    return season_df

def create_month_2012_df(df):
    on_2012_df = df[df.yr == 1]
    month_2012_df = on_2012_df.groupby(by="mnth").agg({
        "cnt": "sum"
    })
    month_2012_df.rename(columns={
        "cnt": "bike_rentals"
    }, inplace=True)
    month_2012_df["month_name"] = ["January","February","March","April","May","June","July","August","September","October", "November","December"]
    return month_2012_df

day_df = pd.read_csv("Dashboard/day.csv")
season_df = create_season_df(day_df)
month_2012_df =  create_month_2012_df (day_df)

st.header("Dashboard - Bike Rentals")
st.subheader("Numbers of Bike Rentals Based on Season")

col1, col2, col3, col4 = st.columns(4)
with col1:
    spring_df = season_df[season_df["season_name"]=="spring"]["bike_rentals"]
    st.metric("Spring:", value= round(spring_df))
with col2:
    summer_df = season_df[season_df["season_name"]=="summer"]["bike_rentals"]
    st.metric("Summer:", value= round(summer_df))
with col3:
    fall_df = season_df[season_df["season_name"]=="fall"]["bike_rentals"]
    st.metric("Fall:", value= round(fall_df))
with col4:
    winter_df = season_df[season_df["season_name"]=="winter"]["bike_rentals"]
    st.metric("Winter:", value= round(winter_df))

fig, ax = plt.subplots(figsize = (20,10))
colors = ["green", "yellow", "red", "skyblue"]
sns.barplot( 
    x="season_name", 
    y="bike_rentals",
    data= season_df, 
    palette= colors,
    ax=ax
)
ax.set_title("Bike Rentals By Season", fontsize = 35)
ax.set_xlabel(None)
ax.set_ylabel("Bike Rentals (Million)", fontsize = 25)
ax.tick_params(axis="x", labelsize = 30)
ax.tick_params(axis="y", labelsize = 20)
st.pyplot(fig)

st.subheader("Number of Bike Rentals in 2012")
col1, col2 = st.columns(2)
with col1:
    most_df = month_2012_df[month_2012_df["bike_rentals"]==month_2012_df["bike_rentals"].max()]
    st.metric("Most:", value= round(most_df["bike_rentals"]))
with col2:
    less_df = month_2012_df[month_2012_df["bike_rentals"]==month_2012_df["bike_rentals"].min()]
    st.metric("Fewest:", value= round(less_df["bike_rentals"]))
    
fig, ax = plt.subplots(figsize = (25,10))
sns.lineplot(
    data=month_2012_df, 
    x="month_name",
    y="bike_rentals",
    linewidth = 2,
    marker= "o",
    ax=ax
    
)
ax.set_xlabel(None)
ax.set_ylabel(None)
ax.set_title("Bike Rentals Performance in 2012", fontsize = 35)
ax.tick_params(axis="x", labelsize = 20)
ax.tick_params(axis="y", labelsize = 20)
st.pyplot(fig)
