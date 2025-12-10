📰 News Paper Customer Churn Prediction

This project predicts whether a newspaper subscriber is likely to churn using a Machine Learning model.
The system is built using Django, and access to the prediction form is secured — only admin users can log in and predict churn.

<img width="100%" alt="image" src="https://github.com/user-attachments/assets/c366d43d-10b1-4d51-b94c-713daa53b4e3" /> 

<img width="100%" alt="image" src="https://github.com/user-attachments/assets/8ba5b2a3-696a-4932-9ddc-fadba08dae10" />


🚀 How to Run This Project on Your Laptop

Follow these steps to run the Django + ML project locally ⬇️

1️⃣ Clone the Repository

Create a folder on your Desktop

Open terminal inside that folder and run:

git clone:  https://github.com/jyothi4218/News-Paper-Customer-Churn-Prediction.git
cd News-Paper-Customer-Churn-Prediction

2️⃣ Create a Virtual Environment (Windows)
python -m venv venv

3️⃣ Activate the Virtual Environment
venv\Scripts\activate

4️⃣ Install Required Libraries
pip install -r requirements.txt

5️⃣ Apply Migrations
python manage.py makemigrations
python.manage.py migrate

6️⃣ Create Superuser (Required to Access the Form)
python manage.py createsuperuser

This account will be used to log in.

7️⃣ Run the Server
  python manage.py runserver
