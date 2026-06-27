from graph import graph
from memory import initialize_database

# Initialize SQLite Database

initialize_database()

# Get Customer Query

query = input("Enter your customer query: ")

# Initial State

state = {
    "customer_name": "David",
    "customer_id": "C001",
    "query": query,
    "memory_response": "",
    "intent": "",
    "department": "",
    "retrieved_context": "",
    "requires_approval": False,
    "approval_status": "",
    "agent_response": "",
    "supervisor_response": "",
    "final_response": ""
}

# --------------------------------------------------
# Execute LangGraph
# --------------------------------------------------

result = graph.invoke(state)

# --------------------------------------------------
# Display Output
# --------------------------------------------------

print("\n")
print("=" * 80)
print("               AI CUSTOMER SUPPORT AUTOMATION SYSTEM")
print("=" * 80)

print(f"\nCustomer Name      : {result['customer_name']}")
print(f"Customer ID        : {result['customer_id']}")
print(f"Intent             : {result['intent']}")
print(f"Department         : {result['department']}")

# --------------------------------------------------
# Memory Recall
# --------------------------------------------------

if result["memory_response"]:
    print("\n" + "=" * 80)
    print("MEMORY RECALL")
    print("=" * 80)
    print(result["memory_response"])

# --------------------------------------------------
# Retrieved Context (RAG)
# --------------------------------------------------

if result["retrieved_context"]:
    print("\n" + "=" * 80)
    print("RETRIEVED KNOWLEDGE")
    print("=" * 80)
    print(result["retrieved_context"])

# --------------------------------------------------
# Agent Response
# --------------------------------------------------

if result["agent_response"]:
    print("\n" + "=" * 80)
    print("AGENT RESPONSE")
    print("=" * 80)
    print(result["agent_response"])

# --------------------------------------------------
# Human Approval
# --------------------------------------------------

print("\n" + "=" * 80)
print("APPROVAL STATUS")
print("=" * 80)

if result["requires_approval"]:
    print("Approval Required : YES")
    print(f"Approval Status   : {result['approval_status']}")
else:
    print("Approval Required : NO")

# --------------------------------------------------
# Supervisor Review
# --------------------------------------------------

if result["supervisor_response"]:
    print("\n" + "=" * 80)
    print("SUPERVISOR REVIEW")
    print("=" * 80)
    print(result["supervisor_response"])

# --------------------------------------------------
# Final Response
# --------------------------------------------------

if result["final_response"]:
    print("\n" + "=" * 80)
    print("FINAL RESPONSE")
    print("=" * 80)
    print(result["final_response"])

# --------------------------------------------------
# Completion
# --------------------------------------------------

print("\n" + "=" * 80)
print("PROCESS COMPLETED SUCCESSFULLY")
print("=" * 80)