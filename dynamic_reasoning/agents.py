class StaticAgent:
    """A simple agent that echoes messages with a static prefix."""

    def reply(self, message: str) -> str:
        return f"StaticAgent: {message}"


class DynamicAgent:
    """A simple agent that provides slightly more dynamic responses."""

    def reply(self, message: str) -> str:
        # For demonstration, reverse the message to show some processing
        reversed_msg = ' '.join(reversed(message.split()))
        return f"DynamicAgent: {reversed_msg}"
