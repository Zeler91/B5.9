import time

class StopWatch:
    def __init__(self, func, NUM_RUNS = 5):
        self.func = func
        self.NUM_RUNS = NUM_RUNS
        self.avg_time = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        for _ in range(self.NUM_RUNS):
            t0 = time.time()
            self.func()
            t1 = time.time()
            self.avg_time += (t1 - t0)
        self.avg_time /= self.NUM_RUNS
        print("Выполнение заняло %.5f секунд" % self.avg_time)
        

def Fiba(i = 1, j = 2, max = 1000000000):
	print(i)
	print(j)
	k = 0
	while(k < max):
		k = i + j
		i = j
		j = k	
		if k < max:
			print(k)

with StopWatch(Fiba, NUM_RUNS = 10) as fiba_time:
    fiba_time
