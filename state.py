from typing import TypedDict


class CustomerSupportState(TypedDict):
    # Customer Details
    customer_name: str
    customer_id: str

    # Customer Query
    query: str

    # Memory
    memory_response: str

    # Intent Classification
    intent: str

    # Department Routing
    department: str

    # RAG Context
    retrieved_context: str

    # Human Approval
    requires_approval: bool
    approval_status: str

    # Agent Outputs
    agent_response: str
    supervisor_response: str

    # Final Response
    final_response: str