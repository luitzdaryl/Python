import operator

def person_lister(f):
    def inner(people):
        # complete the function
        
        # We use itemgetter(2) inside a lambda to grab the age,
        # then immediately wrap it in int() to ensure proper numerical sorting.
        people.sort(key=lambda person: int(operator.itemgetter(2)(person)))
        
        return [f(person) for person in people]
        
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')