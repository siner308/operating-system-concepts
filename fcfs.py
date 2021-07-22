from sort import Sort


class FCFS(Sort):
    def __init__(self, sort_target, segment_count):
        super().__init__(sort_target, segment_count)
        self._sort()

    def _sort(self):
        # sort each sub-list
        self.separated_targets = list(map(self.merge_sort, self.separated_targets))
        print('sort each sub-list   : ', self.separated_targets)
