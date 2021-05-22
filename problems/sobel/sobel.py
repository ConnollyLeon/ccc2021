GX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
GY = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]


def sobel(src, rows, cols):
    result = []  # 718*1278
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            gx = src[(i - 1) * cols + (j - 1)] * GX[0][0] + \
                 src[(i - 1) * cols + j] * GX[0][1] + \
                 src[(i - 1) * cols + (j + 1)] * GX[0][2] + \
                 src[i * cols + (j - 1)] * GX[1][0] + \
                 src[i * cols + j] * GX[1][1] + \
                 src[i * cols + (j + 1)] * GX[1][2] + \
                 src[(i + 1) * cols + (j - 1)] * GX[2][0] + \
                 src[(i + 1) * cols + j] * GX[2][1] + \
                 src[(i + 1) * cols + (j + 1)] * GX[2][2]
            gy = src[(i - 1) * cols + (j - 1)] * GY[0][0] + \
                 src[(i - 1) * cols + j] * GY[0][1] + \
                 src[(i - 1) * cols + (j + 1)] * GY[0][2] + \
                 src[i * cols + (j - 1)] * GY[1][0] + \
                 src[i * cols + j] * GY[1][1] + \
                 src[i * cols + (j + 1)] * GY[1][2] + \
                 src[(i + 1) * cols + (j - 1)] * GY[2][0] + \
                 src[(i + 1) * cols + j] * GY[2][1] + \
                 src[(i + 1) * cols + (j + 1)] * GY[2][2]
            gx = gx if gx > 0 else 0
            gy = gy if gy > 0 else 0
            if gx + gy > 255:
                res = 255
            else:
                res = gx + gy

            result.append(res)
    return result


if __name__ == '__main__':
    data = [int(x.strip()) for x in open('./data.txt').readlines()]
    dst = [int(x.strip()) for x in open('./dst.txt').readlines()]

    # 用来看数组成矩阵排列的时候的样子
    # import numpy as np
    #
    # np_data = np.asarray(data).reshape((720, 1280))
    # np_dst = np.asarray(dst).reshape((718, 1278))
    # import pandas as pd
    #
    # pd.DataFrame(np_data).to_csv("data_matrix.csv",header=None,index=None)
    # pd.DataFrame(np_dst).to_csv("dst_matrix.csv",header=None,index=None)

    result = sobel(data, 720, 1280)

    output_f = open('output.txt', 'w')
    for value in result:
        output_f.write(str(value) + '\n')
