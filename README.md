
# 📄 Assignment 3 – Flask + API + MongoDB Integration

This project demonstrates two tasks using Flask:

---

## ✅ Features Implemented

### 1. Flask API with JSON Backend
- A route `/api` reads data from a backend file `assign3.json` and returns it as a JSON response.
- The data includes a list of user details (id, name, age).
- Example route: `http://localhost:5000/api`

📂 Backend file used: `assign3.json`

---

### 2. Frontend Form with MongoDB Integration
- A modern HTML/CSS sign-up form that:
  - Takes name, email, and password.
  - On submission, stores the data in MongoDB Atlas.
  - Redirects to a success page if inserted successfully.
  - Displays error on the same page if submission fails.

🌐 Frontend files:
- `assign3index.html` — main form page
- `success.html` — animated success message page

💾 Backend:
- MongoDB Atlas using environment variables (`.env` with `MONGO_URI`)

🎨 Styling:
- Clean, animated transitions between pages.
- Background image included: `signup.jpg`

🧠 **Note**: For the advanced HTML/CSS animations and visual design, I took help from **ChatGPT**.

---

## 🛠 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the API app
python assignment3-q1.py

# Run the MongoDB form app
python assignment3-q2.py


assignment-flask/
├── assignment3-q1.py          # API route returning JSON from file
├── assignment3-q2.py          # Form submission Flask app with MongoDB
├── assign3.json               # Backend JSON data
├── requirements.txt           # Python dependencies
├── .env                       # MongoDB URI (not pushed to GitHub)
├── templates/
│   ├── assign3index.html      # Frontend form page
│   └── success.html           # Success message page
├── static/
│   └── signup.jpg             # Background image
