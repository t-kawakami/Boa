# -*- coding: utf-8 -*-
__author__ = 'kawakami_note'

from numpy import random
import datetime
import pandas as pd

file_name = 'data/test_data.csv'
start_time = datetime.datetime.strptime('2016-03-10 10:00:00', '%Y-%m-%d %H:%M:%S')
data_size = 10000

cpu_mean, cpu_sd, cpu_mean_abnormal, cpu_sd_abnormal = 50, 20, 80, 5
free_memory_mean, free_memory_sd, free_memory_mean_abnormal, free_memory_sd_abnormal = 2000, 500, 500, 20
network_usage_mean, network_usage_sd, network_usage_mean_abnormal, network_usage_sd_abnormal = 60, 15, 90, 5

test_cpu = random.normal(cpu_mean, cpu_sd, data_size)
test_free_memory = random.normal(free_memory_mean, free_memory_sd, data_size)
# print(test_cpu)
# print(test_free_memory)

a = random.normal(100, 1)
b = random.normal(2, 1)
test_response = (test_cpu * a - b * test_free_memory) / 10000 + 1.0
# print(a, b)
# print(test_response)

test_network_usage = random.normal(network_usage_mean, network_usage_sd, data_size)
# print(test_network_usage)


test_cpu_abnormal = random.normal(cpu_mean_abnormal, cpu_sd_abnormal, data_size)
test_free_memory_abnormal = random.normal(free_memory_mean_abnormal, free_memory_sd_abnormal, data_size)
# print(test_cpu_abnormal)
# print(test_free_memory_abnormal)

test_response_abnormal = (test_cpu_abnormal * a - b * test_free_memory_abnormal) / 10000 + 1.0
# print(a, b)
# print(test_response_abnormal)

test_network_usage_abnormal = random.normal(network_usage_mean_abnormal, network_usage_sd_abnormal, data_size)
# print(test_network_usage_abnormal)

times = []
for data_index in xrange(data_size):
    start_time += datetime.timedelta(seconds = 1)
    times.append(start_time)

pd.DataFrame({"time":times, "cpu":test_cpu, "memory":test_free_memory, "network":test_network_usage, "response":test_response}).to_csv(file_name)