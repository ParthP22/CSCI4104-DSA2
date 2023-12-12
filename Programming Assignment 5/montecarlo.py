# You will need some import statements up here.
import math
import random
from multiprocessing import Pool
from timeit import timeit

# Programming Assignment 5
#
# Student Name: Parth Patel
#
# Do not delete this comment containing the assignment instructions.
#
# What to submit:
# (a) This montecarlo.py file
#     As always, you are not allowed to change the names of
#     py files I've given you, functions, parameters, etc.
# (b) A text file with the output from when you run your
#     generate_table and time functions.  One text file with
#     both output tables is fine.
#
# 1) Implement the function pi_monte_carlo to estimate
#    the value of pi using Monte Carlo simulation.
#    See the details of how to do this are in Blackboard,
#    which shows pseudocode of the algorithm you are to implement.
#    You will need to import the random module.  Take a
#    look at the documentation of the random module to find
#    the function that generates random floating-point
#    values in the interval [0.0, 1.0).
#
#    IMPORTANT NOTE: Several different Monte Carlo algorithms
#    exist for estimating pi. One of which is described by the
#    pseudocode I have in Blackboard. It happens to be one of
#    the better ones that exist that I have modified slightly
#    to further improve numerical stability, but it is also not
#    the one you would likely find if you attempted to Google
#    for this (even without my modifications). If you implement
#    a different Monte Carlo algorithm for estimating pi other
#    than the one specified in the assignment, then you will
#    lose all points related to this part of the assignment.
#
# 2) Implement a parallel version of this in the function
#    pi_parallel_monte_carlo. The second parameter, processes,
#    indicates how many processes to use. You should use
#    a Pool (see the parallel examples for the import that you
#    will need). The easiest ways to do this is to either use
#    the apply_async method of the Pool class or the map method
#    of the Pool class.
#
#    Hint 1: If you use apply_async, you'll start by determining
#           how many samples per process, which you can compute
#           from n and p.  You would then call apply_async p times
#           to have p processes call pi_monte_carlo (the sequential
#           version) using the number of samples necessary to spread
#           the n samples across p processes. Once you call apply_async
#           p times (make sure you store the Future objects that those
#           calls return in a list), you'll call get() on each of those
#           Future objects, and average the p results.
#
#    Hint 2: If you want to use Pool.map, then start the same
#           way by determining how many samples to use for each
#           process. Create your Pool with p processes.  Generate
#           a list of length p where the elements are the numbers of
#           samples for each process, which should sum to n.
#           Call pool.map (assuming your Pool is named pool) to map
#           your sequential pi_monte_carlo to that list.
#           When pool.map returns, compute the average of the p
#           results and return it.
#
#    Hint 3: Make sure you use a with block for your Pool (see examples
#           in video and corresponding sourcecode) to ensure the Pool
#           is closed properly.
#
# 3) Implement the generate_table function as specified below.
#
# 4) Implement the time function as specified below.
#
# 5) Run your generate_table and time functions from the shell
#    and save the output to a textfile.
#
# 6) Are the results what you expected to see? If so, why?
#    If not, why do you think your results are different
#    then you expected? You can just answer in a comment.
#
# 7) Submit the .py file and the textfile with the output.

def pi_monte_carlo(n) :
    """Computes and returns an estimation of pi
    using Monte Carlo simulation.

    Keyword arguments:
    n - The number of samples.
    """

    # This is the pseudocode based off of what was posted on Blackboard
    m = math.sqrt(1 - math.pow(random.random(),2))
    for k in range(1,n):
        m = m + (math.sqrt(1 - math.pow(random.random(),2)) - m)/k
    return 4*m

    # return None # This statement is here as a placeholder for your code.

