import random

#text file line format: number, Person, Action, Object
#ex: 0, Jesus, singing, microphone
with open('pao.txt', 'r') as f:
    data = f.readlines()
    
pao = {}
numbers = []
for line in data:
    number, p, a, o = line.split(',')
    pao[int(number)] = [p,a,o]
    numbers.append(int(number))
    
def generate_number(digits=3):
    nums = [random.choice(numbers) for i in range(digits)]
    return nums
    
if __name__ == '__main__':
    while True:
        n1, n2, n3 = generate_number(3)
        print(n1, n2 , n3)
        user_input = input("Press any key to see answer or Ctrl+C to exit: ").lower()
        if user_input:
            print(pao[n1][0], pao[n2][1], pao[n3][2])
          