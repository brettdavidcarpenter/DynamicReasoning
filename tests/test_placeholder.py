from static_agent.intent_recognizer import IntentRecognizer
from static_agent.dialogue_manager import DialogueManager
from dynamic_agent.knowledge_graph import KnowledgeGraph
from dynamic_agent.reasoning_engine import ReasoningEngine


def test_intent_recognizer():
    ir = IntentRecognizer()
    assert ir.recognize("I want a refund") == "ask_refund"


def test_dialogue_manager():
    dm = DialogueManager()
    assert "subscription" in dm.handle_intent("cancel_subscription")


def test_reasoning_engine():
    kg = KnowledgeGraph()
    re = ReasoningEngine(kg)
    plan = re.plan("cancel my plan")
    assert "cancel" in plan
