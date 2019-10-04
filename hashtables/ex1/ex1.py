#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)
    
    for i in range(len(weights)):
        subtract = limit - weights[i]
        right_weight = hash_table_retrieve(ht, subtract)
        
        if right_weight is not None:
            return (right_weight, i)
            
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


if __name__ == '__main__':
    # weights_1 = [9]
    # print("LINE 54:", get_indices_of_item_weights(weights_1, 1, 9))
    # weights_2 = [4, 4]
    # print("LINE 56:", get_indices_of_item_weights(weights_2, 2, 8))

    weights_1 = [9]
    get_indices_of_item_weights(weights_1, 4, 20)
