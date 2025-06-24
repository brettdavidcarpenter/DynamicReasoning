# Enhanced agents that can handle real conversations using your existing architecture.

from dynamic_agent.knowledge_graph import KnowledgeGraph
from dynamic_agent.reasoning_engine import ReasoningEngine
from metrics import Metrics
from typing import Dict, List


class ConversationalStaticAgent:
    """Enhanced static agent with rigid conversation flow."""

    def __init__(self, metrics: Metrics):
        self.metrics = metrics
        self.state = "initial"
        self.conversation_history = []

        self.states = {
            "initial": {
                "valid_inputs": ["cancel", "subscription", "cancel subscription"],
                "response": "I can help you cancel your subscription. To proceed, please type 'confirm cancel'.",
                "next_state": "awaiting_confirmation",
                "error_response": "I didn't understand. Please type 'cancel subscription' to begin."
            },
            "awaiting_confirmation": {
                "valid_inputs": ["confirm cancel"],
                "response": "Your subscription has been cancelled. For refund information, please contact billing@company.com.",
                "next_state": "completed",
                "error_response": "Invalid input. Please type 'confirm cancel' to proceed."
            },
            "completed": {
                "valid_inputs": [],
                "response": "Your subscription is already cancelled. Transferring to human agent.",
                "next_state": "completed",
                "error_response": "Your subscription is already cancelled. Transferring to human agent."
            }
        }

    def process_input(self, user_input: str) -> Dict:
        """Process user input and return response with metrics."""
        self.metrics.record_turn()
        self.conversation_history.append(("user", user_input))

        user_input_clean = user_input.lower().strip()
        current = self.states[self.state]

        valid_input_found = any(v in user_input_clean for v in current["valid_inputs"])
        if valid_input_found:
            response = current["response"]
            self.state = current["next_state"]
            if self.state == "completed":
                self.metrics.record_task_completed()
        else:
            response = current["error_response"]
            self.metrics.record_error()
            if "refund" in user_input_clean and self.state == "awaiting_confirmation":
                response = "I can't process multiple requests. Please first type 'confirm cancel'."

        self.conversation_history.append(("bot", response))

        return {
            "response": response,
            "state": self.state,
            "metrics": self.metrics.summary(),
            "completed": self.state == "completed",
        }


