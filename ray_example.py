# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2020年07月14日

import multiprocessing as mp
import pandas as pd
import numpy as np
import ray

if mp.cpu_count() > 2:
    num_cpus = mp.cpu_count() - 1
else:
    num_cpus = mp.cpu_count()


@ray.remote
def get_df(i):
    df = pd.DataFrame(np.ones(12).reshape((4, 3)) * i, columns=['a', 'b', 'c'])
    return df


ray.init(num_cpus=num_cpus, ignore_reinit_error=True)
ray_tasks = [get_df.remote(i) for i in range(5)]
object_ids = ray_tasks

while len(ray_tasks):
    done_tasks, ray_tasks = ray.wait(ray_tasks, 1)
df_list = []
for object_id in object_ids:
    df_id = ray.get(object_id)
    df_list.append(df_id)
ray.shutdown()
df = pd.concat(df_list)
print(df)
