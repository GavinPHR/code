# Employee Importance

"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        lookup = {e.id:i for i, e in enumerate(employees)}
        ans = 0
        rest = [id]
        while rest:
            current = employees[lookup[rest.pop()]]
            ans += current.importance
            rest.extend(x for x in current.subordinates)
        return ans