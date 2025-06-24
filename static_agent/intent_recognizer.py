class IntentRecognizer:
    """Placeholder intent recognizer using simple keyword matching."""

    def recognize(self, text: str) -> str:
        text = text.lower()
        if "cancel" in text:
            return "cancel_subscription"
        if "refund" in text:
            return "ask_refund"
        return "unknown"
