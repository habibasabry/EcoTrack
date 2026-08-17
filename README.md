# 🌱 EcoTrack — Household & Community Recycling Tracker

A simple console-based application for tracking waste, measuring recycling performance, and promoting sustainable waste management.

---

## 📌 Project Overview

**EcoTrack** is a Python-based console application designed to help households and small community groups monitor their waste and recycling activities.

Many households do not have a simple way to track how much waste they recycle compared to the amount sent to landfill. EcoTrack addresses this problem by allowing users to record waste by category, calculate their recycling rate, estimate environmental impact, review waste history, and receive recommendations for improving their recycling habits.

The project supports **United Nations Sustainable Development Goal 11 (SDG 11) — Sustainable Cities and Communities** by encouraging responsible waste management and more sustainable community practices.

---

## 🎯 Objectives

The main objective of EcoTrack is to develop an easy-to-use recycling tracker that helps users understand and improve their waste management behaviour.

### Specific Objectives
* 🗑️ **Record** waste items by category and weight.
* ♻️ **Calculate** the overall recycling rate.
* 🌍 **Estimate** environmental impact and CO₂ savings.
* 📋 **Maintain and review** waste history.
* 💡 **Provide** rule-based recycling recommendations.
* ✅ **Validate** user input and handle errors gracefully.
* 💾 **Persist** waste data between application sessions.

---

## ✨ Key Features

### 1. 🗑️ Waste Logging
Users can record waste according to different categories:
* Plastic
* Paper
* Glass
* Metal
* Organic
* General / Landfill

Each entry includes relevant information such as the waste category and weight.

### 2. ♻️ Recycling Rate Calculation
EcoTrack calculates the percentage of waste that is recycled.

$$\text{Recycling Rate (\%)} = \left(\frac{\text{Recycled Waste Weight}}{\text{Total Waste Weight}}\right) \times 100$$

This allows users to monitor their recycling performance over their tracked period.

### 3. 🌍 Environmental Impact Calculation
The system estimates environmental benefits from recycling based on the material type and weight recorded. The estimated CO₂ savings help users understand that recycling does not only reduce waste but can also contribute to reducing environmental impact.

### 4. 📊 Waste History
EcoTrack maintains previously recorded waste entries so users can:
* View their waste records.
* Search their history.
* Monitor recycling behaviour over time.
* Identify patterns in their waste generation.

### 5. 💡 Recycling Recommendations
The system provides simple rule-based recommendations based on the user's waste data.  
*For example:*
> *"Your recycling rate is low. Try separating recyclable materials from general waste to increase your recycling rate."*

These recommendations are designed to encourage better recycling habits.

### 6. ✅ Input Validation
EcoTrack validates user input to prevent incorrect data from affecting the system. Examples include:
* Negative waste weights
* Unknown waste categories
* Invalid menu choices
* Empty waste records
* Invalid numerical input

The system provides appropriate error messages and allows users to try again.

### 7. 💾 Data Persistence
Waste records are stored so that information is not lost when the application is closed. This allows EcoTrack to track recycling behaviour across multiple sessions rather than only during a single program run.

---

## 🖥️ System Menu

The application provides a simple console-based menu:

```text
======================================
     ECOTRACK — RECYCLING TRACKER
======================================

1. Log a Waste Entry
2. View Recycling Summary & Rate
3. View Environmental Impact Report
4. View / Search Entry History
5. Get Recommendations
6. Exit

======================================
Enter your choice (1-6):
```

---

## ⚙️ Technologies Used

🐍 **Python** - 	Main programming language
📦 **JSON / File Storage** - Data persistence
🧪 **Python Testing** - Testing system functions
🔧 **Git & GitHub** - Version control and collaboration

---

## 👥 Team Contributions

* ABDALLA HABIBA MOHAMED SABRY MOHAMED - 202409010516
* MOHAMMED MOHAMMEDELNOUR ELSAFI AYAT - 202409010471
* GOFRAN OSAMA FATHI ABDALLA - 202405010044
* YUVANESWARY A/P INDRAN - 202306010059 
* MUAWIA ELBASIR ELNOUR MAAB - 202501010210

---

## 🔮 Future Improvements

📱 Mobile application support.
📊 Graphs and visual dashboards.
☁️ Cloud-based data storage.
👥 Multiple household/community accounts.
🏆 Recycling goals and achievements.
📍 Community recycling centre information.

---

## 📄 License

This project was developed for academic and educational purposes.

---

<p align="center">

🌱 EcoTrack — Track Waste. Recycle More. Build Sustainable Communities. ♻️

</p>

