import pathlib


def fileToList(filename):
    # try:
    #     f = open(filename)
    #     f.close()
    # except FileNotFoundError:
    #     return ["hi"]
    path = pathlib.Path(filename)
    if path.exists():
        fin = open(filename, 'r')
        dnacode = []
        for line in fin:
            line = line.strip()
            dnacode.append(line)
        fin.close()
        return dnacode
    else:
        return []


def returnFirstString(strings):
    if len(strings) > 0:
        return strings[0]
    else:
        return ""


def strandsAreNotEmpty(strand1, strand2):
    return len(strand1) > 0 and len(strand2) > 0


def strandsAreEqualLengths(strand1, strand2):
    return len(strand1) == len(strand2)


def candidateOverlapsTarget(target, candidate, overlap):
    tarcom = target[len(target) - overlap:]  # target comparison
    cancom = candidate[:overlap]  # candidate comparison
    return cancom == tarcom


def findLargestOverlap(target, candidate):
    largest = 0
    if target == candidate and len(target) > 0:
        return len(target)
    elif len(target) == len(candidate) and len(target) > 0:
        for i in range(len(target)):
            x = target[len(target) - i:]
            y = candidate[:i]
            if x == y:
                largest = i
        return largest
    else:
        return -1


def findBestCandidate(target, candidates):
    candy = "" # best candidate
    largest = 0
    for candidate in candidates:
        new = findLargestOverlap(target, candidate)
        if new > largest:
            largest = new
            candy = candidate
    return candy, largest


def joinTwoStrands(target, candidate, overlap):
    if len(candidate) == 0:
        return target
    cover = candidate[overlap:]
    newstrand = target + cover
    return newstrand


def main():
    tar = input("Target strand filename: ")
    tarstep = fileToList(tar)  # target.txt to list
    target = returnFirstString(tarstep)  # list to string
    cans = input("Candidate strand filename: ")
    candidates = fileToList(cans)  # candidates.txt to list
    candidate, overlap = findBestCandidate(target, candidates)
    final_strand = joinTwoStrands(target, candidate, overlap)
    print(final_strand)


if __name__ == '__main__':
    main()
