# Google-DuckDuckGo-Video-Agent 🚀✨

An AI-powered video agent integrating Google Gemini Live API and DuckDuckGo web search to provide real-time, accurate answers within live video interactions.

---

## Features 🎯

- 🚀 **Live Interaction:** Conversational AI powered by Google Gemini Live API.  
- 🔎 **Real-Time Search:** Integrates DuckDuckGo for fresh, grounded knowledge.  
- 🛠️ **Modular Design:** Clean, extensible Python codebase for easy customization.  
- 🔧 **Configurable:** Environment-based API key and runtime management.  
- ⚡ **Low Latency:** Optimized streaming for smooth video/voice Q&A.

---

## Architecture Overview 🏗️

This agent orchestrates between user, Google Gemini Live, and DuckDuckGo search:

1. 🎤 User inputs streamed from video/voice client to backend.  
2. 🌐 DuckDuckGo invoked for external knowledge when needed.  
3. 🧠 Combines query + search results as context.  
4. 💬 Google Gemini Live generates grounded, natural responses.  
5. 🔄 Responses streamed back in near real time.

Components are decoupled for independent upgrades and testing.

---

## Getting Started 🏁

### Prerequisites ✔️

- Python 3.9+  
- Google Gemini Live API key  
- Basic familiarity with virtual environments and environment variables

### Installation 🛠️
```bash
git clone https://github.com/venkatsai2004/Google-DuckDuckGo-Video-Agent.git
cd Google-DuckDuckGo-Video-Agent
python -m venv .venv
source .venv/bin/activate # Linux/macOS

or
.venv\Scripts\activate # Windows
pip install -r requirements.txt

```


### Configuration ⚙️

Create a `.env` file with: GEMINI_API_KEY=your_google_gemini_live_api_key_here


Add any other config keys as required.

---

## Usage ▶️

Run the backend agent:

Connect your video/voice frontend to use the agent. The agent will:

- Listen for user queries.  
- Use DuckDuckGo for relevant web searches.  
- Generate accurate responses via Google Gemini Live.  
- Stream replies back seamlessly.

---

## Contributing 🤝

Contributions and enhancements are welcome. Please open issues or submit pull requests.

---

## License 📜

MIT License. See [LICENSE](LICENSE) for details.

---

Enjoy building interactive AI-driven video experiences! 🚀😊










