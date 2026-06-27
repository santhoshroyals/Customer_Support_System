from state import CustomerSupportState


# --------------------------------------------------
# Approval Check Node
# --------------------------------------------------

def approval_check_node(state: CustomerSupportState):
    """
    Check whether the customer request requires
    Human-in-the-Loop approval.
    """

    query = state["query"].lower()

    approval_keywords = [

    "refund",

    "cancel",
    "subscription",

    "close",
    "account closure",
    "delete account",

    "compensation",

    "escalate",
    "management",
    "manager"

]

    if any(keyword in query for keyword in approval_keywords):

        state["requires_approval"] = True

    else:

        state["requires_approval"] = False

    return state


# --------------------------------------------------
# Human Approval Node
# --------------------------------------------------

def human_approval_node(state: CustomerSupportState):

    print("\n========================================")
    print("      HUMAN SUPERVISOR APPROVAL")
    print("========================================\n")

    print("Customer Query:\n")
    print(state["query"])

    print("\nApproval Required.\n")

    decision = input("Approve request? (yes/no): ").strip().lower()

    if decision == "yes":

        state["approval_status"] = "Approved"

    else:

        state["approval_status"] = "Rejected"

    return state