class Assembler():
    def __init__(self):
        #defined instructions here
        self.loadAcc = "Load Instruction"
        self.move = "Move Instruction"
        self.add = "Add Instruction"
        self.inst_input_list = []
        self.registerList = {}
        self.instructionList = {}
        self.instructionType = {}
        for key in [self.load, self.move, self.add]:
            self.instructionType[key] = "IS" #only imperative statements are supported right now, may change later

#This method creates the registers and the instruction table.
    def createSystem(self, registers, instructions):
        flag = -1
        print("\n\n\t\t### System Initial Configuration Setup ###")
        if(int(registers) < 3):
            print(f"\n Minimum Register Number is 3, and you entered {registers}, exiting now...")
            exit()
        else:
            for count in range(0, int(registers)):
                regName = input(f"\nDefine the name for the Register Number {count+1} ")
                self.registerList[regName] = 0
            print("\n\n Checking Validity of Register Names...")
            for key in self.registerList:
                if(key == "A"):
                    flag+=1
                elif(key == "T"):
                    flag+=1
            if(flag == 1):
                print("\n\n\t\t ### All Register Names Are Valid and are Successfully Defined ###")
            else:
                print("\n\n\t\t ### Couldn't find accumulator or temp. register in your system, Creation Unsuccessful ###")
                exit()
            print("\n ### Instruction Editor ### ")
            for count in range(0, int(instructions) ):
                instName = input(f"\nEnter the Instruction Name : ")
                print("\nWhat does the following instruction do ? ")
                self.askInstruction(instName)

            print("\n\n\t\t ### Instructions Successfully Defined ###\n\n Initial Setup Complete ...");

    #This method is used to input the assembly program
    def getInstructions(self):
        while True:
            inst =input(f"\n [Enter the Instruction] : ")
            if inst:
                self.inst_input_list.append(s)
            else:
                break;
        print("\n\n\t\t\t ### Given Assembly Program ### : ")
            for i in self.inst_input_list:
                print (i)
        self.ICGen(inst_input_list)


    #This method shows the system Info.
    def sysInfo(self):
        print("\n\t\t #### Register Information ####")
        for key in self.registerList:
            print(f"\n\t    {key} ================== {self.registerList[key]}")
        print("\n\t\t #### Instruction Set ####")
        for key in self.instructionList:
            print(f"\n\t    {key} ========================= {self.instructionList[key]}")

    #This methos gets the type and task of instruction
    def askInstruction(self, instName):
        option = int(input("\n 1. Load  \n 2. Move Instruction \n 3. Add Instruction"))
        if(option  == 1):
            self.instructionList[instName] = "0b0000" #defined opcodes here
        elif(option == 2):
            self.instructionList[instName] = "0b0001"
        elif(option == 3):
            self.instructionList[instName] = "0b0010"
        else:
            print("\nPlease Enter A Valid option.")
            self.askInstruction()

    def check_instruction_type(self, instruction):
        for key in self.instructionList:
            if(instruction.find(key) == -1)

            else:
                print(f"\n ### Instruction Recognized {key} with OpCode {self.instructionList[key]} ")
                if(self.instructionList[key] == "0b0000"):
                    return "Load Instruction"
                elif(self.instructionList[key] == "0b0001"):
                    return "Move Instruction"
                elif(self.instructionList[key] == "0b0010"):
                    return "Add Instruction"

#This method generates the intermediate code ( Lexical Analyzer + IC Generator)
    def ICGen(self, inst_input_list):
        LiteralTable = {}
        currLitIndex = 0
        ICCode = []
        for i_counter in range(0, len(inst_input_list)):
            if(check_instruction_type(inst_input_list[i_counter]) == "Load Instruction"):
                load_inst_split = inst_input_list[i_counter].split()
                load_code = load_inst_split[0] + " " + f"({self.instructionType[self.load]},'0b0000')" + f"(REG,{load_inst_split[2]}) ({load_inst_split[3]}, {currLitIndex})"
                ICCode.append(load_code)
                LiteralTable[currLitIndex] = load_inst_split[3]
                currLitIndex += 1
                self.registerList[load_inst_split[2]] = load_inst_split[3]
            elif(check_instruction_type(inst_input_list[i_counter]) == "Move Instruction"):
                move_inst_split = inst_input_list[i_counter].split()
                move_code = move_inst_split[0] + " " + f"({self.instructionType[self.move]},'0b0001')" + f"(REG, {move_inst_split[2]}) (REG, {move_inst_split[3]})"
                ICCode.append(move_code)
                self.registerList[move_inst_split[2]] = self.registerList[move_inst_split[3]]
            elif(check_instruction_type(inst_input_list[i_counter]) == "Add Instruction"):
                add_inst_split = inst_input_list[i_counter].split()
                add_code = add_inst_split[0] + " " + f"({self.instructionType[self.add]},'0b0010')" + f"(REG, {add_inst_split[2]}) (REG, {move_inst_split[3]}) (REG, {move_inst_split[4]})"
                ICCode.append(add_code)
                self.registerList[add_inst_split[2]] = self.registerList[add_inst_split[3]] + self.registerList[add_inst_split[4]]

        # Listing Out ALl the Data Structures now
        print("\n\n\n\t\t\t ### Listing out the current state of all the data structures... ###")
        print("\n\n ### Register Table ###")
        for key,val in  self.registerList.items():
            print(f"\n### {key} ------------> {val} ###")
        print("\n\n ### OpCode Table ###")
        for key, val in self.instructionList.items():
            print(f"\n### {key} ------------> {val} ###")
        print("\n\n ### Literal Table ###")
        for key, val in LiteralTable.items():
            print(f"\n### {key} ------------> {val} ###")
        print("\n\n\t\t\t ### Generating Intermediate Code Of the given Assembly Program : ")
        for ic in ICCode:
            print(ic)

if(__name__ == "__main__"):
    assembler = Assembler();
    numReg = input("Enter the Number of Registers You Want \n(Minimum 3, and Make Sure 1 is Accumulator(Denoted By A)), and 1 is Temp(denoted by T) :")
    numInstruction = input("Enter the Number of Instructions You Want :")
    assembler.createSystem(numReg, numInstruction)
    assembler.sysInfo()
    assembler.getInstructions()
