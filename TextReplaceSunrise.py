#import re
test_name = ''

with open("C:\\Users\\iampr\\Desktop\\TextReplacementSunrise.txt") as infile:
    extract = []
    qc_value=''
    for line in infile:
        if line.startswith("qc"):
            qc_value = line.strip()
        extract.append(line)
        for i in range(0,len(extract)):
            if '${TEST_NAME}' in extract[i]:
                extract[i] = [sub.replace('${TEST_NAME}',qc_value) for sub in extract[i].split('    ')]
                extract[i] = '    '.join(extract[i])
        #----2nd part----

            if '[Documentation]' in extract[i] and (extract[i-1].startswith("qc".lstrip()) or extract[i-2].startswith("qc".lstrip())):
               test_name = extract[i].split('   ')[1].strip()
               if '[Setup]' in extract[i-1]:
                    extract[i-2] = [sub.replace(qc_value,test_name) for sub in extract[i-2].split('    ')]

                    extract[i-2] = '    '.join(extract[i-2])

               else:
                    extract[i-1] = [sub.replace(qc_value, test_name) for sub in extract[i-1].split('    ')]
                    extract[i-1] = '    '.join(extract[i-1])



        with open("C:\\Users\\iampr\\Desktop\\TextReplacementSunrise2.txt", "w+") as fout:
            for item in extract:

                try:
                    fout.write(item)
                except EOFError:
                    raise SystemExit




