import random
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Student Data Generator', layout='wide')
st.title('Student CSV File Generator')

names = ['Araiz', 'Misham', 'Labika', 'Mair', 'Zarnish', 'Faiqa', 'Raiqa', 'Fatima', 'Ayesha', 'Zaeema', 'Usman',
         'Ahad', 'Sami', 'Abdullah']

students = []  # Initialize the students list

for i in range(1, 16):  # Ensure the colon is added at the end
    student = {
        'ID': i,
        'Names': random.choice(names),
        'Age': random.randint(18, 25),
        'Grade': random.choice(['A', 'B', 'C', 'D', 'F']),  # Correct the list for grades
        'Marks': random.randint(40, 100)
    }
    students.append(student)  # Append each student

df = pd.DataFrame(students)  # Create DataFrame

st.dataframe(df)  # Display the dataframe

# Generate CSV file
csv_file = df.to_csv(index=False).encode('utf-8')

# Download button to download CSV file
st.download_button('Download CSV File', csv_file, 'student.csv', 'text/csv')

st.success('Student records generated successfully!')