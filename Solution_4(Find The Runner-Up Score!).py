if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score = list(arr)
    score.sort()
    second_score = score[0]
    
    for i in range(n):
        if second_score < score[i] and score[i] < score[n-1]:
            second_score = score[i]
    print(second_score)
