# test initialisation
import time

from ExpressionOptimisationProblem import ExpressionOptimisationProblem
from GeneticAlgorithm import GeneticAlgorithm

# test_problem = ExpressionOptimisationProblem([1, 2, 3, 4, 5, 6], ["/", "*", "+", "-", "-"])
#
# # the result for the following operations should be 1*2+3-4/5-6=-1.8
# print(test_problem.compute(["*", "+", "-", "/", "-"]))
#
# # the result for this crossover operation should be the same as the passed arguments
# test_problem.cross(["*", "+", "-", "/", "-"], ["-", "+", "*", "-", "/"], 0)

# population = [["*", "+", "-", "/", "-"],["-", "-", "*", "*", "*"],["-", "+", "*", "+", "*"],["-", "+", "*", "*", "*"],["+", "+", "*", "*", "/"],["+", "+", "*", "*", "/"]]
# print(test_problem.select(population))

# test_problem = ExpressionOptimisationProblem([1, 2, 3, 4, 5, 6], ["*", "+", "-", "/", "*"])
# # test_problem = ExpressionOptimisationProblem([1, 2, 3, 4, 5, 6], ["*", "*", "*", "/", "*"])
# # print(test_problem.encode(['-', '/', '*', '*', '+']))
# # print(test_problem.decode([0,2,0,1,0]))


setting1 = {'numbers': [2, 17, 3, 4, 6, 5, 9, 2, 24],
            'operations': ["/", "/", "*", "*", "+", "+", "-", "-"],
            'population_size': 4,
            'pc': 0.9,
            'pm': 0.9}

setting2 = {'numbers': [2, 17, 3, 4, 6, 5, 9, 2, 24],
            'operations': ["/", "/", "*", "*", "+", "+", "-", "-"],
            'population_size': 50,
            'pc': 0.9,
            'pm': 0.9}

setting3 = {'numbers': [2, 17, 3, 4, 6, 5, 9, 2, 24],
            'operations': ["/", "/", "*", "*", "+", "+", "-", "-"],
            'population_size': 100,
            'pc': 0.9,
            'pm': 0.9}

setting4 = {'numbers': [2, 17, 3, 4, 6, 5, 9, 2, 24],
            'operations': ["/", "/", "*", "*", "+", "+", "-", "-"],
            'population_size': 300,
            'pc': 0.9,
            'pm': 0.9}
setting5 = {'numbers': [2, 17, 3, 4, 6, 5, 9, 2, 24],
            'operations': ["/", "/", "*", "*", "+", "+", "-", "-"],
            'population_size': 200,
            'pc': 0.9,
            'pm': 0.5}

# 使用字典解包来初始化问题和算法
settings = setting5 # 可以选择其他设置，比如 setting2, setting3, setting4

# 传递字典中相关的值给 ExpressionOptimisationProblem 和 GeneticAlgorithm
test_problem = ExpressionOptimisationProblem(settings['numbers'], settings['operations'])
test_GA = GeneticAlgorithm(test_problem, settings['population_size'], settings['pc'], settings['pm'])

# 运行算法
result = test_GA.run()
# print(result)


# 定义一个函数来计算平均值
def calculate_average(func, iterations=100):
    total = 0
    for _ in range(iterations):

        total += func()
    average = total / iterations
    return average


start_time = time.time()
average_result = calculate_average(test_GA.run, 100)
print(f"The average result after 100 runs is: {average_result}")
end_time = time.time()
total_time = end_time - start_time
print(f"Execution time for the code line: {total_time} seconds")
