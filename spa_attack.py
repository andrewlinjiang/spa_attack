import pickle
import random
import time

traces_to_load = pickle.load(open("traces.p", "rb"))


def flag(inp):
    if str(inp) == "h0px3":
        return ("cyberSec{HOORAY}")
    return ("try again")


def cap_pass_trace(pass_guess):
    if pass_guess.endswith("\n") is False:
        raise ValueError("Password guess must end with \\n")
        
    pass_guess = pass_guess.strip("\n")
    
    known_passwd = "h0px3"
        
    trylist = "abcdefghijklmnopqrstuvwxyz0123456789 \x00"
    
    if len(pass_guess) > 5:
        raise ValueError("Only guesses up to 5 chars recorded, sorry about that.")
        
    for a in pass_guess:
        if a not in trylist:
            raise ValueError("Part of guess (%c) not in recorded enumeration list (%s)"%(a, trylist))
            
    #Only recorded is correct passwords
    recorded_pw = ""
    for i in range(0, len(pass_guess)):
        if known_passwd[i] != pass_guess[i]:
            recorded_pw += " "
        else:
            recorded_pw += pass_guess[i]
            
    time.sleep(0.05)

    return traces_to_load[recorded_pw][random.randint(0, 99)]

