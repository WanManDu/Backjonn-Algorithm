
def permutations(arr, r):
    result = []

    def permute(path, options):
        if len(path) == r:  # r개의 원소를 다 선택한 경우 : 기저조건
            result.append(path)
            return
        
        for i in range(len(options)):
            # 현재 원소를 선택하고, 남은 원소들로 재귀 호출
            permute(path + [options[i]], options[:i] + options[i+1:])
    
    permute([], arr)
    return result

#함수를 끝낼 수 있는 기저조건과 기저조건을 만족시키기 위해 뭐를 증가시켜줘야하는지 생각해보기

#위를 호출하면
#per)[1, 2, 3])