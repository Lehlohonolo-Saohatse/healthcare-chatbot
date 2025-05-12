knowledge_base = {
    'flu': ['fever', 'cough', 'sore_throat'],
    'common_cold': ['sneezing', 'runny_nose', 'mild_fever'],
    'malaria': ['fever', 'chills', 'sweating', 'headache'],
    'covid19': ['fever', 'cough', 'shortness_of_breath', 'loss_of_taste'],
    'strep_throat': ['sore_throat', 'swollen_lymph_nodes', 'fever']
}

advice_base = {
    'flu': 'Drink fluids, rest, and consult a doctor if symptoms worsen.',
    'common_cold': 'Get plenty of rest, drink warm liquids, and use saline nasal drops.',
    'malaria': 'Seek immediate medical attention and take prescribed antimalarial medication.',
    'covid19': 'Isolate yourself, monitor symptoms, and follow local health guidelines.',
    'strep_throat': 'Take prescribed antibiotics, gargle with warm salt water, and rest.'
}

def get_user_symptoms():
    print("Welcome to HealthBot!")
    print("Enter your symptoms (comma-separated):")
    user_input = input("Symptoms: ").lower()
    symptoms = [symptom.strip().replace(' ', '_') for symptom in user_input.split(',')]
    return symptoms

def infer_disease(user_symptoms):
    possible_diseases = []
    for disease, required_symptoms in knowledge_base.items():
        if all(symptom in user_symptoms for symptom in required_symptoms):
            possible_diseases.append(disease)
    return possible_diseases

def run_chatbot():
    user_symptoms = get_user_symptoms()
    diseases = infer_disease(user_symptoms)
    if diseases:
        print("\nBased on your symptoms, you might have:")
        for disease in diseases:
            print(f"- {disease.title()}")
            print(f"  Advice: {advice_base.get(disease, 'Please consult a doctor.')}")
    else:
        print("\nNo matching disease found.")
        print("Please consult a healthcare professional.")

run_chatbot()