# parse_trees.py
# Given a CFG and a sentence, general all possible parse trees for the sentence
# Uses NLTK (Natural Language toolkit) and CYK algorithm
# Jamie Alexander, Luisa Neves, Ben Ouattara, J. Hassler Thurston
# November 15, 2014

from nltk import word_tokenize
from nltk import CFG
from nltk import ChartParser
from nltk.tree import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
# from nltk.corpus import brown
# from nltk.draw.tree import draw_trees
import sys
from subprocess import call

# from nltk.corpus import treebank

# maximum number of trees to generate
MAX_TREES = 1

# grammar that we're using in class
class_grammar_1 = CFG.fromstring("""
    Start -> S
    S -> NP VP | NP aux VP
    NP -> N | Det N | Adj N | Det Adj N | N PP | Det N PP | Adj N PP | Det Adj N PP
    VP -> V | V NP | V PP | V NP PP
    PP -> P NP
    Aux -> 'is' | 'does'
    Det -> 'the' | 'a' | 'an' | 'my'
    N -> 'apple' | 'banana' | 'orange' | 'elephant' | 'pajamas' | 'i'
    V -> 'eats' | 'kills' | 'writes' | 'saw' | 'shot'
    Adj -> 'red' | 'blue' | 'quick' | 'slow'
    P -> 'with' | 'by' | 'in'
    """)
class_grammar_2 = CFG.fromstring("""
    Start -> S
    S -> NP VP | NP Aux VP
    NP -> N | Det N | AdjP N | Det AdjP N | N PP | Det N PP | AdjP N PP | Det AdjP N PP
    VP -> V | V NP | V Vtail | V NP Vtail
    Vtail -> AdvP Vtail | PP Vtail
    Vtail -> 
    PP -> P NP
    AdjP -> Adj | Deg Adj
    AdvP -> Adv | Deg Adv
    S -> S Conj S
    NP -> NP Conj NP
    VP -> VP Conj VP
    AdjP -> AdjP Conj AdjP
    AdvP -> AdvP Conj AdvP
    Aux -> 'is' | 'does'
    Det -> 'the' | 'a' | 'an' | 'my'
    N -> 'apple' | 'banana' | 'orange' | 'elephant' | 'pajamas' | 'i'
    V -> 'eats' | 'kills' | 'writes' | 'saw' | 'shot'
    Adj -> 'red' | 'blue' | 'quick' | 'slow'
    Adv -> 'quickly' | 'slowly' | 'furiously' | 'shyly'
    Conj -> 'and' | 'or'
    P -> 'with' | 'by' | 'in'
    """)
class_grammar_3 = CFG.fromstring("""
    Start -> S
    S -> NP VP | NP Aux VP
    NP -> Nprime | Det Nprime
    Nprime -> AdjP Nprime | Nprime PP | N
    VP -> Vprime
    Vprime -> V NP | Vprime Vtail
    Vtail -> AdvP Vtail | PP Vtail
    Vtail -> 
    PP -> P NP
    AdjP -> Adj | Deg Adj
    AdvP -> Adv | Deg Adv
    S -> S Conj S
    NP -> NP Conj NP
    VP -> VP Conj VP
    AdjP -> AdjP Conj AdjP
    AdvP -> AdvP Conj AdvP
    Aux -> 'is' | 'does'
    Det -> 'the' | 'a' | 'an' | 'my'
    N -> 'apple' | 'banana' | 'orange' | 'elephant' | 'pajamas' | 'i'
    V -> 'eats' | 'kills' | 'writes' | 'saw' | 'shot'
    Adj -> 'red' | 'blue' | 'quick' | 'slow'
    Adv -> 'quickly' | 'slowly' | 'furiously' | 'shyly'
    Conj -> 'and' | 'or'
    P -> 'with' | 'by' | 'in'
    """)
grammars = [class_grammar_1, class_grammar_2, class_grammar_3]


def generate_parse_tree(sentence, grammar):
    # then generate the parse trees
    tokens = word_tokenize(sentence)
    parser = ChartParser(grammar)
    # print type(grammar), type(parser)
    try:
        return parser.parse(tokens)
    except Exception:
        #print "Sentence '" + sentence + "' cannot be parsed using the given grammar."
        return Tree('Error', ['Error'])


def get_grammar(num):
    return grammars[int(num)-1]


# given the sentence, computes the part of the file name using the sentence
def computeNameFromSentence(sentence):
    return sentence.replace(" ", "_")


# main method of the parse tree program
# takes in a sentence in the command-line, outputs all possible parse trees of the sentence
if __name__ == '__main__':
    # first, convert the sentence to lowercase
    low = sys.argv[1].lower()
    # then chop off the punctuation
    # http://stackoverflow.com/questions/16050952/how-to-remove-all-the-punctuation-in-a-string-python
    lower = "".join(c for c in low if c not in ('!', '.', '?'))
    # generate the parse tree for the sentence they inputed
    trees = generate_parse_tree(lower, get_grammar(sys.argv[2]))
    # print type(trees)
    numTrees = 0
    for tree in trees:
        if numTrees >= MAX_TREES:
            break
        # if the tree is an error tree, continue to the next one
        # print tree
        if tree == "Error":
            continue
        # print "tree using grammar " + ": "
        # draw_trees(tree)
        # http://stackoverflow.com/questions/23429117/saving-nltk-drawn-parse-tree-to-image-file
        cf = CanvasFrame()
        tc = TreeWidget(cf.canvas(), tree)
        cf.add_widget(tc, 10, 10)  # (10,10) offsets
        # compute the filename from the input, then write the image to the file
        filename = 'trees/tree_' + sys.argv[2] + '_' + computeNameFromSentence(lower)
        cf.print_to_file(filename + '.ps')
        # convert the file to PNG
        # http://stackoverflow.com/questions/89228/calling-an-external-command-in-python
        call(["convert", filename + '.ps', filename + '.png'])
        cf.destroy()
        print filename + '.png'
        numTrees += 1
