class DialogueManager:
    """Simple state machine for handling predefined intents."""

    def __init__(self):
        self.state = None

    def handle_intent(self, intent: str) -> str:
        if intent == "cancel_subscription":
            return "Your subscription has been canceled."
        if intent == "ask_refund":
            return "I have submitted a refund request."
        return "I'm not sure how to help with that."
