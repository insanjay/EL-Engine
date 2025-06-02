# 🧠 Emotional Learning (EL) Engine

A lightweight emotional engine simulating emotional state transitions in an AI-like agent using vector dynamics, short-term memory, and personality thresholds.
---

Follow the link for the simplified **Medium Blog**👇

https://medium.com/@insanjay.work/teaching-ai-to-feel-the-birth-of-the-emotional-learning-engine-babec5630193

---

## 📌 What It Does

- Works on 5 basic emotions: **Joy, Angry, Sad, Fear, Trust (JASFT)**
- Simulates emotional reactions based on event inputs
- Incorporates emotional memory and personality thresholds
- Visualizes if/when emotions become "visible" (i.e., surpass personality thresholds)
- Models how emotions influence each other via a relationship map

---

## 🛠 How It Works

### Emotion Vector System

The emotional state of the agent is represented as a 5D vector in the JASFT format. Each value is between 0 (inactive) and 1 (fully activated).

```python
available_emotions = ["Joy", "Angry", "Sad", "Fear", "Trust"]
```

---

### Personality Bias

Each emotion has a threshold, called **personality bias**, which determines when that emotion becomes visible or is expressed outwardly.

```python
personality_bias = np.array([0.3, 0.7, 0.5, 0.4, 0.7])
```

---

### Relationship Map

This key component models how one dominant emotion can influence the others. A high Joy, for instance, can slightly increase Trust but suppress Sadness or Fear.

```python
relationship_map = {
    "Joy":   [ 1.0, -0.5, -0.4, -0.3,  0.6],
    "Angry": [-0.6,  1.0,  0.5,  0.7, -0.4],
    "Sad":   [-0.4,  0.6,  1.0,  0.6, -0.5],
    "Fear":  [-0.3,  0.6,  0.5,  1.0, -0.6],
    "Trust": [ 0.7, -0.4, -0.4, -0.3,  1.0],
}
```

---

### Core Flow

1. **Initialize memory** to keep track of recent emotional states (max 3).
2. **Generate an event** (a JASFT vector).
3. **Find the dominant emotion** in the event.
4. **Apply its influence** on the other emotions using the relationship map.
5. **Blend it** with the average of the emotional memory.
6. **Clip the result** to stay between 0 and 1.
7. **Compare each value** with its personality bias.
8. **Print emotions** that surpass the threshold (i.e., expressed emotions).
9. **Update memory**, rolling out older states.

---

## 💻 How to Run

### ✅ Requirements

- Python 3.x
- NumPy installed (`pip install numpy`)
- Any IDE (VSCode, PyCharm, etc.) or a Jupyter Notebook

---

## 🚀 Instructions

1. Open your Python environment (Jupyter, VSCode, or terminal).
2. Copy-paste the full code into a new Python file or notebook.
3. Run the script. It will simulate 10 emotional updates.
4. You'll be prompted to press enter to move through each step.
5. Emotion vectors and visible emotions will be printed in each iteration.

---

### 🎛️ To Use Custom Input

Inside the script, you'll find two versions of the `event` line:

```python
event = np.round(np.random.uniform(0, 1, size=5), 1)  # Random event
event = np.round(np.array([0.8, 0.2, 0.1, 0.3, 0.5]), 1)  # Custom event
```

You can **switch between random or custom input** just by commenting/uncommenting these lines.

- **Want random input every time?** → Keep the first, comment the second.
- **Want to test a fixed emotion?** → Comment the first, edit the second.

---

## 📊 Sample Output

```
Iteration number: 1
Joy
Trust
Final: [0.8 0.  0.  0.  0.5]
Personality: [0.3 0.7 0.5 0.4 0.7]

[0.8 0.  0.  0.  0.5]
```

---

## 🧪 Why This Matters

This simulation helps explore:

- How emotions affect one another dynamically
- How emotional expression can be threshold-dependent
- How short-term memory influences emotional state
- A foundational step toward emotional AI or NPC design

---

## 📦 What You Can Build On Top

- Add decay to simulate emotion fading over time
- Add emotional history for long-term trends
- Integrate with NLP inputs (e.g., emotion extraction from text)
- Build agents that evolve their personality with feedback
- Visualize emotion shifts with Matplotlib

---

## 🧠 Final Notes

This is **Version 1** — intentionally simple and interpretable.  
You’re encouraged to tweak weights, personality, and input to experiment with emergent behaviors.  
The code is readable, testable, and made to inspire experimentation.

---
