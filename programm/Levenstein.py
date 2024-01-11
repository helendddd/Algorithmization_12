#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def edit_dist(a, b):
    def edit_dist_td(i, j):
        if matrix[i][j] == large:
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            else:
                ins = edit_dist_td(i, j - 1) + 1
                delete = edit_dist_td(i - 1, j) + 1
                sub = edit_dist_td(i - 1, j - 1) + (a[i - 1] != b[j - 1])
                matrix[i][j] = min(ins, delete, sub)
        return matrix[i][j]

    def edit_dist_bu():
        matrix = []
        for i in range(len_a + 1):
            matrix.append([i])
        for j in range(1, len_b + 1):
            matrix[0].append(j)
        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                c = a[i - 1] != b[j - 1]
                matrix[i].append(min(
                    matrix[i - 1][j] + 1,
                    matrix[i][j - 1] + 1,
                    matrix[i - 1][j - 1] + c
                ))
        return matrix[len_a][len_b]

    def restore():
        str_re1, str_re2 = [], []
        i, j = len_a, len_b
        while (i, j) != (0, 0):
            if i != 0 and matrix[i][j] == matrix[i - 1][j] + 1:
                str_re1.append(a[i - 1])
                str_re2.append('-')
                i -= 1

            elif j != 0 and matrix[i][j] == matrix[i][j - 1] + 1:
                str_re1.append('-')
                str_re2.append(b[j - 1])
                j -= 1

            elif matrix[i][j] == matrix[i - 1][j - 1] + (a[i - 1] != b[j - 1]):
                str_re1.append(a[i - 1])
                str_re2.append(b[j - 1])
                i -= 1
                j -= 1

        str_re1.reverse()
        str_re2.reverse()
        return str_re1, str_re2

    len_a = len(a)
    len_b = len(b)
    large = float('inf')
    matrix = [[large] * (len_b + 1) for _ in range(len_a + 1)]
    edit1 = edit_dist_td(len_a, len_b)
    edit2 = edit_dist_bu()
    solution = restore()

    return edit1, edit2, solution


if __name__ == '__main__':
    str1 = "editing"
    str2 = "distance"
    edit_td, edit_bu, sol = edit_dist(str1, str2)
    print("Minimum Edit Distance, according to editDistTD:", edit_td)
    print("Minimum Edit Distance, according to editDistBU:", edit_bu)
    for item in sol:
        print(item)
