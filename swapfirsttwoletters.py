def swaptwocharacters(string1, string2):
    new_string1 = string2[:2] + string1[2:]
    new_string2 = string1[:2] + string2[2:]
    return new_string1 + " " + new_string2

print(swaptwocharacters("mix", "pod"))