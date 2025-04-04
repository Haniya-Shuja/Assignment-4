import streamlit as st

# Set page configuration
st.set_page_config(page_title='BMI CALCULATOR', page_icon='🏋️‍♂️', layout='centered')

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        font-weight: bold;
    }
    .stInput>div>input {
        font-size: 18px;
    }
    .stTextInput>div>input {
        font-size: 18px;
    }
    .stSubheader {
        font-size: 20px;
        color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.title("Project : 08 BMI Calculator IN Python")
st.markdown("Calculate your body mass index (BMI)")

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input('Weight (kg): ', min_value=1.0, format='%.2f')
    
with col2:
    height = st.number_input('Height (m): ', min_value=1.0, format='%.2f')

# Calculate BMI
if height > 0 and weight > 0:
    bmi = weight / (height ** 2)

    st.subheader('Your BMI: ')

    # Display BMI result
    st.markdown(f'{bmi:.2f}', unsafe_allow_html=True)

    # Categorize BMI with emojis
    if bmi < 18.5:
        st.error('🟠 Underweight')
    elif 18.5 <= bmi < 24.99:
        st.success('🟢 Normal weight')
    elif 25 <= bmi < 29.9:
        st.warning('🟡 Overweight')
    else:
        st.error('🔴 Obesity')
else:
    st.info('⚠️ Please enter a valid weight and height.')


