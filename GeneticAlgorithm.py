import random
from statistics import mean


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

            if self.problem.compute(self.offspring[0]) > self.problem.compute(self.bestFitness): self.bestFitness = self.offspring[0]
            print("(self.problem.compute(self.offspring[0])", self.offspring[0],self.problem.compute(self.offspring[0]))
            print("(self.problem.compute(bestFitness) ", self.bestFitness,self.problem.compute(self.bestFitness))

            # compare with children
            # difference = abs(self.problem.compute(self.offspring[0]) - self.problem.compute(self.offspring[1]))
            # compare with parent
            # difference = abs(self.problem.compute(self.offspring[0]) - self.problem.compute(self.candidate1))
            # compare to the best fitness
            difference = abs(self.problem.compute(self.offspring[0]) - self.problem.compute(self.bestFitness))

            if difference / 100 < 0.0000001:
                # print("(self.problem.compute(self.offspring[0])", self.problem.compute(self.offspring[0]))
                # print("(self.problem.compute(self.candidate1) ", self.problem.compute(self.candidate1))
                # print("terminate condition satisfied",
                #       float((self.problem.compute(self.offspring[0]) - (self.problem.compute(self.candidate1))) / 100))
                self.numberOfStabilization += 1
                print("Number of Stabilization:", self.numberOfStabilization)

            if self.numberOfStabilization >= 20:
                isNotStabilized = False
                print("Final choice:", self.problem.compute(self.offspring[0]) if self.problem.compute(
                    self.offspring[0]) - self.problem.compute(self.offspring[1]) >= 0 else self.problem.compute(
                    self.offspring[1]))
                print("Final Number of Iteration:", self.numberOfIteration)
        return isNotStabilized

    def run(self):
        """
        Run the Genetic Algorithm until termination condition is met.
        """
        numbers = self.problem.numbers
        operations = self.problem.operations
        # candidate1 = self.problem.operations.copy()
        # candidate2 = self.problem.operations.copy()
        random.shuffle(self.candidate1)
        random.shuffle(self.candidate2)

        while self.terminate():
            self.numberOfIteration += 1
            print("Number of Iteration:", self.numberOfIteration)
            self.count += 1

            if len(self.offspring) > 0:
                self.candidate1 = self.offspring[0]
                self.candidate2 = self.offspring[1]
                self.population.clear()
                self.offspring.clear()

            i = 0
            while len(self.population) < self.population_size:

                newCandidate1, newCandidate2 = self.problem.cross(self.problem.encode(self.candidate1),
                                                                  self.problem.encode(self.candidate2), self.pc)

                newCandidate1 = self.problem.decode(newCandidate1)
                newCandidate2 = self.problem.decode(newCandidate2)

                for i in range(len(self.population)):
                    ''''
                    print("--before mutation ---print all polulation and fitness:", self.population[i],self.problem.compute(self.population[i]))
                    '''''
                self.population.append(self.problem.mutate(newCandidate1, self.pm))
                self.population.append(self.problem.mutate(newCandidate2, self.pm))

                for i in range(len(self.population)):
                    ''''
                    print("--after mutation --- print all polulation and fitness:", self.population[i],self.problem.compute(self.population[i]))
                    '''''
            childrenFitnessList = []
            for candidate in (self.population):
                childrenFitnessList.append(self.problem.compute(candidate))

            newCandidate1 = self.problem.select(self.population)
            self.population.remove(newCandidate1)
            newCandidate2 = self.problem.select(self.population)
            self.population.remove(newCandidate2)
            self.offspring.append(newCandidate1)
            self.offspring.append(newCandidate2)
            # print("--final output candidate1", self.candidate1, self.problem.compute(self.candidate1))
            # print("--final output candidate2", self.candidate2, self.problem.compute(self.candidate2))
            # print("--final output offspring1", self.offspring[0], self.problem.compute(self.offspring[0]))
            # print("--final output offspring2", self.offspring[1], self.problem.compute(self.offspring[1]))
