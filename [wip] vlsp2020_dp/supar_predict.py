from supar import Parser

parser = Parser.load('biaffine-dep-en')

dataset = parser.predict([['She', 'enjoys', 'playing', 'tennis', '.']], prob=True, verbose=False)
print(dataset)