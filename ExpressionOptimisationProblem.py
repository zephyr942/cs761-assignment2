import random


class ExpressionOptimisationProblem(object):

    def __init__(self, numbers: list[int], operations: list[str]):
        """
        Initialise the problem with a list of numbers and a list of operations.

        :param numbers: A list of integers representing the numbers to be used in the expression.
        :param operations: A list of strings representing the operations to be performed.
        """
        self.numbers = numbers
        self.operations = operations

    def select(self, population: list[list[str]]) -> list[str]:
        """
        Select a candidate from the population based on their fitness values.
        If the population is empty, initialise a candidate randomly by shuffling the operations.

        :param population: A list of candidates.
        :return: A selected candidate.
        """
        if not population:
            new_Candidate = self.operations
            random.shuffle(new_Candidate)
            return new_Candidate

        # Calculate fitness for each candidate
        fitness_values = [self.compute(candidate) for candidate in population]

        # Convert fitness to probabilities
        total_fitness = sum(fitness_values)
        probabilities = [fitness / total_fitness for fitness in fitness_values]

        # Select a candidate based on its probabilities
        selected_Candidate = random.choices(population, weights=probabilities, k=1)[0]

        return selected_Candidate

    def cross(self, candidate1: list[str], candidate2: list[str], pc: float) -> list[str]:
        """
        Perform a crossover operation between two candidates with a given probability.
        The cross site should be selected randomly.

        :param candidate1: The first parent candidate.
        :param candidate2: The second parent candidate.
        :param pc: Crossover probability.
        :return: Two new candidates resulting from the crossover operation.
        """
        crossoverProbability = random.random()
        crossoverSite = random.randrange(len(candidate1))


        if crossoverProbability < pc:
            candidate1Copy = candidate1.copy()
            candidate2Copy = candidate2.copy()
            newCandidate1 = candidate1Copy[:crossoverSite] + candidate2Copy[crossoverSite:]
            candidate1Copy = candidate1.copy()
            candidate2Copy = candidate2.copy()
            newCandidate2 = candidate2Copy[:crossoverSite] + candidate1Copy[crossoverSite:]

            candidate1 = newCandidate1
            candidate2 = newCandidate2


        return candidate1,candidate2

    def mutate(self, candidate: list[str], pm: float) -> list[str]:
        """
        Apply mutation to a candidate with a given mutation probability.

        :param candidate: The candidate to be mutated.
        :param pm: Mutation probability.
        :return: The mutated candidate, or the original candidate if no mutation occurs.
        """
        mutationProbability = random.random()
        if mutationProbability < pm:
            mutationSite1 = random.randrange(len(candidate))
            mutationSite2 = mutationSite1
            newCandidate = candidate.copy()
            while mutationSite2 == mutationSite1:
                mutationSite2 = random.randrange(len(candidate))

            exchangeOperation1 = candidate[mutationSite1]
            exchangeOperation2 = candidate[mutationSite2]

            newCandidate[mutationSite1] = exchangeOperation2
            newCandidate[mutationSite2] = exchangeOperation1
            candidate = newCandidate

        return candidate

    def fitness(self, candidate: list[str]) -> float:
        """
        Calculate the fitness of a candidate based on the result of the arithmetic expression.

        :param candidate: A candidate.
        :return: The fitness value.
        """

        return self.compute(candidate)

    def encode(self, string: list[str]) -> list[int]:
        """
        Encode a candidate.

        :param string: A candidate.
        :return: A list of integers representing the encoded candidate.
        """
        encoded_List = self.operations.copy()
        encoded_candidate = []
        i = 0

        while i < len(string):
            numberIndex = 0
            while numberIndex < len(encoded_List):
                if string[i] == encoded_List[numberIndex]:
                    encoded_candidate.append(numberIndex)
                    encoded_List.pop(numberIndex)
                    break
                else:
                    numberIndex += 1
            i += 1

        return encoded_candidate
    def decode(self, indices: list[int]) -> list[str]:
        """
        Decode a indices back into the original candidate.

        :param indices: A list of indegers.
        :return: A list of operations representing the decoded candidate.
        """
        decoded_List = self.operations.copy()
        decoded_candidate = []
        i = 0
        while decoded_List and i < len(indices):

            decoded_candidate.append( decoded_List[indices[i]])
            decoded_List.pop(indices[i])
            i += 1

        return decoded_candidate


    def compute(self, operations: list[str]) -> float:
        """
        Compute the result of the expression given the list of operations

        :param operations: A list of operations.
        :return: The result of the expression.
        """

        expression = str(self.numbers[0])
        for i in range(len(operations)):
            expression += f" {operations[i]} {self.numbers[i + 1]}"

        try:
            result = eval(expression)
        except ZeroDivisionError:
            result = float('inf')

        return round(result, 2)

    def selectBest(self, population: list[list[str]]) -> list[str]:

        if not population:
            new_Candidate = self.operations
            random.shuffle(new_Candidate)
            selected_Candidate = new_Candidate
        else:
            selected_Candidate = population[0]
            for i in range(1, len(population)):
                if self.compute(selected_Candidate) < self.compute(population[i]):
                    selected_Candidate = population[i]

        return selected_Candidate
