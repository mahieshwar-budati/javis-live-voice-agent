# 🎙️ LiveKit Voice Agent

A **LiveKit-powered Voice AI Agent** that demonstrates how to build **real-time conversational AI** with **Model Context Protocol (MCP)** server integration.

This project provides both:

- A **minimal voice agent** for learning and experimentation.
- A **production-ready MCP-enabled voice agent** with tool calling, multiple AI providers, and extensible architecture.

---

# ✨ Features

- 🎤 Natural real-time voice conversations
- ⚡ Low-latency speech pipeline
- 🔄 Interruptible conversations
- 🛠️ MCP (Model Context Protocol) server integration
- 🤖 Configurable LLM providers
- 🎧 Multiple Speech-to-Text providers
- 🗣️ Multiple Text-to-Speech providers
- 🌍 Multilingual turn detection
- 📊 Logging and metrics support
- 🔌 Easily extensible with custom tools

---

# 🏗️ Architecture

```text
                     ┌───────────────────────┐
                     │     LiveKit Client    │
                     └──────────┬────────────┘
                                │
                                ▼
                  ┌──────────────────────────┐
                  │      Voice Agent         │
                  └──────────┬───────────────┘
                             │
        ┌────────────────────┼─────────────────────┐
        │                    │                     │
        ▼                    ▼                     ▼
 ┌──────────────┐    ┌──────────────┐     ┌────────────────┐
 │  Deepgram    │    │   OpenAI     │     │   MCP Servers  │
 │     STT      │    │  LLM / TTS   │     │     (Tools)    │
 └──────────────┘    └──────────────┘     └────────────────┘
```

---

# 📦 Project Structure

```text
livekit-agent/
│
├── livekit_basic_agent.py      # Minimal voice agent
├── livekit_mcp_agent.py        # MCP-enabled voice agent
├── pyproject.toml              # Python dependencies
├── Dockerfile                  # Docker deployment
├── .env.example                # Environment variables
└── README.md
```

---

# 📋 Prerequisites

- Python **3.9+**
- UV Package Manager

API Keys:

- OpenAI API Key
- Deepgram API Key

Optional:

- LiveKit Cloud Account
- LiveKit API Key
- LiveKit API Secret

---

# 🚀 Quick Start

## 1. Clone the Repository

```bash
git clone <repository-url>

cd livekit-agent
```

---

## 2. Install Dependencies

Using **UV**

```bash
uv sync
```

---

## 3. Configure Environment Variables

Copy the example environment file.

```bash
cp .env.example .env
```

Configure the following values.

| Variable | Required | Description |
|-----------|----------|-------------|
| OPENAI_API_KEY | ✅ | OpenAI API Key |
| DEEPGRAM_API_KEY | ✅ | Deepgram API Key |
| LIVEKIT_URL | Optional | LiveKit Cloud URL |
| LIVEKIT_API_KEY | Optional | LiveKit API Key |
| LIVEKIT_API_SECRET | Optional | LiveKit API Secret |
| LLM_CHOICE | Optional | Model selection |
| LOG_LEVEL | Optional | Logging level |

---

## 4. Download Required Models

The first run requires downloading the voice activity detection and turn detection models.

### Basic Agent

```bash
uv run python livekit_basic_agent.py download-files
```

### MCP Agent

```bash
uv run python livekit_mcp_agent.py download-files
```

---

## 5. Run the Agent

### Basic Agent

Console Mode

```bash
uv run python livekit_basic_agent.py console
```

Development Mode

```bash
uv run python livekit_basic_agent.py dev
```

Production Mode

```bash
uv run python livekit_basic_agent.py start
```

---

### MCP Agent

Console Mode

```bash
uv run python livekit_mcp_agent.py console
```

---

# 🤖 Available Agents

## Basic Agent

**File**

```text
livekit_basic_agent.py
```

A lightweight implementation intended for learning and quick experimentation.

### Includes

- OpenAI LLM
- Deepgram STT
- OpenAI TTS
- Silero VAD
- Example Tool

```python
get_current_date_and_time()
```

Ideal for:

- Learning LiveKit
- Local testing
- Voice pipeline experiments

---

## MCP Agent

**File**

```text
livekit_mcp_agent.py
```

A production-oriented implementation featuring:

- MCP Tool Calling
- Configurable AI Providers
- Event Handling
- Multilingual Turn Detection
- Logging
- Metrics
- State Management

Ideal for:

- AI Assistants
- Enterprise Applications
- Production Voice Agents

---

# 🎙️ Voice Pipeline

The voice pipeline is modular and every component can be replaced.

---

## Speech-to-Text (STT)

Default

- Deepgram Nova-2

Alternatives

