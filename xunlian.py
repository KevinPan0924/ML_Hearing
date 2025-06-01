import streamlit as st
import h2o
import pandas as pd

# 1. Start H2O and load model
h2o.init()
model = h2o.load_model("XRT_1_AutoML_1_20250527_112911")  # Modify to your actual model path

st.title("Online Hearing Risk Prediction")

st.markdown("Please fill in the following information according to your situation, and click the button below to get your hearing risk prediction.")

Sex = st.selectbox("Sex", ["Female", "Male"])
Age = st.selectbox("Age", ["45-55", ">=65", "55-65"])
Regional = st.selectbox("Region", ["West", "East", "Central"])
Education_level = st.selectbox("Education Level", [
    "Less than elementary school", "Elementary school", "Middle school", "High school or above"
])
Standard_of_living = st.selectbox("Standard of Living", [
    "Average", "Relatively poor", "Poor", "Very high", "Relatively high"
])
Sleeping_time = st.selectbox("Sleeping Time", ["≤6 h", "6–8 h", ">8 h"])
Smoking_Status = st.selectbox("Smoking Status", ["No", "Yes"])
Drinking_Status = st.selectbox("Drinking Status", ["No", "Yes"])
Depression_category = st.selectbox("Depression", ["No", "Yes"])
Hypertension = st.selectbox("Hypertension", ["No", "Yes"])
Dyslipidaemia = st.selectbox("Dyslipidaemia", ["Yes", "No"])
Diabetes = st.selectbox("Diabetes", ["Yes"])
Liver_disease = st.selectbox("Liver Disease", ["No", "Yes"])
Heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
Stroke = st.selectbox("Stroke", ["No", "Yes"])
Kidney_disease = st.selectbox("Kidney Disease", ["No", "Yes"])
Stomach_or_other_digestive_disease = st.selectbox("Stomach or Other Digestive Disease", ["No", "Yes"])
Memory_related_disease = st.selectbox("Memory Related Disease", ["No", "Yes"])
Arthritis_or_rheumatism = st.selectbox("Arthritis or Rheumatism", ["No", "Yes"])
Lung_related_disease = st.selectbox("Lung Related Disease", ["No", "Yes"])
psyche_related_disease = st.selectbox("Mental/Psychological Related Disease", ["No", "Yes"])
vigorous_physical_activity = st.selectbox("Vigorous Physical Activity", ["No", "Yes"])
moderate_physical_activity = st.selectbox("Moderate Physical Activity", ["Yes", "No"])
light_physical_activity = st.selectbox("Light Physical Activity", ["Yes", "No"])
Menopause = st.selectbox("Menopause", ["Yes", "Not applicable"])
Prostatic_diseases = st.selectbox("Prostatic Diseases", ["Not applicable", "Yes"])
Pain = st.selectbox("Pain", ["No", "Yes"])
Weight_change = st.selectbox("Weight Change", [
    "Don't Know", "No", "Yes, only lost weight", "Yes, only gained weight",
    "Yes, first lost and then gained weight", "Yes, first gained and then lost weight"
])
Health_status_during_childhood = st.selectbox("Health Status During Childhood", [
    "Good", "Fair", "Poor", "Excellent"
])
self_expectations_of_health_status = st.selectbox("Self Expectations of Health Status", [
    "Almost impossible", "Maybe", "Almost certain", "Very likely", "Not very likely"
])
BMI_category = st.selectbox("BMI Category", [
    "Normal weight", "Obese", "Overweight", "Underweight"
])
Hand_grip_strength = st.selectbox("Hand Grip Strength", [
    "2.left hand", "1.right hand", "3.both hands equally dominant"
])
House_structure = st.selectbox("House Structure", [
    "Traditional", "Other", "Temporary"
])
Heating_energy = st.selectbox("Heating Energy", [
    "Coal", "Electric", "Other", "Solar"
])
Cooking_energy = st.selectbox("Cooking Energy", [
    "Clean fuel", "Non-clean fuel", "Other/Not cooking"
])
Room_temperature = st.selectbox("Room Temperature", [
    "Bearable", "Cold", "Hot"
])
Vision = st.selectbox("Vision Problem", ["No", "Yes"])
Province = st.selectbox("Province", [
    'Yunnan', 'Fujian', 'Qinghai', 'Sichuan', 'Hebei', 'Jiangxi', 'Xinjiang',
    'Beijing', 'Inner Mongolia', 'Jiangsu', 'Chongqing', 'Gansu', 'Heilongjiang', 'Guangdong', 'Liaoning',
    'Shanxi', 'Shanghai', 'Tianjin', 'Zhejiang', 'Jilin', 'Guangxi', 'Anhui', 'Hubei', 'Shaanxi',
    'Shandong', 'Henan', 'Hunan', 'Guizhou'
])

