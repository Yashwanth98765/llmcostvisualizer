# 💸 LLM Token Cost Visualizer & Simulator

A interactive full-stack AI FinOps (Financial Operations) dashboard built with **Python**, **Streamlit**, and **Plotly**. This application serves as a strategic sandbox environment designed to forecast, simulate, and optimize API inference expenditures across major Large Language Model (LLM) providers before production deployment.

🚀 **Live Application Link:** [Insert your Streamlit live URL here]  
💻 **Developer:** [Your Name] ([Your LinkedIn Profile Link])

---

## 📌 The Business Problem

When engineering generative AI features, a single API call feels remarkably cheap (often a tiny fraction of a cent). However, when scaling that feature to production environments handling tens of thousands of users or executing high-volume automation loops, these micro-fractions compound exponentially. 

Defaulting to premium, heavy-reasoning models for simple processing tasks can lead to massive financial overruns. This simulation tool bridges the gap between software engineering and cloud economics, providing teams with the mathematical proof needed to implement cost-effective **Model Routing** strategies.

---

## 🛠️ Core Features

- **Local Tokenization Tracking:** Utilizes OpenAI's official `tiktoken` library to break down and count sub-word tokens instantly on the client side. This eliminates live network API overhead, rendering calculations with zero latency.
- **Live Market Price Mapping:** Cross-references exact token metrics against public enterprise market rates (per 1 Million tokens) for industry-leading models including OpenAI (GPT-4o, GPT-4o-mini), Anthropic (Claude 3.5 Sonnet, Claude 4.5 Haiku), and Google (Gemini 1.5 Flash).
- **Enterprise Traffic Simulator:** Features a dynamic scale multiplier allowing architectural teams to simulate anywhere from 1 to 100,000 concurrent production API requests to forecast budgetary compounding.
- **Dynamic Visualizations:** Generates rich, interactive stacked bar charts via **Plotly Express** to visually isolate and compare input (prompt) vs. output (completion) cost distributions across different model tiers.

---

## 📊 Application Architecture & Logic

The application computes data strictly using the core AI financial operations formula:

$$\text{Total Cost} = \left[ \left( \frac{\text{Input Tokens}}{1,000,000} \times \text{Input Rate} \right) + \left( \frac{\text{Output Tokens}}{1,000,000} \times \text{Output Rate} \right) \right] \times \text{Simulated API Calls}$$

No live model endpoints are triggered during execution, rendering the tool entirely cost-free, secure, and performant for mock testing.

---

## 🚀 Local Installation & Setup

To run this dashboard locally on your machine, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/llm-cost-visualizer.git](https://github.com/YOUR_USERNAME/llm-cost-visualizer.git)
cd llm-cost-visualizer


