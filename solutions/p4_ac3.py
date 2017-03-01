# -*- coding: utf-8 -*-

from collections import deque


def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())

    # TODO implement this

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
        # Check if none of the value in xi satisfy the
        if (not found):
            xi.domain.remove(valXI)
            revised = True
    return revised







