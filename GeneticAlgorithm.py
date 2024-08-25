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

    def terminate(self) -> bool:
        """
        Check if the algorithm should terminate.

        :return: True if the condidtion satisfied, False otherwise.
        """
        return True

    def run(self):
        """
        Run the Genetic Algorithm until termination condition is met.
        """

        while self.terminate():
            numbers = self.problem.numbers
            operations = self.problem.operations
            i=0
            while len(self.population) < self.population_size:



                return

            return
