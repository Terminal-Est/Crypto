def otp():
    ints = [0, 0, 0]
    y = 0
    while y < len(ints):
        ints[y] = input("Enter integer: ")
        y += 1
    return int(ints[0]) ^ int(ints[1]) ^ int(ints[2]), ints

def sec_key():
    ints = [0, 0]
    y = 0
    while y < len(ints):
        ints[y] = input("Enter integer: ")
        y += 1
    return ints

def regen_otp(secInts, otpInts, secKey):
    print(otpInts)
    print(secInts)
    foo = int(secInts[0]) ^ int(secInts[1]) ^  secKey
    # bar = int(otpInts[0]) ^ int(otpInts[1]) ^ int(otpInts[2])
    # used for validation?
    return foo

def main():
    menu = True
    otpGen = False
    keyGen = False
    oneTimePad = 0
    regenPad = 0
    secKey = 0
    otpInts = []
    secInts = []

    while menu == True:
        select = input("Enter 1 to generate one-time pad, 2 to generate secret key, 3 regen OTP, 4 Exit: ")
        menuCheck = 0

        if select in ('1'):
            menuCheck = 1
            oneTimePad, otpInts = otp()
            otpGen = True
            print('One-time pad = ', oneTimePad)

        if select in ('2'):
            if not otpGen:
                print('One-time pad not generated!')
            else:
                menuCheck = 2
                secInts = sec_key()
                print(secInts[0])
                secKey = int(secInts[0]) ^ int(secInts[1]) ^ oneTimePad
                print('Security key = ', secKey)

        if select in ('3'):
            if not otpGen and keyGen:
                print('One-time pad and Key not generated!')
            else:
                menuCheck = 3
                regenPad = regen_otp(secInts, otpInts, secKey)
                print('Regenerated One-time pad = ', regenPad)

        if menuCheck != 1 and menuCheck != 2 and menuCheck != 3:
            if select in ('4'):
                menu = False
            else:
                print('Invalid menu option')

if __name__ == "__main__":
    main()
