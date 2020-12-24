from input_data import InputData
from population import Population

if __name__ == '__main__':
    MAX_ITER = 1000
    MAX_FITNESS_COUNT = 200
    data = InputData()

    p = Population(data)
    p.generate_initial_population()
    max_fitness_list = []

    broken = False
    max_count = 0
    max_fitness = 0
    for i in range(MAX_ITER):
        p.generate_new_population()
        max_fitness_new = p.get_max_fitness()
        max_fitness_list.append(max_fitness_new)
        if max_fitness_new == max_fitness:
            max_count += 1
            if max_count > MAX_FITNESS_COUNT:
                broken = True
                break
        else:
            max_count = 0
            max_fitness = max_fitness_new

    print('END: ', p.get_end_result())
    print(broken)
    print(max_fitness_list)
