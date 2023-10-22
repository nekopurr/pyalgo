# https://pyalgo.co.kr/?page=1#

def solution(data):
    answer = ''
    bin_data = []
    for i in data:
        i = i.replace('+', '1').replace('-', '0').split()
        bin_data.append(''.join(i))

    for j in bin_data:
        asc_j = int('0b' + j, 2)
        answer += chr(asc_j)

    return answer