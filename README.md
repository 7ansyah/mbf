# BTC/USDT Futures Trading AI

This project is a BTC/USDT futures trading AI program with two AI agents sharing a centralized knowledge base ("brain").

## Features

- **Two AI Agents**: Agent-Alpha (fundamental analysis) and Agent-Beta (technical analysis).
- **Centralized "Brain"**: A shared knowledge base for collaboration.
- **Real-time Recommendations**: Provides trading recommendations based on chart analysis.
- **Reinforcement Learning**: Optimizes trading strategies using a reward function.

## Setup

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the main application:**
    ```bash
    python3 main.py
    ```

3.  **Run the web server:**
    ```bash
    python3 app.py
    ```

## Usage

1.  Open a web browser and go to `http://0.0.0.0:5000`.
2.  Upload a chart screenshot and ask a question.
3.  Click the "Analyze!" button to get a trading recommendation.
