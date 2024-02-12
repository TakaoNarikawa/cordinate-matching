import torch
import utils

DIM = 250
VMAX = 8
N = 1000000
MATCHING_COUNT = 50


def main():
    source   = torch.randint(high=VMAX, size=(N, DIM, 2), dtype=torch.int16)
    variable = torch.randint(high=VMAX, size=(DIM, 2),    dtype=torch.int16)

    print("initialize completed!")


    @utils.timer
    def run():
        dist = torch.sqrt(((source - variable) ** 2)).sum(dim=2)
        condition = (dist <= 2).to(torch.uint8).sum(dim=1) >= MATCHING_COUNT
        result_count = len(condition[condition])
        print(f'結果: {N} -> {result_count} ({result_count / N:.3f})')


    # warn up
    run()
    
    elapsed_times = torch.tensor([run() for _ in range(30)])
    print(f'平均：{elapsed_times.mean()}, 標準偏差：{elapsed_times.std()}')


if __name__ == '__main__':
    main()