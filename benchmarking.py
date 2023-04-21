import time 
import random 
import pandas as pd 
import numpy as np 
import merge
import bubble
import quick 
import counting 
import insertion 

import matplotlib.pyplot as plt 

def benchmarking(algorhtims, Sizes, runs):
    
    elapsed_times = [] 
    input_size = [] 
    trials = [] 
    type = [] 
    
    for sort_algo in algorhtims:
        print(f"running  {sort_algo}")
        
    for size in Sizes:
        for run in range(runs):
            x = [random.randint(0,100) for i in range (size)]
    algorhtim = algorhtims[sort_algo]
    start_time = time.time()
    algorhtim(x)
    end_time = time.time()
    time_elapsed = (end_time - start_time) * 1000
    
    df = pd.DataFrame({"Sort":type, "Size":input_size, "Times":elapsed_times, "trialNo":trials})
    return df

# Define a function to take the output of the benchmarking function and calculate the averages 
def mean_sorts(df):
    # use the Size column of the dataframe as the index
    df.set_index('Size', inplace=True)
    # calculate the averages for each sorting algorithm at each level of input size
    means = (df.iloc[:, 0:2].groupby(['Sort','Size']).mean()).round(3)
    # unstack the dataframe to get the desired format for the output to the console
    return means.unstack()

# define a function to plot the averages on a graph
def plot_averages(df2):
    # import plotting libraries
    import seaborn as sns
    import matplotlib.pyplot as plt
    # set the plot paramters
    plt.rcParams["figure.figsize"]=(16,8)
    sns.set(style= "darkgrid")
    # transpose the dataframe for plotting
    df2.T.plot(lw=2, colormap='jet', marker='.', markersize=10, 
         title='Benchmarking Simple Sorting Algorithms - Average Times')
    plt.ylabel("Running time (milliseconds)")
    plt.xlabel("Input Size")
    #plt.ylim(0,80)
    #plt.show()
    # save image
    plt.savefig('Averagesplot100.png', bbox_inches='tight')
 
# define a function to export the results to csv
def export_results(times, means):
    # change this to store in a different file each time so I can compare results
    times.to_csv('Time_trials' + '100'+'.csv')
    means.to_csv('Averages' + '100' + '.csv')

# call the main program
if __name__ == "__main__":
    # the list of algorithms to be used
    algorithms = {"BubbleSort": bubble.BubbleSort,"InsertionSort":insertion.InsertionSort,"MergeSort":merge.merge_sort, "quickSort":quick.quickSort, "CountingSort": counting.CountingSort}

    # provide the sizes for the arrays to be sorted    

    sizeN = [100,250,500,750,1000,1250,2500,3750,5000,6250,7500,8750,10000]
 
    # call the benchmarking function
    results = benchmarking(algorithms, sizeN, 10)
    
    print("The running time for each of the 5 sorting algorithms have been measured 10 times and the averages of the 10 runs for each algorithm and each input size are as follows \n ")
    # create a dataframe to store the averages resulting from the benchmarking
    df2=  mean_sorts(results)
    # drop 'Sort'
    df2.rename_axis(None, inplace=True)
    # drop one of the multi-index levels
    df2.columns = df2.columns.droplevel()
    # print the results to the console
    print(df2)
    # call the plotting function
    plot_averages(df2)
    # export the results to csv
    export_results(results, df2)
    
    