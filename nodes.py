from state import CustomerSupportState
from memory import save_conversation, get_previous_issue


# --------------------------------------------------
# Intent Classification
# --------------------------------------------------

def classify_intent(state: CustomerSupportState):
    """
    Classify the customer's query into the correct support department.
    """

    # Skip classification for memory queries
    if state["intent"] == "Memory":
        return state

    query = state["query"].lower()

    # --------------------------------------------------
    # Billing (Highest Priority)
    # --------------------------------------------------
    if any(word in query for word in [
        "refund",
        "billing",
        "payment",
        "invoice",
        "charge",
        "compensation",
        "escalate",
        "management",
        "manager"
    ]):
        state["intent"] = "Billing"

    # --------------------------------------------------
    # Sales
    # --------------------------------------------------
    elif any(word in query for word in [
        "price",
        "pricing",
        "plan",
        "subscription",
        "product",
        "cancel"
    ]):
        state["intent"] = "Sales"

    # --------------------------------------------------
    # Technical Support
    # --------------------------------------------------
    elif any(word in query for word in [
        "error",
        "bug",
        "login",
        "install",
        "configuration",
        "crash",
        "upload",
        "application"
    ]):
        state["intent"] = "Technical"

    # --------------------------------------------------
    # Account
    # --------------------------------------------------
    elif any(word in query for word in [
        "password",
        "profile",
        "account",
        "activate",
        "deactivate",
        "close",
        "delete"
    ]):
        state["intent"] = "Account"

    # --------------------------------------------------
    # Unknown
    # --------------------------------------------------
    else:
        state["intent"] = "Unknown"

    return state


# --------------------------------------------------
# SQLite Memory Check
# --------------------------------------------------

def memory_check_node(state: CustomerSupportState):

    query = state["query"].lower()

    if "previous support issue" in query:

        previous_issue = get_previous_issue(
            state["customer_id"]
        )

        state["memory_response"] = (
            f"Your previous support issue was: {previous_issue}"
        )

        # Skip intent classification
        state["intent"] = "Memory"

    return state


# --------------------------------------------------
# Save Conversation
# --------------------------------------------------

def save_memory_node(state: CustomerSupportState):

    save_conversation(
        state["customer_id"],
        state["customer_name"],
        state["query"]
    )

    return state