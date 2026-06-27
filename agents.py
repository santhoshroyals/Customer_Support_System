from state import CustomerSupportState
from rag import retrieve_context

# -------------------------------
# Sales Support Agent
# -------------------------------

def sales_agent(state):

    state["department"] = "Sales"

    context = retrieve_context(state["query"])

    state["retrieved_context"] = context

    state["agent_response"] = (
        "Sales Support Response\n\n"
        + context
    )

    print("Sales Support Agent Executed")

    return state
# -------------------------------
# Technical Support Agent
# -------------------------------

def technical_agent(state: CustomerSupportState):

    state["department"] = "Technical Support"

    state["agent_response"] = (
        "Thank you for contacting Technical Support. "
        "Please restart the application, verify your internet connection, "
        "and ensure you are using the latest version of the software."
    )

    print("Technical Support Agent Executed")

    return state


# -------------------------------
# Billing Support Agent
# -------------------------------

def billing_agent(state: CustomerSupportState):

    state["department"] = "Billing"

    state["agent_response"] = (
        "Thank you for contacting Billing Support. "
        "Your billing request has been received. "
        "If this is a refund request, it will require supervisor approval."
    )

    print("Billing Support Agent Executed")

    return state


# -------------------------------
# Account Support Agent
# -------------------------------

def account_agent(state: CustomerSupportState):

    state["department"] = "Account"

    state["agent_response"] = (
        "Thank you for contacting Account Support. "
        "You can reset your password using the 'Forgot Password' option "
        "available on the login page."
    )

    print("Account Support Agent Executed")

    return state