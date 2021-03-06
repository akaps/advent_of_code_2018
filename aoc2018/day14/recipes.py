import copy
import utils

class Recipes:

    def __init__(self):
        self.recipe = [3, 7]
        self.current = 0
        self.next = 1
        self.processed = 0

    def step(self):
        score = self.recipe[self.current] + self.recipe[self.next]
        score = [int(d) for d in str(score)]
        self.recipe.extend(score)
        self.current = (self.current + (self.recipe[self.current] + 1)) % len(self.recipe)
        self.next = (self.next + (self.recipe[self.next] + 1)) % len(self.recipe)
        return len(score)

    def __repr__(self):
        pretty = copy.deepcopy(self.recipe)
        pretty[self.current] = '({num})'.format(num=pretty[self.current])
        pretty[self.next] = '[{num}]'.format(num=pretty[self.next])
        return ' '.join(map(str, pretty))

    def next_ten(self, num):
        while self.processed < num + 10:
            self.processed += self.step()
        return ''.join(map(str, self.recipe[num:num+10]))

    def length_before(self, seq, step_size):
        output = ''.join(map(str, self.recipe))
        while seq not in output:
            for _ in range(step_size):
                self.processed += self.step()
            output = ''.join(map(str, self.recipe))
        return output.index(seq)

#sample
recipes = Recipes()
assert recipes.next_ten(9) == '5158916779'
assert recipes.length_before('51589', 1) == 9
empty = Recipes()
assert empty.length_before('51589', 1) == 9
assert recipes.next_ten(5) == '0124515891'
assert recipes.length_before('01245', 1) == 5
assert recipes.next_ten(18) == '9251071085'
assert recipes.length_before('92510', 1) == 18
assert recipes.next_ten(2018) == '5941429882'
assert recipes.length_before('59414', 1) == 2018

#input
ans = recipes.next_ten(409551)
assert ans == '1631191756'
utils.pretty_print_answer(1, ans)

utils.pretty_print_answer(2, recipes.length_before('409551', 100000))
