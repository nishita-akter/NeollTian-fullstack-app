import React from "react";

const ChatWindow = ({ messages }) => {
  return (
    <div className="chat-window">
      {messages.map((msg) => (
        <div
          key={msg.id}
          className={`message ${msg.sender === "user" ? "user" : "ai"}`}
        >
          <div className="bubble">{msg.text}</div>
        </div>
      ))}
    </div>
  );
};

export default ChatWindow;
