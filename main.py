from input_data import InputData
from population import Population

if __name__ == '__main__':
    MAX_ITER = 500
    data = InputData()
    # print(data.max_capacity)
    # for i in data.items:
    #     print(i)
    p = Population(data)
    p.generate_initial_population()
    for i in range(len(p.chromosomes)):
        print(p.chromosomes[i])
    print()
    print()
    # par = p.choose_pair_of_parents()
    # print(par[0], '\n', par[1])
    p.generate_new_population()
    for i in range(len(p.chromosomes)):
        print(p.chromosomes[i])
