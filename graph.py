from langgraph.graph import StateGraph, END
from supervisor import supervisor_agent
from state import CustomerSupportState

from nodes import (
    classify_intent,
    memory_check_node,
    save_memory_node
)

from agents import (
    sales_agent,
    technical_agent,
    billing_agent,
    account_agent
)
from approval import (
    approval_check_node,
    human_approval_node
)
# -------------------------------
# Router Function
# -------------------------------

def route_department(state: CustomerSupportState):

    intent = state["intent"]

    if intent == "Memory":
        return "Memory"

    elif intent == "Sales":
        return "Sales"

    elif intent == "Technical":
        return "Technical"

    elif intent == "Billing":
        return "Billing"

    elif intent == "Account":
        return "Account"

    # Unknown queries also go for approval checking
    return "Approval Check"

def approval_router(state: CustomerSupportState):

    if state["requires_approval"]:
        return "Human Approval"

    return "Supervisor"
# -------------------------------
# Build LangGraph
# -------------------------------

builder = StateGraph(CustomerSupportState)

# Memory node
builder.add_node("Memory Check", memory_check_node)

# Intent Classification
builder.add_node("Intent Classification", classify_intent)

# Department Agents
builder.add_node("Sales", sales_agent)
builder.add_node("Technical", technical_agent)
builder.add_node("Billing", billing_agent)
builder.add_node("Account", account_agent)
builder.add_node("Approval Check", approval_check_node)

builder.add_node("Human Approval", human_approval_node)
builder.add_node("Supervisor", supervisor_agent)
# Save Memory
builder.add_node("Save Memory", save_memory_node)
builder.add_node("Memory", lambda state: state)

# Entry Point
builder.set_entry_point("Memory Check")

# Memory -> Intent
builder.add_edge(
    "Memory Check",
    "Intent Classification"
)

# Intent Routing
builder.add_conditional_edges(
    "Intent Classification",
    route_department
)

# Save conversations before ending
builder.add_edge(
    "Sales",
    "Approval Check"
)

builder.add_edge(
    "Technical",
    "Approval Check"
)

builder.add_edge(
    "Billing",
    "Approval Check"
)

builder.add_edge(
    "Account",
    "Approval Check"
)
builder.add_conditional_edges(
    "Approval Check",
    approval_router
)
builder.add_edge(
    "Supervisor",
    "Save Memory"
)
builder.add_edge(
    "Human Approval",
    "Supervisor"
)
builder.add_edge(
    "Save Memory",
    END
)
builder.add_edge("Memory", END)
graph = builder.compile()