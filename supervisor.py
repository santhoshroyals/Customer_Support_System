from state import CustomerSupportState


def supervisor_agent(state: CustomerSupportState):
    """
    Supervisor reviews and improves the response
    before sending it to the customer.
    """

    response = state["agent_response"]

    if state["requires_approval"]:

        response += (
            "\n\nSupervisor Review:\n"
            "This request has been reviewed and approved "
            "by the Human Supervisor."
        )

    else:

        response += (
            "\n\nSupervisor Review:\n"
            "The response has been reviewed and verified."
        )

    state["supervisor_response"] = response

    state["final_response"] = response

    print("Supervisor Agent Executed")

    return state