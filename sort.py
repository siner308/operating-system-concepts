import itertools


class Sort:
    def __init__(self, sort_target, segment_count):
        self.sort_target = sort_target
        self.segment_count = segment_count
        self.separated_targets = []
        len_target = len(self.sort_target)
        len_separated = 0
        while True:
            if len_target - len_separated <= self.segment_count:
                self.separated_targets.append(self.sort_target[len_separated:])
                break
            else:
                self.separated_targets.append(self.sort_target[len_separated:len_separated + self.segment_count])
                len_separated += self.segment_count
        print('separated            : ', self.separated_targets)

    def _sort(self):
        raise NotImplementedError

    def merge_sort(self, items):
        length = len(items)

        if length < 2:
            return items

        left = self.merge_sort(items[0:int(length / 2)])
        right = self.merge_sort(items[int(length / 2):])
        return self.merge(left, right)

    def merge(self, left, right):
        len_left = len(left)
        len_right = len(right)
        i, j = 0, 0
        result = []

        while i + j < len_left + len_right:
            if i == len_left:
                result.append(right[j])
                j += 1
            elif j == len_right:
                result.append(left[i])
                i += 1
            elif left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result

    def merge_sub_lists(self):
        result = []
        i = 0
        length = len(self.separated_targets)
        while length > i:
            result = self.merge(result, self.separated_targets[i])
            i += 1
        return result

    def get_cpu_burst_time(self):
        return sum(list(itertools.chain(*self.separated_targets)))

    def get_total_waiting_time(self):
        current_waiting_time = 0
        len_group_list = len(self.separated_targets)
        result, i, j = 0, 0, 0
        while len_group_list > i:
            len_sub_list = len(self.separated_targets[i])
            j = 0
            while len_sub_list > j:
                current_waiting_time += self.separated_targets[i][j]
                result += current_waiting_time
                j += 1
            i += 1
        return result
