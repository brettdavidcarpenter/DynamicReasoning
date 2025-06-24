from .intent_recognizer import IntentRecognizer
from .dialogue_manager import DialogueManager
from common.api import APIClient


class StaticAgent:
    """Simple agent that maps user text to intent and predefined responses."""

    def __init__(self, api_client: APIClient | None = None) -> None:
        self.intent_recognizer = IntentRecognizer()
        self.dialogue_manager = DialogueManager()
        self.api = api_client or APIClient()

    def handle(self, text: str) -> str:
        """Process user text and return a response string."""
        intent = self.intent_recognizer.recognize(text)
        # Trigger backend side effects based on intent
        if intent == "cancel_subscription":
            self.api.cancel_subscription("user")
        elif intent == "ask_refund":
            self.api.request_refund("user", "order")
        return self.dialogue_manager.handle_intent(intent)
