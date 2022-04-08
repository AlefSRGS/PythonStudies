registry = []
students = {}
name_search = ''
while True:
    name = input("Enter the student's name(if you want to stop enter exit): ")
    if name != 'exit':
        num_registry = input('registry number: ')
        subject = input('subjects coursed: ')
        grade = input('final grades: ')
        students['name'] = name
        students['registry number'] = num_registry
        students['subject coursed'] = subject
        students['final grade'] = grade
        registry.append(students)
    else:
        while name_search != 'exit':
            name_search = input("Enter the student name or registry number for search, or enter 'exit' for return to the students registry : ")
            for i in registry:
                if name_search == i['name'] or name_search == i['registry number']:
                    print('name: ', i['name'])
                    print('registry number: ', i['registry number'])
                    print('subject coursed: ', i['subject coursed'])
                    print('final grades: ', i['final grade'])