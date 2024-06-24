import Levenshtein
import json


fourconer_code = json.load(open("./dict/fourconer.dict"))
structure = json.load(open("./dict/structure.dict"))
chaizi = json.load(open("./dict/chaizi.dict"))
stroke_order = json.load(open("./dict/order.dict"))


def fourconer_new(char1, char2):
    f1 = fourconer_code.get(char1, "")
    f2 = fourconer_code.get(char2, "")
    res = 0
    if f1 and f2:
        for i, j in zip(f1[:4], f2[:4]):
            if i == j:
                res += 1
        res /= 4
    return res


def four(char1):
    fc = fourconer_code.get(char1, "")
    res = fc[:4] if fc else ""
    return res


def fourconer_detailed(char1, char2):
    fd1 = structure.get(char1, "")
    fd2 = structure.get(char2, "")

    # 如果是独体字就不要再拆成笔画了
    chaizi1 = chaizi.get(char1, [char1]) if fd1 != 0 else [char1]
    chaizi2 = chaizi.get(char2, [char2]) if fd2 != 0 else [char2]
    res = 0
    if chaizi1 and chaizi2:
        if fd1 == fd2:
            char1_four = ''.join("a" + four(cz) for cz in chaizi1)
            char2_four = ''.join("a" + four(cz) for cz in chaizi2)
        else:
            char1_four = ''.join("a" + four(cz) for cz in chaizi1)
            char2_four = ''.join("b" + four(cz) for cz in chaizi2)
        res = Levenshtein.ratio(char1_four, char2_four)
    return res


def order(char1, char2):
    order1 = stroke_order.get(char1, "")
    order2 = stroke_order.get(char2, "")
    res = 0
    if order1 and order2:
        res = Levenshtein.ratio(order1, order2)
    return res


def order_lcs(char1, char2):
    order1 = list(stroke_order.get(char1, ""))
    order2 = list(stroke_order.get(char2, ""))
    if len(order1) > 0 and len(order2) > 0:
        m = len(order1)
        n = len(order2)

        # 生成一个零矩阵（m+1）*（n+1）来保存LCS长度
        L = [[None] * (n + 1) for i in range(m + 1)]

        # 以下步骤构建L[m+1][n+1]，保存X[0..m-1]和Y[0..n-1]的LCS
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif order1[i - 1] == order2[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])

        # L[m][n] 包含X[0..n-1]和Y[0..m-1]的LCS长度
        return L[m][n] / max(m, n)
    else:
        return 0


if __name__ == "__main__":
    print(fourconer_new("人", "大"))
