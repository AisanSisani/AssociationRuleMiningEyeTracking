import dataset
from apriori_python import apriori


def main():
    d = dataset.get_dataset("Apple_sequence_dataset.txt")
    print("Transactions:")
    print(d, end='\n\n')

    freqItemSet, rules = apriori(d, minSup=0.75, minConf=0.75)
    print("Frequent Item Sets")
    for i in freqItemSet:
        print(i, freqItemSet[i])


if __name__ == '__main__':
    main()
