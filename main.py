from fcfs import FCFS
from sjf import SJF

SORT_TARGET = [
    4, 10, 15, 6, 13, 20, 8, 11, 9, 14, 0, 5, 19, 1, 2, 7, 16
]


def run(sort_target, segment_count):
    print('========SJF========')
    print('input                : ', sort_target)
    sjf = SJF(sort_target, segment_count)
    print('result               : ', sjf.merge_sub_lists())
    print('cpu burst time       : ', sjf.get_cpu_burst_time())
    print('average waiting time : ', sjf.get_total_waiting_time())

    print('========FCFS=======')
    print('input                : ', sort_target)
    fcfs = FCFS(sort_target, segment_count)
    print('result               : ', fcfs.merge_sub_lists())
    print('cpu burst time       : ', fcfs.get_cpu_burst_time())
    print('average waiting time : ', fcfs.get_total_waiting_time())


if __name__ == '__main__':
    run(SORT_TARGET, 7)
