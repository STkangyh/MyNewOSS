import matplotlib.pyplot as plt

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'): # If 'line' is not a header
                data.append([int(word) for word in line.split(',')])
    return data

if __name__ == '__main__':
    # Load score data
    class_kr = read_data('class_score_kr.csv')
    class_en = read_data('class_score_en.csv')

    # TODO) Prepare midterm, final, and total scores
    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40/125*midterm + 60/100*final for (midterm, final) in class_kr]
    midterm_en, final_en = zip(*class_en)
    total_en = [40/125*midterm + 60/100*final for (midterm, final) in class_en]

    # TODO) Plot midterm/final scores as points
    xk = [x for x in midterm_kr]
    yk = [y for y in final_kr]
    xe = [x for x in midterm_en]
    ye = [y for y in final_en]

    plt.plot(xk, yk, 'ro', xe, ye, 'b+')
    plt.grid()

    plt.show()
    
    # TODO) Plot total scores as a histograms
    plt.hist(total_kr, bins=5, alpha=0.5, label="Korean")
    plt.hist(total_en, bins=5, alpha=0.5, label="English")
    plt.legend()

    plt.show()