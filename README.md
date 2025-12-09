NEWS Paper customer churn prediction 

This project predicts whether a newspaper subscriber is likely to churn using a Machine Learning model. The prediction system is integrated into a Django web application, where an admin user can log in and test customer data through a secured form.

<img width="1871" height="846" alt="image" src="https://github.com/user-attachments/assets/c366d43d-10b1-4d51-b94c-713daa53b4e3" />

<img width="761" height="758" alt="image" src="https://github.com/user-attachments/assets/8ba5b2a3-696a-4932-9ddc-fadba08dae10" />


🚀 How to Run This Project on Your Laptop

Follow these steps to run the Django + ML project locally ⬇️
1️⃣ Clone the Repository:
     * create a folder on the desktop 
     * clone : git clone https://github.com/jyothi4218/News-Paper-Customer-Churn-Prediction.git
2️⃣ Create a Virtual Environment:
     * In the created folder itself create a virtual environment 
     *python -m venv venv   (for windows)
3️⃣ Activate the Virtual Environment:
     *  go to this path venv\Scripts
     * type activate
4️⃣ Install Required Libraries:
     * pip install -r requirements.txt 
5️⃣ Run Migrations:
     python manage.py makemigrations
     python manage.py migrate
6️⃣ Create Superuser (IMPORTANT ‼️)
      This is required to access the Customer Churn Prediction form.
      *python manage.py createsuperuser
7️⃣ Start the Server:
      * python manage.py runserver 
      * Login with your superuser username and password to view the prediction form.
