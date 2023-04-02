def solution(N, stages):
    각스테이지별_실패율 = {}
    for stageNum in range(1, N+1):
        stageNum에_도달한_플레이어 = list(filter(lambda x: x >= stageNum, stages))
        stageNum에_도달한_플레이어수 = len(stageNum에_도달한_플레이어)
        stageNum애_도달했으나_아직클리어못한_플레이어수 = stages.count(stageNum)

        if stageNum에_도달한_플레이어수 == 0:
            실패율 = 0
        else:
            실패율 = stageNum애_도달했으나_아직클리어못한_플레이어수 / stageNum에_도달한_플레이어수
        각스테이지별_실패율[stageNum] = 실패율

    answer = {k: v for k, v in sorted(
        각스테이지별_실패율.items(), key=lambda item: (-item[1], item[0]))}

    return list(answer.keys())


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

solution(N, stages)
