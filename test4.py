def recursive_function(n, current_depth=0):
    # 들여쓰기 설정
    indentation = "____" * current_depth
    
    # 기본 질문 출력
    print(indentation + '"재귀함수가 뭔가요?"')
    
    if current_depth == n:
        # 재귀의 마지막 단계에서 출력할 문장
        print(indentation + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        # 재귀 호출 이전에 출력할 문장들
        print(indentation + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print(indentation + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(indentation + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        
        # 재귀 호출
        recursive_function(n, current_depth + 1)
    
    # 재귀 호출 이후에 출력할 문장
    print(indentation + '라고 답변하였지.')

# 재귀 호출 횟수 입력
n = int(input("재귀 호출 횟수를 입력하세요: "))

# 함수 호출
recursive_function(n)
