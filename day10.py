import itertools

# def main(input):
#     adapters = sorted([int(line) for line in input])
#     built_in = max(adapters) + 3

#     adapters.insert(0, 0)

#     out = [adapters[a+1] - adapters[a] for a in range(len(adapters)-1)]
#     ones = len([a for a in out if a == 1])
#     thres = len([a for a in out if a == 3]) + 1

#     print(ones * thres)


def get_sequences(adapters, start_position):
    cache = {}
    neighbors = {j: [i for i in adapters if 1 <= j - i <= 3] for j in adapters}

    def helper(adapters, start_position):
        if start_position in cache:
            return cache[start_position]

        if start_position == 0:
            return 1 

        found = 0
        for i in neighbors[start_position]:
            found += helper(adapters, i)

        cache[start_position] = found
        
        return found
    
    return helper(adapters, start_position)


def main(input):
    adapters = [0] + sorted([int(line) for line in input])
    adapters = adapters + [max(adapters) + 3]
    print(get_sequences(adapters, max(adapters)))


if __name__ == '__main__':

#     ingoing = '''28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3'''

    ingoing = '''84
60
10
23
126
2
128
63
59
69
127
73
140
55
154
133
36
139
4
70
110
97
153
105
41
106
79
145
35
134
146
148
13
77
49
107
46
138
88
152
83
120
52
114
159
158
53
76
16
28
89
25
42
66
119
3
17
67
94
99
7
56
85
122
18
20
43
160
54
113
29
130
19
135
30
80
116
91
161
115
141
102
37
157
129
34
147
142
151
68
78
24
90
121
123
33
98
1
40'''

    lines = ingoing.split('\n')

    print(main(lines))
