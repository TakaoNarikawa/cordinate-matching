import torch
import os
import tqdm
import math
import numpy as np
import time

DIM = 250
VMAX = 256

MATCHING_COUNT = 80
device = 'cuda'
SAVE_TENSOR_DIR = 'source'

N = 100_000_000
SUB_N = 1_000_000

def create_save_tensor_path(i):
    return os.path.join(SAVE_TENSOR_DIR, f'run4-source{i}.pt')

def initialize():
    os.makedirs(SAVE_TENSOR_DIR, exist_ok=True)
    for i, sn in enumerate(tqdm.tqdm(split_num(N, SUB_N))):
        source = torch.randint(high=VMAX, size=(sn, DIM, 2), dtype=torch.int16)
        torch.save(source, create_save_tensor_path(i))
    print("initialize completed!")

def split_num(total, part_size):
    group_num = math.ceil(total / part_size)
    parts = np.full(group_num, part_size)
    parts[-1] = total - part_size * (group_num - 1)
    return parts.tolist()

def timer(fn):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('{0} took {1:.8f}s to execute'.format(fn.__name__, execution_time))
        return execution_time
    
    return inner

@timer
def search(variable):
    result_index = []
    load_durations = []
    calc_durations = []
    iter_durations = []
    for i in tqdm.tqdm(range(len(split_num(N, SUB_N)))):
        t1 = time.perf_counter()
        source = torch.load(create_save_tensor_path(i), map_location=torch.device(device))
        load_durations.append(time.perf_counter() - t1)

        t2 = time.perf_counter()
        dist = torch.abs((source - variable)).sum(dim=2)
        condition = (dist <= 2).to(torch.uint8).sum(dim=1) >= MATCHING_COUNT
        calc_durations.append(time.perf_counter() - t2)


        start_index = SUB_N * i

        result_index += (condition.nonzero() + start_index).tolist()
        iter_durations.append(time.perf_counter() - t1)

    print(f'結果: {N} -> {len(result_index)} ({len(result_index) / N:.3f})')
    load_durations = torch.tensor(load_durations)
    calc_durations = torch.tensor(calc_durations)
    iter_durations = torch.tensor(iter_durations)
    print(f'[読み込み時間] 平均：{load_durations.mean()}, 標準偏差：{load_durations.std()}')
    print(f'[計算時間] 平均：{calc_durations.mean()}, 標準偏差：{calc_durations.std()}')
    print(f'[イテレーション時間] 平均：{iter_durations.mean()}, 標準偏差：{iter_durations.std()}')



def main():
    variable = torch.randint(high=VMAX, size=(DIM, 2),    dtype=torch.int16).to(device)
    search(variable)


if __name__ == '__main__':
    if not all([os.path.exists(create_save_tensor_path(i)) for i, _ in enumerate(split_num(N, SUB_N))]):
        initialize()
    main()