Minimalist Task Manager
A beautiful, beginner-friendly To-Do application built with Python and the Django Web Framework.

📖 Table of Contents
About the Project
How it Works (The Logic)
Features
Installation
Screenshots

☁️ About the Project

I created this project to practice my skills in Backend Development and UI/UX Design. It moves away from the standard, boring "system" look and adopts a clean, aesthetic "Soft Pink" interface.The goal was to create a space that feels calm and organized for managing daily habits and tasks.

🧠 How it Works (The Logic)
As a beginner, I focused on mastering the MVT (Model-View-Template) architecture
1. Model: Defines how the tasks are stored (Title, Description, Completion status).
2. View: Handles the "brain" of the app—checking if a user is logged in and filtering tasks so you only see your items.
3. Template: The "face" of the app—custom HTML and CSS with Glassmorphism effects.

✨ Features
User Accounts: Personalize your list by signing up.
Task Counter: A dynamic counter that tells you exactly how many items are left.
Live Search: Filter your tasks instantly by typing in the search bar.
CRUD Operations: * Create new tasks.
- Read/View task details.
- Update/Edit existing tasks.
- Delete tasks when finished.


🛠️ Installation for Beginners
If you want to run this project on your computer, follow these simple steps:
1. Clone the project:
git clone https://github.com/yourusername/your-repo-name.git
3. Set up a Virtual Environment:
Think of this as a "clean box" where you install tools just for this project.
python -m venv myenv
source myenv/bin/activate  # On Windows use: myenv\Scripts\activate
3.Install Django:
pip install django
4.Prepare the Database:
python manage.py migrate
5.Launch:
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/.

🎨 UI Design Choices
Colors: Soft Blush (#ffafcc) and Deep Lavender (#5e548e).
Typography: 'Poppins' Sans-Serif for a modern, high-end feel.
Cards: Used rounded corners ($30px$) to make the app feel "soft" and approachable.

Author
Kritika Maharjan

<img width="667" height="746" alt="todoe" src="https://github.com/user-attachments/assets/38e7d40f-150d-4d15-a1a9-561e9e9d2a7c" />
