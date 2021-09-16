from time_range import trange
import pprint


def main():
    result: list = [time for time in trange((10, 10, 10), (13, 50, 15), (0, 15, 12))]

    print('Result:')
    pprint.pprint(result)

    assert result[1] == (10, 25, 22)
    assert result[-1] == (13, 42, 58)
    assert type(result[-1]) == tuple
    assert len(result[0]) == 3


if __name__ == '__main__':
    main()
