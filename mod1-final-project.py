import statistics

filename = "sample_grades.csv" # csv file in PyCharm
fh = open(filename,"r")

def median(grades):
    med = statistics.median(grades)
    return med

def std_dev(grades):
    dev = statistics.stdev(grades)
    return dev

def main():
    count_fall = 0  # total number of Fall students/rows in csv
    grades_fall = []
    count_spring = 0  # total number of Spring students/rows in csv
    grades_spring = []
    for line in fh:
        if line.rstrip().split(",")[1] == "Fall 2016":
            grades_fall.append(eval(line.rstrip().split(",")[2]))
            count_fall += 1
        else:
            grades_spring.append(eval(line.rstrip().split(",")[2]))
            count_spring += 1
    print("\t\tFall 2016\tSpring 2016")
    print("Mean:\t",round(sum(grades_fall)/count_fall,2),"\t\t",round(sum(grades_spring)/count_spring,2)) # could probably use mean from statistics
    print("Median:\t",median(grades_fall),"\t\t",median(grades_spring))
    print("STD:\t",round(std_dev(grades_fall),2),"\t\t",round(std_dev(grades_spring),2))
    fh.close()

main()
