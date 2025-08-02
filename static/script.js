function sayHello() {
  const userConfirmed = confirm(
    "👋 Hello! You've triggered the AI Voice Agent interface.\n\nSoon, voice interaction and AI features will be live. Stay tuned!"
  );

  if (userConfirmed) {
    alert("Thanks for showing interest! 🔊");
  }
}

// Optional: Responsive greeting (based on device)
window.onload = () => {
  if (window.innerWidth < 500) {
    console.log("📱 Mobile view detected");
  } else {
    console.log("🖥️ Desktop view detected");
  }
};
