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

        self.candidate1 = self.problem.operations.copy()
        self.candidate2 = self.problem.operations.copy()

        self.parentGenerationAverage = 0
        self.childrenGenerationAverage = 0
        self.numberOfIteration = 0
        self.numberOfStabilization = 0
        self.bestFitness = []

        self.count = 0

    def terminate(self) -> bool:
        """
        Check if the algorithm should terminate.

        :return: True if the condidtion satisfied, False otherwise.
        """
        isNotStabilized = True

        if len(self.offspring) > 0:

            if self.problem.compute(self.problem.selectBest(self.offspring)) > self.problem.compute(
                self.bestFitness): self.bestFitness = self.problem.selectBest(self.offspring)

            difference = abs(self.problem.compute(self.problem.selectBest(self.population)) - self.problem.compute(self.bestFitness))

            if difference / 100 < 0.0001:
                self.numberOfStabilization += 1

            if self.numberOfStabilization >= 20:
                isNotStabilized = False

        return isNotStabilized

    def run(self):
        """
        Run the Genetic Algorithm until termination condition is met.
        """
        random.shuffle(self.candidate1)
        random.shuffle(self.candidate2)

        while self.terminate():
            self.numberOfIteration += 1

            self.count += 1

            if len(self.offspring) > 0:
                self.population.clear()
                self.population = self.offspring.copy()
                self.offspring.clear()

            i = 0
            while len(self.offspring) < self.population_size:

                self.candidate1 = self.problem.select(self.population)
                self.candidate2 = self.problem.select(self.population)
                newCandidate1, newCandidate2 = self.problem.cross(self.problem.encode(self.candidate1),
                                                                  self.problem.encode(self.candidate2), self.pc)

                newCandidate1 = self.problem.decode(newCandidate1)
                newCandidate2 = self.problem.decode(newCandidate2)

                self.offspring.append(self.problem.mutate(newCandidate1, self.pm))
                self.offspring.append(self.problem.mutate(newCandidate2, self.pm))


            self.offspring = self.offspring + self.population
            offspringTopX = sorted(self.offspring, key=self.problem.compute, reverse=True)[:self.population_size]
            self.offspring = offspringTopX

        return self.problem.compute(self.bestFitness)
