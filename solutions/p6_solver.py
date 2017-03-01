# -*- coding: utf-8 -*-

from collections import deque
from operator import itemgetter


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P6, *you do not need to modify this method.*
    """
    return ac3(csp, csp.constraints[variable].arcs())


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P6, *you do not need to modify this method.*
    """
    if backtrack(csp):
        return csp.assignment
    else:
        return None

# Method is_complete
def is_complete(csp):
    for variable in csp.variables:
       # Check if variable is assigned or not
       if (variable.is_assigned() == False):
           return False                                                   
    # Return true when CSP have values assigned
    return True

# Method is_consistent
def is_consistent(csp, variable, value):
    # Look for all the constraints linked to the variable
    for c in csp.constraints[variable]:
        # Look through all the CSP variables
        for var in csp.variables:
            # Check if the variable is assigned 
            if (var == c.var2 and var.is_assigned()):
                # check if satisfied
                if not c.is_satisfied(value, var.value):
                    return False
    return True

def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.
    """

    # TODO copy from p3
    # TODO implement this
    # Check if CSP is complete then there is solution
    if (is_complete(csp)):
        return csp.assignment
    else:
        # Get unassigned variables
        unassignedVar = select_unassigned_variable(csp)
        # Get all possible values 
        for domValues in order_domain_values(csp, unassignedVar):
            # Check if value doesn't violate any constraint
            if (is_consistent(csp, unassignedVar, domValues)):
                # Update the value
                csp.variables.begin_transaction()
                unassignedVar.assign(domValues)
                inference(csp, unassignedVar)
                retVal = backtrack(csp)

                if (retVal != False):
                    return True
                else:
                    # Rollback any changes in the domains
                    csp.variables.rollback()
    return False

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


def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise.  Note that this method does not
    return any additional variable assignments (for simplicity)."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())

   # Loop as long as queue is not empty
    while (queue_arcs):
        # Take the element in the queue
        qArcs = queue_arcs.popleft()
        xi, xj = qArcs[0], qArcs[1]

        if (revise(csp, xi, xj)):
            # Check if the domain still contain some variable
            if(len(xi.domain) == 0):
                return False
            else:
                # Loop through arcs[0] neighbors
                for arcs in csp.constraints[xi].arcs():
                    if (arcs[0] == xj or arcs[1] == xj):
                        continue
                    queue_arcs.append(arcs)
    return True

def revise(csp, xi, xj):
    # You may additionally want to implement the 'revise' method.
    revised = False
    # Loop value in xi domain
    for valXI in xi.domain:
        found = False
        # Loop value in xj
        for valXJ in xj.domain:
            # check if domain for xj satisfies constraints
            satisfied = True
            for constraint in csp.constraints[xi, xj]:
                if (not constraint.is_satisfied(valXI, valXJ)):
                    satisfied = False
                    break
            # Check if the value of xj is consistent already
            if (satisfied):
                found = True
                break
        # Check if none of the value in xi satisfy the constraint with xj
        if (not found):
            xi.domain.remove(valXI)
            revised = True
    return revised







