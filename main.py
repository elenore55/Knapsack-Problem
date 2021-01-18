from input_data import InputData
from population import Population
from time import time
import config as cfg
import matplotlib.pyplot as plt
import json


def plot_result_history(best_results):
    y = best_results
    x = [c for c in range(1, len(best_results) + 1)]
    plt.plot(x, y, 'green', markersize=5)
    plt.xlabel('Generation')
    plt.ylabel('Best fitness')
    plt.show()


def save_result(fitness, weight, t):
    with open(cfg.RESULTS_PATH, 'r+') as file:
        dt = json.load(file)
        dt.append({'max_iter': cfg.MAX_ITER,
                   'max_fitness_count': cfg.MAX_FITNESS_COUNT,
                   'mutation_rate': cfg.RATE_OF_MUTATION,
                   'elitism': cfg.ELITISM,
                   'fitness': fitness,
                   'population size': cfg.DEFAULT_POPULATION_SIZE,
                   'overall_weight': weight,
                   'time': round(t, 3)
                   })
        file.seek(0)
        json.dump(dt, file, indent=2)


if __name__ == '__main__':
    data = InputData()
    p = Population(data)
    p.generate_initial_population()
    max_fitness_list = []
    loop_broken = False
    max_count = max_fitness = 0
    start = time()
    for i in range(cfg.MAX_ITER):
        p.generate_new_population()
        max_fitness_new = p.get_max_fitness()
        max_fitness_list.append(max_fitness_new)
        if max_fitness_new == max_fitness:
            max_count += 1
            if max_count > cfg.MAX_FITNESS_COUNT:
                loop_broken = True
                break
        else:
            max_count = 0
            max_fitness = max_fitness_new
    overall_time = time() - start
    print('RESULT >> ')
    result = p.get_end_result()
    print(result)
    if loop_broken:
        print('Algorithm converged')
    else:
        print('Max number of iterations reached')
    plot_result_history(max_fitness_list)
    print('TIME: {0:.4f}s'.format(overall_time))
    save_result(result.fitness, result.calculate_total_weight(), overall_time)
