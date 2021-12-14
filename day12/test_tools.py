from tools import *


input_text = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

input2 = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc'''

larger_int = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''

def test_part1():
    assert part1(input_text) == 10
    assert part1(input2) == 19
    assert part1(larger_int) == 226
    # assert part2(larger_int) == 3509
    # assert part2(input2) == 103
    assert part2(input_text) == 36

