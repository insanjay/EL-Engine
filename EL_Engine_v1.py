import numpy as np

# Keep your definitions:
memory = []
available_emotions = ["Joy", "Angry", "Sad", "Fear", "Trust"]
personality_bias = np.array([0.3, 0.7, 0.5, 0.4, 0.7])

# THE NEW RELATIONSHIP MAP (example weights, you can tweak)
relationship_map = {
    "Joy":   [ 1.0, -0.5, -0.4, -0.3,  0.6],
    "Angry": [-0.6,  1.0,  0.5,  0.7, -0.4],
    "Sad":   [-0.4,  0.6,  1.0,  0.6, -0.5],
    "Fear":  [-0.3,  0.6,  0.5,  1.0, -0.6],
    "Trust": [ 0.7, -0.4, -0.4, -0.3,  1.0],
}

for iteration in range(10):
    print(f"Iteration number: {iteration + 1}")

    # 1) Generate a random event vector (JASFT)
    event = np.round(np.random.uniform(0, 1, size=5), 1)
    event = np.round(np.array([0.8, 0.2, 0.1, 0.3, 0.5]), 1)  # Example event for testing

    # 2) Compute current state as the mean of memory (or zero if empty)
    if memory:
        memory_mean = np.mean(memory, axis=0)
    else:
        memory_mean = np.zeros(5)

    # 3) Find which emotion is dominant in this event
    dominant_index = np.argmax(event)
    dominant_emotion = available_emotions[dominant_index]

    # 4) Build delta from the relationship map row × magnitude of that dominant emotion
    relation_vector = np.array(relationship_map[dominant_emotion])
    delta = event[dominant_index] * relation_vector

    # 5) Update the “current emotion” by adding the delta
    final_emotion = np.clip(memory_mean + delta, 0, 1)

    # 6) Check if any final_emotion exceeds personality_bias (i.e., visible reaction)
    for i in range(5):
        if final_emotion[i] > personality_bias[i]:
            print(available_emotions[i])

    print("Final:", final_emotion.round(1))
    print("Personality:", personality_bias)
    print()

    # 7) Roll memory: keep only last 3 (or fewer)
    if len(memory) > 2:
        memory.pop(0)
    memory.append(final_emotion)

    # 8) Print memory contents for debugging
    for mem in memory:
        print(mem.round(1))
    input("Enter to continue: ")