# test initialisation

from ExpressionOptimisationProblem import ExpressionOptimisationProblem
from GeneticAlgorithm import GeneticAlgorithm

# test_problem = ExpressionOptimisationProblem([1, 2, 3, 4, 5, 6], ["/", "*", "+", "-", "-"])
#
# # the result for the following operations should be 1*2+3-4/5-6=-1.8
# print(test_problem.compute(["*", "+", "-", "/", "-"]))
#
# # the result for this crossover operation should be the same as the passed arguments
# test_problem.cross(["*", "+", "-", "/", "-"], ["-", "+", "*", "-", "/"], 0)

# i=0
# while i< 100:
#     # print(test_problem.mutate(["*", "+", "-", "/", "-"],1))
#     print(test_problem.mutate(["*", "*", "-"], 1))
#     i+=1


# population = [["*", "+", "-", "/", "-"],["-", "-", "*", "*", "*"],["-", "+", "*", "+", "*"],["-", "+", "*", "*", "*"],["+", "+", "*", "*", "/"],["+", "+", "*", "*", "/"]]
# print(test_problem.select(population))

# setting1 = {'numbers': [2, 17, 3, 4, 6, 5, 9, 2, 24],
#             'operations': ["/", "/", "*", "*", "+", "+", "-", "-"],
#             'population_size': 4,
#             'pc': 0.9,
#             'pm': 0.9}
#
test_problem = ExpressionOptimisationProblem([2, 17, 3, 4, 6, 5, 9, 2, 24], ["/", "/", "*", "*", "+", "+", "-", "-"])
# test_problem = ExpressionOptimisationProblem([1, 2, 3, 4, 5, 6], ["*", "+", "-", "/", "*"])
# # test_problem = ExpressionOptimisationProblem([1, 2, 3, 4, 5, 6], ["*", "*", "*", "/", "*"])
# # print(test_problem.encode(['-', '/', '*', '*', '+']))
# # print(test_problem.decode([0,2,0,1,0]))
test_GA = GeneticAlgorithm(test_problem, 100, 0.9, 0.9)
GeneticAlgorithm.run(test_GA)

