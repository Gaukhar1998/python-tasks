# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 16:56:55 2018

@author: hp
"""

class State(object):
    def __init__(self, label, rules, dot, start, end, 
                 idx, made_from, producer):
        self.label = label
        self.rules = rules
        self.dot = dot
        self.start = start
        self.end = end
        self.idx = idx
        self.made_from = made_from
        self.producer = producer

    def next(self):
        """Returns the tag after the dot"""
        return self.rules[self.dot]

    def complete(self):
        return len(self.rules) == self.dot

    def __eq__(self, other):
        return (self.label == other.label and
                self.rules == other.rules and
                self.dot == other.dot and
                self.start == other.start and
                self.end == other.end)

    def __str__(self):
        rule_string = ''
        for i, rule in enumerate(self.rules):
            if i == self.dot:
                rule_string += '* '
            rule_string += rule + ' '
        if self.dot == len(self.rules):
            rule_string += '*'
        return 'S%d %s -> %s %s' % (self.idx, self.label, rule_string, self.producer)

"""
Create Earley model to distinguish 
type of words
"""
class Earley:
    def __init__(self, words, grammar, terminals):
        self.chart = [[] for _ in range(len(words) + 1)]
        self.current_id = 0
        self.words = words
        self.grammar = grammar
        self.terminals = terminals

    def get_new_id(self):
        self.current_id += 1
        return self.current_id - 1

    def is_terminal(self, tag):
        return tag in self.terminals

    def is_complete(self, state):
        return len(state.rules) == state.dot

    def enqueue(self, state, chart_entry):
        if state not in self.chart[chart_entry]:
            self.chart[chart_entry].append(state)
        else:
            self.current_id -= 1

    def predictor(self, state):
        for production in self.grammar[state.next()]:
            self.enqueue(State(state.next(), production, 0, state.end, state.end, self.get_new_id(), [], 'predictor'), state.end)

    def scanner(self, state):
        if self.words[state.end] in self.grammar[state.next()]:
            self.enqueue(State(state.next(), [self.words[state.end]], 1, state.end, state.end + 1, self.get_new_id(), [], 'scanner'), state.end + 1)

    def completer(self, state):
        for s in self.chart[state.start]:
            if not s.complete() and s.next() == state.label and s.end == state.start and s.label != 'gamma':
                self.enqueue(State(s.label, s.rules, s.dot + 1, s.start, state.end, self.get_new_id(), s.made_from + [state.idx], 'completer'), state.end)

    def parse(self):
        self.enqueue(State('sentence', ['S'], 0, 0, 0, self.get_new_id(), [], 'start state'), 0)
        
        for i in range(len(self.words) + 1):
            for state in self.chart[i]:
                if not state.complete() and not self.is_terminal(state.next()):
                    self.predictor(state)
                elif i != len(self.words) and not state.complete() and self.is_terminal(state.next()):
                    self.scanner(state)
                else:
                    self.completer(state)

    def __str__(self):
        res = ''
        for i, chart in enumerate(self.chart):
            res += '\nChart[%d]\n' % i
            for state in chart:
                res += str(state) + '\n'

        return res


if __name__ == '__main__':
    grammar = {
        'S':           [['NP', 'VP'], ['Aux', 'NP', 'VP'], ['VP']],
        'NP':          [['Det', 'Nominal'], ['Proper-Noun']],
        'Nominal':     [['Noun'], ['Noun', 'Nominal']],
        'VP':          [['Verb'], ['Verb', 'NP']],
        'Det':         ['that', 'this', 'a'],
        'Noun':        ['book', 'flight', 'meal', 'money'],
        'Verb':        ['book', 'include', 'prever'],
        'Aux':         ['does'],
        'Prep':        ['from', 'to', 'on'],
        'Proper-Noun': ['Houston', 'TWA']
    }
    terminals = ['Det', 'Noun', 'Verb', 'Aux', 'Prep', 'Proper-Noun']
    line="Book that flight"
    line=line.lower().split()
    earley = Earley(line, grammar, terminals)
    earley.parse()
    print (earley)
