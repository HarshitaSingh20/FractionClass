import math
class Fraction:
#fraction creation
    def __init__(self,n,d):
        self.num=n
        self.den=d

#fraction display
    def __str__(self):
        return "{}/{}".format(self.num,self.den)

#fraction addition using magic method __add__
    def __add__(self,other):

        temp_num= self.num * other.den + other.num * self.den
        temp_den= self.den * other.den
        return "{}/{}".format(temp_num,temp_den)

#fraction subtraction using magic method subtract
    def __sub__(self,other):

        temp_num= self.num * other.den - other.num * self.den
        temp_den= self.den * other.den
        return "{}/{}".format(temp_num,temp_den)

#fraction multiplication using magic method
    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)

#fraction division using magic method
    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return "{}/{}".format(temp_num, temp_den)

#ceiling function
    def ceiling(self):
        temp_num= self.num//self.den
        if self.num%self.den==0:
            return self.num//self.den
        else:
            return (self.num//self.den)+1

#floor function
    def floor(self):
        return self.num//self.den

#converting fractions to decimals
    def to_decimal(self,val=2):
        return round((self.num/self.den),val)


    def to_mixed_fraction(self):
        if self.num<=self.den:
            return "{}/{}".format(self.num, self.den)

        elif self.num%self.den==0:
            return self.num//self.den

        else:
            whole_part= self.num//self.den
            temp_num= self.num%self.den
            return "({}){}/{}".format(whole_part,temp_num,self.den)

    def to_simple_form(self):
        x=self.num
        y=self.den
        if x > y:
            small = y
        else:
            small = x
        for i in range(1, small + 1):
            if ((x % i == 0) and (y % i == 0)):
                d = i

        self.num = self.num // d;
        self.den = self.den // d;
        return "{}/{}".format(self.num, self.den)

    def frac_log(self):

        return math.log(self.num)-math.log(self.den)

    def frac_pow(self,power):
        x=round(self.num**power,2)
        y=round(self.den**power,2)
        return "{}/{}".format(x,y)










