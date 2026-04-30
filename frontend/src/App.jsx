import { useState, useRef, useEffect } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chat]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const currentMessage = message; // ✅ capture before clearing
    const updatedChat = [...chat, { sender: "user", text: currentMessage }];
    setChat(updatedChat);
    setMessage("");
    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: currentMessage }), // ✅ send saved value
      });

      const data = await res.json();

      setChat([...updatedChat, { sender: "ai", text: data.reply }]);
    } catch {
      setChat([
        ...updatedChat,
        { sender: "ai", text: "Error connecting to server." },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className="h-screen flex flex-col bg-gray-900 text-white">
      {/* Header */}
      <div className="p-4 text-center text-xl font-bold border-b border-gray-700">
        🤖 AI Chatbot
      </div>

      {/* Chat */}
      <div className="flex-1 overflow-y-auto p-4 space-y-3">
        {chat.map((msg, i) => (
          <div
            key={i}
            className={`p-3 rounded-lg max-w-[70%] ${
              msg.sender === "user" ? "bg-blue-500 ml-auto" : "bg-gray-700"
            }`}
          >
            {msg.text}
          </div>
        ))}

        {loading && <div className="text-gray-400">AI is typing...</div>}

        <div ref={bottomRef}></div>
      </div>

      {/* Input */}
      <div className="p-4 flex gap-2 border-t border-gray-700">
        <input
          className="flex-1 p-2 rounded bg-gray-800 border border-gray-600 outline-none"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message..."
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
        <button
          onClick={sendMessage}
          className="bg-blue-600 px-4 rounded hover:bg-blue-700"
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default App;
