# -*- coding: utf-8 -*-



def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    For P3, *you do not need to modify this method.*
    """
    return next((variable for variable in csp.variables if not variable.is_assigned()))


def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    For P3, *you do not need to modify this method.*
    """
    return [value for value in variable.domain]


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P3, *you do not need to modify this method.*
    """
    return True


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P3, *you do not need to modify this method.*
    """
    if backtrack(csp):
        return csp.assignment
    else:
        return None

# Method is_complete   (P1)
def is_complete(csp):
    for variable in csp.variables:
       if (not variable.is_assigned()):
           return False                                                   
    return True

# Method is_consistent (P2)
def is_consistent(csp, variable, value):
    for nConstraints in csp.constraints[variable]:
        # Look through all the CSP variables
        for var in csp.variables:
            # Check if the variable is assigned 
            if (var == nConstraints.var2 and var.is_assigned()):
                if not nConstraints.is_satisfied(value, var.value):
                    return False
    return True

def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.
    """

    # TODO implement this
    # Check if CSP is complete then there is solution
    if (is_complete(csp)):
        return True
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
                retVal = backtrack(csp)

                if (retVal != False):
                    return True
                else:
                    # Rollback any changes in the domains
                    csp.variables.rollback()
    return False

