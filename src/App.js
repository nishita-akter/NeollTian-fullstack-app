import React, { useState } from "react";
import ChatWindow from "./ChatWindow";
import ChatInput from "./ChatInput";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([]);

  const handleSend = (text) => {
    const newMessage = { id: Date.now(), sender: "user", text };
    setMessages((prev) => [...prev, newMessage]);

    setTimeout(() => {
      const aiMessage = {
        id: Date.now() + 1,
        sender: "ai",
        text: `@NeollTian: Hello! Here's a concise breakdown.\n\nComputer Science (CS) is the foundational science of computation...`,
      };
      setMessages((prev) => [...prev, aiMessage]);
    }, 800);
  };

  return (
    <div className="App">
      <aside className="sidebar">
        <h3>💬 Chat History</h3>
        <ul>
          {messages.map((msg) => (
            <li key={msg.id} className={msg.sender === "user" ? "user-msg" : "ai-msg"}>
              {msg.text.slice(0, 20)}...
            </li>
          ))}
        </ul>
      </aside>

      <main className="chat-main">
        <div className="header">
          <h1>🤖 NeollTian</h1>
          <p>Your Personal Software Engineer Assistant</p>
        </div>

        <ChatWindow messages={messages} />
        <ChatInput onSend={handleSend} />
      </main>
    </div>
  );
}

export default App;
