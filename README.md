# 🚀 Intervue.ai
  <br />


  **The world's most advanced AI interviewer. Real-time voice feedback, code analysis, and behavioral coaching.**

  <br />
  <br />
 
  [![Vercel Deploy](https://deploy.workers.cloudflare.com/button)](https://intervueainewtest.vercel.app)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  
  [**🔴 Live Demo**](https://intervueainewtest.vercel.app) | [**🐛 Report Bug**](https://github.com/Swarup6002/Intervue.ai.newtest/issues) |
  <br />

<div align="center">

**Home Page**
<img width="1915" height="875" alt="Screenshot 2026-01-13 031311" src="https://github.com/user-attachments/assets/8468fd69-5559-4a89-b75a-380c449bf835" />
<br />
**Test Window**
<img width="1919" height="879" alt="Screenshot 2026-01-13 031429" src="https://github.com/user-attachments/assets/b10c6b25-0034-49b5-86a9-d133602b16f7" />
<br />
**Mission**
<img width="1919" height="898" alt="Screenshot 2026-01-13 031518" src="https://github.com/user-attachments/assets/936743fc-b879-4716-84be-3699c1f48b66" />



  <br />
  <br />


</div>

---

## 📖 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [How It Works](#-how-it-works)
- [Getting Started](#-getting-started)
- [The Team](#-the-team)
- [Contact](#-contact)

---

## 🤖 About the Project

**Intervue.ai** is a cutting-edge platform designed to help developers crack technical interviews at top-tier tech companies. Unlike static flashcards or standard coding platforms, Intervue.ai leverages the power of **Google Gemini 2.0** to conduct realistic, context-aware mock interviews.

Whether you are preparing for a System Design round, a LeetCode-style algorithm challenge, or a behavioral interview, our AI adapts to your skill level, analyzes your voice tone, and checks your code complexity in real-time.

---

## ✨ Key Features

* **🧠 Context-Aware Dialogue:** The AI remembers your previous answers and digs deeper, just like a real human interviewer.
* **🗣️ Voice & Tone Analysis:** Analyzes your speech pace, confidence markers, and filler words using Web Speech API.
* **💻 Live Code Execution:** Integrated IDE to write, run, and debug code. The AI reviews syntax and time complexity (Big O) instantly.
* **📊 Deep Analytics:** Track your performance over time with detailed session reports and scoring.
* **🎨 Glassmorphism UI:** A stunning, modern interface built with Tailwind CSS and Framer Motion.
* **🔐 Secure Authentication:** Seamless sign-up and login using Supabase Auth.

---

## 🛠 Tech Stack

This project is built using the latest web technologies to ensure speed, scalability, and a premium user experience.

| Component | Technology | Badge |
| :--- | :--- | :--- |
| **Frontend** | React (Vite) | ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) |
| **Language** | TypeScript | ![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white) |
| **Styling** | Tailwind CSS | ![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white) |
| **Animations** | Framer Motion | ![Framer](https://img.shields.io/badge/Framer-black?style=for-the-badge&logo=framer&logoColor=blue) |
| **Database & Auth** | Supabase | ![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white) |
| **AI Model** | Google Gemini | ![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white) |
| **Deployment** | Vercel | ![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white) |

---

## ⚙️ How It Works

1.  **Sign Up:** Create an account to save your progress.
2.  **Choose a Mode:** Select from Data Structures, System Design, or Behavioral interview tracks.
3.  **The Interview:**
    * The AI asks a question via text and voice.
    * You respond by speaking (Voice Mode) or typing.
    * For coding questions, use the built-in code editor.
4.  **Real-time Feedback:** The AI analyzes your answer immediately and provides constructive criticism.
5.  **Review:** After the session, view your detailed scorecard and areas for improvement.

---

## 🚀 Getting Started

To run this project locally, follow these steps:

### Prerequisites
* Node.js (v18 or higher)
* npm or yarn

### Installation

1.  **Clone the repo**
    ```bash
    git clone [https://github.com/Swarup6002/Intervue.ai.newtest.git](https://github.com/Swarup6002/Intervue.ai.newtest.git)
    cd Intervue.ai.newtest
    ```

2.  **Install dependencies**
    ```bash
    npm install
    ```

3.  **Set up Environment Variables**
    Create a `.env` file in the root directory and add your keys:
    ```env
    VITE_SUPABASE_URL=your_supabase_url
    VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
    VITE_GEMINI_API_KEY=your_google_gemini_key
    ```

4.  **Run the development server**
    ```bash
    npm run dev
    ```

---

## 👥 The Team

<table align="center">
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/swarup-purkayastha/">
        <img src="https://zyqjwjpncnsizjfxytyy.supabase.co/storage/v1/object/sign/Developers/WhatsApp%20Image%202026-01-01%20at%2013.20.47.jpeg?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV9kNjA0MTcwMC0wMGEyLTQ0NDAtODdjYy1mYjljNGYyODcxYzAiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJEZXZlbG9wZXJzL1doYXRzQXBwIEltYWdlIDIwMjYtMDEtMDEgYXQgMTMuMjAuNDcuanBlZyIsImlhdCI6MTc2NzI1Mzg5MSwiZXhwIjoyMDgyNjEzODkxfQ.pEfU2h78nO4fO0ZUOthQ-T747ewDJZOj7ffpfqWQLnA" width="100px;" alt="" style="border-radius:50%"/>
        <br />
        <sub><b>Swarup Purkayastha</b></sub>
      </a>
      <br />
      <sub>Full Stack & AI Engineer</sub>
    </td>
    <td align="center">
      <a href="https://www.linkedin.com/in/priyanshu-kumar-gupta-a4b9a4250/">
        <img src="https://zyqjwjpncnsizjfxytyy.supabase.co/storage/v1/object/sign/Developers/WhatsApp%20Image%202026-01-01%20at%2013.01.48.jpeg?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV9kNjA0MTcwMC0wMGEyLTQ0NDAtODdjYy1mYjljNGYyODcxYzAiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJEZXZlbG9wZXJzL1doYXRzQXBwIEltYWdlIDIwMjYtMDEtMDEgYXQgMTMuMDEuNDguanBlZyIsImlhdCI6MTc2NzI1Mjc2NSwiZXhwIjoyMDgyNjEyNzY1fQ.V3Iz7NPUBI4qE2I2gDtI1yze1cGccHrx1zEEHYY5PH4" width="100px;" alt="" style="border-radius:50%"/>
        <br />
        <sub><b>Priyanshu Kumar Gupta</b></sub>
      </a>
      <br />
      <sub>Full Stack & AI Engineer</sub>
    </td>
  </tr>
</table>

---

## 📧 Contact

If you have any questions or suggestions, feel free to reach out to us at:  
**Email:** [intervuedotai@gmail.com](mailto:intervuedotai@gmail.com)

<div align="center">
  <sub>Built with ❤️ by the Intervue.ai Team</sub>
</div>







