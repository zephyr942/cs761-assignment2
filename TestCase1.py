# test initialisation
from ExpressionOptimisationProblem import ExpressionOptimisationProblem

test_problem = ExpressionOptimisationProblem([1, 2, 3, 4, 5, 6], ["/", "*", "+", "-", "-"])

# the result for the following operations should be 1*2+3-4/5-6=-1.8
print(test_problem.compute(["*", "+", "-", "/", "-"]))

# the result for this crossover operation should be the same as the passed arguments
test_problem.cross(["*", "+", "-", "/", "-"], ["-", "+", "*", "-", "/"], 0)


print(test_problem.mutate(["*", "+", "-", "/", "-"],1))