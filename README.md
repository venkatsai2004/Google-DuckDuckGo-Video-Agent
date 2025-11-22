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

