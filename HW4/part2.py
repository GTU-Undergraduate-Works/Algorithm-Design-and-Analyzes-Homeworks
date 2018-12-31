word_dictionary = ["it", "was", "the", "there", "best", "of", "times"]


def dict(str):
    return str in word_dictionary



def is_valid_sentence(str):
    word_list = []
    n = len(str)
    if n == 0:
        return True
    d = [False]*(n+1)
    for i in range(1,n+1):

        if not d[i] and dict(str[0:i]):
            d[i] = True
            word_list.append(str[0:i])

        if d[i]:
            if i == n:
                return True, word_list

            for j in range(i+1, n+1):
                if not d[j] and dict(str[i:j]):
                    word_list.append(str[i:j])
                    d[j] = True

                if j == n and d[j]:
                    return True, word_list

    return False, []


is_valid, word_list = is_valid_sentence("itwasthebestoftimes")
if is_valid:
    print("String is valid")
    print("Reconstructed String :", end=' ')
    for i in range(len(word_list)):
        print(word_list[i], end=' ')
    print()
else:
    print("String is not valid")




