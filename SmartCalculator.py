class SmartCalculator():
    
    def run(self):
        self.available = ['0','1','2','3','4','5','6','7','8','9','-','+','*','/','//','(',')',' ']
        self.new_string = ''
        try:
            while self.new_string != '/exit':
                self.new_string = input()
                if len(self.new_string) == 0:
                    self.run()
                if not self.new_string.startswith('/'):
                    for i in self.new_string:
                        if i not in self.available:
                            print('Invalid expression')
                            self.run()
                if self.new_string.startswith('/'):
                    if self.new_string == '/exit':
                        print('Bye!')
                        break
                    elif self.new_string == '/help':
                        print('The program calculated equation')
                        continue
                    else:
                        print('Unknown command')
                elif self.new_string.lstrip('-+').isdigit():
                    minus = 0
                    for i in self.new_string:
                        if i == '-':
                            minus += 1
                    if minus % 2 == 0:
                        print(int(self.new_string.lstrip('-+')))
                    else:
                        print(0 - int(self.new_string.lstrip('-+')))
                elif self.new_string.rstrip('-+').isdigit():
                    print('Invalid expression')
                    continue
                self.normal_expression()
        except Exception:
            pass
    
    def normal_expression(self):
        self.input_string = self.new_string.split()
        self.new_list = []
        for i in self.input_string:
            try:
                if i.lstrip('-+').isdigit():
                    self.new_list.append(i)
                else:
                    flag = False
                    count_minus = 0
                    count_plus = 0
                    for j in i:
                        if j == '-':
                            count_minus += 1
                            flag = True
                        elif j == '+':
                            count_plus += 1
                    if i == '*':
                        self.new_list.append(i)
                    elif i == '/':
                        self.new_list.append(i)
                    elif i == '//':
                        self.new_list.append(i)
                    elif flag == True:
                        if count_minus % 2 == 0:
                            self.new_list.append('+')
                        elif count_minus % 2 != 0:
                            self.new_list.append('-')
                    elif count_plus >= 1:
                        self.new_list.append('+')
                    elif i == '(':
                        self.new_list.append(i)
                    elif i == ')':
                        self.new_list.append(i)
            except Exception:
                pass
        self.digits = []
        self.another = []
        for i in self.new_list:
            if i.isdigit():
                self.digits.append(i)
            else:
                self.another.append(i)
        for i in self.digits:
            if not i.lstrip('-+').isdigit():
                print('Invalid expression')
                self.run()
        for i in self.another:
            if i.lstrip('-+').isdigit():
                print('Invalid expression')
                self.run()
        self.polish_reversed()

    def polish_reversed(self):
        self.reverse_polish = []
        self.operations = []
        for i in self.new_list:
            if i.lstrip('-').isdigit():
                self.reverse_polish.append(i)
            else:
                if i == '-' or i == '+':
                    if self.operations != [] and self.operations[-1] != '(' and self.operations[-1] != ')':
                        self.reverse_polish.append(self.operations[-1])
                        del self.operations[-1]
                        self.operations.append(i)
                    else:
                        self.operations.append(i)
                elif i == '*' or i == '/' or i == '//':
                    if self.operations != []:
                        if self.operations[-1] == '*' or self.operations[-1] == '/' or self.operations[-1] == '//':
                            self.reverse_polish.append(self.operations[-1])
                            del self.operations[-1]
                            self.operations.append(i)
                        else:
                            self.operations.append(i)
                    else:
                            self.operations.append(i)
                elif i == '(':
                    self.operations.append(i)
                elif i == ')':
                    while self.operations[-1] != '(':
                        self.reverse_polish.append(self.operations[-1])
                        del self.operations[-1]
                    del self.operations[-1]
        while self.operations != []:
            self.reverse_polish.append(self.operations[-1])
            del self.operations[-1]
        '''count_digits = 0
        count_sign = 0
        for i in self.reverse_polish:
            if i.lstrip('-').isdigit():
                count_digits += 1
            else:
                count_sign += 1
        if count_digits - count_sign != 1:
            print('Invalid expression')
            self.run()'''
        self.solution()
        
    def solution(self):
        self.restart = True
        while self.restart and len(self.reverse_polish) != 1:
            self.restart = False
            self.reverse_polish = [str(i) for i in self.reverse_polish]
            for idx, item in enumerate(self.reverse_polish):
                if item == '+':
                    self.reverse_polish[idx - 2] = float(self.reverse_polish[idx - 2]) + float(self.reverse_polish[idx - 1])
                    del self.reverse_polish[idx - 1]
                    del self.reverse_polish[idx - 1]
                    self.restart = True
                    break
                elif item == '-':
                    self.reverse_polish[idx - 2] = float(self.reverse_polish[idx - 2]) - float(self.reverse_polish[idx - 1])
                    del self.reverse_polish[idx - 1]
                    del self.reverse_polish[idx - 1]
                    self.restart = True
                    break
                elif item == '*':
                    self.reverse_polish[idx - 2] = float(self.reverse_polish[idx - 2]) * float(self.reverse_polish[idx - 1])
                    del self.reverse_polish[idx - 1]
                    del self.reverse_polish[idx - 1]
                    self.restart = True
                    break
                elif item == '/':
                    self.reverse_polish[idx - 2] = float(self.reverse_polish[idx - 2]) / float(self.reverse_polish[idx - 1])
                    del self.reverse_polish[idx - 1]
                    del self.reverse_polish[idx - 1]
                    self.restart = True
                    break
                elif item == '//':
                    self.reverse_polish[idx - 2] = float(self.reverse_polish[idx - 2]) // float(self.reverse_polish[idx - 1])
                    del self.reverse_polish[idx - 1]
                    del self.reverse_polish[idx - 1]
                    self.restart = True
                    break
        if len(self.reverse_polish) != 0:        
            print(int(self.reverse_polish[0]))

sm = SmartCalculator()
sm.run()



