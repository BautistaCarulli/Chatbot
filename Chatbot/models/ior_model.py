def recognize_object(message):
    """Simulated object recognition logic."""
    objects = {
        "cat": "A small domesticated carnivorous mammal.",
        "dog": "A loyal domesticated animal often called man's best friend.",
        "car": "A road vehicle, typically with four wheels, powered by an engine.",
        "tree": "A perennial plant with a woody trunk, branches, and leaves.",
        "phone": "A portable electronic device used for communication.",
        "book": "A set of written or printed pages bound together, often containing knowledge or stories.",
    }

    for obj in objects:
        if obj in message.lower():
            return f"I recognized a {obj}: {objects[obj]}"
    return "I couldn't recognize any object in your message."