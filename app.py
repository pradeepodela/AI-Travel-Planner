import os
import google.generativeai as genai
import streamlit as st
from datetime import date



st.title("Pradeep's AI Travel Planner")
st.subheader('Plan your next trip with AI')


# User input section in the sidebar
st.sidebar.header('Enter details to generate a travel plan:')
api_key = st.sidebar.text_input('Enter Your Google API Key ', type="password")
destination = st.sidebar.text_input('Destination', 'Bangalore')
date_input = st.sidebar.date_input('Travel Start Date', min_value=date.today())
date = date_input.strftime('%Y-%m-%d')
budget = st.sidebar.number_input('Budget', min_value=100, value=5000, step=100)
traviltype = st.sidebar.selectbox('Travel Type', ['train', 'road', 'air'])
# duration = st.sidebar.slider('Duration (days)', 1, 3, 3)
duration = st.sidebar.number_input('Duration (days)', min_value=1, value=3, step=1)

# Additional user preferences
st.sidebar.subheader('Your Preferences:')
# interests = st.sidebar.checklist('Interests', ['historical sites','nature','temples','food','shopeing'])
interests = st.sidebar.text_input('Interests', "historical sites,nature,temples,food,shopping")
specific_interests = st.sidebar.text_input('Specific Interests', 'art museums, hiking trails')
accommodation_preference = st.sidebar.selectbox('Accommodation Preference', ['Hotel', 'Hostel', 'No Preference'])
travel_style = st.sidebar.selectbox('Travel Style', ['Relaxed', 'Fast-Paced', 'Adventurous', 'Cultural', 'Family-Friendly'])

# Function to create a detailed message for the AI
def get_personalized_travel_plan(user_preferences, trip_details, api_key):
    genai.configure(api_key=api_key)
    message = (
        f"Create a detailed travel itinerary  focused on attractions, restaurants, and activities for a trip "
        f" to {trip_details['destination']}, starting on {trip_details['date']}, lasting for "
        f"{trip_details['duration']} days, within a budget of {trip_details['budget']}. This should include daily timings, "
        f"preferences for {user_preferences['accommodation_preference']} accommodations, a {user_preferences['travel_style']} travel style, "
        f"and interests in {user_preferences['interests']}.  dietary restrictions include "
        
        f"Must-visit landmarks include . Also, provide a travel checklist relevant to the destination and duration. rech the destination by {traviltype}"
    )
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(message)
    return response.text

# Collecting user preferences and trip details for travel planning
user_preferences = {
    'interests': interests,
    'specific_interests': specific_interests,
    'accommodation_preference': accommodation_preference,
    'travel_style': travel_style
}

trip_details = {
    'destination': destination,
    'date': date,
    'budget': budget,
    'duration': duration
}

# Generate a personalized travel plan
if st.sidebar.button('Generate Travel Plan'):
    with st.spinner('Generating your personalized travel plan...'):
        response = get_personalized_travel_plan(user_preferences, trip_details, api_key)
        st.success(response)
        st.balloons()
