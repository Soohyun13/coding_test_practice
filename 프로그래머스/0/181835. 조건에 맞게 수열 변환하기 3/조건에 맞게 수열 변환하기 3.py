def solution(arr, k):
    answer = []
    if k % 2 != 0:
        for i in range(len(arr)):
            answer.append(arr[i] * k)
    else:
        for i in range(len(arr)):
            answer.append(arr[i]+k)
    return answer
