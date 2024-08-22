from collections import Counter

def check_full_house(sequence: list()) -> int:
    counter = Counter(sequence)
    if len(counter.keys()) == 2:
        for key in counter.keys():
            if counter[key] == 3:
                return 40
    return 0

def check_small_straight(sequence: list()) -> int:
    is_small1 = True
    is_small2 = True
    sequence.sort()
    for i in range(2,5):
        if sequence[i] - sequence[i-1] != 1:
            is_small1 = False
    for i in range(1,4):
        if sequence[i] - sequence[i-1] != 1:
            is_small2 = False
    if is_small1 or is_small2:
        return 25
    return 0

def check_large_straight(sequence: list()) -> int:
    is_large = True
    sequence.sort()
    for i in range(1,5):
        if sequence[i] - sequence[i-1] != 1:
            is_large = False
    if is_large:
        return 35
    return 0

def check_3_like(sequence: list()) -> int:
    counter = Counter(sequence)
    for key in counter.keys():
        if counter[key] >= 3:
            return sum(sequence)
    return 0

def check_4_like(sequence: list()) -> int:
    counter = Counter(sequence)
    for key in counter.keys():
        if counter[key] == 3:
            return sum(sequence)
    return 0
    
def check_5_like(sequence: list()) -> int:
    counter = Counter(sequence)
    if len(counter.keys()) == 5:
        return 50
    return 0

def ones(sequence: list())-> int:
    soma = 0
    for number in sequence:
        if number == 1:
            soma += 1
    return soma

def twos(sequence: list())-> int:
    soma = 0
    for number in sequence:
        if number == 2:
            soma += 2
    return soma

def threes(sequence: list())-> int:
    soma = 0
    for number in sequence:
        if number == 3:
            soma += 3
    return soma

def fours(sequence: list())-> int:
    soma = 0
    for number in sequence:
        if number == 4:
            soma += 4
    return soma
    
def fives(sequence: list())-> int:
    soma = 0
    for number in sequence:
        if number == 5:
            soma += 5
    return soma
    
def six(sequence: list())-> int:
    soma = 0
    for number in sequence:
        if number == 6:
            soma += 6
    return soma

def chance(sequence: list())-> int:
    soma = 0
    for number in sequence:
        soma += number
    return soma

def main():
    available_scores = [1]*13
    answers = list()
    sequences = list()
    for i in range(13):
        line = input()
        line_list = line.split()
        for i in range(len(line_list)):
            line_list[i] = int(line_list[i])
        sequences.append(line_list)
    resultado = combinatoria(sequences, available_scores, answers)
    print(resultado)
    
def combinatoria(sequences: list(), available_scores: list(), answers: list()) -> list(list()):
    if not sequences:
        return answers

    
    answer_lists = list(list())
    
    for i in range(len(sequences)):
        current_list = list(sequences)
        del current_list[i]
        if available_scores[0] == 1:
            current_answer = ones(sequences[i])
            current_types = list(available_scores)
            current_types[0] = -1
            answers.append(current_answer)
            answer_lists.append(combinatoria(current_list, current_types, answers))
        
        if available_scores[1] == 1:
            current_answer = twos(sequences[i])
            current_types = list(available_scores)
            current_types[1] = -1
            answers.append(current_answer)
            answer_lists.append(combinatoria(current_list, current_types, answers))
        
        if available_scores[2] == 1:
            current_answer = threes(sequences[i])
            current_types = list(available_scores)
            current_types[2] = -1
            answers.append(current_answer)
            answer_lists.append(combinatoria(current_list, current_types, answers))
        
        if available_scores[3] == 1:
            current_answer = fours(sequences[i])
            current_types = list(available_scores)
            current_types[3] = -1
            answers.append(current_answer)
            answer_lists.append(combinatoria(current_list, current_types, answers))
        
        if available_scores[4] == 1:
            current_answer = fives(sequences[i])
            current_types = list(available_scores)
            current_types[4] = -1
            answers.append(current_answer)
            answer_lists.append(combinatoria(current_list, current_types, answers))
        
        if available_scores[5] == 1:
            current_answer = six(sequences[i])
            current_types = list(available_scores)
            current_types[5] = -1
            answers.append(current_answer)
            answer_lists.append(combinatoria(current_list, current_types, answers))
        
        
        if available_scores[6] == 1:
            current_answer = chance(sequences[i])
            current_types = list(available_scores)
            current_types[6] = -1
            answers.append(current_answer)
            answer_lists.append(combinatoria(current_list, current_types, answers))
            
        if available_scores[7] == 1:
            current_answer = check_3_like(sequences[i])
            current_types = list(available_scores)
            current_types[7] = -1
            answers.append(current_answer)
            answer_lists.append(combinatoria(current_list, current_types, answers))
            
        if available_scores[8] == 1:
            current_answer = check_4_like(sequences[i])
            current_types = list(available_scores)
            current_types[8] = -1
            answers.append(current_answer)
            answer_lists.append(combinatoria(current_list, current_types, answers))
            
        if available_scores[9] == 1:
            current_answer = check_5_like(sequences[i])
            current_types = list(available_scores)
            current_types[9] = -1
            answers.append(current_answer)
            answer_lists.append(combinatoria(current_list, current_types, answers))
            
        if available_scores[10] == 1:
            current_answer = check_small_straight(sequences[i])
            current_types = list(available_scores)
            current_types[10] = -1
            answers.append(current_answer)
            answer_lists.append(combinatoria(current_list, current_types, answers))
            
        if available_scores[11] == 1:
            current_answer = check_large_straight(sequences[i])
            current_types = list(available_scores)
            current_types[11] = -1
            answers.append(current_answer)
            answer_lists.append(combinatoria(current_list, current_types, answers))
            
        if available_scores[12] == 1:
            current_answer = check_full_house(sequences[i])
            current_types = list(available_scores)
            current_types[12] = -1
            answers.append(current_answer)
            answer_lists.append(combinatoria(current_list, current_types, answers))

    highest = list()
    highest_sum = 0
    for answer_list in answer_lists:
        soma = sum(answer_list)
        if soma > highest_sum:
            highest_sum = soma
            highest = answer_list
    return highest
main()