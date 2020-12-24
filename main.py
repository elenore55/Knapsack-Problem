from input_data import InputData

if __name__ == '__main__':
    data = InputData()
    print(data.max_capacity)
    for i in data.items:
        print(i)
