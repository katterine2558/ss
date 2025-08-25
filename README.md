# 📊 Clockify Hours Proration Web App

This is a web application deployed on Azure, designed to generate the **proration of hours logged** by team members in [Clockify](https://clockify.me/).

With a simple interface, the user enters a **start date** and an **end date**, and the app generates an **automatic report** that downloads directly in the browser.

> ⚠️ **Important note:** The app only works within the office’s local network.

---

## 🚀 How to Use

1. Connect to the office’s internal network.
2. Access the web app from your browser.
3. Enter the **start date** and **end date**.
4. Click **Generate Report**.
5. The file will download automatically.

---

## 🛠️ Technologies Used

- 🌐 Azure Web App
- 🧠 Backend: Flask
- 🎨 Frontend: HTML/CSS/JS
- 🔄 Integration with the Clockify API

---

## 🧭 Accessibility & Restrictions

- ✅ Available **only** from the office’s internal network.
- ❌ Not accessible from the internet or external networks.

---

## 🔄 Integrated CI/CD

This project includes a **Continuous Integration (CI)** and **Continuous Deployment (CD)** pipeline using **GitHub Actions**. Every change to the `main` branch automatically triggers:

1. Source code validation and tests.
2. Build of the package/web app.
3. Automatic deployment to the production environment on **Azure Web App**.

> ✅ This ensures the application is always up to date with the latest working version.
