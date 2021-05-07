import unittest
import time
import numpy as np
from numpy.lib.function_base import average

from solver import sudoku_solver


class SolverTest(unittest.TestCase):
    def test_all_sudokus(self):
        total = 1000
        sudokus = np.zeros((total, 81), np.int32)
        solutions = np.zeros((total, 81), np.int32)
        for i, line in enumerate(open('data/sudoku.csv', 'r').read().splitlines()[1:]):
            if i >= total:
                break

            quiz, solution = line.split(",")
            for j, q_s in enumerate(zip(quiz, solution)):
                q, s = q_s
                sudokus[i, j] = q
                solutions[i, j] = s

        sudokus = sudokus.reshape((-1, 9, 9))
        solutions = solutions.reshape((-1, 9, 9))

        times = []

        for i in range(0, len(sudokus)):
            start_time = time.process_time()
            solution = sudoku_solver(sudokus[i])
            end_time = time.process_time()
            times.append(end_time - start_time)
            np.testing.assert_array_equal(solution, solutions[i])

        avg = str(round(average(times) * 1000, 2))
        total_time = str(round(sum(times), 2))
        
        print('-----')
        print('Done!')
        print(f' - Solved: {total} sudokus')
        print(f' - Average time: {avg}ms')
        print(f' - Total time: {total_time}s')
    
    def test_hard_sudoku(self):
        sudoku = [
            [8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 6, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 2, 0, 0],
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 7, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8],
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0],
        ]
        solution = [
            [8, 1, 2, 7, 5, 3, 6, 4, 9],
            [9, 4, 3, 6, 8, 2, 1, 7, 5],
            [6, 7, 5, 4, 9, 1, 2, 8, 3],
            [1, 5, 4, 2, 3, 7, 8, 9, 6],
            [3, 6, 9, 8, 4, 5, 7, 2, 1],
            [2, 8, 7, 1, 6, 9, 5, 3, 4],
            [5, 2, 1, 9, 7, 4, 3, 6, 8],
            [4, 3, 8, 5, 2, 6, 9, 1, 7],
            [7, 9, 6, 3, 1, 8, 4, 5, 2],
        ]

        start_time = time.process_time()
        solver_solution = sudoku_solver(sudoku)
        end_time = time.process_time()
        print('Time:', end_time - start_time, 'seconds')
        np.testing.assert_array_equal(solver_solution, solution)
    
    def test_invalid(self):
        sudoku = [
            [8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 6, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 2, 0, 0],
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [1, 0, 0, 0, 4, 5, 7, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8],
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0],
        ]
        solution = np.ones((9,9)) * -1

        start_time = time.process_time()
        solver_solution = sudoku_solver(sudoku)
        end_time = time.process_time()
        print('Time:', end_time - start_time, 'seconds')
        np.testing.assert_array_equal(solver_solution, solution)