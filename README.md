# Healthcare Chatbot 🩺

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

A simple healthcare chatbot built using Python and first-order logic (FOL) to diagnose diseases based on user-reported symptoms. The chatbot matches symptoms to a predefined knowledge base and provides actionable advice for potential diseases.

## ✨ Features

- **Diagnosis:** Identifies diseases like flu, common cold, malaria, COVID-19, and strep throat based on symptoms.
- **Tailored Advice:** Provides specific recommendations for each diagnosed disease.
- **User-Friendly Interface:** Simple command-line interface for easy interaction.

## 📋 Prerequisites

- **Python 3.x** installed on your system.
- No additional libraries required—uses only built-in Python modules.

## 🚀 Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Lehlohonolo-Saohatse/healthcare-chatbot.git
   ```

2. Navigate to the project directory:
   ```bash
   cd healthcare-chatbot
   ```

## 🛠️ Usage

1. Run the chatbot script:
   ```bash
   python healthcare_chatbot.py
   ```

2. Follow the prompts to enter your symptoms (comma-separated, e.g., `fever, cough, sore throat`).
3. The chatbot will analyze your symptoms and provide a possible diagnosis along with advice.

### Example
```plaintext
Welcome to HealthBot!
Enter your symptoms (comma-separated):
Symptoms: fever, cough, sore throat

Based on your symptoms, you might have:
- Flu
  Advice: Drink fluids, rest, and consult a doctor if symptoms worsen.
```

## 📂 Project Structure

- `healthcare_chatbot.py`: The main script containing the chatbot logic.
- `README.md`: Project documentation.
- `.gitignore`: File to ignore unnecessary files during version control.
- `LICENSE`: MIT License for the project.

## 🧠 Knowledge Base

The chatbot uses a predefined knowledge base with the following diseases and symptoms:

| Disease        | Symptoms                              |
|----------------|---------------------------------------|
| **Flu**        | Fever, cough, sore throat            |
| **Common Cold**| Sneezing, runny nose, mild fever     |
| **Malaria**    | Fever, chills, sweating, headache    |
| **COVID-19**   | Fever, cough, shortness of breath, loss of taste |
| **Strep Throat**| Sore throat, swollen lymph nodes, fever |

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request with a detailed description of your changes.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🔮 Future Enhancements

- Add symptom severity assessment for more nuanced diagnoses.
- Implement multilingual support for broader accessibility.
- Integrate with wearable devices for real-time health data.
- Add a probabilistic scoring system for partial symptom matches.

## 📬 Contact

For questions or suggestions, contact the author [Lehlohonolo Saohatse](https://github.com/Lehlohonolo-Saohatse) or open an issue on this repository.