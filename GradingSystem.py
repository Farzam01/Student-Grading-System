def StudentGradingSystem():
    import csv
    stdlst = ['Std_name', 'std_id', 'final_Score']
    scores_lst = ['mid_avg', 'project_avg', 'final_avg', 'total_avg']
    avg_lst = ['mid_avg', 'project_avg', 'final_avg']
    n = int(input("Enter No of Fields You want in course details:"))
    dict_coursedetail = {}
    for i in range(n):
        key = input("Enter Field:")
        value = input("Enter Record:")
        dict_coursedetail[key] = value
    print(dict_coursedetail)
    std_lst = []
    mid_lst = []
    project_lst = []
    final_lst = []
    total_lst = []
    r = int(input("Enter no of Student Records you want:"))
    for i in range(r):
        std_name = input("Enter Student Name:")
        std_Id = input("Enter Student Id:")
        mid_marks = eval(input("Enter Mid Marks:"))
        project_marks = eval(input("Enter project marks: "))
        final_marks = eval(input("Enter final marks: "))
        total = (mid_marks * 0.3) + (project_marks * 0.3) + (final_marks * 0.4)
        if total < 60:
            print("Student is failed.")
            print(total)
        std_lst.append(std_name)
        std_lst.append(std_Id)
        std_lst.append(total)
        mid_lst.append(mid_marks)
        project_lst.append(project_marks)
        final_lst.append(final_marks)
        total_lst.append(total)
    print(std_lst, end="")
    print('Mid Marks of these Students are:', mid_lst, end="")
    print("\n")
    print('Project marks of these students are:', project_lst, end="")
    print("\n")
    print('final marks of these students are:', final_lst, end="")
    print("\n")
    print('total marks of these students are :', total_lst, end="")
    print("\n")
    avg_per_assessment = []
    avg_final_score = []
    mid_avg = sum(mid_lst) / len(mid_lst)
    avg_per_assessment.append(mid_avg)
    project_avg = sum(project_lst) / len(project_lst)
    avg_per_assessment.append(project_avg)
    final_avg = sum(final_lst) / len(final_lst)
    avg_per_assessment.append(final_avg)
    total_avg = sum(total_lst) / len(total_lst)
    avg_final_score.append(total_avg)
    print('The Average per assessments are:', avg_per_assessment)
    print('')
    print('The Average final score is:', total_avg)
    print('')
    '''print('The Average of all project marks are:', project_avg)
    print('The Average of all final exam marks  are:', final_avg)
    print('The Average of  total marks are:', total_avg)'''
    fail_std = []
    pass_marks = 60
    for x in total_lst:
        if pass_marks > x:
            fail_std.append(x)
    print("Total No of Students Fail in this Course are:", len(fail_std))
    def SaveRecord():
        q = str(input("Do you want to save the report ? "))
        if q == 'yes':
            filename = "Records.csv"
            with open(filename, 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([dict_coursedetail.keys()])
                csvwriter.writerows([dict_coursedetail.values()])
                csvwriter.writerow([stdlst])
                csvwriter.writerows([std_lst])
                csvwriter.writerow([avg_lst])
                csvwriter.writerows([avg_per_assessment])
        else:
            print("Record is not saved !")
        pass

    SaveRecord()
StudentGradingSystem()





