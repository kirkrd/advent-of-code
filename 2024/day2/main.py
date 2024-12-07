with open('./input.txt') as f:
    data = f.readlines()
    data = [x.replace('\n', '') for x in data]

    number_of_safe_reports = 0
    max_diff = 3
    min_diff = 1

    for report in data:
        if report != '':
            report_numbers = report.split(" ")
            report_numbers = [int(a) for a in report_numbers]
            is_report_safe = False
            report_results = []
            for i, y in enumerate(report_numbers):
                if (i + 1 < report_numbers.__len__()):
                    curr_number = y
                    next_number = report_numbers[i+1]
                    diff = abs(curr_number - next_number)
                    is_increase = next_number > curr_number
                    if diff <= max_diff and diff >= min_diff:
                        report_results.append([True, is_increase])
                    else:
                        report_results.append([False, is_increase])
            if all(i == report_results[0] for i in report_results):
                number_of_safe_reports = number_of_safe_reports + 1

    print("Answer: ", number_of_safe_reports)
