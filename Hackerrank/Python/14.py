def freqQuery(queries):
    results = []
    d = dict()
    freqs = defaultdict(set)
    for command, value in queries:
        freq = d.get(value, 0)
        if command == 1:
            d[value] = freq + 1
            freqs[freq].discard(value)
            freqs[freq + 1].add(value)
        elif command == 2:
            d[value] = max(0, freq - 1)
            freqs[freq].discard(value)
            freqs[freq - 1].add(value)
        elif command == 3:
            results.append(1 if freqs[value] else 0)
    return results  
