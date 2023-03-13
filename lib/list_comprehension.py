#!/usr/bin/env python3

def return_evens(num_list):
    events_list = [n for n in num_list if n % 2 == 0]
    return events_list

def make_exclamation(sentence_list):
    exclamation_list = [n + "!" for n in sentence_list]
    return exclamation_list