def pi_parallel_monte_carlo(n, p=4) :
    """Computes and returns an estimation of pi
    using a parallel Monte Carlo simulation.

    Keyword arguments:
    n - The total number of samples.
    p - The number of processes to use.
    """
    # I divide n by p to get the number of samples per process.
    # I do integer division to ensure that it is still an integer
    # so that I can pass it in as a parameter later.
    samples_per_process = n // p
    samples_per_process_list = [samples_per_process for x in range(p)]

    # with-block for the pool where I do my parallel approximations
    with Pool(p) as pool:
        process_approximations = pool.map(pi_monte_carlo, samples_per_process_list)

    # I average all the approximations done separately by the processes
    pi_approx = 0.0
    for i in process_approximations:
        pi_approx += i

    # I return the final approximation of pi
    return pi_approx / p

    # return None # This statement is here as a placeholder for your code.

def generate_table() :
    """This function should generate and print a table
    of results to demonstrate that both versions
    compute increasingly accurate estimations of pi
    as n is increased.  It should use the following
    values of n = {12, 24, 48, ..., 50331648}. That is,
    the first value of n is 12, and then each subsequent
    n is 2 times the previous.  The reason for starting at 12
    is so that n is always divisible by 1, 2, 3, and 4.
    The first column should be n, the second column should
    be the result of calling pi_monte_carlo(n), and you
    should then have 4 more columns for the parallel
    version, but with 1, 2, 3, and 4 processes in the Pool."""

    # This is the title of this table
    print("Approximations of Sequential and Parallel Monte Carlo Algorithms")

    # These are the headers for the table
    headers = ["n", "sequential", "p = 1", "p = 2", "p = 3", "p = 4"]
    print(f"{headers[0]:<{10}}| "
          f"{headers[1]:<{14}}| "
          f"{headers[2]:<{14}}| "
          f"{headers[3]:<{14}}| "
          f"{headers[4]:<{14}}| "
          f"{headers[5]:<{14}}")

    # This will add a divider/line between the header and the values in the table
    for i in range(90):
        if i == 10 or i == 26 or i == 42 or i == 58 or i == 74:
            print("|",end="")
            continue
        print("-",end="")
    print("")

    # So, I figured out that 12 * 2^0 = 12, which is the first sample.
    # Then, I figured out that 12 * 2^(22) = 50331648, which is the last sample.
    # This is why my for-loop starts at 0 and goes to 22 (23 is exclusive).
    # Here, I calculate and print the approximations of pi for the sequential version,
    # as well as for the parallel versions for 1,2,3, and 4 processes.
    for i in range(23):
        sequential_approx = pi_monte_carlo(math.floor(12*math.pow(2,i)))
        parallel_approx_1 = pi_parallel_monte_carlo(math.floor(12 * math.pow(2, i)),1)
        parallel_approx_2 = pi_parallel_monte_carlo(math.floor(12 * math.pow(2, i)),2)
        parallel_approx_3 = pi_parallel_monte_carlo(math.floor(12 * math.pow(2, i)),3)
        parallel_approx_4 = pi_parallel_monte_carlo(math.floor(12 * math.pow(2, i)),4)

        print(f"{math.floor(12*math.pow(2,i)) :< {10}}| "
              f"{sequential_approx :< {14}.8f}| "
              f"{parallel_approx_1 :< {14}.8f}| "
              f"{parallel_approx_2 :< {14}.8f}| "
              f"{parallel_approx_3 :< {14}.8f}| "
              f"{parallel_approx_4 :< {14}.8f}")


    pass # This statement is here as a placeholder for your code.

