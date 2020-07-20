# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2020年07月14日

import multiprocessing as mp
import pandas as pd
import numpy as np
import ray

if mp.cpu_count() > 1:
    num_cpus = mp.cpu_count() - 1
else:
    num_cpus = mp.cpu_count()

df_list = []

@ray.remote
def get_df(i):
    global df_list
    df = pd.DataFrame(np.ones(12).reshape((4,3)) * i,columns=['a','b','c'])
    df_list.append(df)


ray.init(num_cpus=num_cpus,ignore_reinit_error=True)
ray_tasks = [get_df.remote(i) for i in range(5)]
while len(ray_tasks):
    done_tasks, ray_tasks = ray.wait(ray_tasks, 1)

ray.shutdown()

df = pd.concat(df_list)
print(df)


