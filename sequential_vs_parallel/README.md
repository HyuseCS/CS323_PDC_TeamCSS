All observations, analysis, and insights must be documented in your README.md. Each student
must write their own <b>individual reflection</b>, in paragraph form, discussing:
<ul>
    <li> Differences observed between sequential and parallel execution
    <li> Performance behavior across dataset sizes
    <li> Challenges encountered during implementation
    <li> Insights about overhead, synchronization, or merging
    <li> Situations where parallelism was beneficial or unnecessary
</ul>

<b>Kent Vincent Butaya</b>
<ul>
    <li>I was tasked to make the parallel search algorithm. i expected parallel execution to outperform sequential execution as the dataset grew, similar to how merge sort behaves,but i was wrong and the testing data proved otherwise, sequential linear search was consistently much faster, even on the 1,000,000 element dataset, this proved to me that for extremely lightweight operations like a basic search, the overhead and inter-process communication costs of parallelization far outweigh any benefits. Parallelism is highly effective for heavy operations on large datasets, but unnecessary and actually detrimental for simple linear searching.
</ul>

<b>Theodore Pagalan</b>
<ul>
    <li> What I observed between sequential and parallel sort is the former is faster on the dataset with 1000 elements, and the latter being superior on datasets with 100000 and 1000000 elements. This shows that for smaller datasets, the overhead outweighs the benefits that parallelism has to offer. Parallelism works best for larger datasets (in this case, elements >= 100000). The challenges that I encountered when implementing parallel sort is the part where the individual chunks need to be merged efficiently. At first the implementation had inefficiencies where some sorting operations are actually redundant. With the help of AI, the implementation was optimized where the benefits of parallelism are maximized. 
</ul>

<b> Carl Dominic Rejas </b>
<ul>
    <li> I found that sequential execution was faster for the small dataset of elements because the computational work was outweighed by the overhead of process creation and synchronization. On the other hand, I discovered that parallelizing the straightforward linear search was mostly superfluous and frequently slower across all sizes because of inter-process communication costs. I learned from this exercise that parallelism is not necessary for small datasets.

</ul>

<b> Christian John Legaspi </b>
<ul>
    <li> I was tasked to do the sequential sort version of the merge sort, and upon our testing, I have observed that on small data sets it is favorable to use the sequential execution since it demonstrates that it is faster and I have also observed that there is parallel overhead when using parallel execution in small datasets. Parallelization definitely should be used on medium (in our case, 100000 values) and large datasets, since tasks are distributed evenly to all the available and alloted cpu cores.

</ul>