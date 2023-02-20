import pandas as pd
import streamlit as st
import pickle


#Declaring Teams

teams = ['Sunrisers Hyderabad', 'Mumbai Indians','Royal Challengers Bangalore',
       'Kolkata Knight Riders','Kings XI Punjab','Chennai Super Kings', 'Rajasthan Royals','Delhi Capitals']

#Declaring City

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))

st.title('IPL Kaun Banega Baazigar')

col1, col2 = st.columns(2)

with col1:
       battingteam=st.selectbox("Select the Batting Team", sorted(teams))

with col2:
       bowlingteam=st.selectbox("Select the Bowling Team", sorted(teams))

city = st.selectbox("Select the Bowling Team", sorted(cities))

target = st.number_input('Target')

col3, col4, col5 = st.columns(3)

with col3:
       score = st.number_input('Score')

with col4:
       overs = st.number_input('Overs Completed')

with col5:
       wickets = st.number_input('Wickets Fallen')

if st.button('Predict Probability'):
       runs_left = target - score
       balls_left = 120 - (overs*6)
       wickets = 10 - wickets
       currentrunrate = score / overs
       requiredrunrate = (runs_left*6) / balls_left

       data = {
              'batting_team' : [battingteam],
              'bowling_team' : [bowlingteam],
              'city' : [city],
              'total_runs_x' : [target],
              'curr_run_rate' : [currentrunrate],
              'req_run_rate' : [requiredrunrate],
              'wickets' : [wickets],
              'balls_left' : [balls_left]
       }

       df = pd.DataFrame(data)
       # print(df)

       result = pipe.predict_proba(df)

       losspro = result[0][0]
       winpro = result[0][1]

       st.header(battingteam + ':-' + str(round((winpro*100),2)) + '%')
       st.header(bowlingteam + ':-' + str(round((losspro*100),2)) + '%')