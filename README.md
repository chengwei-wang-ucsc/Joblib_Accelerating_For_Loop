# Joblib_Accelerating_For_Loop
While one is using for-loops in Python, the CPU usage is always very low. This is fine when one is dealing with a short dataset, but very problematic for long datasets. While there are plenty of existing examples of using the Numba's Jit modifier or transferring the for loop to Cython, there are still lots of occasions that either Numba can't help or takes too long to re-write the code in Cython. I decide to research on alternative approaches other than Cython and Numba's Jit and made some progress.  

Take a look into the notebook to see if it helps.