class ConversationalDynamicAgent:
    """Enhanced dynamic agent using knowledge graph reasoning."""

    def __init__(self, metrics: Metrics, knowledge_graph: KnowledgeGraph):
        self.metrics = metrics
        self.kg = knowledge_graph
        self.reasoning_engine = ReasoningEngine(knowledge_graph)
        self.conversation_history = []
        self.user_context = {
            "subscription_type": "Premium",
            "monthly_cost": 29,
            "months_subscribed": 8,
            "eligible_for_refund": True,
            "prorated_refund": 19,
        }
        self.conversation_state = {
            "goals": set(),
            "completed_actions": set(),
            "current_focus": None,
        }
        self._init_knowledge_graph()

    def _init_knowledge_graph(self):
        self.kg.add_fact("user_request", "contains_intent", "cancel_subscription")
        self.kg.add_fact("user_request", "contains_intent", "refund_inquiry")
        self.kg.add_fact("cancel_subscription", "requires", "account_verification")
        self.kg.add_fact("cancel_subscription", "enables", "refund_processing")
        self.kg.add_fact("refund_inquiry", "requires", "policy_check")
        self.kg.add_fact("policy_check", "enables", "refund_calculation")
        self.kg.add_fact("account_verification", "leads_to", "cancellation_processing")
        self.kg.add_fact("refund_calculation", "leads_to", "refund_offer")
        self.kg.add_fact("cancellation_processing", "can_combine_with", "refund_processing")
        self.kg.add_fact("combined_service", "improves", "customer_satisfaction")
        self.kg.add_fact("single_interaction", "reduces", "service_calls")

    def _analyze_intent(self, user_input: str) -> List[str]:
        intents = []
        lower = user_input.lower()
        if any(w in lower for w in ["cancel", "stop", "end", "quit"]):
            intents.append("cancel_subscription")
        if any(w in lower for w in ["refund", "money", "back", "return", "reimburse"]):
            intents.append("refund_inquiry")
        if any(w in lower for w in ["help", "support", "question"]):
            intents.append("general_help")
        return intents

    def _generate_contextual_response(self, intents: List[str]) -> str:
        if not intents:
            return "I'm here to help with your account. What would you like to do today?"
        if "cancel_subscription" in intents and "refund_inquiry" in intents:
            self.conversation_state["goals"].update(["cancel_subscription", "refund_inquiry"])
            return (
                f"I understand you want to cancel your {self.user_context['subscription_type']} "
                f"subscription and learn about refunds. Let me help with both. "
                f"You're eligible for a ${self.user_context['prorated_refund']} prorated refund "
                f"for this billing period. Would you like me to process both the cancellation "
                f"and refund together?"
            )
        elif "cancel_subscription" in intents:
            self.conversation_state["goals"].add("cancel_subscription")
            return (
                f"I can help you cancel your {self.user_context['subscription_type']} subscription. "
                f"Before proceeding, you should know you're eligible for a "
                f"${self.user_context['prorated_refund']} refund. Would you like me to "
                f"handle both the cancellation and refund?"
            )
        elif "refund_inquiry" in intents:
            self.conversation_state["goals"].add("refund_inquiry")
            return (
                f"I can help with refund information. Based on your "
                f"{self.user_context['subscription_type']} subscription, you're eligible "
                f"for a ${self.user_context['prorated_refund']} prorated refund if you "
                f"cancel within this billing period. Would you like to proceed with cancellation?"
            )
        else:
            return "I can assist with subscription changes, billing questions, or account management. How can I help?"

    def _check_completion(self) -> bool:
        if not self.conversation_state["goals"]:
            return False
        positive = ["yes", "proceed", "ok", "sure", "please"]
        last_user = ""
        for msg_type, msg_text in reversed(self.conversation_history):
            if msg_type == "user":
                last_user = msg_text.lower()
                break
        return any(p in last_user for p in positive)

    def process_input(self, user_input: str) -> Dict:
        self.metrics.record_turn()
        self.conversation_history.append(("user", user_input))
        intents = self._analyze_intent(user_input)

        if self._check_completion() and self.conversation_state["goals"]:
            goals = list(self.conversation_state["goals"])
            if "cancel_subscription" in goals and "refund_inquiry" in goals:
                response = (
                    f"Perfect! I've cancelled your {self.user_context['subscription_type']} "
                    f"subscription and processed a ${self.user_context['prorated_refund']} "
                    f"prorated refund. You'll receive confirmation shortly, and the refund "
                    f"will appear in 3-5 business days. Your service remains active until "
                    f"the end of your billing period. Anything else I can help with?"
                )
            elif "cancel_subscription" in goals:
                response = (
                    f"Your {self.user_context['subscription_type']} subscription has been "
                    f"cancelled successfully. You're also eligible for a "
                    f"${self.user_context['prorated_refund']} refund. Would you like me "
                    f"to process that as well?"
                )
            else:
                response = "I've processed your request. Is there anything else I can help you with?"
            self.conversation_state["completed_actions"].update(self.conversation_state["goals"])
            self.metrics.record_task_completed()
        else:
            response = self._generate_contextual_response(intents)

        self.conversation_history.append(("bot", response))
        completed = bool(self.conversation_state["completed_actions"])

        return {
            "response": response,
            "intents": intents,
            "goals": list(self.conversation_state["goals"]),
            "metrics": self.metrics.summary(),
            "completed": completed,
        }


# API Layer for React Integration
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

static_metrics = Metrics()
dynamic_metrics = Metrics()
kg = KnowledgeGraph()

static_agent = ConversationalStaticAgent(static_metrics)
dynamic_agent = ConversationalDynamicAgent(dynamic_metrics, kg)


@app.route('/api/static-agent', methods=['POST'])
def static_agent_endpoint():
    data = request.json
    user_input = data.get('input', '')
    try:
        result = static_agent.process_input(user_input)
        return jsonify({
            'success': True,
            'response': result['response'],
            'metrics': result['metrics'],
            'completed': result['completed'],
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/dynamic-agent', methods=['POST'])
def dynamic_agent_endpoint():
    data = request.json
    user_input = data.get('input', '')
    try:
        result = dynamic_agent.process_input(user_input)
        return jsonify({
            'success': True,
            'response': result['response'],
            'metrics': result['metrics'],
            'completed': result['completed'],
            'intents': result.get('intents', []),
            'goals': result.get('goals', []),
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/reset', methods=['POST'])
def reset_agents():
    global static_agent, dynamic_agent, static_metrics, dynamic_metrics, kg
    static_metrics = Metrics()
    dynamic_metrics = Metrics()
    kg = KnowledgeGraph()
    static_agent = ConversationalStaticAgent(static_metrics)
    dynamic_agent = ConversationalDynamicAgent(dynamic_metrics, kg)
    return jsonify({'success': True, 'message': 'Agents reset successfully'})


@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    return jsonify({
        'static': static_metrics.summary(),
        'dynamic': dynamic_metrics.summary(),
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