- AssemblyAI
- Azure Speech
- Whisper

---

## Large Language Model (LLM)

Default

- GPT-4.1 Mini

Alternatives

- Anthropic Claude
- Google Gemini
- Groq

---

## Text-to-Speech (TTS)

Default

- OpenAI Echo

Alternatives

- Cartesia
- ElevenLabs

---

## Voice Activity Detection

Default

- Silero VAD

---

## Turn Detection

Default

- Multilingual Turn Detector

Alternatives

- Semantic Turn Detection
- VAD-based Detection

---

# 🔌 MCP Server Integration

The voice agent supports **Model Context Protocol (MCP)** servers for extending capabilities with external tools.

Example configuration:

```python
session = AgentSession(
    ...
    mcp_servers=[
        mcp.MCPServerHTTP(
            url="http://localhost:8089/mcp"
        )
    ]
)
```

---

# 🛠️ Creating Custom Tools

You can define tools directly inside the agent using the `@function_tool` decorator.

```python
from datetime import datetime
from livekit.agents import Agent
from livekit.agents import RunContext
from livekit.agents import function_tool


class Assistant(Agent):

    @function_tool
    async def get_current_time(
        self,
        context: RunContext,
    ) -> str:
        """Returns the current system time."""

        return datetime.now().strftime("%I:%M %p")
```

---

# 📥 Installing Additional Providers

## Additional TTS Providers

```bash
uv add \
livekit-plugins-cartesia \
livekit-plugins-elevenlabs
```

---

## Additional LLM Providers

```bash
uv add \
livekit-plugins-anthropic \
livekit-plugins-google \
livekit-plugins-groq
```

---

## Additional STT Providers

```bash
uv add \
livekit-plugins-assemblyai \
livekit-plugins-azure
```

---

# ☁️ Deploy to LiveKit Cloud

## Step 1

Create a LiveKit Cloud account.

---

## Step 2

Install the LiveKit CLI.

### Windows

```powershell
winget install LiveKit.LiveKitCLI
```

### macOS

```bash
brew install livekit
```

### Linux

```bash
curl -sSL https://get.livekit.io/ | bash
```

---

## Step 3

Authenticate

```bash
lk cloud auth
```

---

## Step 4

Configure Environment Variables

```bash
lk app env -w
```

This generates:

```text
.env.local
```

---

## Step 5

Start the Agent

```bash
uv run python livekit_basic_agent.py start
```

---

## Step 6

Register the Agent

```bash
lk agent create
```

---

## Step 7

Test in Playground

Open the LiveKit Agents Playground and test your voice assistant directly in the browser.

---

## Step 8 (Optional)

Integrate with LiveKit Telephony for phone call support.

---

# 🧪 Console Mode

No LiveKit server is required.

Basic Agent

```bash
uv run python livekit_basic_agent.py console
```

MCP Agent

```bash
uv run python livekit_mcp_agent.py console
```

This launches an interactive session using your:

- Microphone
- Speakers

Perfect for local development.

---

# ⚡ Performance Optimization

## Reduce Latency

- Deploy close to users
- Use Deepgram for STT
- Use Cartesia for TTS
- Prefer streaming APIs

---

## Improve Scalability

- Configure prewarm workers
- Reuse API connections
- Cache frequent responses
- Optimize external API calls

---

# 🐳 Docker

Build

```bash
docker build -t livekit-agent .
```

Run

```bash
docker run --env-file .env livekit-agent
```

---

# 🛠️ Troubleshooting

## Python Version

Verify Python version.

```bash
python --version
```

Requires:

```text
Python 3.9+
```

---

## Model Download Issues

The first startup downloads:

- Silero VAD
- Turn Detection Models

This may take several minutes.

---

## API Key Problems

Verify:

- API keys are valid
- Environment variables are loaded
- No extra whitespace
- Account has sufficient credits

---

## Audio Issues

Check:

- Microphone permissions
- Speaker output
- Audio devices
- VAD sensitivity

---

# 📖 Environment Variables

| Variable | Required | Description |
|-----------|----------|-------------|
| OPENAI_API_KEY | ✅ | OpenAI API Key |
| DEEPGRAM_API_KEY | ✅ | Deepgram API Key |
| LIVEKIT_URL | Optional | LiveKit Server URL |
| LIVEKIT_API_KEY | Optional | LiveKit API Key |
| LIVEKIT_API_SECRET | Optional | LiveKit API Secret |
| LLM_CHOICE | Optional | Preferred LLM |
| LOG_LEVEL | Optional | Logging Level |

---

# 📚 Resources

- LiveKit Agents Documentation
- LiveKit Python SDK
- Model Context Protocol (MCP)
- OpenAI API
- Deepgram Documentation

---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.
