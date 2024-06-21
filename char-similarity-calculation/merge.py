from pinyin_similarity import calculate
from shape_similarity import fourconer_new, fourconer_detailed, order_lcs, order
import numpy as np
from tqdm import tqdm


if __name__ == '__main__':
    vocab_path = "bert-base-chinese vocabulary"
    vocab = [i.strip() for i in open(vocab_path)]
    n_words = len(vocab)
    pinyin_similarity = np.zeros((n_words, n_words), dtype=np.float32)
    fourconer_new_similarity = np.zeros((n_words, n_words), dtype=np.float32)
    fourconer_detailed_similarity = np.zeros((n_words, n_words), dtype=np.float32)
    order_lcs_similarity = np.zeros((n_words, n_words), dtype=np.float32)
    order_similarity = np.zeros((n_words, n_words), dtype=np.float32)
    similarity = np.zeros((n_words, n_words), dtype=np.float32)

    l = list(range(670, 7992))
    for i in tqdm(l):
        for j in l:
            if i == j:
                continue
            char1 = vocab[i]
            char2 = vocab[j]
            pinyin_sim = calculate(char1, char2)
            fourconer_new_sim = fourconer_new(char1, char2)
            fourconer_detailed_sim = fourconer_detailed(char1, char2)
            order_lcs_sim = order_lcs(char1, char2)
            order_sim = order(char1, char2)

            pinyin_similarity[i, j] = pinyin_sim
            fourconer_new_similarity[i, j] = fourconer_new_sim
            fourconer_detailed_similarity[i, j] = fourconer_detailed_sim
            order_lcs_similarity[i, j] = order_lcs_sim
            order_similarity[i, j] = order_sim

        # 小trick，对自身的相似度是对其它字符的最大值，而非1.0
        pinyin_similarity[i, i] = pinyin_similarity[i].max()
        fourconer_new_similarity[i, i] = fourconer_new_similarity[i].max()
        fourconer_detailed_similarity[i, i] = fourconer_detailed_similarity[i].max()
        order_lcs_similarity[i, i] = order_lcs_similarity[i].max()
        order_similarity[i, i] = order_similarity[i].max()
        similarity[i] = 0.7 * pinyin_similarity[i] + 0.3 * (
                    fourconer_new_similarity[i] + fourconer_detailed_similarity[i] + order_lcs_similarity[i] +
                    order_similarity[i]) / 4


    # np.save("pinyin_similarity.npy", pinyin_similarity)
    # np.save("shape_similar/fourconer_new_similarity_max.npy", fourconer_new_similarity)
    # np.save("shape_similar/fourconer_detailed_similarity_max.npy", fourconer_detailed_similarity)
    # np.save("shape_similar/order_lcs_similarity_max.npy", order_lcs_similarity)
    # np.save("shape_similar/scope_order_similarity_max.npy", order_similarity)
    # np.save("similarity.npy", similarity)
