# AI Chatbot Project

A full-stack AI-powered chatbot application built with **Flask** (backend) and **React** (frontend), integrated with **OpenAI's GPT-4o-mini** model.

---

## 📁 Project Structure

```
openAI-test/
├── backend/                 # Flask backend server
│   ├── app.py              # Main Flask application
│   ├── requirements.txt    # Python dependencies
│   └── README.md           # Backend documentation
│
└── frontend/               # React frontend
    ├── src/
    │   ├── App.jsx        # Main chat component
    │   ├── App.css        # Component styles
    │   ├── main.jsx       # React entry point
    │   └── index.css     # Global styles
    ├── public/            # Static assets
    ├── index.html        # HTML template
    ├── package.json     # Node dependencies
    ├── vite.config.js   # Vite configuration
    └── eslint.config.js # ESLint configuration
```

---

## 🛠️ Technology Stack

| Layer                 | Technology            |
| --------------------- | --------------------- |
| **Backend**           | Flask, Python 3.x     |
| **AI Model**          | OpenAI GPT-4o-mini    |
| **Frontend**          | React 19, Vite 8      |
| **Styling**           | Tailwind CSS 4        |
| **API Communication** | REST (JSON over HTTP) |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed
- **Node.js 18+** installed
- **OpenAI API Key** — Get one at [platform.openai.com](https://platform.openai.com)

### Backend Setup

```bash
cd backend

# Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo OPEN_AI_SECRET_KEY=your_api_key_here > .env

# Run the server
python app.py
```

The backend will run at `http://127.0.0.1:5000`

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will run at `http://localhost:5173` (default Vite port)

---

## 💬 How It Works

### Architecture Flow

```
User Input (React Frontend)
        │
        ▼
POST /chat (JSON: { message: "Hello" })
        │
        ▼
Flask Backend (app.py)
        │
        ▼
OpenAI API (GPT-4o-mini)
        │
        ▼
AI Response
        │
        ▼
JSON Response: { reply: "Hello! How can I help?" }
        │
        ▼
Display in Chat UI
```

### Key Components

#### Backend (`app.py`)

- **CORS enabled** — Allows cross-origin requests from the frontend
- **Message history** — Maintains conversation context in memory
- **System prompt** — Sets AI behavior as "helpful assistant"

#### Frontend (`App.jsx`)

- **State management** — Tracks messages, loading state
- **Auto-scroll** — Keeps chat scrolled to latest message
- **Error handling** — Displays connection errors gracefully

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the `backend/` directory:

```env
OPEN_AI_SECRET_KEY=sk-your-openai-api-key-here
```

> ⚠️ **Important:** Never commit your API key to version control!

### Changing the AI Model

In `backend/app.py`, modify the model name:

```python
response = client.chat.completions.create(
    model="gpt-4o",        # Change from gpt-4o-mini
    messages=messages,
    temperature=0.7,
)
```

---

## 🎯 Current Features

- ✅ Real-time chat with AI
- ✅ Message history persistence (in-memory)
- ✅ Loading indicator during API calls
- ✅ Error handling for connection failures
- ✅ Dark theme UI
- ✅ Auto-scroll to latest message

---

## 🚧 Potential New Features

### High Priority

| Feature                      | Description                                                           |
| ---------------------------- | --------------------------------------------------------------------- |
| **Streaming Responses**      | Stream AI responses token-by-token for faster perceived response time |
| **Chat History Persistence** | Save conversations to database (SQLite/PostgreSQL)                    |
| **Multiple AI Models**       | Allow users to choose between GPT-4, GPT-4o, Claude, etc.             |
| **User Authentication**      | Login/signup to save personal chat history                            |
| **Chat Export**              | Export conversations as PDF or Markdown                               |

### Medium Priority

| Feature                      | Description                                        |
| ---------------------------- | -------------------------------------------------- |
| **Voice Input**              | Speech-to-text using Web Speech API                |
| **Text-to-Speech**           | Read AI responses aloud                            |
| **Code Syntax Highlighting** | Detect and format code blocks in responses         |
| **Markdown Rendering**       | Support bold, italic, lists, links in AI responses |
| **Theme Toggle**             | Light/dark mode switch                             |

### Lower Priority

| Feature                   | Description                                       |
| ------------------------- | ------------------------------------------------- |
| **Image Generation**      | Integrate DALL-E for image creation               |
| **File Upload**           | Allow users to upload PDFs/documents for analysis |
| **Custom System Prompts** | Let users define AI personality/behavior          |
| **Keyboard Shortcuts**    | Send with Ctrl+Enter, clear with Escape           |
| **Mobile Responsive**     | Improve mobile chat experience                    |

### Advanced Features

| Feature                    | Description                                            |
| -------------------------- | ------------------------------------------------------ |
| **Plugin System**          | Extend bot capabilities (web search, calculator, etc.) |
| **Webhooks**               | Integrate with Slack, Discord, Telegram                |
| **Analytics Dashboard**    | Track usage, response times, popular topics            |
| **Fine-tuned Models**      | Train custom model on specific data                    |
| **Multi-language Support** | Translate conversations in real-time                   |

---

## 📝 API Reference

### POST `/chat`

Send a message to the AI.

**Request:**

```json
{
  "message": "Hello, how are you?"
}
```

**Response:**

```json
{
  "reply": "Hello! I'm doing well, thank you for asking. How can I help you today?"
}
```

---

## 🐛 Troubleshooting

### Common Issues

| Issue                    | Solution                                         |
| ------------------------ | ------------------------------------------------ |
| **CORS Error**           | Ensure `CORS(app)` is called in Flask            |
| **API Key Not Found**    | Check `.env` file exists in `backend/`           |
| **ModuleNotFoundError**  | Run `pip install -r requirements.txt`            |
| **Port Already in Use**  | Change port in `app.py` or kill existing process |
| **React not connecting** | Ensure backend runs on `127.0.0.1:5000`          |

---

## 📄 License

MIT License — Feel free to use this project for learning or commercial purposes.

---

## 🙏 Acknowledgments

- [OpenAI](https://openai.com) — For providing the GPT API
- [Flask](https://flask.palletsprojects.com) — Lightweight WSGI web application framework
- [React](https://react.dev) — UI component library
- [Tailwind CSS](https://tailwindcss.com) — Utility-first CSS framework
