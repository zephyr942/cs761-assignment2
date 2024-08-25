import random


class GeneticAlgorithm(object):
    def __init__(self, problem, population_size: int, pc: float, pm: float):
        """
        Initialise the Genetic Algorithm.

        :param problem: An instance of the problem to solve, which should provide methods
                        for selection, crossover, mutation, and fitness evaluation.
        :param population_size: The number of individuals in the population.
        :param pc: Crossover probability.
        :param pm: Mutation probability.
        """
        self.problem = problem
        self.population_size = population_size
        self.pc = pc  # Crossover probability
        self.pm = pm  # Mutation probability
        self.population = []  # Current population of candidates
        self.offspring = []  # Offspring generated during evolution
        self.count = 0

    def terminate(self) -> bool:
        """
        Check if the algorithm should terminate.

        :return: True if the condidtion satisfied, False otherwise.
        """
        isNotStabilized = True

        if len(self.offspring) > 0:
            if ((self.problem.compute(self.offspring[0]) - self.problem.compute(self.offspring[1]))/100) < 0.1:
                print  ("terminate condition satisfied", (self.problem.compute(self.offspring[0]) - self.problem.compute(self.offspring[1]))/100)
                isNotStabilized = False

        return isNotStabilized

    def run(self):
        """
        Run the Genetic Algorithm until termination condition is met.
        """
        numbers = self.problem.numbers
        operations = self.problem.operations
        candidate1 = self.problem.operations.copy()
        candidate2 = self.problem.operations.copy()
        random.shuffle(candidate1)
        random.shuffle(candidate2)

        while self.terminate():
            self.count += 1

            if len(self.offspring) > 0:
                candidate1 = self.offspring[0]
                candidate2 = self.offspring[1]
                self.population.clear()
                self.offspring.clear()

            i = 0
            while len(self.population) < self.population_size:
                newCandidate1, newCandidate2 = self.problem.cross(self.problem.encode(candidate1),
                                                                  self.problem.encode(candidate2), self.pc)
                newCandidate1 = self.problem.decode(newCandidate1)
                newCandidate2 = self.problem.decode(newCandidate2)
                self.population.append(self.problem.mutate(newCandidate1, self.pm))
                self.population.append(self.problem.mutate(newCandidate2, self.pm))
                print(self.population)

                for i in range(len(self.population)):
                    print(self.population[i], self.problem.compute(self.population[i]))

            newCandidate1 = self.problem.select(self.population)
            self.population.remove(newCandidate1)
            newCandidate2 = self.problem.select(self.population)
            self.population.remove(newCandidate2)
            self.offspring.append(newCandidate1)
            self.offspring.append(newCandidate2)
            print(self.offspring)
