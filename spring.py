import svd_solve as svd
import numpy as np

def define_A(shape):
    """
    Matrix A based on the specified shape, representing a system of springs and masses.

    Parameters:
        shape (tuple): A tuple specifying the shape of the matrix A.

    Returns:
        numpy.ndarray: A matrix representing the system's configuration.

    """
    A = np.zeros(shape)
    np.fill_diagonal(A, 1)
    if shape[0] > 1:
        np.fill_diagonal(A[1:], -1)
    return A

def define_C(spring_constant_list):
    """
    Diagonal matrix C based on a list of spring constants.

    Parameters:
        spring_constant_list (list): List of spring constants.

    Returns:
        numpy.ndarray: Diagonal matrix C.

    """

    return np.diag(spring_constant_list)

def define_force_vector(mass_list):
    """
    Force vector based on a list of masses.

    Parameters:
        mass_list (list): List of masses.

    Returns:
        numpy.ndarray: Force vector.

    """

    f = np.array(mass_list) * -9.81
    return f

def stiffness_definition(A: np.array, C):
    """
    Calculates stiffness matrix K based on matrices A and C.

    Parameters:
        A (numpy.ndarray): Matrix A representing the system's configuration.
        C (numpy.ndarray): Diagonal matrix of spring constants.

    Returns:
        numpy.ndarray: Stiffness matrix K.

    """

    K = A.T @ C @ A
    return K

def displacement_solve(K, f):
    """
    Solve for displacements.

    Parameters:
        K (numpy.ndarray): Stiffness matrix.
        f (numpy.ndarray): Force vector.

    Returns:
        numpy.ndarray: Displacement vector.

    """

    U, Sigma, V_T, cond_number, inv_K = svd.svd_solve(K)
    disp_vector = inv_K @ f
    return disp_vector

def solve_elongation(A, u):
    """
    Calculate elongations of the springs.

    Parameters:
        A (numpy.ndarray): Matrix A representing the system's configuration.
        u (numpy.ndarray): Displacement vector.

    Returns:
        numpy.ndarray: Elongation vector.

    """

    e = A @ u
    return e

def internal_force_solve(C, e):
    """
    Calculates internal forces in the springs.

    Parameters:
        C (numpy.ndarray): Diagonal matrix of spring constants.
        e (numpy.ndarray): Elongation vector.

    Returns:
        numpy.ndarray: Internal force vector.

    """

    w = C @ e
    return w

def input_springs_masses():
    """
    Prompt the user for input regarding the # of springs, masses, spring constants, and masses.

    Returns:
        tuple: # of springs, # of masses, spring constants list, mass values list.

    """
    while True:
        try:
            spring_num = int(input("Enter the number of springs:\n"))
            mass_num = int(input("Enter the number of masses:\n"))
            boundary_cond = str(input("Enter boundary condition ('Fixed-Free' or 'Fixed-Fixed'):\n"))
            if spring_num > 0 and mass_num > 0 and (
                (spring_num == mass_num and boundary_cond == "Fixed-Free") or
                (spring_num == mass_num + 1 and boundary_cond == "Fixed-Fixed")
            ):
                break
            else:
                print("Input not accepted. Please follow the instructions.")
                print("The number of masses must be equal to the number of springs for 'Fixed-Free' or one less for 'Fixed-Fixed'.")
                print("The boundary condition must be either 'Fixed-Free' or 'Fixed-Fixed'.")
        except Exception as e:
            print(f'Error: {e}')
            print("Please enter positive integers for the number of springs and masses.")
            print("The boundary condition must be either 'Fixed-Free' or 'Fixed-Fixed'.")
    
    spring_consts = []
    mass_values = []
    for i in range(spring_num):
        while True:
            try:
                c = float(input(f"Enter the spring constant for spring {i+1}:\n"))
                if c > 0:
                    spring_consts.append(c)
                    break
                else:
                    print("Please enter a positive value for the spring constant.")
            except Exception as e:
                print(f"Error: {e}\nPlease enter a valid positive number for the spring constant.")

    for i in range(mass_num):
        while True:
            try:
                mass = float(input(f"Enter the mass for mass {i+1}:\n"))
                if mass > 0:
                    mass_values.append(mass)
                    break
                else:
                    print("Please enter a positive value for the mass.")
            except Exception as e:
                print(f"Error: {e}\nPlease enter a valid positive number for the mass.")

    return spring_num, mass_num, spring_consts, mass_values

def main():
    num_spring, num_mass, spring_consts, mass_list = input_springs_masses()
    A_shape = (num_spring, num_mass)

    # Define matrices and vectors
    A = define_A(A_shape)
    C = define_C(spring_consts)
    f = define_force_vector(mass_list)
    K = stiffness_definition(A, C)

    # Solve for displacements
    u = displacement_solve(K, f)
    # Calculate elongations and internal forces
    e = solve_elongation(A, u)
    w = internal_force_solve(C, e)

    # Perform SVD on the stiffness matrix K
    U, Sigma, V_T, cond_number, inv_K = svd.svd_solve(K)

    # Print results
    print(f'\nA matrix:\n{A}')
    print(f'\nSpring constant matrix C:\n{C}')
    print(f'\nForce vector f:\n{f}')
    print(f'\nStiffness matrix K:\n{K}')
    print(f'\nDisplacement vector u:\n{u}')
    print(f'\nElongation vector e:\n{e}')
    print(f'\nInternal forces w:\n{w}')
    print(f'\nSingular value matrix Sigma:\n{Sigma}')
    print(f'\nThe stiffness matrix K has condition number: {cond_number}')

if __name__ == "__main__":
    main()
