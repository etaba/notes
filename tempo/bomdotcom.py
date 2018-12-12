import sys
import re
import json

REGS = [
        #MPN:Manufacturer:ReferenceDesignators
        re.compile(r'(?P<mpn>[a-zA-Z0-9-]+):(?P<man>\w+):(?P<rds>.+)$'),
        #Manufacturer -- MPN:ReferenceDesignators
        re.compile(r'(?P<man>\w+)\s--\s(?P<mpn>[a-zA-Z0-9-]+):(?P<rds>.+)$'),
        #ReferenceDesignators;MPN;Manufacturer
        re.compile(r'(?P<rds>.+);(?P<mpn>[a-zA-Z0-9-]+);(?P<man>\w+)$')
        ] 

#Parses BOM lines of formats defined in REGS array, returns None if no match found
def parse_bom_line(line):
    for reg in REGS:
        match = reg.match(line)
        if match != None and len(match.groups()) == 3:
            return {'MPN':match.group('mpn'),
                    'Manufacturer':match.group('man'),
                    'ReferenceDesignators':match.group('rds').split(',')}
    return None

#Sort and group MPNs
def organize_mpns(mpns):
    #sort MPNs by MPN and Manufacturer
    mpns.sort(key=lambda mpn:(mpn['MPN'],mpn['Manufacturer']))
    #group similar MPNs and assign NumOccurences
    prev_mpn = mpns[0]
    prev_mpn['NumOccurences'] = 1
    i = 1
    while i < len(mpns):
        if mpns[i]['MPN'] == prev_mpn['MPN'] \
           and mpns[i]['Manufacturer'] == prev_mpn['Manufacturer']:
            prev_mpn['NumOccurences'] += 1
            prev_mpn['ReferenceDesignators'] = \
                        list(set(mpns[i]['ReferenceDesignators'])
                        | set(prev_mpn['ReferenceDesignators']))
            del mpns[i]
        else:
            prev_mpn = mpns[i]
            prev_mpn['NumOccurences'] = 1
            i += 1
    #sort mpns by NumOccurences and the amount of ReferenceDesignators
    mpns.sort(
        key=lambda mpn:(mpn['NumOccurences'],len(mpn['ReferenceDesignators'])),
        reverse=True)
    return

if __name__ == '__main__':
    mpns = []
    n = int(sys.stdin.readline())
    for line in sys.stdin:
        mpn = parse_bom_line(line)
        #only append MPNs which matched one of the compatible formats
        if mpn != None:
            mpns.append(mpn)
    organize_mpns(mpns)
    #jsonify top n results
    print(json.dumps(mpns[:n]))
         
