
#logic gate module can calculate truth table for two bits which is then implemented into a 2-decoder, 2-multiplexor, 4-input multiplexor, 1-bit adder, and 1-bit ALU


from abstractclasses import solver, solver_model

class logic_gate_solver(solver):
    def prompt_inputs(self) -> None:
        a_arg = self.prompt_integer(
            "Please enter the value of A ", 
        )
        b_arg = self.prompt_integer(
            "Please enter the value of B > ",
        )
        

        # Set inputs
        self.inputs["a_arg"] = a_arg
        self.inputs["b_arg"] = b_arg

class logic_gate_solver(solver_model):
    # Function Calls 
    def not_gate( A):
        if (A):
            return 0
        else:
            return 1
    
    def or_gate( A,  B):
        # TODO: implement logical OR
        if (A):
            return 1
        if (B):
            return 1
        else:
            return 0
    
    
    def and_gate( A,  B):
        # TODO: implement logical AND
        if (A):
            if (B):
                return 1
        else:
            return 0
    
    def xor_gate( A,  B):
        # TODO: implement logical XOR
        if (A ^ B):
            return 1
        else:
            return 0

    def decoder2( I0,  I1, O0, O1, O2, O3):
        # TO DO: implement a 2-input decoder
        O0 = and_gate(not_gate(I1), not_gate(I0))
        O1 = and_gate(I1, not_gate(I0))
        O2 = and_gate(not_gate(I1), I0)
        O3 = and_gate(I1, I0)
        return

    def multiplexor2( S,  I0,  I1):
        # TODO: implement a 2-input multiplexor
        x0 = and_gate(not_gate(S), I0)
        x1 = and_gate(S, I1)
        return or_gate(x0, x1)  


    def multiplexor4( S0,  S1,  I0,  I1,  I2,  I3):
        # TODO: implement a 4-input multiplexor
        x0, x1, x2, x3 = 0
        decoder2(S0, S1, x0, x1, x2, x3)

        y0 = and_gate(x0, I0)
        y1 = and_gate(x1, I1)
        y2 = and_gate(x2, I2)
        y3 = and_gate(x3, I3)

        z0 = or_gate(y0, y1)
        z1 = or_gate(y2, y3)

        return or_gate(z0, z1)  


    def adder( A,  B,  CarryIn, CarryOut, Sum):
        # TODO: implement a 1-bit adder
        x0 = xor_gate(A, B)
        Sum = xor_gate(CarryIn, x0)

        y0 = and_gate(x0, CarryIn)
        y1 = and_gate(A, B)
        CarryOut = or_gate(y0, y1)


    def ALU( A,  B,  Binvert,  CarryIn,  Op0,  Op1, Result,CarryOut):
        # TODO: implement a 1-bit ALU 
        x0 = multiplexor2(Binvert, B, not_gate(B))

        y0 = and_gate(A, x0)
        y1 = or_gate(A, x0)

        y2 = 0
        adder(A, x0, CarryIn, CarryOut, y2)  
        if (and_gate(Op0, Op1)):
            Result = -1
        else:
            Result = multiplexor4(Op0, Op1, y0, y1, y2, 0)



