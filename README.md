# The-Guessing-Game

🧠 LLM Guessing Game: Duel of Minds
This project simulates a game where two language models debate and guess a hidden concept. One model plays the host, choosing a secret word, while the other acts as a player, asking yes/no questions to figure out what the secret word is. It's an interactive blend of logic, language understanding, and strategy.

🚀 Features
🧩 One-word concept guessing game.

🤖 Dual LLM setup: Host vs Player.

❓ Binary (yes/no) questioning format.

♻️ Turn-based gameplay over multiple rounds.

✅ Modular and extendable design using LangChain.

📦 Dependencies
Ensure you have the following packages installed:

pip install langchain langchain-community langchain-core langchain-openai langchain-groq python-dotenv

You’ll also need to configure models like llama2, gpt-4-turbo, or Llama3-70b via LangChain's supported backends (e.g., Ollama, OpenAI, Groq).

🧠 How It Works
1. Host Initialization
The host selects a random common object (1 word only) not used in previous rounds.

2. Player Turn
The player asks yes/no questions to guess the object.

The fewer questions used, the better.

3. Game Flow
Each round has a host and a player.

After a number of questions or a correct guess, the role switches.

Scores are tracked and displayed.






