#221RDB041 Ēriks Lijurovs 16. grupa
# python3
import time

class Query:
    def __init__(self, query):
        if query.__len__() == 0 or query.__len__() == 1 or query.__len__() > 3:
            self.type = 'invalid'
            self.number = 0
        elif query[0].isnumeric():
            self.type = 'invalid'
            self.number = 0
        elif query[1].isnumeric() == False:
            self.type = 'invalid'
            self.number = 0
        elif len(query[1]) > 7:
            self.type = 'invalid'
            self.number = 0
        elif query[0] == 'add' and len(query[2]) > 15:
            self.type = 'invalid'
            self.number = 0
        else:
            self.type = query[0]
            self.number = int(query[1])

        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [[], [], [], [], [], [], [], [], [], []]
    
    for cur_query in queries:
        if cur_query.type == 'add':
            index = int(str(cur_query.number)[0])
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts[index]:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    
                    break
            else: # otherwise, just add it
                contacts[index].append(cur_query)
        elif cur_query.type == 'del':
            index = int(str(cur_query.number)[0])
            for j in range(len(contacts[index])):
                if contacts[index][j].number == cur_query.number:
                    contacts[index].pop(j)
                    
                    break
        elif cur_query.type == 'invalid':
            response = 'invalid query'
            result.append(response)
        else:
            response = 'not found'
            index = int(str(cur_query.number)[0])
            for contact in contacts[index]:
                if contact.number == cur_query.number:
                    response = contact.name
                    
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

