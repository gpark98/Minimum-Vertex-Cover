In this folder you can find the algorithms for our project. 

To run a test case, use the main.py code. 

------------------------------------Input------------------------------------------------------------

  file name = jazz.graph, karate.graph, football.graph, as-22july06.graph, hep-th.graph, star.graph, star2.graph, netscience.graph, email.graph, delaunay_n10.graph, power.graph. 
  
  method = BnB, Approx, LS1, LS2
  
  time = possitive float.
  
  seed = possitive float. 

---------------------------------Output------------------------------------------------------------

The name of the output files changes if the methods depend on a random seed or if they do not. 

  Solution file:
  
                instance_method_cutoff.sol  (Deterministic methods)
                
                instance_method_cutoff_seed.sol  (Stochastic methods)
                
  Trace file:
            
            instance_method_cutoff.trace  (Deterministic methods)
                
            instance_method_cutoff_seed.trace  (Stochastic methods)
            
                

For running the code from terminal run 

            python3 <file name> <method> <time> <seed>, 

example :
 
            python3 main.py jazz.graph BnB 100 10
  
 

WARNINGS:

            -If the .graph file is not in the same folder as this code the path should be included as follows
            
                    python3 main.py PATH/<file name> <method> <time> <seed>
            
            -Make sure that the follwing files are in the folder:
            
                    BnB.py, MDG_final.py, genetic_algorithm_v5.py, hill_climbing.py, main.py, read_data.py, utils_BnB.py, write_results.py
