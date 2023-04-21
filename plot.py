import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

means = pd.read_csv("Averages100.csv",index_col=0)
# transpose the dataframe
means=means.T
plt.rcParams["figure.figsize"]=(16,8)
simpleSorts = means[['BubbleSort','InsertionSort']]
otherSorts=means[['MergeSort','quickSort','CountingSort']]

#colormap='rainbow'
means.plot(lw=2, color=['red','green','blue','cyan','yellow'], marker='.', markersize=10, 
title='Benchmarking Sorting Algorithms - Average Times')
plt.ylabel("Running time (milliseconds)")
plt.xlabel("Input Size")

plt.savefig('plotAll.png', bbox_inches='tight')
#aplot =plt.rcParams["figure.figsize"]=(16,8)
#aplot.set(yscale="log")
f, axes = plt.subplots(2, 1, figsize=(12, 16))

simpleSorts.plot(lw=2, marker='.', markersize=10,ax=axes[0], color=['r','b'])
otherSorts.plot(lw=2, color=['cyan','yellow','green'], marker='.', markersize=10,ax=axes[1])

plt.suptitle("Benchmarking Sorting Algorithms - Average Times")
plt.ylabel("Running time (milliseconds)")
plt.xlabel("Input Size")
#axes[0].legend()
#plt.legend()
plt.savefig('splitPlots.png', bbox_inches='tight')

"""
bubble.plot(lw=2, colormap='jet', marker='.', markersize=10, 
title='Benchmarking Sorting Algorithms - Average Times', ax=axes[0])
insertion.plot(ax=axes[0])
plt.ylabel("Running time (milliseconds)")
plt.xlabel("Input Size")
axes[0].set_title("Bubble Sort")
plt.show()
"""
