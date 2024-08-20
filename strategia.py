from collections import Counter

def check_full_house(sequence: list) -> int:
    counter = Counter(sequence)
    if len(counter.keys()) == 2:
        for key in counter.keys():
            if counter[key] == 3:
                return 40
    return 0

def check_small_straight(sequence: list) -> int:
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

def check_large_straight(sequence: list) -> int:
    is_large = True
    sequence.sort()
    for i in range(1,5):
        if sequence[i] - sequence[i-1] != 1:
            is_large = False
    if is_large:
        return 35
    return 0

def check_3_like(sequence: list) -> int:
    counter = Counter(sequence)
    for key in counter.keys():
        if counter[key] >= 3:
            return sum(sequence)
    return 0

def check_4_like(sequence: list) -> int:
    counter = Counter(sequence)
    for key in counter.keys():
        if counter[key] == 3:
            return sum(sequence)
    return 0
    
def check_5_like(sequence: list) -> int:
    counter = Counter(sequence)
    for key in counter.keys():
        if counter[key] == 5:
            return 50
    return 0

def ones(sequence: list)-> int:
    soma = 0
    for number in sequence:
        if number == 1:
            soma += 1
    return soma

def twos(sequence: list)-> int:
    soma = 0
    for number in sequence:
        if number == 2:
            soma += 2
    return soma

def threes(sequence: list)-> int:
    soma = 0
    for number in sequence:
        if number == 3:
            soma += 3
    return soma

def fours(sequence: list)-> int:
    soma = 0
    for number in sequence:
        if number == 4:
            soma += 4
    return soma
    
def fives(sequence: list)-> int:
    soma = 0
    for number in sequence:
        if number == 5:
            soma += 5
    return soma
    
def six(sequence: list)-> int:
    soma = 0
    for number in sequence:
        if number == 6:
            soma += 6
    return soma

def chance(sequence: list)-> int:
    soma = 0
    for number in sequence:
        soma += number
    return soma


class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.chance = chance(sequence)
        self.available = True

class Game:

    def __init__(self):
        self.sequences = list()
        #matriz contendo o maior valor possível para cada tipo de score, em ordem crescente de chance
        #cada sequência será identificada por um id
        self.highest_scores = list()
        for i in range(13):
            self.highest_scores.append(list())

        self.filled_scores = [False]*13

        #sequência os pontos finais
        self.maximum_sequence = list()


    #adiciona um id de uma sequência a um determinado tipo de score
    def __add_score(self, index, id, chance):
        
        #temp é usado apenas para adicionar o id na posição que deveria estar
        self.highest_scores[index].append(chance)

    #para adicionar os scores referentes aos números (1,2,...,6) é necessário
    #uma política diferente (eles são oordenados pelo score ao invés de chance)
    def __add_number_scores(self,index, id, score):
        
        self.highest_scores[index].append(score)



    def add_sequence(self, sequence: Sequence):
        id = len(self.sequences)
        chance = sequence.chance
        self.sequences.append(sequence)
        
        self.__add_number_scores(0, id, ones(sequence.sequence)) #index = 0
        self.__add_number_scores(1 ,id, twos(sequence.sequence)) #index = 1
        self.__add_number_scores(2 ,id, threes(sequence.sequence)) #index = 2
        self.__add_number_scores(3 ,id, fours(sequence.sequence)) #index = 3
        self.__add_number_scores(4 ,id, fives(sequence.sequence)) #index = 4
        self.__add_number_scores(5 ,id, six(sequence.sequence)) #index = 5

        self.__add_number_scores(6, id, six(sequence.sequence)) #chance index = 6

        three_like = check_3_like(sequence.sequence) #index = 7
        four_like = check_4_like(sequence.sequence) #index = 8
        five_like = check_5_like(sequence.sequence) #index = 9
        small_straight = check_small_straight(sequence.sequence) #index = 10
        large_straight = check_large_straight(sequence.sequence) #index = 11
        full_house = check_full_house(sequence.sequence) #index = 12

        #Esses índices são adotados de tal maneira simplesmente para poder 

        if three_like != 0:
            self.__add_score(7, id, three_like)
        else: self.__add_score(7, id, 0)
        if  four_like != 0:
            self.__add_score(8, id, four_like)
        else: self.__add_score(8, id, 0)
        if  five_like != 0:
            self.__add_score(9, id, five_like)
        else: self.__add_score(9, id, 0)
        if  small_straight != 0:
            self.__add_score(10, id, small_straight)
        else: self.__add_score(10, id, 0)
        if  large_straight != 0:
            self.__add_score(11, id, large_straight)
        else: self.__add_score(11, id, 0)
        if  full_house != 0:
            self.__add_score(12, id, full_house)
        else: self.__add_score(12, id, 0)
    
    #IGNORE ESSA FUNÇÃO POR ENQUANTO
    #é necessário começar atribuindo o ponto para os scores de maior valor primeiro (5_like, full_house, 4_like, ...)
    #tal qual atualmente, essa função começará pelos 1's
    def attribute_points(self) -> list:
        for i in range(len(self.highest_scores)):
            highest_score = self.find_higher(self.highest_scores[i])
        
                
        return list

    
    #Encontra o maior valor de um tipo de score das 13 rodadas realizadas
    def find_higher(self, scores) -> int:
        result = 0

        return result
        

def main():
    game = Game()
    for i in range(13):
        line = "1 2 3 4 5"
        line_list = line.split()
        for i in range(len(line_list)):
            line_list[i] = int(line_list[i])
        sequence = Sequence(line_list)
        game.add_sequence(sequence)
    resultado = game.attribute_points()
    soma = sum(resultado)
    print(resultado, end='')
    print(soma)

if __name__ == '__main__':
    main()