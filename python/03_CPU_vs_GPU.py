import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import timeit
import tensorflow as tf

def run():
    n = 1000
    # CPU 運算矩陣
    with tf.device('/CPU:0'):
        cpu_a = tf.random.normal([n, n])
        cpu_b = tf.random.normal([n, n])
        print(cpu_a.device, cpu_b.device)

    # GPU 運算矩陣
    with tf.device('/GPU:0'):
        gpu_a = tf.random.normal([n, n])
        gpu_b = tf.random.normal([n, n])
        print(gpu_a.device, gpu_b.device)

    def cpu_run():
        with tf.device('/CPU:0'):
            c = tf.matmul(cpu_a, cpu_b)
        return c

    def gpu_run():
        with tf.device('/GPU:0'):
            c = tf.matmul(gpu_a, gpu_b)
        return c

    number = 1000

    print("First Run:")
    cpu_time = timeit.timeit(cpu_run, number=number)
    gpu_time = timeit.timeit(gpu_run, number=number)
    print("CPU Run Time: ", cpu_time)
    print("GPU Run Time: ", gpu_time)

    print("2nd Run: ")
    cpu_time = timeit.timeit(cpu_run, number=number)
    gpu_time = timeit.timeit(gpu_run, number=number)
    print("CPU Run Time: ", cpu_time)
    print("GPU Run Time: ", gpu_time)

run()
