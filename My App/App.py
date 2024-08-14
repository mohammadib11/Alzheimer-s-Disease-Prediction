from controller.LoadModel import LoadModel
from controller.GetPrediction import GetPrediction
import streamlit as st 

Gender = st.number_input('Gender (0 : M,1 : F)' , min_value=0, max_value=1, step=1)
Ethnicity = st.number_input('Ethnicity (0: Caucasian, 1: African American, 2: Asian, 3: Other)' , min_value=0, max_value=3, step=1)
EducationLevel = st.number_input('Education Level (0: None, 1: High School, 2: Bachelor, 3: Higher)' , min_value=0, max_value=3, step=1)
BMI = st.number_input('BMI (15,40)' , min_value=15.0000, max_value=40.0000, step=0.0001)
AlcoholConsumption = st.number_input('Alcohol Consumption (0,20)' , min_value=0.0000, max_value=20.0000, step=0.0001)
DietQuality = st.number_input('Diet Quality (0,10)' , min_value=0.0000, max_value=10.0000, step=0.0001)
SleepQuality = st.number_input('Sleep Quality (4,10)' , min_value=4.0000, max_value=10.0000, step=0.0001)
FamilyHistoryAlzheimers = st.number_input('Family History Alzheimers (0: No, 1: Yes)' , min_value=0, max_value=1, step=1)
CardiovascularDisease = st.number_input('Cardio vascular Disease (0: No, 1: Yes)' , min_value=0, max_value=1, step=1)
Diabetes = st.number_input('Diabetes (0: No, 1: Yes)' , min_value=0, max_value=1, step=1)
HeadInjury = st.number_input('Head Injury (0: No, 1: Yes)' , min_value=0, max_value=1, step=1)
Hypertension = st.number_input('Hypertension (0: No, 1: Yes)' , min_value=0, max_value=1, step=1)
SystolicBP = st.number_input('Systolic BP (90,179)' , min_value=90.0000, max_value=179.0000, step=0.0001)
CholesterolLDL = st.number_input('Cholesterol LDL (50,200)' , min_value=50.0000, max_value=200.0000, step=0.0001)
CholesterolHDL = st.number_input('Cholesterol HDL (20,100)' , min_value=20.0000, max_value=100.0000, step=0.0001)
CholesterolTriglycerides = st.number_input('Cholesterol Triglycerides (50,400)' , min_value=50.0000, max_value=400.0000, step=0.0001)
MMSE = st.number_input('MMSE (0,30)' , min_value=0.0000, max_value=30.0000, step=0.0001)
FunctionalAssessment = st.number_input('Functional Assessment (0,10)' , min_value=0.0000, max_value=10.0000, step=0.0001)
MemoryComplaints = st.number_input('Memory Complaints (0: No, 1: Yes)' , min_value=0, max_value=1, step=1)
BehavioralProblems = st.number_input('Behavioral Problems (0: No, 1: Yes)' , min_value=0, max_value=1, step=1)
ADL = st.number_input('ADL (0,10)' , min_value=0.0000, max_value=10.0000, step=0.0001)
Confusion = st.number_input('Confusion (0: No, 1: Yes)' , min_value=0, max_value=1, step=1)
Disorientation = st.number_input('Disorientation (0: No, 1: Yes)' , min_value=0, max_value=1, step=1)
PersonalityChanges = st.number_input('Personality Changes (0: No, 1: Yes)' , min_value=0, max_value=1, step=1)
DifficultyCompletingTasks = st.number_input('Difficulty Completing Tasks (0: No, 1: Yes)' , min_value=0, max_value=1, step=1)

information = [
    Gender,
    Ethnicity,
    EducationLevel,
    BMI,
    AlcoholConsumption,
    DietQuality,
    SleepQuality,
    FamilyHistoryAlzheimers,
    CardiovascularDisease,
    Diabetes,
    HeadInjury,
    Hypertension,
    SystolicBP,
    CholesterolLDL,
    CholesterolHDL,
    CholesterolTriglycerides,
    MMSE,
    FunctionalAssessment,
    MemoryComplaints,
    BehavioralProblems,
    ADL,
    Confusion,
    Disorientation,
    PersonalityChanges,
    DifficultyCompletingTasks
]

model = LoadModel('model/Alzheimer\'s_Disease_Prediction.pkl')

if st.button('Start prediction') :
    prediction = GetPrediction(model, information)
    if prediction == 0 :
        st.write('This patient does not suffer from Alzheimer\'s')
    else:
        st.write('This patient suffers from Alzheimer\'s')