from linkedQFile import LinkedQ

def question(q):
    user_answer = input("Vilken ordning ligger korten i? ")
    numbers = user_answer.split(" ")
    
    for number in numbers:
        q.enqueue(int(number))

def cardmethod(q):
    li = []
    while not q.isEmpty():
        q.enqueue(q.dequeue()) # Först tar första värdet och sätter längst bak i kön
        li.append(q.dequeue()) # 

    return li

def main():
    q = LinkedQ()
    question(q)
    userlistS = cardmethod(q)
    print(userlistS)

main()

    
# Vilken ordning ligger korten i? 7 1 12 2 8 3 11 4 9 5 13 6 10
