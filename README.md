## Singular Value Decomposition Calculator

  

**Files**

*svd_solve.py:* A Custom SVD decomposition function

  

*spring.py:* Functions to solve spring-mass systems

  

*svd_test.ipynb:* Compares custom solver and numpy results for first part of the project

  
  

### Solving a SVD using svd solve and showing the results.

  

The following is visible in the *svd_test.ipynb*. This matrix was used for comparison

    A = np.array([[10, 2, 3],
    [4, 5, 6],
    [7, 8, 9],])


The output was the following

    Custom U: 
    [[ 0.49323762 0.86819544 -0.05434456] 
     [ 0.460219 -0.31345194 -0.8306301 ]
     [ 0.73818367 -0.38468761 0.55416632]] 
    
    NumPy U: 
    [[-0.49323762 0.86819544 -0.05434456]
     [-0.460219 -0.31345194 -0.8306301 ]
     [-0.73818367 -0.38468761 0.55416632]] 
     
    Custom V_T: 
    [[ 0.6423315 0.49453207 0.58553248]
     [ 0.76435664 -0.46945622 -0.44200655]
     [ 0.05629545 0.73147036 -0.67954538]] 
     
    NumPy V_T: 
    [[-0.6423315 -0.49453207 -0.58553248]
     [ 0.76435664 -0.46945622 -0.44200655]
     [ 0.05629545 0.73147036 -0.67954538]] 
     
    Custom Sigma: 
    [[18.58936996 0. 0. ]
     [ 0. 6.19518838 0. ]
     [ 0. 0. 0.23444694]] 
    
    NumPy Sigma: 
    [[18.58936996 0. 0. ]
     [ 0. 6.19518838 0. ]
     [ 0. 0. 0.23444694]] 
     
    Custom Reconstructed Matrix (U @ Sigma @ V_T): 
    [[10. 2. 3.] 
     [ 4. 5. 6.] 
     [ 7. 8. 9.]] 
    
    NumPy Reconstructed Matrix (U @ Sigma @ V_T): 
    [[10. 2. 3.]
     [ 4. 5. 6.]
     [ 7. 8. 9.]]

In the above output, the values of every matrix is not exactly the same. However, this is because there is more than one functional SVD decomposition for a given matrix. Additionally, the reconstructed matrices are also identical proving that both solutions work. 

    Custom SVD solver condition number and inverse matrix: 
    Condition Number: 79.29030599962555 
    Inverse of A: 
    [[ 0.11111111 -0.22222222 0.11111111] 
     [-0.22222222 -2.55555556 1.77777778]
     [ 0.11111111 2.44444444 -1.55555556]] 
     
    NumPy condition number and inverse matrix: 
    Condition Number: 79.2903059996245 
    Inverse of A: 
    [[ 0.11111111 -0.22222222 0.11111111]
     [-0.22222222 -2.55555556 1.77777778]
     [ 0.11111111 2.44444444 -1.55555556]]

Additionally, the inverse matrix and condition numbers matched up. The minor differences are a result of floating point imprecision.

### Running spring.py to solve a spring mass system

In terminal, within this repository's directory, run `python3 spring.py`

  
User will be prompted with the following with sample input:

    Enter the number of springs:
    3
    Enter the number of masses:
    3
    Enter boundary condition ('Fixed-Free' or 'Fixed-Fixed'):
    Fixed-Free
    Enter the spring constant for spring 1:
    100
    Enter the spring constant for spring 2:
    100
    Enter the spring constant for spring 3:
    100
    Enter the mass for mass 1:
    10 
    Enter the mass for mass 2:
    10
    Enter the mass for mass 3:
    10


If the input is not an acceptable number, it will return an error

        Please enter positive integers for the number of springs and masses.
    The boundary condition must be either 'Fixed-Free' or 'Fixed-Fixed'.

Depending on the error it will prompt different messages.

        Input not accepted. Please follow the instructions.
    The number of masses must be equal to the number of springs for 'Fixed-Free' or one less for 'Fixed-Fixed'.
    The boundary condition must be either 'Fixed-Free' or 'Fixed-Fixed'.


When the input is valid, it will return an output similar to this:

    A matrix:
    [[ 1.  0.  0.]
     [-1.  1.  0.]
     [ 0. -1.  1.]]
    
    Spring constant matrix C:
    [[100.   0.   0.]
     [  0. 100.   0.]
     [  0.   0. 100.]]
    
    Force vector f:
    [-98.1 -98.1 -98.1]
    
    Stiffness matrix K:
    [[ 200. -100.    0.]
     [-100.  200. -100.]
     [   0. -100.  100.]]
    
    Displacement vector u:
    [-2.943 -4.905 -5.886]
    
    Elongation vector e:
    [-2.943 -1.962 -0.981]
    
    Internal forces w:
    [-294.3 -196.2  -98.1]
    
    Singular value matrix Sigma:
    [[324.69796037   0.           0.        ]
     [  0.         155.49581321   0.        ]
     [  0.           0.          19.80622642]]
    
    The stiffness matrix K has condition number: 16.39373162228442

Note on 2 free ends examination:

A system with two free ends does not make sense in a physical context. For example, in a free-free system with three masses and two springs, the stiffness matrix is a 3x3 matrix with only two independent rows, resulting in a rank of two. This makes the matrix non-invertible and unsolvable, as there are more unknowns than equations, leading to no unique solution. To achieve solvability, the stiffness matrix must reach full rank (rank 3 in this case), which is only possible by applying a boundary condition, as handled by the SVD algorithm.
