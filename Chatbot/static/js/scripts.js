document.getElementById("send-btn").addEventListener("click", () => {
    const userInput = document.getElementById("user-input").value.trim();
    if (!userInput) return;

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class="user-message"><strong>You:</strong> ${userInput}</div>`;
    document.getElementById("user-input").value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput }),
    })
        .then((response) => response.json())
        .then((data) => {
            chatBox.innerHTML += `<div class="bot-message"><strong>Bot:</strong> ${data.response}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        })
        .catch((error) => {
            console.error("Error:", error);
            chatBox.innerHTML += `<div class="bot-message error"><strong>Bot:</strong> Oops! Something went wrong.</div>`;
        });
});

// Handle Send Button
document.getElementById("send-btn").addEventListener("click", () => {
    const userInput = document.getElementById("user-input").value.trim();
    if (!userInput) return;

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class="user-message"><strong>You:</strong> ${userInput}</div>`;
    document.getElementById("user-input").value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput }),
    })
        .then((response) => response.json())
        .then((data) => {
            chatBox.innerHTML += `<div class="bot-message"><strong>Bot:</strong> ${data.response}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        })
        .catch((error) => {
            console.error("Error:", error);
            chatBox.innerHTML += `<div class="bot-message error"><strong>Bot:</strong> Oops! Something went wrong.</div>`;
        });
});

// Handle Restart Button
document.getElementById("restart-btn").addEventListener("click", () => {
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML = ""; // Clear the chat box

    // Optionally, send a reset request to the backend
    fetch("/restart", {
        method: "POST",
    })
        .then(() => {
            chatBox.innerHTML += `<div class="bot-message"><strong>Bot:</strong> Chatbot has been restarted. 😊</div>`;
        })
        .catch((error) => {
            console.error("Error:", error);
            chatBox.innerHTML += `<div class="bot-message error"><strong>Bot:</strong> Failed to restart the chatbot.</div>`;
        });
});

document.getElementById("help-btn").addEventListener("click", () => {
    const chatBox = document.getElementById("chat-box");

    // Check if the help message already exists
    if (document.querySelector(".help-message")) {
        return; // Do nothing if the help message is already displayed
    }

    // Add the help message to the chat box
    chatBox.innerHTML += `
        <div class="bot-message help-message">
            <strong>Bot:</strong> Here are some things you can ask me:
            <ul>
                <li><strong>Tell me a joke</strong> - I’ll share a funny joke with you.</li>
                <li><strong>Share a fact</strong> - I’ll tell you an interesting fact.</li>
                <li><strong>Start a quiz</strong> - I’ll start a fun quiz for you.</li>
                <li><strong>Recognize an object</strong> - I’ll try to recognize an object you mention.</li>
                <li><strong>Restart</strong> - Reset the chatbot.</li>
            </ul>
        </div>`;
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom of the chat box
});

// Display a welcome message when the chat starts
window.addEventListener("load", () => {
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `
        <div class="bot-message">
            <strong>Bot:</strong> Welcome to BC-Chatbot! 😊 How can I assist you today?
        </div>`;
});

const canvas = document.getElementById("background-canvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const particles = [];

// Create particles
for (let i = 0; i < 100; i++) {
    particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 3 + 1,
        dx: Math.random() * 2 - 1,
        dy: Math.random() * 2 - 1,
    });
}

// Draw particles
function drawParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach((p) => {
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(255, 255, 255, 0.7)";
        ctx.fill();
    });
}

// Update particle positions
function updateParticles() {
    particles.forEach((p) => {
        p.x += p.dx;
        p.y += p.dy;

        // Bounce particles off edges
        if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
        if (p.y < 0 || p.y > canvas.height) p.dy *= -1;
    });
}

// Animate particles
function animateParticles() {
    drawParticles();
    updateParticles();
    requestAnimationFrame(animateParticles);
}

animateParticles();

// Adjust canvas size on window resize
window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});