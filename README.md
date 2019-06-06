# LabelPropagationAlgorithm

This project shows a simple implementation of the APM algorithm presented in http://ra.ethz.ch/CDstore/www2011/proceedings/p587.pdf.
In order to make it work, you have to download some graph data from https://snap.stanford.edu/data/. Our implementation works with a binary format text file, following the rule "InputNode OutputNode". 
The algorithm has two variants: the first, called APM_with_analytics, will run just as the normal APM function, but it will also save a log file in the 'logs' folder (if you don't have it, create one).
Keep in mind that this implementation works on a single core of your CPU, so it isn't designed to work with very large graph: with 20.000 nodes, a single iteration takes about 35 min to end on an Intel i5 6th generation.

Instructions:
1. Download the data you want to use
2. Save your data in a 'data' folder (create it if you haven't one)
3. Change the 'graph_name' parameter with your graph's data name
4. Set the gamma and the number of iterations in the APM() or APM_with_analytics() call
5. Run the algorithm
6. When the computation ends, the program will print the results in the terminal. If you run APM_with_analytics you will find a log .txt file with the same informations printed in the terminal. Use this for later statistics.
