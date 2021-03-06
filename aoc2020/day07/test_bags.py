import re
import utils
from aoc2020.day07.bags import Bags, RULES_REGEX

def test_matches():
    lines = utils.read_lines('sample.txt')
    for line in lines:
        assert re.match(RULES_REGEX, line)

def test_sample_nonexistent():
    rules = Bags('sample.txt')
    assert rules.contain_count('rainbow') == 0

def test_sample_bright_white():
    rules = Bags('sample.txt')
    assert rules.contain_count('bright white') == 2

def test_sample_muted_yellow():
    rules = Bags('sample.txt')
    assert rules.contain_count('muted yellow') == 2

def test_sample_shiny_gold():
    rules = Bags('sample.txt')
    assert rules.contain_count('shiny gold') == 4

def test_sample_black():
    rules = Bags('sample.txt')
    assert rules.contain_count('dotted black') == 7

def test_sample_count_bags():
    rules = Bags('sample.txt')
    assert rules.count_bags('shiny gold') == 32

def test_saample_count_bags_2():
    rules = Bags('sample2.txt')
    assert rules.count_bags('shiny gold') == 126
