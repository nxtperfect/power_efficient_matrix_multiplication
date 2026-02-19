import time


def run():
    matrixA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrixB = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

    start = time.perf_counter_ns()
    assert simpleMul(matrixA, matrixB) == [
        [84, 90, 96],
        [201, 216, 231],
        [318, 342, 366],
    ]
    end = time.perf_counter_ns()
    print(f"Took {end-start}ns")


def simpleMul(matrixA: list[list[int]], matrixB: list[list[int]]):
    res = []
    for i in range(len(matrixA)):
        tempRow = []
        for j in range(len(matrixA[0])):
            temp = 0
            for k in range(len(matrixB[0])):
                temp += matrixA[i][k] * matrixB[k][j]
            tempRow.append(temp)
        res.append(tempRow)
    return res


if __name__ == "__main__":
    run()
