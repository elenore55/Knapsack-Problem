from input_data import InputData
from population import Population
from time import time
from config import MAX_ITER, MAX_FITNESS_COUNT

if __name__ == '__main__':
    data = InputData()
    p = Population(data)
    p.generate_initial_population()
    max_fitness_list = []
    loop_broken = False
    max_count = max_fitness = 0
    start = time()
    for i in range(MAX_ITER):
        p.generate_new_population()
        max_fitness_new = p.get_max_fitness()
        max_fitness_list.append(max_fitness_new)
        if max_fitness_new == max_fitness:
            max_count += 1
            if max_count > MAX_FITNESS_COUNT:
                loop_broken = True
                break
        else:
            max_count = 0
            max_fitness = max_fitness_new

    print('END: ', p.get_end_result())
    print(loop_broken)
    print(max_fitness_list)
    print('TIME: {0:.4f}s'.format(time() - start))