# Continuous variables
BMI = st.number_input("BMI")
waist = st.number_input("Waist Circumference")
White_blood_cell = st.number_input("White Blood Cell Count")
Platelets = st.number_input("Platelet Count")
Glycated_hemoglobin = st.number_input("Glycated Hemoglobin")
Haemoglobin = st.number_input("Hemoglobin")
Glucose = st.number_input("Glucose")
Total_cholesterol = st.number_input("Total Cholesterol")
Triglycerides = st.number_input("Triglycerides")
High_density_lipoprotein_cholesterol = st.number_input("HDL Cholesterol")
Low_density_lipoprotein_cholesterol = st.number_input("LDL Cholesterol")
Hematocrit = st.number_input("Hematocrit")
Creatinine = st.number_input("Creatinine")
BUN = st.number_input("Blood Urea Nitrogen (BUN)")
Uric_Acid = st.number_input("Uric Acid")

# Assemble all inputs as a dictionary
input_dict = {
    "Sex": Sex, "Age": Age, "Regional": Regional, "Sleeping_time": Sleeping_time, 
    "Smoking_Status": Smoking_Status, "Drinking_Status": Drinking_Status, "Pain": Pain,
    "Weight_change": Weight_change, "Health_status_during_childhood": Health_status_during_childhood,
    "self_expectations_of_health_status": self_expectations_of_health_status, "Depression_category": Depression_category,
    "Hypertension": Hypertension, "Dyslipidaemia": Dyslipidaemia, "Diabetes": Diabetes,
    "Liver_disease": Liver_disease, "Heart_disease": Heart_disease, "Stroke": Stroke,
    "Kidney_disease": Kidney_disease, "Stomach_or_other_digestive_disease": Stomach_or_other_digestive_disease,
    "Memory_related_disease": Memory_related_disease, "Arthritis_or_rheumatism": Arthritis_or_rheumatism,
    "Menopause": Menopause, "Prostatic_diseases": Prostatic_diseases, "House_structure": House_structure,
    "Heating_energy": Heating_energy, "Cooking_energy": Cooking_energy, "Room_temperature": Room_temperature,
    "Education_level": Education_level, "Standard_of_living": Standard_of_living,
    "Hand_grip_strength": Hand_grip_strength, "waist": waist, "BMI": BMI,
    "White_blood_cell": White_blood_cell, "Platelets": Platelets,
    "Glycated_hemoglobin": Glycated_hemoglobin, "Glucose": Glucose,
    "Total_cholesterol": Total_cholesterol, "Triglycerides": Triglycerides,
    "High_density_lipoprotein_cholesterol": High_density_lipoprotein_cholesterol,
    "Low_density_lipoprotein_cholesterol": Low_density_lipoprotein_cholesterol,
    "Vision": Vision, "Hematocrit": Hematocrit, "Uric_Acid": Uric_Acid,
    "BUN": BUN, "Creatinine": Creatinine, "Lung_related_disease": Lung_related_disease,
    "psyche_related_disease": psyche_related_disease, 
    "vigorous_physical_activity": vigorous_physical_activity,
    "moderate_physical_activity": moderate_physical_activity,
    "light_physical_activity": light_physical_activity
}

if st.button("Predict Hearing Risk"):
    input_df = pd.DataFrame([input_dict])
    h2o_df = h2o.H2OFrame(input_df)
    pred = model.predict(h2o_df)
    pred_label = pred.as_data_frame().iloc[0,0]
    pred_prob = pred.as_data_frame().iloc[0,1] if pred.as_data_frame().shape[1] > 1 else None
    st.success(f"Prediction: {pred_label}, Probability: {pred_prob:.2%}" if pred_prob else f"Prediction: {pred_label}")
