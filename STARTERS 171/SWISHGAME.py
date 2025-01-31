def pari_max_value(niki, nidz, shagi):
    diksi = shagi.count('S')
    if diksi >= nidz:
        return niki
    return niki + nidz - diksi - 1


def main():
    iri = int(input())
    for _ in range(iri):
        niki, nidz = map(int, input().split())
        shagi = input().strip()
        print(pari_max_value(niki, nidz, shagi))


if __name__ == "__main__":
    main()
