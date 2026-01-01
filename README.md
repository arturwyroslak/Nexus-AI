# Nexus-AI 🧠🔗

**Nexus-AI** is a local-first, privacy-focused platform for orchestrating autonomous AI agent swarms. Inspired by the best innovations in Generative AI from 2025, it combines the orchestration power of hive-mind systems with the privacy of local execution and the interoperability of standard agent protocols.

## 🚀 Vision

Existing AI tools are often siloed or cloud-dependent. **Nexus-AI** bridges this gap by providing:
1.  **Local Sovereignty**: All agents run on your machine (via Ollama or local keys).
2.  **Swarm Intelligence**: Specialized agents (Researcher, Coder, Reviewer) collaborate to solve complex tasks.
3.  **Persistent Memory**: A shared "brain" that remembers project context across sessions.
4.  **Standardized Protocol**: Agents communicate using a simplified version of the A2A (Agent2Agent) protocol.

## ✨ Key Features

*   **🕵️ Local Swarm Orchestration**: Spin up multiple agents that talk to each other.
*   **💾 Nexus Memory Bank**: Vector-based semantic search for long-term context (using local embeddings).
*   **🔌 Pluggable Backends**: Support for Ollama (local) and OpenAI/Anthropic (cloud).
*   **📊 Visual Control Plane**: A Streamlit-based dashboard to watch your swarm work in real-time.

## 🛠️ Architecture

*   **Orchestrator (The Nexus)**: Central hub that manages agent lifecycles and message routing.
*   **Agents**: Independent entities with specific system prompts and tool capabilities.
*   **Memory**: Shared SQLite + Vector store for knowledge retrieval.
*   **UI**: Streamlit interface for interaction and visualization.

## 📦 Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/Nexus-AI.git
    cd Nexus-AI
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Run the Nexus:
    ```bash
    streamlit run app.py
    ```

## 🚀 Usage

1.  Open the Streamlit dashboard.
2.  Define your objective (e.g., "Research the history of Rust and write a summary").
3.  Select your swarm configuration (e.g., "Research Team").
4.  Watch agents collaborate, share memories, and produce results.

## 📄 License

MIT License
