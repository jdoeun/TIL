# programmers: 모음사전

word_list = []

def dfs(cnt, w, words):
    global word_list

    if cnt == 5:
        return

    for i in range(len(words)):
        word_list.append(w + words[i])
        dfs(cnt + 1, w + words[i], words)


def solution(word):
    global word_list
    dfs(0, "", "AEIOU")

    return word_list.index(word) + 1