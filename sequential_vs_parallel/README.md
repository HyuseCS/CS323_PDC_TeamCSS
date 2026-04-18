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
    <li>Parallel is definitely faster than sequential when it comes to larger datasets, i was tasked to make the parallel search algorithm, and in the tests i have, when it was time for the smaller dataset, it performed much slower than when the number of elemts where to increase, this proves that parallel is better for larger datasets.
</ul>

<b>Theodore Pagalan</b>
<ul>
    <li> What I observed between sequential and parallel sort is the former is faster on the dataset with 1000 elements, and the latter being superior on datasets with 100000 and 1000000 elements. This shows that for smaller datasets, the overhead outweighs the benefits that parallelism has to offer. Parallelism works best for larger datasets (in this case, elements >= 100000). The challenges that I encountered when implementing parallel sort is the part where the individual chunks need to be merged efficiently. At first the implementation had inefficiencies where some sorting operations are actually redundant. With the help of AI, the implementation was optimized where the benefits of parallelism are maximized. 
</ul>