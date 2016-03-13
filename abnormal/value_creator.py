# -*- coding: utf-8 -*-
__author__ = 'kawakami_note'

import numpy as np
import datetime
import pandas as pd

file_name = 'data/test_data.csv'
start_time = datetime.datetime.strptime('2016-03-10 10:00:00', '%Y-%m-%d %H:%M:%S')
data_size = 100000

cpu_mean, cpu_sd, cpu_mean_abnormal, cpu_sd_abnormal = 50, 10, 80, 1
free_memory_mean, free_memory_sd, free_memory_mean_abnormal, free_memory_sd_abnormal = 2000, 100, 500, 10
network_usage_mean, network_usage_sd, network_usage_mean_abnormal, network_usage_sd_abnormal = 40, 5, 90, 1

cpu_normal = np.random.normal(cpu_mean, cpu_sd, data_size)
free_memory_normal = np.random.normal(free_memory_mean, free_memory_sd, data_size)
network_usage_normal = np.random.normal(network_usage_mean, network_usage_sd, data_size)

cpu_abnormal = np.random.normal(cpu_mean_abnormal, cpu_sd_abnormal, data_size)
free_memory_abnormal = np.random.normal(free_memory_mean_abnormal, free_memory_sd_abnormal, data_size)
network_usage_abnormal = np.random.normal(network_usage_mean_abnormal, network_usage_sd_abnormal, data_size)

cpu_rnd = np.random.random_integers(0, 100, data_size / 100)
free_memory_rnd = np.random.random_integers(0, 100, data_size / 100)
network_usage_rnd = np.random.random_integers(0, 100, data_size / 100)

times = []
test_cpu = np.zeros(data_size, dtype=np.float32)
test_free_memory = np.zeros(data_size, dtype=np.float32)
test_network_usage = np.zeros(data_size, dtype=np.float32)
for index in xrange(data_size):
    start_time += datetime.timedelta(seconds = 1)
    times.append(start_time)
    if cpu_rnd[index / 100] == 0:
        test_cpu[index] = (cpu_abnormal[index])
    else:
        test_cpu[index] = (cpu_normal[index])
    if free_memory_rnd[index / 100] == 0:
        test_free_memory[index] = (free_memory_abnormal[index])
    else:
        test_free_memory[index] = (free_memory_normal[index])
    if network_usage_rnd[index / 100] == 0:
        test_network_usage[index] = (network_usage_abnormal[index])
    else:
        test_network_usage[index] = (network_usage_normal[index])

a = np.random.normal(100, 1)
b = np.random.normal(2, 1)
test_response = (test_cpu * a - b * test_free_memory) / 10000 + 1.0

pd.DataFrame({"time":times, "cpu":test_cpu, "memory":test_free_memory, "network":test_network_usage, "response":test_response}).to_csv(file_name)