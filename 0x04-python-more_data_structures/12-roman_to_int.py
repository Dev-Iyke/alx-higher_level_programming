#!/usr/bin/python3
if __name__ == "__main__":
    import roman
    def roman_to_int(roman_string):
        if type(roman_string) != str or type(roman_string) == None:
            return 0
        else:
            return (roman.fromRoman(roman_string))
