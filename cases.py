import random
import time
import pandas as pd
import numpy as np
import bubble
import merge
import counting
import insertion
import quick

import matplotlib.pyplot as plt
   
# runs the benchmarking,
def benchmarking(algorithms, Sizes, runs):
    # create some variables to append the output to
    elapsed_times = [] # this should end up with 10 elapsed times 
    input_size =[]
    trials =[] # for the current trial number for each algorithm
    type =[] # for the type of sorting algorithm


    # for each of the 5 sorting algorithms
    #for sort_algo in sort_type:
    for sort_algo in algorithms:
        print(f"running {sort_algo}")
        
        # for each array size in the size array
        for size in Sizes:
            # run this 10 times for each size for each sort type
            for run in range(runs):
                # generate random arrays
                # using large values here 
                x = [random.randint(0,10000000) for i in range(size)]
                # testing reverse order
                x.sort()
                
                #print(f" function {sort_algo} on array of length {len(x)}")
                algorithm = algorithms[sort_algo]
                
                # time.time return the time in seconds since the epoch as a floating point number
                start_time = time.time()
                # run the actual algorithm on the current run on the current array size
                algorithm(x)
                end_time = time.time()
                time_elapsed = (end_time - start_time)* 1000 ## need milliseconds
                
                # Here I want the results from each run, for each algorithm for each size
                # append the results of each run to the results array
                elapsed_times.append(time_elapsed)
                
                # append the current run number (from 1 to 10)
                trials.append(run+1)
                input_size.append(size)
                type.append(sort_algo) # for each algorithm type 

    # outputs a dataframe with the raw times for each trial              
    df = pd.DataFrame({"Sort":type, "Size":input_size, "Times":elapsed_times, "trialNo":trials})
    return df

# tidy up into a function to take the output of the benchmarking and calculate the averages 
def mean_sorts(df):
    
    df.set_index('Size', inplace=True)
    # calculate the averages for each sorting algorithm at each level of input size
    means = (df.iloc[:, 0:2].groupby(['Sort','Size']).mean()).round(3)
    # float("{:10.3f}")
    # unstack to get the desired format for the output to the console
    return means.unstack()

def plot_averages(df2):

    import seaborn as sns
    import matplotlib.pyplot as plt

    plt.rcParams["figure.figsize"]=(16,8)
    sns.set(style= "darkgrid")
    df2.T.plot(lw=2, colormap='jet', marker='.', markersize=10, 
         title='Benchmarking Sorting Algorithms - Average Times. (using large values')
    plt.ylabel("Running time (milliseconds)")
    plt.xlabel("Input Size")
    #plt.ylim(0,80)
    #plt.show()
    # change this to save the image name different each time instead of overwriting existing image

    plt.savefig('largevalues.png', bbox_inches='tight')
 
def export_results(times, means):
    # change this to store in a different file each time so I can compare results
    times.to_csv('largevalue_trials' + '10000'+'.csv')
    means.to_csv('largevalues' + '10000' + '.csv')


if __name__ == "__main__":

    #algorithms = {"BubbleSort": bubble.bubbleSort,"insertionSort":insertion.insertionSort,"mergeSort":merge.merge_sort,"quickSort":quick.quickSort, "CountingSort": counting.CountingSort}
    algorithms = {"insertionSort":insertion.insertionSort,"mergeSort":merge.merge_sort,"CountingSort": counting.CountingSort}
    # provide the sizes for the arrays to be sorted    
    sizeN = [250,500,1000]
    sizeN = [100,250,500,750,1000,1250,2500,3750,5000,6250,7500,8750,10000]
    # call the benchmarking function
    results = benchmarking(algorithms, sizeN, 5)
    
    print("The running time for each of the 5 sorting algorithms have been measured 10 times and the averages of the 10 runs for each algorithm and each input size are as follows \n ")
    df2=  mean_sorts(results)
    # drop 'Sort'
    df2.rename_axis(None, inplace=True)
    # drop one of the multi-index levels
    df2.columns = df2.columns.droplevel()
    print(df2)

    plot_averages(df2)
    export_results(results, df2)