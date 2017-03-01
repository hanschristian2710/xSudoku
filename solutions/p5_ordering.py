# -*- coding: utf-8 -*-
from collections import deque
from operator import itemgetter

def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    This method implements the minimum-remaining-values (MRV) and degree heuristic. That is,
    the variable with the smallest number of values left in its available domain.  If MRV ties,
    then it picks the variable that is involved in the largest number of constraints on other
    unassigned variables.
    """

    # TODO implement this
    smallestVal = float("inf")
    largestVal = float("-inf")

    unassignedVar = deque()

    for var in csp.variables:
        fDomain = len(var.domain)
        # Check if domain value is smaller than the smallest domain
        if (fDomain < smallestVal and fDomain != 1):
            unassignedVar.clear()
            unassignedVar.append(var)
            smallestVal = fDomain

        # Check if the value ties 
        if (fDomain == smallestVal):
            unassignedVar.append(var)

    for uVar in unassignedVar:
        if (len(csp.constraints[uVar]) > largestVal):
            nextUVar = uVar
    return nextUVar


def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    This method implements the least-constraining-value (LCV) heuristic; that is, the value
    that rules out the fewest choices for the neighboring variables in the constraint graph
    are placed before others.
    """

    # TODO implement this
    orderList = []

    for val in variable.domain:
        conf = 0

        # For every neighbor append the value to the list
        for arc in csp.constraints[variable].arcs():
            conf += arc[0].domain.count(val)
            conf += arc[1].domain.count(val)
        orderList.append([val, conf])

    # Sort the list 
    orderListSorted = sorted(orderList, key=itemgetter(1))
    newOrderList = []
    for value in orderListSorted:
        newOrderList.append(value[0])

    # Return order list of domain
    return newOrderList