def time() :
    """This function should generate a table of runtimes
    using timeit.  Use the same columns and values of
    n as in the generate_table() function.  When you use timeit
    for this, pass number=1 (because the high n values will be slow)."""

    # This is the title of this table
    print("Runtimes of Sequential and Parallel Monte Carlo Algorithms")

    # These are the headers for the table
    headers = ["n", "sequential", "p = 1", "p = 2", "p = 3", "p = 4"]
    print(f"{headers[0]:<{10}}| "
          f"{headers[1]:<{14}}| "
          f"{headers[2]:<{14}}| "
          f"{headers[3]:<{14}}| "
          f"{headers[4]:<{14}}| "
          f"{headers[5]:<{14}}")

    # This will add a divider/line between the header and the values in the table
    for i in range(90):
        if i == 10 or i == 26 or i == 42 or i == 58 or i == 74:
            print("|", end="")
            continue
        print("-", end="")
    print("")

    # So, I figured out that 12 * 2^0 = 12, which is the first sample.
    # Then, I figured out that 12 * 2^(22) = 50331648, which is the last sample.
    # This is why my for-loop starts at 0 and goes to 22 (23 is exclusive).
    # Here, I calculate the approximations of pi for the sequential version,
    # as well as for the parallel versions for 1,2,3, and 4 processes.
    # I do these calculations inside the timeit method to get the runtime, and
    # once I'm done, I print them all out.
    for i in range(23):
        sequential_approx = timeit(lambda: pi_monte_carlo(math.floor(12*math.pow(2,i))),number=1)
        parallel_approx_1 = timeit(lambda: pi_parallel_monte_carlo(math.floor(12 * math.pow(2, i)),1),number=1)
        parallel_approx_2 = timeit(lambda: pi_parallel_monte_carlo(math.floor(12 * math.pow(2, i)),2),number=1)
        parallel_approx_3 = timeit(lambda: pi_parallel_monte_carlo(math.floor(12 * math.pow(2, i)),3),number=1)
        parallel_approx_4 = timeit(lambda: pi_parallel_monte_carlo(math.floor(12 * math.pow(2, i)),4),number=1)

        print(f"{math.floor(12*math.pow(2,i)) :< {10}}| "
              f"{sequential_approx :< {14}.8f}| "
              f"{parallel_approx_1 :< {14}.8f}| "
              f"{parallel_approx_2 :< {14}.8f}| "
              f"{parallel_approx_3 :< {14}.8f}| "
              f"{parallel_approx_4 :< {14}.8f}")


    pass # This statement is here as a placeholder for your code.

# 6) Are the results what you expected to see? If so, why?
#    If not, why do you think your results are different
#    than you expected? You can just answer in a comment.
#
# The results align with what I expected to see. The sequential version has a faster
# runtime at the start, which makes sense, since the processes have to allocate memory
# when they're initialized, as well as start up their own interpretator (as you mentioned
# in your recorded lecture). This is why the parallel versions take longer and it makes
# sense. However, as the number of samples increases and the time it takes
# to start up a process becomes more negligible, we can see that the parallel version for
# 1 process takes roughly the same time as the sequential version. This makes sense, since
# both involve one process. We can see that the parallel versions of 2, 3, and 4 processes
# are all faster by the time we reach higher sample sizes, and that 2 processes is faster
# than 1, and 3 processes is faster than both 2 and 1, and 4 processes is the fastest of them all.
# This makes sense, because as you increase the number of processors for this code, there
# will be more concurrent work being done simulatenously, thus making it faster.
# 
# For the approximations, we can see that the different versions of this algorithm all vary
# in their estimations, but as the sample sizes increase, they become more consistent, and
# this happens upon reaching higher numbers. This makes sense, since as the sample size  
# increases, the approximation would become more precise. For example, the sequential version
# consistently has 3.14 as its first digits by the time it reaches a sample size of 786432; 
# for 1 processor, its when it reaches 196608; for 2 processors, its when it reaches 49152; 
# for 3 processors, its when it reaches 393216; for 4 processors, its when it reaches 49152.
# I don't think the precision of the approximation is related to the number of processors
# because of this. This makes sense, since the algorithm isn't doing a different way of
# estimating pi. The algorithm, regardless of whether its sequential or parallel, is still
# using Monte Carlo's function for pi. The only difference is that the parallel algorithms
# will get it done faster when the sample size is large. 
