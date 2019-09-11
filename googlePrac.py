# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, K):
    # write your code in Python 3.6
    realKey = S.replace("-", "").upper()
    firstLen = len(realKey)%K
    returnVal = ""
    for i in range(firstLen):
        returnVal += realKey[i]
    for i in range(firstLen, len(realKey)):
        if (i != firstLen and i%K == firstLen) or (i == firstLen and len(returnVal) > 0):
            returnVal += "-"
        returnVal += realKey[i]
    return returnVal


if __name__ == '__main__':
    print(solution("2-4A0r7-4k", 3))
    print(solution("aBdsghjkl7-5feghjkdmnb-hwi389-f-henjk-as---lmfiooobrjdkn", 1))