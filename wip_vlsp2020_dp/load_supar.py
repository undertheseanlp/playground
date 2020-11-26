from supar import Parser, BiaffineDependencyParser

# parser = Parser.load('biaffine-dep-en')

parser = BiaffineDependencyParser()
parser.train()