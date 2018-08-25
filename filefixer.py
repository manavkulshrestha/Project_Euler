import os

for i in range(1, 100):
	os.system(f'mv problem_{i}.py problem_{"0" if i < 10 else ""}0{i}.py')